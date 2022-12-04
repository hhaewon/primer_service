import json
from typing import Callable

from app.common import consts
from app.model import Data

def find_data_by_id(id: int) -> Callable[[Data], bool]:
    def closure(data: Data) -> bool:
        return data.id == id
    return closure

async def get_datas() -> list[Data]:
    with open(str(consts.WORKSPACE_PATH / "datas.json"), 'r', encoding='utf-8') as f:
        datas: list[Data] = [Data(**data) for data in json.loads(f.read())]
        return datas