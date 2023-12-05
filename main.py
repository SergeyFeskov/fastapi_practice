from fastapi import FastAPI

from api.main_router import main_api_router
from infrastructure.db import orm

orm.start_mapping()

app = FastAPI()

app.include_router(main_api_router)
