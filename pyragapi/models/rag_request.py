from pydantic import BaseModel, Field


class RagRequest(BaseModel):
    question: str = Field(
        ...,
        min_length=1,
        description="User question"
    )