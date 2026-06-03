from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.dependencies import get_db
from app.schemas.customer import (
    CustomerCreate,
    CustomerResponse
)
from app.services.customer_service import create_customer_service


router = APIRouter(
    prefix="/customers",
    tags=["Customers"]
)

@router.post("/", response_model=CustomerResponse, status_code=201)
async def create_customer(
        customer_data: CustomerCreate,
        db: AsyncSession = Depends(get_db)
):
    customer = await create_customer_service(
        db,
        customer_data
    )
    return customer




