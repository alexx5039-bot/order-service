from __future__ import annotations

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from decimal import Decimal

from app.models.order import Order
from app.models.order_item import OrderItem


async def get_order_by_customer_id(
        db: AsyncSession,
        customer_id: int
) -> list[Order]:

    result = await db.execute(
        select(Order).where(
            Order.customer_id == customer_id
        )
    )
    orders = result.scalars().all()

    return list(orders)


async def create_order(
        db: AsyncSession,
        customer_id: int,
        total_amount: Decimal
) -> Order:

    order = Order(
        customer_id=customer_id,
        amount=total_amount
    )
    db.add(order)

    return order


async def create_order_item(
        db: AsyncSession,
        order_id: int,
        product_id: int,
        quantity: int,
) -> OrderItem:

    order_item = OrderItem(
        order_id=order_id,
        product_id=product_id,
        quantity=quantity
    )
    db.add(order_item)

    return order_item


async def get_order_by_id(
        db: AsyncSession,
        order_id: int,
) -> Order | None:

    result = await db.execute(
        select(Order).where(
            Order.id == order_id
        )
    )
    order = result.scalar_one_or_none()

    return order


async def get_orders_by_customer(
        db: AsyncSession,
        customer_id: int,
) -> list[Order]:

    result = await db.execute(
        select(Order)
        .options(
            selectinload(Order.items)
            .selectinload(OrderItem.product)
        )
        .where(
            Order.customer_id == customer_id
        )
    )
    orders = result.scalars().all()

    return list(orders)