from pydantic import BaseModel


class Primers(BaseModel):
    primer_1: str | None
    primer_2: str | None
    template: str | None
    
class Data(BaseModel):
    id: int
    chr: Primers
    plsm: Primers
    name: str
    scientific_name: str