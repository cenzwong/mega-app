from typing import Union
# from typing import Annotated
from typing_extensions import Annotated

# from fastapi import FastAPI
from fastapi import Depends, FastAPI
from .module import myai21

app = FastAPI()

@app.post("/ai21/paraphrase/")
async def ai21_rewrite(text:str, intent: str, key: str):
    return myai21.ai21_rewrite(text, intent, key)

@app.post("/ai21/complete/{model}")
async def ai21_prompt(model:str, text: str, key: str):
    return myai21.ai21_prompt(model, text, key)