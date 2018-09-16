from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.exceptions import ParseError
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from utils.serializers import validate
from bill import settings
from .models import Bill
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
        return Response(serializer.data)


class GetUserBills(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = BillSerializer

    def get(self, request):
        bills = Bill.objects.filter(user_id=request.user.id)
        serializer = self.serializer_class(bills, many=True)

        return Response(serializer.data)


class GetUserBillDetail(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = BillSerializer

    def get(self, request, bill_id):
        bill = get_object_or_404(Bill, pk=bill_id)

        if bill.user_id != request.user.id:
            raise ParseError(settings.MSG_FORBIDDEN_USER_BILL)

        serializer = self.serializer_class(bill)

        return Response(serializer.data)
