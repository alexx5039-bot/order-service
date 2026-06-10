from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.sales import get_sales_report, get_top_sales_products, get_top_customers


async def get_sales_report_service(
    db: AsyncSession,
) -> dict:

    report = await get_sales_report(db)

    top_products = await get_top_sales_products(db)

    top_customers = await get_top_customers(db)

    return {
        **report,
        "top_products": [
            p.model_dump(mode="json")
            for p in top_products
        ],
        "top_customers": [
            c.model_dump(mode="json")
            for c in top_customers
        ],
    }