# Documentação do Script `merge_notebooks.py`

## Visão Geral

O script `merge_notebooks.py` é uma ferramenta para mesclar múltiplos notebooks Jupyter em um único arquivo. Isso é útil para combinar notebooks de diferentes fases de um projeto em um notebook final consolidado. O script ordena automaticamente os notebooks com base em seus prefixos (fase0_, fase1a_, etc.).

## Funcionalidades

- Mescla múltiplos notebooks Jupyter (.ipynb) em um único arquivo
- Ordena automaticamente os notebooks com base em seus prefixos numéricos
- Mantém a formatação e estrutura original de cada notebook
- Adiciona células de markdown como separadores entre os notebooks, formatadas como "## Fase X Nome"
- Preserva todas as células (código, markdown, saídas) dos notebooks originais
- Encontra automaticamente todos os notebooks no diretório 'notebooks' se nenhum for especificado

## Requisitos

- Python 3.6 ou superior
- Biblioteca `json` (padrão do Python)

## Como Funciona

O script funciona da seguinte maneira:

1. Se nenhum notebook de entrada for especificado, encontra automaticamente todos os notebooks com prefixo "fase" no diretório 'notebooks'
2. Ordena os notebooks com base em seus prefixos numéricos (fase0_, fase1a_, etc.)
3. Usa o primeiro notebook como base para o notebook mesclado
4. Para cada notebook subsequente, adiciona uma célula de markdown como separador formatada como "## Fase X Nome"
5. Adiciona todas as células do notebook subsequente ao notebook mesclado
6. Salva o notebook mesclado no diretório 'notebooks' com o nome especificado

## Uso

```bash
python merge_notebooks.py <arquivo_saida.ipynb> [<arquivo_entrada1.ipynb> <arquivo_entrada2.ipynb> ...]
```

### Parâmetros

- `<arquivo_saida.ipynb>`: Nome do arquivo de notebook de saída (será criado ou sobrescrito)
- `[<arquivo_entrada1.ipynb> <arquivo_entrada2.ipynb> ...]`: Lista opcional de arquivos de notebook de entrada a serem mesclados. Se não for fornecida, todos os notebooks com prefixo "fase" no diretório 'notebooks' serão usados.

### Exemplos

#### Mesclar notebooks específicos

```bash
python merge_notebooks.py notebook_final.ipynb notebooks/fase1_preparo_ambiente.ipynb notebooks/fase2_analise_exploratoria.ipynb notebooks/fase3_clusterizacao.ipynb notebooks/fase4_modelagem_preditiva.ipynb
```

Este comando mesclará os notebooks especificados em um único arquivo chamado `notebook_final.ipynb` no diretório 'notebooks'.

#### Mesclar todos os notebooks automaticamente

```bash
python merge_notebooks.py notebook_final.ipynb
```

Este comando encontrará automaticamente todos os notebooks com prefixo "fase" no diretório 'notebooks', ordenará com base nos prefixos e os mesclará em um único arquivo chamado `notebook_final.ipynb`.

## Ordenação dos Notebooks

O script ordena automaticamente os notebooks com base em seus prefixos numéricos:

1. Extrai o prefixo numérico do nome do arquivo (por exemplo, '1a' de 'fase1a_intro.ipynb')
2. Converte para um formato ordenável ('1a' -> '01a')
3. Ordena os notebooks com base nesses prefixos

Isso garante que os notebooks sejam mesclados na ordem correta, independentemente da ordem em que são fornecidos na linha de comando.

## Saída do Script

Durante a execução, o script exibe informações sobre o processo de mesclagem:

```
Mesclando 4 notebooks...
Processando 1/4: notebooks/fase1_preparo_ambiente.ipynb
  Usando notebooks/fase1_preparo_ambiente.ipynb como notebook base
Processando 2/4: notebooks/fase2_analise_exploratoria.ipynb
  Adicionando 24 células de notebooks/fase2_analise_exploratoria.ipynb
Processando 3/4: notebooks/fase3_clusterizacao.ipynb
  Adicionando 28 células de notebooks/fase3_clusterizacao.ipynb
Processando 4/4: notebooks/fase4_modelagem_preditiva.ipynb
  Adicionando 16 células de notebooks/fase4_modelagem_preditiva.ipynb

Notebooks mesclados com sucesso em: notebooks/notebook_final.ipynb
Total de células no notebook final: 83
```

## Limitações

- O script assume que os notebooks seguem a convenção de nomenclatura com prefixos "fase" (por exemplo, fase0_, fase1a_, etc.)
- Notebooks sem o prefixo "fase" não serão encontrados automaticamente
- O script não verifica a compatibilidade entre os notebooks (por exemplo, dependências de variáveis)
- Não há opção para excluir células específicas durante a mesclagem
- Não há validação do conteúdo dos notebooks (é responsabilidade do usuário garantir que os notebooks sejam válidos)

## Dicas de Uso

1. **Verifique os notebooks antes da mesclagem**: Certifique-se de que cada notebook esteja funcionando corretamente antes de mesclá-los.

2. **Siga a convenção de nomenclatura**: Para aproveitar a ordenação automática, nomeie seus notebooks com prefixos "fase" seguidos de números e letras opcionais (por exemplo, fase0_, fase1a_, fase1b_, fase2_, etc.).

3. **Renomeie variáveis conflitantes**: Se houver variáveis com o mesmo nome em diferentes notebooks, considere renomeá-las para evitar conflitos.

4. **Adicione células de transição**: Após a mesclagem, pode ser útil adicionar células de markdown adicionais para melhorar a transição entre os notebooks.

5. **Execute o notebook mesclado**: Após a mesclagem, execute todas as células do notebook mesclado para garantir que tudo funcione corretamente.

6. **Faça backup dos notebooks originais**: Sempre mantenha cópias dos notebooks originais, caso precise fazer alterações.
