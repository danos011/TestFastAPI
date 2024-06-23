from ...models.products.domains import UpdateProduct
from ...models.products.enums import ProductsCategory
from ...models.products.requests import CreateProductRequest, UpdateProductRequest
from ...models.products.responses import ProductResponse
from ...registry import products_storage
from ...utils import throw_failed_dependency


async def get_products_service(name: str, category: ProductsCategory, amount_min: int, amount_max: int) \
        -> list[ProductResponse]:
    if amount_max <= amount_min:
        raise throw_failed_dependency("The maximum quantity must be greater than the minimum!")

    return await products_storage.get_all(name, category, amount_min, amount_max)


async def get_product_by_id_service(product_id: int) -> ProductResponse:
    return await products_storage.get_by_id(product_id)


async def create_product_service(product: CreateProductRequest) -> ProductResponse:
    return await products_storage.create(**product.dict())


async def update_product_service(product_id: int, product_update_request: UpdateProductRequest) -> ProductResponse:
    profile_update = UpdateProduct(**product_update_request.model_dump())
    return await products_storage.update(product_id, profile_update)


async def delete_product_service(product_id: int) -> ProductResponse:
    return await products_storage.delete(product_id)
