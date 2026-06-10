from decimal import Decimal

from langchain_core.tools import tool
from app.services.customer_service import (
    get_customer_by_id_service,
    create_customer_service,
    get_all_customers_service
)


from app.models import Product
from app.database import AsyncSessionLocal
from app.schemas.customer import CustomerResponse, CustomerCreate
from app.schemas.product import ProductCreate, ProductResponse
from app.services.product_service import create_product_service, get_product_by_id_service, get_all_products_service


@tool
async def get_customer(customer_id: int) -> str:
    """
    Get customer information by customer id.
    """
    async with AsyncSessionLocal() as db:
        customer = await get_customer_by_id_service(
            db=db,
            customer_id=customer_id
        )

        if customer is None:
            return ("Customer not found")

        return CustomerResponse.model_validate(
            customer
        ).model_dump()

@tool
async def get_all_customers() -> list[dict]:
    """
    Get all customers from database.
    """
    async with AsyncSessionLocal() as db:
        customers = await get_all_customers_service(
            db=db,
        )

        return [
            CustomerResponse.model_validate(
                customer
            ).model_dump()
            for customer in customers
        ]


@tool
async def create_customer(
        name: str,
        email: str
) -> dict:
    """
    Create a new customer
    """
    try:
        async with AsyncSessionLocal()  as db:
            customer_data = CustomerCreate(
                name=name,
                email=email,
            )
            customer = await create_customer_service(
                db=db,
                customer_data=customer_data
            )
            return CustomerResponse.model_validate(
                customer
            ).model_dump()
    except ValueError as e:
        return {
            "error": str(e)
        }

@tool
async def create_product(
        name: str,
        price: Decimal
) -> dict:
    """
    Create a new product
    """
    try:
        async with AsyncSessionLocal()  as db:
            product_data = ProductCreate(
                name=name,
                price=price
            )
            product = await create_product_service(
                db=db,
                product_data=product_data
            )
            return ProductResponse.model_validate(
                product
            ).model_dump(mode="json")

    except ValueError as e:
        return {
            "error": str(e)
        }

@tool
async def get_product(product_id: int) -> str:
    """
    Get product information by product id.
    """
    async with AsyncSessionLocal() as db:
        product = await get_product_by_id_service(
            db=db,
            product_id=product_id
        )

        if product is None:
            return ("Product is not found")

        return ProductResponse.model_validate(
            product
        ).model_dump()

@tool
async def get_all_products() -> list[dict]:
    """
    Get product information about all products in database.
    """
    async with AsyncSessionLocal() as db:
        products = await get_all_products_service(
            db=db,

        )

        if products is None:
            return ("No products in DB")

        return [ProductResponse.model_validate(
            product
        ).model_dump(mode="json")
        for product in products]
