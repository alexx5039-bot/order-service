from decimal import Decimal
from fastapi import HTTPException

from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.order import OrderCreate
from app.crud.customer import get_customer_by_id
from app.crud.product import get_product_by_id
from app.crud.order import (
    create_order,
    create_order_item,
    get_order_by_customer_id,
    get_order_by_id,
)


async def create_order_service(db: AsyncSession, order_data: OrderCreate):
    try:

        customer = await get_customer_by_id(db, order_data.customer_id)
        if not customer:
            raise HTTPException(status_code=404, detail="Customer not found")
        total_amount = Decimal("0.00")

        for item in order_data.items:
            product = await get_product_by_id(db, item.product_id)
            if not product:
                raise HTTPException(
                    status_code=404, detail=f"Product{item.product_id} not found"
                )
            total_amount += product.price * item.quantity

        order = await create_order(
            db=db, customer_id=customer.id, total_amount=total_amount
        )
        await db.flush()

        for item in order_data.items:
            await create_order_item(
                db=db,
                order_id=order.id,
                product_id=item.product_id,
                quantity=item.quantity,
            )
        await db.commit()

        return await get_order_by_id(db, order.id)

    except Exception:
        await db.rollback()
        raise


async def get_customer_orders_service(db: AsyncSession, customer_id: int):
    customer = await get_customer_by_id(db, customer_id)

    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")

    orders = await get_order_by_customer_id(db, customer_id)
    return orders
