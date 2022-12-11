# pyright: reportUnknownMemberType=false
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.exceptions import RequestValidationError
import uvicorn

from app.routers import datas, info, index, error_handling
from app.common import consts

app = FastAPI()
app.mount("/static", StaticFiles(directory=consts.BASE_PATH / 'static'), name="static")
app.include_router(datas.router)
app.include_router(info.router)
app.include_router(index.router)
app.add_exception_handler(RequestValidationError, error_handling.validation_error_handler)


if __name__ == "__main__":
    uvicorn.run("main:app", host=consts.HOST, port=consts.PORT, reload=True) #type: ignore
