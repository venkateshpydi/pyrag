from datetime import datetime

from fastapi import APIRouter

router = APIRouter(
    tags=["Health"]
)


@router.get("/health")
def health():

    return {
        "status": "UP",
        "service": "rag-api",
        "timestamp": datetime.utcnow()
    }


@router.get("/health/live")
def liveness():

    return {
        "status": "alive"
    }


@router.get("/health/ready")
def readiness():

    return {
        "status": "ready"
    }