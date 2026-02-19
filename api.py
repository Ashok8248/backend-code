from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "ashok, World!"}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": 5}
