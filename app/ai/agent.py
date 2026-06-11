import os
from dotenv import load_dotenv
from langchain.agents import create_agent
from langgraph.checkpoint.memory import MemorySaver


from app.ai.tools import (
    get_customer,
    create_customer,
    get_all_customers,
    create_product,
    get_product,
    get_all_products,
    create_order,
    get_customer_orders,
    get_orders_by_id,
    get_sales_report
)
from langchain_mistralai import (
    ChatMistralAI
)

load_dotenv()

memory = MemorySaver()

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
        get_all_products,
        create_order,
        get_customer_orders,
        get_orders_by_id,
        get_sales_report
    ],
    system_prompt="""
        You are an Order Management Assistant.

        Never invent customer, product or order data.

        If a required parameter for a tool is missing,
        ask the user for it.

        Do not generate fake emails,
        names, ids, quantities or prices.
        """,
    checkpointer=memory
)