from rest_framework.response import Response
from rest_framework.views import exception_handler


def handle_exception(ex, context):
    response = exception_handler(ex, context)

    status_code = getattr(response, 'status_code', 500)
    data = getattr(response, 'data', {})

    err = 'Unexpected error'

    if isinstance(data, dict):
        if 'detail' in data:
            err = data.get('detail')
        else:
            err = data

    return Response(data=err, status=status_code)
