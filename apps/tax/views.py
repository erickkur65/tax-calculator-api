from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from utils.serializers import validate
from .models import TaxItem
from .serializers import TaxItemSerializer


class TaxItemView(generics.ListCreateAPIView):
    """
    get:
    Get tax item list

    post:
    Create new tax item
    """

    permission_classes = (IsAuthenticated,)
    serializer_class = TaxItemSerializer

    def get(self, request):
        tax_items = TaxItem.objects.all()
        serializer = self.serializer_class(tax_items, many=True)

        return Response(serializer.data)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        validate(serializer)

        serializer.save()
        return Response(serializer.data)
