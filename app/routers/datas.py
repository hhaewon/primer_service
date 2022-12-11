from fastapi import APIRouter, Path

from app.model import Data
from app.util import get_datas, find_data_by_id

router = APIRouter(prefix="/datas",
                   tags=["datas"],
                   responses={404: {"description": "Not found"}})

@router.get("/{id}", response_model=Data)
async def read_data(id: int = Path(..., ge=1, le=30)):
    datas = await get_datas()
    data = next(filter(find_data_by_id(id=id), datas))
    return data
    
@router.get("/", response_model=list[Data])
async def read_datas():
    return await get_datas()

