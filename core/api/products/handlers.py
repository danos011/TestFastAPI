import logging

from fastapi import APIRouter, Query

from core.models.products.enums import ProductsCategory
from core.models.products.requests import CreateProductRequest, UpdateProductRequest
from core.models.products.responses import ProductResponse
from core.services.products.services import get_products_service, get_product_by_id_service, create_product_service, \
    update_product_service, delete_product_service

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/products", tags=["Products"])


@router.get("/all")
async def get_all_products(name: str = Query(None, ),
                           category: ProductsCategory = Query(None, ),
                           amount_min: int = Query(0, ),
                           amount_max: int = Query(100, )) -> list[ProductResponse]:
    return await get_products_service(name, category, amount_min, amount_max)


@router.get("/get_by_id")
async def get_product_by_id(product_id: int) -> ProductResponse:
    return await get_product_by_id_service(product_id)


@router.post("/create")
async def create_product(product: CreateProductRequest) -> ProductResponse:
    return await create_product_service(product)


@router.post("/update")
async def update_product(product_id: int, product: UpdateProductRequest) -> ProductResponse:
    return await update_product_service(product_id, product)


@router.delete("/delete")
async def delete_product(product_id: int) -> ProductResponse:
    return await delete_product_service(product_id)
