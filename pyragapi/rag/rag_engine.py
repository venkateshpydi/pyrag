import os
import logging

from dotenv import load_dotenv

from langchain_community.vectorstores import Chroma

from langchain_openai import (
    ChatOpenAI,
    OpenAIEmbeddings
)

logger = logging.getLogger(__name__)


class RagEngine:

    def __init__(self):

        load_dotenv()

        self.db_directory = "chroma_db"

        self.embeddings = OpenAIEmbeddings()

        self.llm = ChatOpenAI(
            model="gpt-4o-mini",
            temperature=0
        )

    def _load_vector_store(self):

        logger.info(
            "Loading ChromaDB"
        )

        return Chroma(
            persist_directory=self.db_directory,
            embedding_function=self.embeddings
        )

    def ask(
        self,
        question: str
    ) -> str:

        try:

            db = self._load_vector_store()

            docs = db.similarity_search(
                question,
                k=3
            )

            context = "\n\n".join(
                doc.page_content
                for doc in docs
            )

            prompt = f"""
You are a helpful assistant.

Use ONLY the supplied context.

If answer is not available in the context,
say:

I could not find the answer in the documents.

Context:
{context}

Question:
{question}
"""

            logger.info(
                "Sending prompt to LLM"
            )

            response = self.llm.invoke(
                prompt
            )

            return response.content

        except Exception as ex:

            logger.exception(
                "Error during RAG execution"
            )

            raise RuntimeError(
                str(ex)
            )