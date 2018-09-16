from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from utils.serializers import validate
from .serializers import BillSerializer


class CreateBill(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = BillSerializer

    def post(self, request):
        serializer = self.serializer_class(
            data=request.data,
            context={'request': request}
        )
        validate(serializer)

        serializer.save()
        return Response()


class GetUserBills(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        return Response('get bills')


class GetUserBillDetail(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, bill_id):
        return Response('get bill detail')
