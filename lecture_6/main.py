"""
It is app for dockerize
"""
from fastapi import FastAPI

app = FastAPI()

@app.get("/healthcheck")
async def healthcheck() -> dict:
    """
    This endpoint return status
    """
    return {"status": "ok"}
