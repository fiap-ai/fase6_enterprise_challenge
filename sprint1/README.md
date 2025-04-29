# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
<a href= "https://www.fiap.com.br/"><img src="assets/logo-fiap.png" alt="FIAP - Faculdade de Informática e Admnistração Paulista" border="0" width=40% height=40%></a>
</p>

<br>

# Challenge Ingredion - Sprint 1: Análise de Dados de NDVI/EVI para Previsão de Produtividade Agrícola

## 🔗 Links Importantes
- [PDF do Projeto](GabrielMule_RM560586.pdf)  
- [Notebook Completo do Projeto](notebooks/GabrielMule_RM560586.ipynb)
- [Notebook Fase 5A: Preparação dos Dados NDVI/EVI](notebooks/fase5a_preparacao_dados_ndvi_parte1.ipynb)
- [Notebook Fase 5B: Visualização dos Dados NDVI/EVI (Parte 1)](notebooks/fase5b_visualizacao_dados_ndvi_parte1.ipynb)
- [Notebook Fase 5C: Visualização dos Dados NDVI/EVI (Parte 2)](notebooks/fase5c_visualizacao_dados_ndvi_parte2.ipynb)
- [Notebook Fase 5D: Visualização dos Dados NDVI/EVI (Parte 3)](notebooks/fase5d_visualizacao_dados_ndvi_parte3.ipynb)
- [Notebook Fase 5E: Conclusão da Análise NDVI/EVI](notebooks/fase5e_conclusao_ndvi.ipynb)

## 👨‍🎓 Integrantes: 
- <a href="https://www.linkedin.com/in/gabemule/">Gabriel Mule Monteiro - RM560586</a>

## 👩‍🏫 Professores:
### Tutor(a) 
- <a href="https://www.linkedin.com/company/inova-fusca">Lucas Gomes Moreira</a>

## 📜 Descrição

Este projeto faz parte do Challenge Ingredion - Sprint 1, que tem como objetivo explorar a plataforma [SATVeg](https://www.satveg.cnptia.embrapa.br) e entender como os índices vegetativos NDVI (Índice de Vegetação por Diferença Normalizada) e EVI (Índice de Vegetação Melhorado) podem ser utilizados para prever a produtividade agrícola.

A plataforma SATVeg, desenvolvida pela Embrapa, permite o acesso a séries temporais de índices vegetativos derivados de imagens de satélite, que são indicadores da saúde e do vigor da vegetação. Esses índices têm sido amplamente utilizados para monitorar culturas agrícolas e prever a produtividade.

Neste projeto, exploramos os dados de NDVI/EVI para as regiões de Nova Friburgo e Teresópolis, no estado do Rio de Janeiro, e analisamos como esses índices podem ser correlacionados com a produtividade agrícola.

## 📊 Análise de Dados

### Fase 5A: Preparação dos Dados NDVI/EVI
- Carregamento dos dados de NDVI/EVI para Nova Friburgo e Teresópolis
- Verificação e tratamento de valores ausentes
- Conversão da coluna de data para o formato adequado
- Extração do ano e mês da data
- Cálculo de estatísticas mensais e anuais dos índices

### Fase 5B: Visualização dos Dados NDVI/EVI (Parte 1)
- Análise da evolução temporal dos índices NDVI e EVI
- Análise da sazonalidade dos índices
- Identificação de padrões e tendências nos dados

### Fase 5C: Visualização dos Dados NDVI/EVI (Parte 2)
- Análise da tendência anual dos índices NDVI e EVI
- Comparação entre os índices NDVI e EVI
- Identificação de correlações entre os índices

### Fase 5D: Visualização dos Dados NDVI/EVI (Parte 3)
- Análise da variabilidade dos índices por mês (boxplots)
- Análise da variabilidade anual dos índices
- Análise da amplitude anual dos índices

### Fase 5E: Conclusão da Análise NDVI/EVI
- Resumo das análises realizadas
- Principais conclusões sobre os dados de NDVI/EVI
- Implicações para a previsão de produtividade agrícola
- Próximos passos para o desenvolvimento de modelos de previsão

## 🌱 Resultados Principais

Os principais resultados obtidos neste projeto são:

1. **Evolução Temporal e Sazonalidade**: Observamos uma variação sazonal nos índices NDVI e EVI ao longo dos anos, com picos e vales que se repetem anualmente. Também notamos uma tendência geral de aumento nos valores dos índices ao longo do período analisado.

2. **Tendência Anual e Variabilidade**: Identificamos uma tendência de crescimento nos índices NDVI e EVI ao longo dos anos para ambas as regiões, o que indica uma melhoria na cobertura vegetal e na saúde da vegetação.

3. **Comparação entre Índices e Regiões**: Verificamos que existe uma forte correlação positiva entre os índices NDVI e EVI para ambas as regiões. Além disso, Nova Friburgo apresenta, em geral, valores de NDVI e EVI ligeiramente superiores aos de Teresópolis.

4. **Distribuição dos Índices por Mês**: Confirmamos o padrão sazonal observado anteriormente, com valores mais altos e menor variabilidade nos meses de verão (dezembro a março) e valores mais baixos e maior variabilidade nos meses de inverno (junho a setembro).

## 📁 Estrutura de Arquivos

```
projeto/
├── assets/                  # Arquivos de dados e imagens
│   ├── logo-fiap.png
│   ├── satveg_grafico_nova_friburgo.png
│   ├── satveg_grafico_teresopolis.png
│   ├── satveg_planilha_nova_friburgo.csv
│   ├── satveg_planilha_nova_friburgo.xlsx
│   ├── satveg_planilha_teresopolis.csv
│   └── satveg_planilha_teresopolis.xlsx
├── notebooks/               # Jupyter notebooks
│   ├── fase0a_headers.ipynb
│   ├── fase0b_config.ipynb
│   ├── fase1a_intro_projeto.ipynb
│   ├── fase1b_metodologia.ipynb
│   ├── fase2a_satveg_conceitos.ipynb
│   ├── fase2b_ndvi_conceitos.ipynb
│   ├── fase2c_satveg_navegacao.ipynb
│   ├── fase2d_satveg_analise.ipynb
│   ├── fase3a_regiao_socioeconomia.ipynb
│   ├── fase3b_regiao_dados_ibge.ipynb
│   ├── fase3c_regiao_dados_censo.ipynb
│   ├── fase3d_regiao_dados_ceasa.ipynb
│   ├── fase4a_bases_dados_ibge.ipynb
│   ├── fase4b_bases_dados_embrapa.ipynb
│   ├── fase4c_bases_dados_outras1.ipynb
│   ├── fase4d_bases_dados_outras2.ipynb
│   ├── fase4e_coleta_dados_temporaria.ipynb
│   ├── fase4f_coleta_dados_permanente.ipynb
│   ├── fase4g_analise_exploratoria_parte1.ipynb
│   ├── fase4h_analise_exploratoria_parte2.ipynb
│   ├── fase5a_preparacao_dados_ndvi_parte1.ipynb
│   ├── fase5b_visualizacao_dados_ndvi_parte1.ipynb
│   ├── fase5c_visualizacao_dados_ndvi_parte2.ipynb
│   ├── fase5d_visualizacao_dados_ndvi_parte3.ipynb
│   ├── fase5e_conclusao_ndvi.ipynb
│   ├── GabrielMule_rm560586_pbl_fase6.ipynb
│   ├── setup_notebook.py    # Configuração do ambiente para os notebooks
│   └── utils.py             # Funções utilitárias
├── convert_xlsx_to_csv.py   # Script para converter arquivos XLSX para CSV
├── merge_notebooks.py       # Script para mesclar notebooks
├── setup_env.sh             # Script para configurar o ambiente
├── requirements.txt         # Dependências do projeto
├── checklist-sprint1.md     # Checklist para a Sprint 1
└── README.md                # Este arquivo
```

### Arquivos Principais:

1. **Fase 0: Configuração inicial**
   - **notebooks/fase0a_headers.ipynb**: Cabeçalhos e informações gerais
   - **notebooks/fase0b_config.ipynb**: Configuração do ambiente

2. **Fase 1: Introdução ao projeto**
   - **notebooks/fase1a_intro_projeto.ipynb**: Introdução e contextualização
   - **notebooks/fase1b_metodologia.ipynb**: Metodologia utilizada

3. **Fase 2: Exploração da plataforma SATVeg**
   - **notebooks/fase2a_satveg_conceitos.ipynb**: Conceitos da plataforma SATVeg
   - **notebooks/fase2b_ndvi_conceitos.ipynb**: Conceitos sobre NDVI e EVI
   - **notebooks/fase2c_satveg_navegacao.ipynb**: Navegação na plataforma
   - **notebooks/fase2d_satveg_analise.ipynb**: Análise das funcionalidades

4. **Fase 3: Análise da região de estudo**
   - **notebooks/fase3a_regiao_socioeconomia.ipynb**: Contexto socioeconômico
   - **notebooks/fase3b_regiao_dados_ibge.ipynb**: Dados do IBGE
   - **notebooks/fase3c_regiao_dados_censo.ipynb**: Dados do Censo
   - **notebooks/fase3d_regiao_dados_ceasa.ipynb**: Dados do CEASA

5. **Fase 4: Coleta e análise exploratória de dados**
   - **notebooks/fase4a_bases_dados_ibge.ipynb**: Bases de dados do IBGE
   - **notebooks/fase4b_bases_dados_embrapa.ipynb**: Bases de dados da Embrapa
   - **notebooks/fase4c_bases_dados_outras1.ipynb**: Outras bases de dados (parte 1)
   - **notebooks/fase4d_bases_dados_outras2.ipynb**: Outras bases de dados (parte 2)
   - **notebooks/fase4e_coleta_dados_temporaria.ipynb**: Coleta de dados temporários
   - **notebooks/fase4f_coleta_dados_permanente.ipynb**: Coleta de dados permanentes
   - **notebooks/fase4g_analise_exploratoria_parte1.ipynb**: Análise exploratória (parte 1)
   - **notebooks/fase4h_analise_exploratoria_parte2.ipynb**: Análise exploratória (parte 2)

6. **Fase 5: Preparação, visualização e conclusão**
   - **notebooks/fase5a_preparacao_dados_ndvi_parte1.ipynb**: Preparação dos dados de NDVI/EVI
   - **notebooks/fase5b_visualizacao_dados_ndvi_parte1.ipynb**: Visualização da evolução temporal e sazonalidade
   - **notebooks/fase5c_visualizacao_dados_ndvi_parte2.ipynb**: Visualização da tendência anual e comparação
   - **notebooks/fase5d_visualizacao_dados_ndvi_parte3.ipynb**: Visualização da variabilidade e amplitude
   - **notebooks/fase5e_conclusao_ndvi.ipynb**: Conclusões e implicações para previsão

## 📺 Demonstração

O projeto pode ser testado através dos notebooks Jupyter, que demonstram:
- Carregamento e preparação dos dados de NDVI/EVI
- Visualização e análise dos dados
- Identificação de padrões e tendências
- Conclusões e implicações para a previsão de produtividade

## 📋 Licença

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/">MODELO GIT FIAP por <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://fiap.com.br">Fiap</a> está licenciado sobre <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International</a>.</p>
