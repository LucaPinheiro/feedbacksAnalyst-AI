from fastapi import FastAPI
from app.api.v1.router.feedback_router import router

app = FastAPI()

app.include_router(router, prefix="/api/v1")
