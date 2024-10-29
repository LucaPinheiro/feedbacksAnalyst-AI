from app.core.helpers.errors.base_error import BaseError


class MissingParameters(BaseError):
    def __init__(self, message: str):
        super().__init__(f'Field {message} is missing')
class WrongTypeParameter(BaseError):
    def __init__(self, fieldName: str, fieldTypeExpected: str, fieldTypeReceived: str):
        super().__init__(f'Field {fieldName} isn\'sot in the right type.\n Received: {fieldTypeReceived}.\n Expected: {fieldTypeExpected}')