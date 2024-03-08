from typing import Dict

class HttpRequest:
    def __init__(self, header: Dict=None, body: Dict=None, query: Dict=None, params: Dict=None) -> None:
        self.header = header
        self.body = body
        self.query = query
        self.params = params
        