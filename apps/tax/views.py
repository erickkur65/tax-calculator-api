from rest_framework import generics
from rest_framework.response import Response

from utils.serializers import validate
from .serializers import TaxSerializer


class CreateTaxItem(generics.CreateAPIView):
    serializer_class = TaxSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        validate(serializer)

        serializer.save()
        return Response()
