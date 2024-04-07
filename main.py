
from fastapi import FastAPI
from modules.module1 import routers

app = FastAPI()

app.include_router(routers.router, prefix="/api/module1")

