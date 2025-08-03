# veilblock/core/context.py
class RequestContext:
    def __init__(self, url, headers, content_type):
        self.url = url
        self.headers = headers
        self.content_type = content_type
