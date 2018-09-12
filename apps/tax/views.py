from rest_framework import generics
from rest_framework.response import Response


#generics.CreateAPIView
class CreateTax(generics.RetrieveUpdateAPIView):
    def get(self, request):
        return Response('asd')
