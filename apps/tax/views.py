from rest_framework import generics
from rest_framework.response import Response


class CreateTaxItem(generics.CreateAPIView):
    def post(self, request):
        return Response('create tax item')
