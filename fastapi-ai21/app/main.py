from typing import Union
# from typing import Annotated
from typing_extensions import Annotated

# from fastapi import FastAPI
from fastapi import Depends, FastAPI
from .module import myai21

app = FastAPI()

@app.get("/ai21/paraphrase/{text}")
async def paraphrase(text:str, intent: str, key: str):
    return myai21.ai21_rewrite(text, intent, key)