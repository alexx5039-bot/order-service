from collections.abc import Sequence

from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.product import create_product, get_product_by_id, get_all_products
from app.models import Product
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


async def get_product_by_id_service(db: AsyncSession, product_id: int) -> Product:

    product = await get_product_by_id(
        db=db,
        product_id=product_id
    )
    return product


async def get_all_products_service(db: AsyncSession) -> Sequence[Product]:

    products = await get_all_products(
        db=db,
)
    return products
