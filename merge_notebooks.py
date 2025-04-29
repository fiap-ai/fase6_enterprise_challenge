#!/usr/bin/env python3
"""
Script para mesclar múltiplos notebooks Jupyter em um único arquivo.
Ordena automaticamente os notebooks com base em seus prefixos (fase0_, fase1a_, etc.).
"""

import json  # Usando json em vez de nbformat
import sys
import os
import re
import glob

def extract_prefix(filename):
    """
    Extrai o prefixo numérico do nome do arquivo para ordenação.
    Exemplo: 'fase1a_' de 'fase1a_intro.ipynb'
    """
    # Padrão para extrair prefixos como 'fase0_', 'fase1a_', etc.
    match = re.match(r'fase(\d+[a-z]?)_', os.path.basename(filename))
    if match:
        prefix = match.group(1)
        # Converter para um formato ordenável: '1a' -> '01a'
        if prefix.isdigit():
            return prefix.zfill(2)
        else:
            num_part = re.match(r'(\d+)', prefix).group(1)
            alpha_part = prefix[len(num_part):]
            return num_part.zfill(2) + alpha_part
    return '99'  # Arquivos sem prefixo vão para o final

def find_notebooks(directory='notebooks'):
    """
    Encontra todos os notebooks Jupyter no diretório especificado.
    """
    return glob.glob(os.path.join(directory, 'fase*.ipynb'))

def merge_notebooks(notebook_filenames, output_filename, output_directory='notebooks'):
    """
    Mescla múltiplos notebooks Jupyter em um único arquivo.
    
    Args:
        notebook_filenames: Lista de caminhos para os notebooks de entrada
        output_filename: Nome do arquivo de saída
        output_directory: Diretório onde o notebook de saída será criado (padrão: 'notebooks')
    """
    # Ordenar os notebooks por prefixo
    sorted_notebooks = sorted(notebook_filenames, key=extract_prefix)
    
    merged = None
    
    print(f"Mesclando {len(sorted_notebooks)} notebooks...")
    
    for i, filename in enumerate(sorted_notebooks):
        print(f"Processando {i+1}/{len(sorted_notebooks)}: {filename}")
        
        with open(filename, 'r', encoding='utf-8') as f:
            nb = json.load(f)
            
            # Se este é o primeiro notebook, usamos como base
            if merged is None:
                merged = nb
                print(f"  Usando {filename} como notebook base")
            else:
                # Para os notebooks subsequentes, adicionamos apenas as células
                # Adicionamos uma célula de markdown como separador
                base_name = os.path.basename(filename)
                section_name = base_name.replace('fase', 'Fase ').replace('.ipynb', '').replace('_', ' ').title()
                
                # Criar uma nova célula de markdown
                markdown_cell = {
                    "cell_type": "markdown",
                    "metadata": {},
                    "source": [f"## {section_name}"]
                }
                
                merged['cells'].append(markdown_cell)
                print(f"  Adicionando {len(nb['cells'])} células de {filename}")
                merged['cells'].extend(nb['cells'])
    
    # Escrever o notebook mesclado
    if merged:
        # Garantir que o diretório de saída exista
        os.makedirs(output_directory, exist_ok=True)
        
        # Construir o caminho completo do arquivo de saída
        output_path = os.path.join(output_directory, output_filename)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(merged, f, indent=1)
        print(f"\nNotebooks mesclados com sucesso em: {output_path}")
        print(f"Total de células no notebook final: {len(merged['cells'])}")
    else:
        print("Erro: Nenhum notebook foi processado.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python merge_notebooks.py output.ipynb [input1.ipynb input2.ipynb ...]")
        print("Se nenhum notebook de entrada for especificado, todos os notebooks no diretório 'notebooks' serão usados.")
        sys.exit(1)
    
    output_filename = sys.argv[1]
    output_directory = '.'  # Diretório raiz para o notebook de saída
    
    # Verificar se existe um notebook com o mesmo nome no diretório raiz e removê-lo
    if os.path.exists(os.path.join(output_directory, output_filename)):
        try:
            os.remove(output_filename)
            print(f"Arquivo existente removido: {output_filename}")
        except OSError as e:
            print(f"Erro ao remover arquivo existente: {e}")
    
    if len(sys.argv) > 2:
        notebook_filenames = sys.argv[2:]
    else:
        notebook_filenames = find_notebooks()
        if not notebook_filenames:
            print("Erro: Nenhum notebook encontrado no diretório 'notebooks'.")
            sys.exit(1)
    
    merge_notebooks(notebook_filenames, output_filename, output_directory)
