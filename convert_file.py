import json
import openpyxl

from model import Data, Primers
from pydantic.json import pydantic_encoder
excel_file = openpyxl.load_workbook(filename="../성현.xlsx")
sheet = excel_file.active
datas: list[Data] = []

for i in range(0, 30):
    data: Data = Data(id=i+1,
                      chr=Primers(primer_1=sheet[f'D{2 + i * 4}'].value,
                                  primer_2=sheet[f'E{2 + i * 4}'].value,
                                  template=sheet[f'F{2 + i * 4}'].value),
                      plsm=Primers(primer_1=sheet[f'D{3 + i * 4}'].value,
                                  primer_2=sheet[f'E{3 + i * 4}'].value,
                                  template=sheet[f'F{3 + i * 4}'].value),
                      name=sheet[f'B{2 + i * 4}'].value.split("(")[0].strip(),
                      scientific_name=sheet[f'B{2 + i * 4}'].value.split("(")[1].replace(')', ''))
    datas.append(data)

print(datas)
with open('datas.json', 'w', encoding='utf-8') as f:
    f.write(json.dumps(datas, indent=4, default=pydantic_encoder, ensure_ascii=False))

