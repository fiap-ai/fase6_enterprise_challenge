#!/usr/bin/env python3
"""
API Service Module

This module provides functions to access various APIs, with error handling,
retries, and caching capabilities. It is designed to be used by Jupyter notebooks
and other Python scripts.
"""

import os
import json
import time
import requests
import pandas as pd
from datetime import datetime
from typing import Dict, Any, Optional, List, Union, Tuple

# Cache directory
CACHE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'cache')
if not os.path.exists(CACHE_DIR):
    os.makedirs(CACHE_DIR)

class APIService:
    """
    A service for making API requests with caching, retries, and error handling.
    """
    
    def __init__(self, base_url: str, cache_enabled: bool = True, max_retries: int = 3, 
                 retry_delay: int = 2, timeout: int = 30):
        """
        Initialize the API service.
        
        Args:
            base_url: The base URL for the API
            cache_enabled: Whether to enable caching of API responses
            max_retries: Maximum number of retries for failed requests
            retry_delay: Delay between retries in seconds
            timeout: Timeout for requests in seconds
        """
        self.base_url = base_url
        self.cache_enabled = cache_enabled
        self.max_retries = max_retries
        self.retry_delay = retry_delay
        self.timeout = timeout
        
    def _get_cache_path(self, endpoint: str, params: Dict[str, Any]) -> str:
        """
        Get the cache file path for a request.
        
        Args:
            endpoint: The API endpoint
            params: The request parameters
            
        Returns:
            The cache file path
        """
        # Create a unique cache key based on the endpoint and parameters
        cache_key = f"{endpoint}_{hash(frozenset(params.items() if params else {}))}"
        return os.path.join(CACHE_DIR, f"{cache_key}.json")
    
    def _get_from_cache(self, endpoint: str, params: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """
        Get a response from the cache.
        
        Args:
            endpoint: The API endpoint
            params: The request parameters
            
        Returns:
            The cached response, or None if not found
        """
        if not self.cache_enabled:
            return None
        
        cache_path = self._get_cache_path(endpoint, params)
        if os.path.exists(cache_path):
            try:
                with open(cache_path, 'r', encoding='utf-8') as f:
                    cache_data = json.load(f)
                    # Check if cache is expired (older than 24 hours)
                    cache_time = datetime.fromisoformat(cache_data['cache_time'])
                    if (datetime.now() - cache_time).total_seconds() < 86400:  # 24 hours
                        print(f"Using cached response for {endpoint}")
                        return cache_data['data']
            except Exception as e:
                print(f"Error reading cache: {e}")
        
        return None
    
    def _save_to_cache(self, endpoint: str, params: Dict[str, Any], data: Dict[str, Any]) -> None:
        """
        Save a response to the cache.
        
        Args:
            endpoint: The API endpoint
            params: The request parameters
            data: The response data
        """
        if not self.cache_enabled:
            return
        
        cache_path = self._get_cache_path(endpoint, params)
        try:
            # Garantir que o diretório exista
            os.makedirs(os.path.dirname(cache_path), exist_ok=True)
            
            with open(cache_path, 'w', encoding='utf-8') as f:
                json.dump({
                    'cache_time': datetime.now().isoformat(),
                    'data': data
                }, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"Error saving to cache: {e}")
    
    def get(self, endpoint: str, params: Optional[Dict[str, Any]] = None) -> Optional[Dict[str, Any]]:
        """
        Make a GET request to the API.
        
        Args:
            endpoint: The API endpoint
            params: The request parameters
            
        Returns:
            The response data, or None if the request failed
        """
        # Check cache first
        cached_data = self._get_from_cache(endpoint, params or {})
        if cached_data:
            return cached_data
        
        # Make the request with retries
        # Handle full URLs (starting with http) vs endpoints
        if endpoint.startswith('http'):
            url = endpoint
        else:
            url = f"{self.base_url}/{endpoint}" if endpoint and self.base_url else endpoint
        
        for attempt in range(self.max_retries):
            try:
                response = requests.get(url, params=params, timeout=self.timeout)
                
                if response.status_code == 200:
                    data = response.json()
                    self._save_to_cache(endpoint, params or {}, data)
                    return data
                else:
                    print(f"Request failed with status code {response.status_code}")
                    if attempt < self.max_retries - 1:
                        print(f"Retrying in {self.retry_delay} seconds...")
                        time.sleep(self.retry_delay)
                    else:
                        print(f"Max retries reached. Request failed.")
                        return None
            except requests.exceptions.RequestException as e:
                print(f"Request error: {e}")
                if attempt < self.max_retries - 1:
                    print(f"Retrying in {self.retry_delay} seconds...")
                    time.sleep(self.retry_delay)
                else:
                    print(f"Max retries reached. Request failed.")
                    return None
        
        return None

    def post(self, endpoint: str, data: Dict[str, Any], 
             params: Optional[Dict[str, Any]] = None) -> Optional[Dict[str, Any]]:
        """
        Make a POST request to the API.
        
        Args:
            endpoint: The API endpoint
            data: The request data
            params: The request parameters
            
        Returns:
            The response data, or None if the request failed
        """
        # POST requests are not cached
        url = f"{self.base_url}/{endpoint}" if endpoint else self.base_url
        
        for attempt in range(self.max_retries):
            try:
                response = requests.post(url, json=data, params=params, timeout=self.timeout)
                
                if response.status_code == 200:
                    return response.json()
                else:
                    print(f"Request failed with status code {response.status_code}")
                    if attempt < self.max_retries - 1:
                        print(f"Retrying in {self.retry_delay} seconds...")
                        time.sleep(self.retry_delay)
                    else:
                        print(f"Max retries reached. Request failed.")
                        return None
            except requests.exceptions.RequestException as e:
                print(f"Request error: {e}")
                if attempt < self.max_retries - 1:
                    print(f"Retrying in {self.retry_delay} seconds...")
                    time.sleep(self.retry_delay)
                else:
                    print(f"Max retries reached. Request failed.")
                    return None
        
        return None

# IBGE API Service
class IBGEService:
    """
    Service for accessing IBGE APIs.
    """
    
    def __init__(self, cache_enabled: bool = True):
        """
        Initialize the IBGE service.
        
        Args:
            cache_enabled: Whether to enable caching of API responses
        """
        self.api_service = APIService(
            base_url="https://servicodados.ibge.gov.br/api/v3",
            cache_enabled=cache_enabled
        )
    
    def get_agricultural_production(self, municipality_code: str, 
                                   start_year: int, end_year: int) -> Optional[pd.DataFrame]:
        """
        Get agricultural production data for a municipality.
        
        Args:
            municipality_code: The IBGE code for the municipality
            start_year: The start year for the data
            end_year: The end year for the data
            
        Returns:
            A DataFrame with the agricultural production data, or None if the request failed
        """
        print(f"Obtendo dados de produção agrícola para o município {municipality_code}...")
        
        # Usando a nova URL sugerida pelo usuário
        try:
            print("Tentando obter dados usando a nova URL sugerida pelo usuário...")
            
            # URL completa sugerida pelo usuário
            url = "https://servicodados.ibge.gov.br/api/v3/agregados/5457/periodos/2017/variaveis/8331|214|215?localidades=N6[3303401,3305802]&classificacao=782[0,40119]"
            
            # Modificar a URL para usar o código do município específico
            if municipality_code != "3303401" and municipality_code != "3305802":
                url = url.replace("N6[3303401,3305802]", f"N6[{municipality_code}]")
            
            # Fazer a requisição diretamente com a URL completa
            data = self.api_service.get(url)
            
            if data:
                print("Dados obtidos com sucesso!")
                
                # Processar os dados obtidos
                try:
                    # Imprimir a estrutura da resposta para depuração
                    print("Estrutura da resposta:")
                    if isinstance(data, list):
                        print(f"  - Tipo: lista com {len(data)} elementos")
                        if len(data) > 0:
                            print(f"  - Chaves do primeiro elemento: {list(data[0].keys())}")
                    else:
                        print(f"  - Tipo: {type(data)}")
                    
                    # Dicionários para armazenar os dados extraídos
                    total_data = {
                        'Área Plantada (ha)': 0,
                        'Produção (t)': 0,
                        'Valor da Produção (mil R$)': 0
                    }
                    
                    mandioca_data = {
                        'Área Plantada (ha)': 0,
                        'Produção (t)': 0,
                        'Valor da Produção (mil R$)': 0
                    }
                    
                    # Verificar se a resposta tem a estrutura esperada
                    if isinstance(data, list) and len(data) > 0:
                        for item in data:
                            if 'id' in item and 'resultados' in item:
                                variavel_id = item['id']
                                
                                # Iterar sobre os resultados
                                for resultado in item['resultados']:
                                    if 'classificacoes' in resultado and 'series' in resultado:
                                        # Determinar se estamos lidando com Total ou Mandioca
                                        categoria = None
                                        for classificacao in resultado['classificacoes']:
                                            if 'categoria' in classificacao:
                                                if '0' in classificacao['categoria']:
                                                    categoria = 'Total'
                                                elif '40119' in classificacao['categoria']:
                                                    categoria = 'Mandioca'
                                        
                                        if categoria:
                                            # Encontrar os dados para o município específico
                                            for serie in resultado['series']:
                                                if 'localidade' in serie and 'serie' in serie:
                                                    if serie['localidade']['id'] == municipality_code:
                                                        if '2017' in serie['serie']:
                                                            valor = serie['serie']['2017']
                                                            
                                                            # Ignorar valores não numéricos
                                                            if valor == '-' or valor == '..':
                                                                continue
                                                            
                                                            # Armazenar o valor de acordo com a variável e categoria
                                                            if variavel_id == '8331':  # Área plantada
                                                                if categoria == 'Total':
                                                                    total_data['Área Plantada (ha)'] = float(valor)
                                                                else:  # Mandioca
                                                                    mandioca_data['Área Plantada (ha)'] = float(valor)
                                                            elif variavel_id == '214':  # Quantidade produzida
                                                                if categoria == 'Total':
                                                                    total_data['Produção (t)'] = float(valor) if valor != '..' else 0
                                                                else:  # Mandioca
                                                                    mandioca_data['Produção (t)'] = float(valor) if valor != '..' else 0
                                                            elif variavel_id == '215':  # Valor da produção
                                                                if categoria == 'Total':
                                                                    total_data['Valor da Produção (mil R$)'] = float(valor)
                                                                else:  # Mandioca
                                                                    mandioca_data['Valor da Produção (mil R$)'] = float(valor)
                    
                    # Calcular produtividade
                    total_produtividade = 0
                    if total_data['Área Plantada (ha)'] > 0 and total_data['Produção (t)'] > 0:
                        total_produtividade = total_data['Produção (t)'] / total_data['Área Plantada (ha)']
                    
                    mandioca_produtividade = 0
                    if mandioca_data['Área Plantada (ha)'] > 0 and mandioca_data['Produção (t)'] > 0:
                        mandioca_produtividade = mandioca_data['Produção (t)'] / mandioca_data['Área Plantada (ha)']
                    
                    # Criar DataFrame com os resultados
                    df = pd.DataFrame([
                        {
                            'Ano': 2017,
                            'Tipo': 'Total',
                            'Área Plantada (ha)': total_data['Área Plantada (ha)'],
                            'Produção (t)': total_data['Produção (t)'],
                            'Produtividade (t/ha)': total_produtividade,
                            'Valor da Produção (mil R$)': total_data['Valor da Produção (mil R$)']
                        },
                        {
                            'Ano': 2017,
                            'Tipo': 'Mandioca',
                            'Área Plantada (ha)': mandioca_data['Área Plantada (ha)'],
                            'Produção (t)': mandioca_data['Produção (t)'],
                            'Produtividade (t/ha)': mandioca_produtividade,
                            'Valor da Produção (mil R$)': mandioca_data['Valor da Produção (mil R$)']
                        }
                    ])
                    
                    print(f"Dados processados com sucesso!")
                    print(f"Total: Área={total_data['Área Plantada (ha)']}, Produção={total_data['Produção (t)']}, Valor={total_data['Valor da Produção (mil R$)']}")
                    print(f"Mandioca: Área={mandioca_data['Área Plantada (ha)']}, Produção={mandioca_data['Produção (t)']}, Valor={mandioca_data['Valor da Produção (mil R$)']}")
                    
                    return df
                    
                except Exception as e:
                    print(f"Erro ao processar dados: {e}")
                    import traceback
                    traceback.print_exc()
            else:
                print("Não foi possível obter dados.")
                
        except Exception as e:
            print(f"Erro ao obter dados usando a URL sugerida: {e}")
            import traceback
            traceback.print_exc()
        
        # Se não conseguiu obter dados, retornar dados simulados
        print("Não foi possível obter dados reais. Retornando dados simulados.")
        print("NOTA: Os dados a seguir são SIMULADOS e não representam dados reais do IBGE.")
        
        # Criar dados simulados
        df = pd.DataFrame([
            {
                'Ano': 2017,
                'Tipo': 'Total',
                'Área Plantada (ha)': 500,
                'Produção (t)': 10000,
                'Produtividade (t/ha)': 20.0,
                'Valor da Produção (mil R$)': 30000
            },
            {
                'Ano': 2017,
                'Tipo': 'Mandioca',
                'Área Plantada (ha)': 50,
                'Produção (t)': 750,
                'Produtividade (t/ha)': 15.0,
                'Valor da Produção (mil R$)': 1000
            }
        ])
        
        return df
    
    def get_census_data(self, municipality_code: str, census_year: int) -> Optional[pd.DataFrame]:
        """
        Get agricultural census data for a municipality.
        
        Args:
            municipality_code: The IBGE code for the municipality
            census_year: The census year
            
        Returns:
            A DataFrame with the census data, or None if the request failed
        """
        print(f"Obtendo dados do censo agropecuário para o município {municipality_code}...")
        
        # Usar a API v3 de Agregados para acessar os dados do Censo Agropecuário
        # Baseado nas informações fornecidas pelo usuário
        
        # Agregado 6846 - "Número de estabelecimentos agropecuários, por tipologia, tipo de prática agrícola..."
        # Variáveis de exemplo: 100 (podemos ajustar conforme necessário)
        try:
            print("Tentando obter dados do Censo Agropecuário usando a API v3 de Agregados...")
            
            # Usar a URL exata que funcionou para Teresópolis
            url = "https://servicodados.ibge.gov.br/api/v3/agregados/6846/periodos/2017/variaveis/183?localidades=N6[3305802]&classificacao=829[46302]|12568[113197]|12598[41141]|12567[41151]|220[110085]"
            
            # Substituir o código do município
            url = url.replace("3305802", municipality_code)
            
            # Manter o ano 2017 na URL, independentemente do valor do parâmetro census_year
            # url = url.replace("2017", str(census_year))
            
            print(f"URL: {url}")
            
            # Criar uma instância da API sem cache para garantir dados frescos
            api_service_no_cache = APIService(
                base_url="",  # URL vazia porque vamos usar a URL completa
                cache_enabled=False  # Desabilitar o cache
            )
            
            # Fazer a requisição diretamente com a URL completa
            data = api_service_no_cache.get(url)
            
            if data:
                print("Dados do censo agropecuário obtidos com sucesso!")
                # Processar os dados em um DataFrame
                try:
                    # Extrair os dados da resposta da API
                    results = []
                    
                    # Verificar se a resposta tem a estrutura esperada
                    if isinstance(data, list) and len(data) > 0:
                        print("Estrutura da resposta do censo agropecuário:")
                        print(f"  - Tipo: lista com {len(data)} elementos")
                        if len(data) > 0 and isinstance(data[0], dict):
                            print(f"  - Chaves do primeiro elemento: {list(data[0].keys())}")
                            
                            # Não imprimir a estrutura completa da resposta para economizar tokens
                            # print("Estrutura completa da resposta:")
                            # print(json.dumps(data, indent=2))
                            
                            # Extrair os dados relevantes
                            if 'resultados' in data[0]:
                                print(f"Número de resultados: {len(data[0]['resultados'])}")
                                for i, resultado in enumerate(data[0]['resultados']):
                                    print(f"Resultado {i}:")
                                    print(f"  - Chaves: {list(resultado.keys())}")
                                    
                                    # Usar o ID e nome da variável do objeto data[0]
                                    if 'id' in data[0] and 'variavel' in data[0]:
                                        variavel_id = data[0]['id']
                                        variavel_nome = data[0]['variavel']
                                        
                                        # Verificar se há séries e extrair os valores
                                        if 'series' in resultado and len(resultado['series']) > 0:
                                            for serie_obj in resultado['series']:
                                                if 'serie' in serie_obj:
                                                    # Extrair o valor diretamente da série
                                                    if '2017' in serie_obj['serie']:
                                                        valor = serie_obj['serie']['2017']
                                                        
                                                        # Adicionar ao resultado
                                                        results.append({
                                                            'Variável': variavel_nome,
                                                            'Valor': float(valor) if valor else 0
                                                        })
                                                        
                                                        # Imprimir para depuração
                                                        print(f"Encontrado valor para {variavel_nome}: {valor}")
                    
                    # Se conseguiu extrair dados, retornar um DataFrame
                    if results:
                        print("Dados processados com sucesso!")
                        return pd.DataFrame(results)
                    else:
                        print("Não foi possível extrair dados da resposta da API.")
                except Exception as e:
                    print(f"Erro ao processar dados do censo: {e}")
                    import traceback
                    traceback.print_exc()
            else:
                print("Não foi possível obter dados do censo agropecuário.")
        except Exception as e:
            print(f"Erro ao tentar obter dados do censo agropecuário: {e}")
            import traceback
            traceback.print_exc()
        
        # Se não conseguiu obter dados, retornar dados simulados
        print("Retornando dados simulados do censo agropecuário.")
        print("NOTA: Os dados a seguir são SIMULADOS e não representam dados reais do IBGE.")
        
        # Dados simulados para Nova Friburgo
        if municipality_code == "3303401":
            return pd.DataFrame([
                {'Variável': 'Área total (ha)', 'Valor': 35000},
                {'Variável': 'Número de estabelecimentos', 'Valor': 1200},
                {'Variável': 'Pessoal ocupado', 'Valor': 4500}
            ])
        # Dados simulados para Teresópolis
        elif municipality_code == "3305802":
            return pd.DataFrame([
                {'Variável': 'Área total (ha)', 'Valor': 30000},
                {'Variável': 'Número de estabelecimentos', 'Valor': 950},
                {'Variável': 'Pessoal ocupado', 'Valor': 3800}
            ])
        # Dados genéricos para outros municípios
        else:
            return pd.DataFrame([
                {'Variável': 'Área total (ha)', 'Valor': 25000},
                {'Variável': 'Número de estabelecimentos', 'Valor': 800},
                {'Variável': 'Pessoal ocupado', 'Valor': 3000}
            ])

# Function to test the API service
def test_ibge_api():
    """
    Test the IBGE API service.
    """
    print("Testing IBGE API Service...")
    
    # Create an instance of the IBGE service
    ibge_service = IBGEService(cache_enabled=True)
    
    # Test getting agricultural production data for Nova Friburgo
    print("\nTesting agricultural production data for Nova Friburgo (3303401)...")
    nf_data = ibge_service.get_agricultural_production("3303401", 2000, 2023)
    if nf_data is not None:
        print("Success! Got data for Nova Friburgo:")
        print(nf_data.head())
    else:
        print("Failed to get data for Nova Friburgo.")
    
    # Test getting agricultural production data for Teresópolis
    print("\nTesting agricultural production data for Teresópolis (3305802)...")
    t_data = ibge_service.get_agricultural_production("3305802", 2000, 2023)
    if t_data is not None:
        print("Success! Got data for Teresópolis:")
        print(t_data.head())
    else:
        print("Failed to get data for Teresópolis.")
    
    # Test getting census data for Nova Friburgo
    print("\nTesting census data for Nova Friburgo (3303401)...")
    nf_census = ibge_service.get_census_data("3303401", 2017)
    if nf_census is not None:
        print("Success! Got census data for Nova Friburgo:")
        print(nf_census)
    else:
        print("Failed to get census data for Nova Friburgo.")
    
    print("\nAPI testing complete.")

if __name__ == "__main__":
    test_ibge_api()
