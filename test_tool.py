import asyncio
from app.ai.agent import agent


async def main():
    session_id = "user_1"

    while True:
        message = input("You: ")

        result = await agent.ainvoke(
            {
                "messages": [
                    {
                        "role": "user",
                        "content": message
                    }
                ]
            },
            config={
                "configurable": {
                    "thread_id": session_id
                }
            }
        )

        print(result["messages"][-1].content)


asyncio.run(main())