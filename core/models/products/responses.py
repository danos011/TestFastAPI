from .enums import ProductsCategory
from ...common import BaseSchema


class ProductResponse(BaseSchema):
    id: int
    name: str
    category: ProductsCategory
    info: str | None
    amount: int | None

