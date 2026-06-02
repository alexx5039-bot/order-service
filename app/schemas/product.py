from decimal import Decimal

from pydantic import (
    BaseModel,
    ConfigDict
)


class ProductCreate(BaseModel):
    name: str
    price: Decimal


class ProductResponse(BaseModel):
    id: int
    name: str
    price: Decimal

    model_config = ConfigDict(
        from_attributes=True
    )
