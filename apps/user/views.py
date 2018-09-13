from rest_framework import generics
from rest_framework.response import Response


class Login(generics.CreateAPIView):
    def post(self, request):
        return Response('login')


class GetBills(generics.RetrieveAPIView):
    def get(self, request):
        return Response('get bills')


class GetBillDetail(generics.RetrieveAPIView):
    def get(self, request, bill_id):
        return Response('get bill detail')
