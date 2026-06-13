from rag.rag_engine import RagEngine
from services.rag_service import RagService


def get_rag_service():

    rag_engine = RagEngine()

    return RagService(
        rag_engine
    )