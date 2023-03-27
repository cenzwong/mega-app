from typing import Union
# from typing import Annotated
from typing_extensions import Annotated

# from fastapi import FastAPI
from fastapi import Depends, FastAPI
from .module import myai21

from fastapi.security import HTTPBasic, HTTPBasicCredentials

app = FastAPI()
security = HTTPBasic()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/ai21/paraphrase/{text}")
def paraphrase(text:str, intent: str, key: str):
    return myai21.ai21_rewrite(text, intent, key)