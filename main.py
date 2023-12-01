from fastapi import FastAPI

from api.main_router import main_api_router

app = FastAPI()

app.include_router(main_api_router)
