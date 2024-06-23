from fastapi import APIRouter
from .products import products_router


router = APIRouter(prefix="/api")
router.include_router(products_router)
