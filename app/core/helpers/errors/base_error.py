class BaseError(Exception):
    def __init__(self, message: str):
        self.__message: str = message
        super().__init__(message)

    @property
    def message(self):
        return self.__message
    
class InternalServerError(BaseError):
    def __init__(self, message: str):
        super().__init__(f'Internal server error: {message}')