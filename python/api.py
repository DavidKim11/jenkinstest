'''
실행시 명령어
uvicorn api:app --reload
'''

from fastapi import FastAPI, Header, HTTPException, Query
from pydantic import BaseModel
import time
from datetime import datetime
import asyncio

app = FastAPI()

class Data(BaseModel):
    message: float
    
@app.get("/sync")
async def getSync(q: float):
    print(datetime.now())
    time.sleep(3)
    return {"message": q}

@app.get("/async")
async def getAsync(q: float):
    print(datetime.now())
    asyncio.sleep(3)
    return {"message": q}

@app.post("/{data}")
def post(data : str):
    print(data)
    return {"param": data}

@app.post("/")
def post1(data: Data):
    return {"message": data.message}

@app.put("/")
def put(data: Data):
    return {"message": data.message}

@app.delete("/")
def delete(data: Data):
    return {"message": data.message}

@app.get("/authtest")
def getHeaders(q: float | None = Query(default=None), x_auth_token: str | None = Header(None)):
    if x_auth_token != "1234567":
        raise HTTPException(status_code=401, detail="wrong token and failed authentication.")
    print(f"{q}")
    return {"message": 'authenticated.'}
