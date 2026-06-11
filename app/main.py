from fastapi import FastAPI

from app.routers.customer import router as customer_router
from app.routers.product import router as product_router
from app.routers.order import router as order_router
from app.routers.chat import router as chat_router

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Order Service API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(customer_router)
app.include_router(product_router)
app.include_router(order_router)
app.include_router(chat_router)