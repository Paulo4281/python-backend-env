from src.utils.http_response import HttpResponse

class AppError:
    def __init__(self, status_code: int, body: any) -> None:
        self.status_code = status_code
        self.body = str(body)
        self.error = HttpResponse(
            status_code=self.status_code,
            body={
                "title": "Internal Server Error",
                "message": self.body
            }
        )