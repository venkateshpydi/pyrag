import logging

from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import status

from models.rag_request import RagRequest
from models.rag_response import RagResponse

from services.rag_service import RagService
from dependencies import get_rag_service

# --------------------------------------------------
# Logger
# --------------------------------------------------

logger = logging.getLogger(__name__)

# --------------------------------------------------
# Router
# --------------------------------------------------

router = APIRouter(
    prefix="/api/v1/rag",
    tags=["RAG"]
)

# --------------------------------------------------
# Ask Question
# --------------------------------------------------

@router.post(
    "/ask",
    response_model=RagResponse,
    status_code=status.HTTP_200_OK
)
def ask_question(
    request: RagRequest,
    rag_service: RagService = Depends(get_rag_service)
):
    """
    Ask a question against the RAG engine.
    """

    try:

        logger.info(
            "Received RAG request. Question=%s",
            request.question
        )

        if not request.question.strip():

            logger.warning(
                "Empty question received"
            )

            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Question cannot be empty"
            )

        answer = rag_service.ask(
            request.question
        )

        logger.info(
            "Successfully generated response"
        )

        return RagResponse(
            answer=answer
        )

    except HTTPException:
        raise

    except ValueError as ex:

        logger.error(
            "Validation error: %s",
            str(ex)
        )

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(ex)
        )

    except RuntimeError as ex:

        logger.error(
            "RAG processing error: %s",
            str(ex),
            exc_info=True
        )

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Unable to process request"
        )

    except Exception as ex:

        logger.exception(
            "Unexpected error occurred"
        )

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error"
        )