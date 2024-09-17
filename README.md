# RAG-TEI Index Demo

Este projeto demonstra como carregar documentos de um diretório, criar um índice vetorial a partir desses documentos usando `LlamaIndex` (anteriormente conhecido como `GPT Index`), e realizar consultas sobre o índice utilizando um motor de busca semântica.

# Arquitetura RAG - LlamaIndex 🦙

Repositório destinado a elaboração do trabalho do 2º bimestre da disciplina de Tópicos Especiais de Informática.

Link do slide: [Introdução ao Retrieval-Augmented Generation (RAG) - Com o framework LlamaIndex](https://docs.google.com/presentation/d/1TAnXDTgFxXv1jw243Ykxi02_fzLILPL80gAI8BAu77Y/edit#slide=id.p)

## Estrutura do Projeto

A estrutura do projeto é a seguinte:

```bash
.
├── app.py               # Script principal que cria e consulta o índice
├── index/           # Diretório contendo os dados persistidos do índice
│   ├── default__vector_store.json
│   ├── docstore.json
│   ├── graph_store.json
│   ├── image__vector_store.json
│   └── index_store.json
└── data/                    # Diretório com os documentos de entrada
    ├── fatec_pg_ads.txt
    ├── fatec_pg.txt
    ├── fatec_wikipedia.txt
    ├── grade_ads.txt
    └── tei.txt
```

## Arquivos Gerados

- `default__vector_store.json`:

Este arquivo contém os vetores gerados a partir dos documentos indexados. Cada documento é transformado em um vetor numérico, permitindo consultas semânticas. O VectorStore armazena esses vetores, que são usados para comparação e busca.

- `docstore.json`:

Armazena os documentos originais, que foram lidos e indexados. Cada documento é mapeado com um identificador único, permitindo sua recuperação e consulta. É essencial para vincular os vetores às suas representações textuais originais.

- `graph_store.json`:

Contém as relações e conexões entre os diferentes documentos e partes do índice. Esse arquivo é responsável por estruturar como os documentos estão conectados, possibilitando consultas que consideram o contexto entre eles.

- `image__vector_store.json`:

Similar ao `default__vector_store.json`, mas destinado ao armazenamento de vetores para dados de imagem. Se seu projeto não incluiu imagens, este arquivo pode estar vazio ou conter metadados genéricos.

- `index_store.json`:

Esse arquivo gerencia os metadados e a estrutura do índice em si, como os diferentes tipos de dados armazenados (vetores, documentos, etc.). Ele facilita o gerenciamento do índice e sua atualização futura.
Esses arquivos juntos formam o banco de dados vetorial completo necessário para fazer buscas eficientes e semânticas usando o VectorStoreIndex.

## Diretório data

Contém os arquivos de texto que foram carregados e indexados pelo `SimpleDirectoryReader`. Esses são os documentos de entrada que foram transformados em vetores e armazenados no índice.

## Funcionamento do projeto

1. **Carregar variáveis de ambiente:** O script usa `load_dotenv()` para carregar variáveis de ambiente, como chaves de API ou diretórios, a partir de um arquivo `.env`.

2. **Leitura de Documentos:** O `SimpleDirectoryReader` é usado para carregar os documentos do diretório news. Estes documentos são arquivos de texto simples que serão indexados.

3. **Criação do Índice:** O `VectorStoreIndex` cria um índice vetorial a partir dos documentos lidos. Esse índice transforma o conteúdo dos documentos em vetores numéricos, permitindo buscas semânticas.

4. Persistência do Índice: O índice gerado é salvo no diretório `index` para que possa ser reutilizado posteriormente.

5. **Consultas ao Índice:** O motor de consulta (`QueryEngine`) é criado a partir do índice, permitindo a realização de perguntas em linguagem natural. As consultas são respondidas com base na similaridade semântica entre a pergunta e os documentos indexados.

### Executando o projeto

1. Instale as dependências necessárias:

```bash
pip install llama-index dotenv
```

2. Coloque seus documentos no diretório `data`.

3. Execute o script principal:

```bash
python app.py
```
Faça perguntas para o motor de consulta e veja os resultados com base nos documentos indexados.

#### Requisitos
- Python 3.10 ou superior
- Pacotes Python: `llama-index`, `dotenv`

