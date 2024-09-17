from llama_index.core.base.base_query_engine import BaseQueryEngine
from llama_index.core.readers.file.base import SimpleDirectoryReader

# Responsável por ler documentos de um diretório e prepará-los para serem indexados.

from llama_index.core import VectorStoreIndex

# Constrói um índice vetorial dos documentos carregados, permitindo a realização de consultas.

from dotenv import load_dotenv

from loguru import logger

load_dotenv()


def ingest() -> VectorStoreIndex:
    """
    Carrega documentos do diretório, cria um índice vetorial a partir dos documentos e o persiste em um arquivo.

    Returns:
        VectorStoreIndex: O índice vetorial criado.
    """

    # Carrega os documentos do diretório
    documents = SimpleDirectoryReader("data").load_data()

    # Cria o índice a partir dos documentos
    index = VectorStoreIndex.from_documents(documents)

    # Salva o índice em um arquivo
    index.storage_context.persist(persist_dir="index")

    logger.info("Índice criado com sucesso!")

    return index


def querying(index: VectorStoreIndex) -> BaseQueryEngine:
    """
    Cria um motor de consulta (QueryEngine) a partir do índice fornecido.

    Args:
        index (VectorStoreIndex): O índice a ser usado pelo motor de consulta.

    Returns:
        BaseQueryEngine: O motor de consulta configurado.
    """

    # Retorna o motor de consulta (QueryEngine)

    logger.info("Motor de consulta criado com sucesso!")

    return index.as_query_engine()


if __name__ == "__main__":
    index = ingest()

    print(
        """
    Olá, bem vindo ao assistente da Fatec!
    
    Você pode perguntar sobre informações relacionados ao curso ou a diciplina de TEI.
    
    Caso queira sair digite algo como exit, quit ou 0!
    
    Obrigado!
    """
    )

    query_engine = querying(index)

    while True:
        pergunta = input("Insira sua pergunta: ")

        if pergunta.lower() in [
            "q",
            "quit",
            "exit",
            "quit()",
            "exit()",
            "0",
            "sair",
            "parar",
            "stop",
        ]:
            break

        # Realiza uma consulta usando o motor de consulta
        r = query_engine.query(pergunta)

        logger.info("Pesquisando na base de dados...")

        print(r)
