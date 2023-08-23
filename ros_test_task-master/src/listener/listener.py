#!/bin/python3

import json

import requests
import uvicorn as uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

LOGGER_URL = "http://0.0.0.0:8003/log"
app = FastAPI()


class LogItem(BaseModel):
    data: str


@app.post("/info")
async def process(req: LogItem):
    new_data = json.dumps({"log": req.data})
    requests.post(LOGGER_URL, new_data)

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8001)
