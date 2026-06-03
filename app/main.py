from fastapi import FastAPI

from app.routers.customer import router as customer_router
from app.routers.product import router as product_router
from app.routers.order import router as order_router

app = FastAPI(title="Order Service API")


app.include_router(customer_router)
app.include_router(product_router)
app.include_router(order_router)
