class ApiError(Exception):
    def __init__(self, message: str, status_code: int):
        self.message = message
        self.status_code = status_code
        super().__init__(self.message)

class ApiError(Exception):
    def __init__(self, message: str, status_code: int):
        self.message = message
        self.status_code = status_code
        super().__init__(self.message)

def api_error_to_text(e: ApiError) -> str:
    return f"Error {e.status_code}: {e.message}"
