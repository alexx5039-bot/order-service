from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.product import create_product
from app.schemas.product import ProductCreate


async def create_product_service(
    db: AsyncSession,
    product_data: ProductCreate,
):
    try:
        product = await create_product(
            db,
            product_data.name,
            product_data.price,
        )

        await db.commit()
        await db.refresh(product)

        return product

    except Exception:
        await db.rollback()
        raise
