from decimal import Decimal

from pydantic import (
    BaseModel,
    ConfigDict,
    Field
)

class OrderItemCreate(BaseModel):
    product_id: int
    quantity: int = Field(gt=0)


class OrderCreate(BaseModel):
    customer_id: int
    items: list[OrderItemCreate] = Field(
        min_length=1
    )


class OrderItemResponse(BaseModel):
    product_id: int
    quantity: int

    model_config = ConfigDict(
        from_attributes=True
    )


class OrderResponse(BaseModel):
    id: int
    customer_id: int
    total_amount: Decimal
    items: list[OrderItemResponse]

    model_config = ConfigDict(
        from_attributes=True
    )
