from pydantic import BaseModel


class Primers(BaseModel):
    primer_1: str
    primer_2: str
    template: str
    
class Data(BaseModel):
    id: int
    chr: Primers
    plsm: Primers
    name: str
    scientific_name: str