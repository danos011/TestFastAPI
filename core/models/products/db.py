from core.common import BaseSchema
from core.models.products.enums import ProductsCategory


class ProductsDB(BaseSchema):
    id: int
    name: str
    category: ProductsCategory
    info: str | None
    amount: int | None
