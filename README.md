# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
<a href= "https://www.fiap.com.br/"><img src="assets/logo-fiap.png" alt="FIAP - Faculdade de Informática e Admnistração Paulista" border="0" width=40% height=40%></a>
</p>

<br>

# Challenge Ingredion - Modelo de IA para Previsão de Produtividade Agrícola

> **IMPORTANTE**: Atualmente estamos na fase do **Sprint 2**, focado no desenvolvimento do modelo de IA para previsão de produtividade agrícola.

## 🔗 Links Importantes

### Sprint 1: Análise de Dados de NDVI/EVI
- [Documentação Completa do Sprint 1](sprint1/README.md)
- [PDF do Projeto Sprint 1](sprint1/GabrielMule_RM560586.pdf)
- [Notebook Completo do Sprint 1](sprint1/notebooks/GabrielMule_RM560586.ipynb)

### Sprint 2: Modelo de IA para Previsão de Produtividade
- [Documentação Completa do Sprint 2](sprint2/README.md)
- [Checklist do Sprint 2](sprint2/checklist_sprint2.md)
- [Instruções do Sprint 2](sprint2/instructions-sprint2.md)
- [Resumo dos Notebooks do Sprint 2](sprint2/resumo_notebooks.md)

## 👨‍🎓 Integrantes: 
- <a href="https://www.linkedin.com/in/gabemule/">Gabriel Mule Monteiro - RM560586</a>

## 👩‍🏫 Professores:
### Tutor(a) 
- <a href="https://www.linkedin.com/company/inova-fusca">Lucas Gomes Moreira</a>

## 📜 Descrição do Projeto

Este projeto faz parte do Challenge Ingredion, que tem como objetivo explorar a plataforma [SATVeg](https://www.satveg.cnptia.embrapa.br) e desenvolver um modelo de IA para previsão de produtividade agrícola utilizando os índices vegetativos NDVI (Índice de Vegetação por Diferença Normalizada) e EVI (Índice de Vegetação Melhorado).

O projeto está dividido em dois sprints:

### Sprint 1: Análise de Dados de NDVI/EVI
No Sprint 1, exploramos a plataforma SATVeg e analisamos os dados de NDVI/EVI para as regiões de Nova Friburgo e Teresópolis, no estado do Rio de Janeiro. Realizamos uma análise exploratória dos dados, identificamos padrões e tendências, e preparamos o terreno para o desenvolvimento do modelo de IA.

### Sprint 2: Modelo de IA para Previsão de Produtividade
No Sprint 2, estamos utilizando os dados analisados no Sprint 1 para desenvolver um modelo de IA capaz de prever a produtividade agrícola com base nos índices vegetativos. Estamos realizando o pré-processamento dos dados, a extração de informações relevantes, a construção e otimização do modelo, e a avaliação dos resultados.

## 📊 Principais Resultados

### Sprint 1
- Análise da evolução temporal e sazonalidade dos índices NDVI e EVI
- Identificação de tendências anuais e variabilidade dos índices
- Comparação entre os índices NDVI e EVI para diferentes regiões
- Análise da distribuição dos índices por mês e por ano

### Sprint 2
- Identificação das variáveis-chave para a previsão de produtividade agrícola
- Desenvolvimento de um modelo de IA para previsão de produtividade
- Avaliação do desempenho do modelo utilizando métricas como RMSE, MAE e R²
- Interpretação dos resultados e identificação dos fatores que mais influenciam a produtividade

## 📁 Estrutura do Projeto

```
projeto/
├── assets/                  # Arquivos de dados e imagens comuns
├── sprint1/                 # Arquivos do Sprint 1
│   ├── notebooks/           # Notebooks do Sprint 1
│   ├── markdown/            # Arquivos markdown do Sprint 1
│   ├── GabrielMule_RM560586.pdf  # PDF do Sprint 1
│   └── README.md            # Documentação do Sprint 1
├── sprint2/                 # Arquivos do Sprint 2
│   ├── assets/              # Dados processados do Sprint 2
│   ├── notebooks/           # Notebooks do Sprint 2
│   ├── models/              # Modelos treinados
│   ├── optimized_models/    # Modelos otimizados
│   ├── final_model/         # Modelo final
│   ├── checklist_sprint2.md # Checklist do Sprint 2
│   ├── instructions-sprint2.md  # Instruções do Sprint 2
│   ├── resumo_notebooks.md  # Resumo dos notebooks do Sprint 2
│   └── README.md            # Documentação do Sprint 2
├── api_service.py           # Serviço de API para acessar dados
├── convert_xlsx_to_csv.py   # Script para converter arquivos XLSX para CSV
├── merge_notebooks.py       # Script para mesclar notebooks
├── setup_env.sh             # Script para configurar o ambiente
├── requirements.txt         # Dependências do projeto
└── README.md                # Este arquivo
```

## 📺 Demonstração

O projeto pode ser testado através dos notebooks Jupyter em cada sprint:

### Sprint 1
- Carregamento e preparação dos dados de NDVI/EVI
- Visualização e análise dos dados
- Identificação de padrões e tendências

### Sprint 2
- Pré-processamento dos dados de NDVI/EVI e produtividade agrícola
- Extração de informações relevantes para o modelo de IA
- Construção, treinamento e avaliação do modelo de IA
- Previsão de produtividade agrícola com base nos índices vegetativos

## 📋 Licença

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/">MODELO GIT FIAP por <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://fiap.com.br">Fiap</a> está licenciado sobre <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International</a>.</p>
