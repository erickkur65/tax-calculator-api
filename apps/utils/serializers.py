from rest_framework.exceptions import ParseError


def validate(serializer):
    if serializer.is_valid():
        return

    raise ParseError(serializer.errors)
