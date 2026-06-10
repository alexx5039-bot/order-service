from decimal import Decimal

from pydantic import BaseModel

class TopProductResponse(BaseModel):
    product_id: int
    quantity_sold: int

class TopCustomerResponse(BaseModel):
    customer_id: int
    total_spent: Decimal