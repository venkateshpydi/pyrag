import logging

from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware

from api.rag_controller import router as rag_router
from api.health_controller import router as health_router

# --------------------------------------------------
# Logging
# --------------------------------------------------

logging.basicConfig(
    level=logging.INFO,
    format=(
        "%(asctime)s | "
        "%(levelname)s | "
        "%(name)s | "
        "%(message)s"
    )
)

# --------------------------------------------------
# App
# --------------------------------------------------

app = FastAPI(
    title="RAG API",
    version="1.0.0"
)

# --------------------------------------------------
# CORS
# --------------------------------------------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:4200"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# --------------------------------------------------
# Routes
# --------------------------------------------------

app.include_router(
    rag_router
)

app.include_router(
    health_router
)