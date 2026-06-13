import os
from pathlib import Path

from dotenv import load_dotenv

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma

# --------------------------------------------------
# Load Environment Variables
# --------------------------------------------------

load_dotenv()

# --------------------------------------------------
# Configuration
# --------------------------------------------------

DATA_DIR = "data"
CHROMA_DB_DIR = "chroma_db"

CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200

# --------------------------------------------------
# Validate OpenAI Key
# --------------------------------------------------

if not os.getenv("OPENAI_API_KEY"):
    raise ValueError(
        "OPENAI_API_KEY is missing in .env file"
    )

# --------------------------------------------------
# Load PDFs
# --------------------------------------------------

documents = []

pdf_files = list(Path(DATA_DIR).glob("*.pdf"))

if not pdf_files:
    raise FileNotFoundError(
        f"No PDF files found in '{DATA_DIR}' folder"
    )

print(f"Found {len(pdf_files)} PDF(s)")

for pdf_file in pdf_files:

    print(f"Loading: {pdf_file.name}")

    loader = PyPDFLoader(str(pdf_file))

    docs = loader.load()

    documents.extend(docs)

print(
    f"Loaded {len(documents)} pages"
)

# --------------------------------------------------
# Split Documents
# --------------------------------------------------

print("Splitting documents...")

splitter = RecursiveCharacterTextSplitter(
    chunk_size=CHUNK_SIZE,
    chunk_overlap=CHUNK_OVERLAP
)

chunks = splitter.split_documents(
    documents
)

print(
    f"Created {len(chunks)} chunks"
)

# --------------------------------------------------
# Create Embeddings
# --------------------------------------------------

print("Creating embeddings...")

embeddings = OpenAIEmbeddings()

# --------------------------------------------------
# Delete Existing Chroma DB (Optional)
# --------------------------------------------------

if Path(CHROMA_DB_DIR).exists():

    import shutil

    shutil.rmtree(CHROMA_DB_DIR)

    print(
        "Existing Chroma DB removed"
    )

# --------------------------------------------------
# Create Vector Store
# --------------------------------------------------

print(
    "Storing vectors in ChromaDB..."
)

vector_store = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    persist_directory=CHROMA_DB_DIR
)

vector_store.persist()

print(
    "Ingestion completed successfully"
)

print(
    f"Database stored in: {CHROMA_DB_DIR}"
)