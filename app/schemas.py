from pydantic import BaseModel, Field
from typing import Literal, Optional


class RewriteRequest(BaseModel):
    text: str = Field(..., min_length=1)
    tone: Literal["professional", "friendly", "simple", "confident"] = "professional"


class RewriteResponse(BaseModel):
    rewritten_text: str


class ClassifyRequest(BaseModel):
    text: str = Field(..., min_length=1)


class ClassifyResponse(BaseModel):
    category: str
    confidence: float


class ExtractJsonRequest(BaseModel):
    text: str = Field(..., min_length=1)


class ExtractJsonResponse(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    budget: Optional[float] = None


class GenerateEmailRequest(BaseModel):
    purpose: str = Field(..., min_length=1)
    recipient_name: Optional[str] = None
    tone: Literal["professional", "friendly", "short"] = "professional"


class GenerateEmailResponse(BaseModel):
    subject: str
    body: str


class ImprovePromptRequest(BaseModel):
    prompt: str = Field(..., min_length=1)


class ImprovePromptResponse(BaseModel):
    improved_prompt: str