from rest_framework import generics
from rest_framework.response import Response


class CreateBill(generics.CreateAPIView):
    def post(self, request):
        return Response('create bill')
