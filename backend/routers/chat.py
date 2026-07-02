from fastapi import APIRouter

from models.chat import ChatRequest, ChatResponse
from services.agent_service import ask_agent

router = APIRouter()


@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):

    result = ask_agent(
        request.session_id,
        request.message
    )

    # RAG
    if result["type"] == "rag":

        return ChatResponse(
            answer=result["answer"]["answer"],
            sources=result["answer"]["sources"]
        )

    # Conversation / Tool Response
    return ChatResponse(
        answer=result["answer"],
        sources=[]
    )