from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.dependencies import get_db

from app.schemas.order import (
    OrderCreate,
    OrderResponse,
)

from app.services.order_service import (
    create_order_service,
    get_customer_orders_service,
)

router = APIRouter(
    prefix="/orders",
    tags=["Orders"],
)

@router.post(
    "/",
    response_model=OrderResponse,
    status_code=201,
)
async def create_order(
    order_data: OrderCreate,
    db: AsyncSession = Depends(get_db),
):
    order = await create_order_service(
        db,
        order_data,
    )
    return order


@router.get(
    "/customer/{customer_id}",
    response_model=list[OrderResponse]
)
async def get_customer_orders(
        customer_id: int,
        db: AsyncSession = Depends(get_db),
):
    orders = await get_customer_orders_service(
        db,
        customer_id
    )
    return orders
