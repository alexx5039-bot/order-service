from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.customer import create_customer, get_customer_by_email
from app.schemas.customer import CustomerCreate


async def create_customer_service(db: AsyncSession, customer_data: CustomerCreate):
    existing_customer = await get_customer_by_email(db, customer_data.email)
    if existing_customer:
        raise ValueError("Customer with this email already exists")
    try:
        customer = await create_customer(
            db,
            customer_data.name,
            customer_data.email,
        )
        await db.commit()
        await db.refresh(customer)

        return customer

    except Exception:
        await db.rollback()
        raise
