from typing import Union

from fastapi import FastAPI
import myai21

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/ai21/paraphrase/{text}")
def paraphrase(item_id: int):
    return _ai21.ai21_rewrite(text, "general", "")