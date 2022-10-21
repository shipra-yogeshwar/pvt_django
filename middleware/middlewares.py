# My Project Imports
from .utils import usererror
from settings import ERROR_CODES


# ERROR_CODES = {
#     500: "Internal server error, please try again later",
#     404: "Page not found",
#     505: "HTTP version not support",
#     400: "Bad request"
# }


def get_response(message, status_code):
    return {
        "status_code": status_code,
        "error": message,
    }


class ExceptionMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        response = self.get_response(request)

        if response.status_code in ERROR_CODES.keys():
            print("1")
            usererror(response.status_code)
            response.status_code = 200
            response.message = ERROR_CODES.get(response.status_code)
            print("2")
            return response
        return response
