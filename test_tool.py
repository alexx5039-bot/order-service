import asyncio
import app.models

from app.ai.tools import create_customer, get_customer
from app.ai.agent import agent

async def main():
    result = await agent.ainvoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": (
                        "Show sales report"

                    )
                }
            ]
        }
    )
    print(result["messages"][-1].content)
    for message in result["messages"]:
        print(type(message))
        print(message)



asyncio.run(main())