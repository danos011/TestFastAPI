from core.models.products.db import ProductsDB
from core.models.products.domains import UpdateProduct
from core.models.products.enums import ProductsCategory
from core.storage.db.postgres import DB
from core.utils import throw_not_found


class ProductsStorage:
    def __init__(self, db: DB) -> None:
        self.db = db

    async def get_all(self,
                      name: str,
                      category: ProductsCategory,
                      amount_min: int,
                      amount_max: int) -> list[ProductsDB]:

        sql = "SELECT * FROM api_products Where"
        index = 1
        params = []

        if name:
            sql += f" lower(name) ILIKE ${index} AND"
            params.append("%" + name + "%")
            index += 1

        if category:
            sql += f" category=${index} AND"
            params.append(category)
            index += 1

        sql += f" amount > ${index}"
        params.append(amount_min)
        index += 1

        sql += f" AND amount < ${index}"
        params.append(amount_max)

        rows = await self.db.fetch(sql, *params)

        products: list[ProductsDB] = []
        for row in rows:
            products.append(ProductsDB.model_validate(dict(row)))
        return products

    async def get_by_id(self, product_id: int) -> ProductsDB:
        sql = "SELECT * FROM api_products WHERE id=$1"
        row = await self.db.fetch_row(sql, product_id)
        if not row:
            throw_not_found("There ins't product with this id!")
        return ProductsDB.model_validate(dict(row))

    async def create(self,
                     name: str | None,
                     category: str | None,
                     info: str | None,
                     amount: int | None
                     ) -> ProductsDB:
        sql = "INSERT INTO api_products (name, category, info, amount) VALUES ($1, $2, $3, $4) RETURNING *"
        row = await self.db.fetch_row(sql, name, category, info, amount)
        return ProductsDB.model_validate(dict(row))

    async def update(self, product_id: int, product: UpdateProduct) -> ProductsDB:
        sql = "UPDATE api_products SET name=$2, category=$3, info=$4, amount=$5 WHERE id=$1  RETURNING *"
        row = await self.db.fetch_row(sql, product_id, product.name, product.category, product.info, product.amount)
        if not row:
            throw_not_found("There is'nt product with this id")
        return ProductsDB.model_validate(dict(row))

    async def delete(self, product_id: int
                     ) -> ProductsDB:

        sql = "DELETE FROM api_products WHERE id= $1 RETURNING *"
        row = await self.db.fetch_row(sql, product_id)
        if not row:
            throw_not_found("There is'nt product with this id")
        return ProductsDB.model_validate(dict(row))
