from typing import Any
from fastapi.responses import JSONResponse

from app.core.domain.enums.http_status_code_enum import HttpStatusCodeEnum

class OK(JSONResponse):
    def __init__(self, body: Any = None) -> None:
        super().__init__(content=body, status_code=HttpStatusCodeEnum.OK.value)


class Created(JSONResponse):
    def __init__(self, body: Any = None) -> None:
        super().__init__(content=body, status_code=HttpStatusCodeEnum.CREATED.value)


class NoContent(JSONResponse):
    def __init__(self) -> None:
        super().__init__(content=None, status_code=HttpStatusCodeEnum.NO_CONTENT.value)


class BadRequest(JSONResponse):
    def __init__(self, body: Any) -> None:
        super().__init__(content={"error": body}, status_code=HttpStatusCodeEnum.BAD_REQUEST.value)


class InternalServerError(JSONResponse):
    def __init__(self, body: Any) -> None:
        super().__init__(content={"error": body}, status_code=HttpStatusCodeEnum.INTERNAL_SERVER_ERROR.value)


class NotFound(JSONResponse):
    def __init__(self, body: Any) -> None:
        super().__init__(content={"error": body}, status_code=HttpStatusCodeEnum.NOT_FOUND.value)


class Conflict(JSONResponse):
    def __init__(self, body: Any) -> None:
        super().__init__(content={"error": body}, status_code=HttpStatusCodeEnum.CONFLICT.value)


class RedirectResponse(JSONResponse):
    def __init__(self, location: str) -> None:
        super().__init__(content=None, status_code=HttpStatusCodeEnum.REDIRECT.value)
        self.headers["Location"] = location


class Forbidden(JSONResponse):
    def __init__(self, body: Any) -> None:
        super().__init__(content={"error": body}, status_code=HttpStatusCodeEnum.FORBIDDEN.value)
