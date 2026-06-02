from __future__ import annotations

from decimal import Decimal

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.product import Product


async def create_product(
        db: AsyncSession,
        name: str,
        price: Decimal
) -> Product:

    product = Product(
        name=name,
        price=price
    )
    db.add(product)

    return product


async def get_product_by_id(
        db: AsyncSession,
        product_id: int
) -> Product | None:

    result = await db.execute(
        select(Product).where(
            Product.id == product_id
        )
    )
    product = result.scalar_one_or_none()

    return product