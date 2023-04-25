from fastapi import FastAPI
from typing import Union
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

#uvicorn main:app --host='0.0.0.0' --reload