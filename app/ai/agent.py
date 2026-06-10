import os
from dotenv import load_dotenv
from langchain.agents import create_agent

from app.ai.tools import (
    get_customer,
    create_customer,
    get_all_customers,
    create_product,
    get_product,
    get_all_products
)
from langchain_mistralai import (
    ChatMistralAI
)

load_dotenv()

llm = ChatMistralAI(
    model="mistral-small-latest",
    api_key=os.getenv("MISTRAL_API_KEY")
)

agent = create_agent(
    model=llm,
    tools=[
        get_customer,
        create_customer,
        get_all_customers,
        create_product,
        get_product,
        get_all_products
    ]
)