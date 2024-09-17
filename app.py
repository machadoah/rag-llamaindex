from typing import Dict

from fastapi import FastAPI
from llama_index.core import Response

from rag import querying, ingest
from schemas import Question, Answer, Members

app = FastAPI(description="RAG - Fatecana")

# Cria o índice e o motor de consulta uma vez para uso nas requisições
index = ingest()
query_engine = querying(index)


@app.get("/", response_model=Members, tags=["Root 🦙"])
def read_root():
    """
    Leitura GET da raiz

    :return:
        Conjunto com os membros do grupo
    """
    return {
        "Members": {
            "Antonio Henrique Nascimento Machado de Souza",
            "Isadora Mota de Souza",
            "Ingridy Guerra Rosa Cordeiro",
        }
    }


@app.post("/question/", response_model=Answer, tags=["Query 🦙"])
def query(question: Question) -> Dict[str, str]:
    """
    Realiza uma consulta ao índice e retorna a resposta.

    :arg question:
        question (Question): A pergunta a ser consultada.

    :return:
        Answer: A resposta à pergunta consultada.
    """
    # Usa o atributo correto da classe Question
    answer = query_engine.query(question.question)
    return {"answer": answer.response}
