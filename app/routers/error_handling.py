from fastapi import Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import PlainTextResponse

async def validation_error_handler(request: Request, ext: RequestValidationError):
    return PlainTextResponse(content=f"{ext} \n 유효하지 않은 값입니다.", status_code=400)
