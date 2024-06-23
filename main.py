"""
Main config file for FastAPI
"""

import logging
from logging import config as logging_config
import multiprocessing
import os
from contextlib import asynccontextmanager

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi

load_dotenv()

from core import api
from core.registry import db, ENV

logging_config.fileConfig("./logging.conf", disable_existing_loggers=False)
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    process_name = multiprocessing.current_process().name
    logger.info(f"Process {process_name} started")
    if ENV != "PROD":
        for k, v in os.environ.items():
            logger.info(f"{k}={v}")

    await db.connect()

    logger.info("Server started")
    logger.info(f"ENV: {ENV}")
    logger.info("Open http://localhost:8000/api/ping")

    yield

    await db.close()
    logger.info("Server shutting down")


app = FastAPI(lifespan=lifespan)
app.include_router(api.router)


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="CORE API",
        version="0.1",
        routes=app.routes,
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi
