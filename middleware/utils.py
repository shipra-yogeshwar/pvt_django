# Django Imports
import traceback

# My Project Imports
from .models import Errorcode


def usererror(status_code):
    try:
        err_stack = traceback.format_stack()
        print(err_stack)
        save_response = Errorcode.objects.create(message=str(err_stack), status_code=status_code)
        save_response.save()
    except Exception as e:
        pass
        # logger.error(e.__str__())