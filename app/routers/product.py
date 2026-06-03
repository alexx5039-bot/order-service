from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.dependencies import get_db
from app.schemas.product import (
    ProductCreate,
    ProductResponse,
)
from app.services.product_service import (
    create_product_service,
)

router = APIRouter(
    prefix="/products",
    tags=["Products"]
)

@router.post("/", response_model=ProductResponse, status_code=201)
async def create_product(
        product_data: ProductCreate,
        db: AsyncSession = Depends(get_db)
):
    product = await create_product_service(
        db,
        product_data
    )
    return product