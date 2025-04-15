#!/bin/bash
# Script para executar o teste do serviço de API

# Verificar se o ambiente virtual existe
if [ ! -d "venv" ]; then
    echo "Ambiente virtual não encontrado. Criando..."
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
else
    source venv/bin/activate
fi

# Verificar se o diretório cache existe
if [ ! -d "cache" ]; then
    echo "Criando diretório de cache..."
    mkdir cache
fi

# Executar o teste do serviço de API
echo "Executando teste do serviço de API..."
python test_api_service.py "$@"

# Desativar o ambiente virtual
deactivate

echo -e "\nTeste concluído!"
