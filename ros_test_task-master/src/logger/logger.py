#!/bin/python3

import logging
from typing import Any

import uvicorn as uvicorn
from fastapi import FastAPI
from pydantic import BaseModel, Json

app = FastAPI()
logger = logging.getLogger("logger")


class LogItem(BaseModel):
    log: str


@app.post("/log")
async def log(req: LogItem):
    logger.info(req)

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8003)