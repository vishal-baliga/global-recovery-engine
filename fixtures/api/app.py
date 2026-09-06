"""Setup-only API contract. No customer or domain functionality."""
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(title="GRE environment fixture", version="0.1.0",
              servers=[{"url": "http://127.0.0.1:8000", "description": "Local setup fixture only"}])


class EchoRequest(BaseModel):
    message: str = Field(min_length=1, max_length=128)


class EchoResponse(BaseModel):
    message: str
    length: int


@app.post("/setup/echo", response_model=EchoResponse, operation_id="setup_echo")
def echo(request: EchoRequest) -> EchoResponse:
    return EchoResponse(message=request.message, length=len(request.message))
