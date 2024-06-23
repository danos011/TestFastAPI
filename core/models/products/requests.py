from core.common import BaseSchema
from core.models.products.enums import ProductsCategory


class CreateProductRequest(BaseSchema):
    name: str
    category: ProductsCategory
    info: str | None
    amount: int | None


class UpdateProductRequest(BaseSchema):
    name: str
    category: ProductsCategory
    info: str | None
    amount: int | None

