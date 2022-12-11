# pyright: reportUnknownMemberType=false
from fastapi import APIRouter, Path, Request
from fastapi.templating import Jinja2Templates
from httpx import AsyncClient

from app.common import consts
from app.model import Data

router = APIRouter(prefix="/info",
                   tags=["info"],
                   responses={404: {"description": "Not found"}})

TEMPLATES = Jinja2Templates(directory=str(consts.BASE_PATH / "templates"))

@router.get("/{id}")
async def show_info(request: Request, id: int = Path(..., ge=1, le=30)):
    async with AsyncClient(base_url=consts.BASE_URL) as client:
        data = await client.get(url=f"/datas/{id}")
        json_data: Data = data.json()
    return TEMPLATES.TemplateResponse("info.html", {"request": request, "data": json_data})
