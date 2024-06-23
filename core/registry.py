import datetime
import os

from core.storage.db import postgres
from core.storage.produts_storage import ProductsStorage

server_started = datetime.datetime.now()
VERSION = os.getenv("VERSION", "0")
ENV = os.environ.get("ENV", "LOCAL")

db: postgres.DB = postgres.get_database()
products_storage = ProductsStorage(db)
