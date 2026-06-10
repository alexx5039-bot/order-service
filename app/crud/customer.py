from __future__ import annotations

from collections.abc import Sequence

from pydantic import EmailStr
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.customer import Customer


async def create_customer(db: AsyncSession, name: str, email: str) -> Customer:
    customer = Customer(name=name, email=email)
    db.add(customer)

    return customer


async def get_customer_by_id(db: AsyncSession, customer_id: int) -> Customer | None:
    result = await db.execute(select(Customer).where(Customer.id == customer_id))
    customer = result.scalar_one_or_none()

    return customer


async def get_customer_by_email(db: AsyncSession, email: EmailStr) -> Customer | None:

    result = await db.execute(select(Customer).where(Customer.email == email))
    customer = result.scalar_one_or_none()

    return customer

async def get_all_customers(db: AsyncSession) -> Sequence[Customer] | None:
    result = await db.execute(select(Customer))
    customers = list(result.scalars().all())

    return customers
