import logging

from rag.rag_engine import RagEngine

logger = logging.getLogger(__name__)


class RagService:

    def __init__(
        self,
        rag_engine: RagEngine
    ):
        self.rag_engine = rag_engine

    def ask(
        self,
        question: str
    ) -> str:

        try:

            logger.info(
                f"Received question: {question}"
            )

            answer = self.rag_engine.ask(
                question
            )

            logger.info(
                "Answer generated successfully"
            )

            return answer

        except Exception as ex:

            logger.exception(
                "Failed to generate answer"
            )

            raise RuntimeError(
                f"RAG processing failed: {str(ex)}"
            )

    def ask_with_sources(
        self,
        question: str
    ):

        try:

            logger.info(
                f"Received question: {question}"
            )

            result = self.rag_engine.ask_with_sources(
                question
            )

            return result

        except Exception as ex:

            logger.exception(
                "Failed to generate answer"
            )

            raise RuntimeError(
                f"RAG processing failed: {str(ex)}"
            )