from collections.abc import Sequence

from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import Order, OrderItem, Product, Customer
from app.schemas.sales import TopProductResponse, TopCustomerResponse


async def get_sales_report(db: AsyncSession) -> dict:
    result = await db.execute(
        select(
            func.count(Order.id),
            func.sum(Order.total_amount),
            func.avg(Order.total_amount),
        )
    )
    orders_count, total_revenue, average_order = result.one()
    return {
        "orders_count": orders_count,
        "total_revenue": total_revenue,
        "average_order": average_order
    }

async def get_top_sales_products(db: AsyncSession) -> list[TopProductResponse]:
    result = await db.execute(
        select(
            OrderItem.product_id,
            func.sum(OrderItem.quantity).label("quantity_sold"),

        ).group_by(OrderItem.product_id)
        .order_by(func.sum(OrderItem.quantity).desc())
    )
    return [TopProductResponse(
            product_id=row.product_id,
            quantity_sold=row.quantity_sold,
    )
    for row in result.all()
]


async def get_top_customers(db: AsyncSession) -> list[TopCustomerResponse]:
    result = await db.execute(
        select(
            Order.customer_id,
            func.sum(Order.total_amount).label("total_spent"),

        ).group_by(Order.customer_id)
        .order_by(func.sum(Order.total_amount).desc())
    )
    return [
        TopCustomerResponse(
            customer_id=row.customer_id,
            total_spent=row.total_spent
        )
        for row in result.all()
    ]
