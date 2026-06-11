from fastapi import APIRouter

from app.schemas.chat import ChatRequest, ChatResponse
from app.ai.agent import agent

router = APIRouter(
    prefix="/chat",
    tags=["Chat"]
)

@router.post(
    "",
    response_model=ChatResponse
)
async def chat(request: ChatRequest):
    result = await agent.ainvoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": request.message
                }
            ]
        },
        config={
            "configurable": {
                "thread_id": request.session_id
            }
        }
    )


    return ChatResponse(
        response=result["messages"][-1].content
    )