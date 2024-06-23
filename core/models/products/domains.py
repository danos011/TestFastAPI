from core.common import BaseSchema
from core.models.products.enums import ProductsCategory


class UpdateProduct(BaseSchema):
    name: str
    category: ProductsCategory
    info: str | None
    amount: int | None
