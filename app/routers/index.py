# pyright: reportUnknownMemberType=false
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from httpx import AsyncClient

from app.common import consts
from app.model import Data

router = APIRouter()

TEMPLATES = Jinja2Templates(directory=str(consts.BASE_PATH / "templates"))

@router.get("/", response_class=HTMLResponse)
async def read_index(request: Request):
    async with AsyncClient(base_url=consts.BASE_URL) as client:
        datas = await client.get(url="/datas/")
        json_data: list[Data] = datas.json()
    return TEMPLATES.TemplateResponse("index.html", {"request": request, "datas": json_data})