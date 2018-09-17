from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.exceptions import ParseError
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from utils.serializers import validate
from transaction import settings
from .models import Bill
from .serializers import BillSerializer


class UserBill(generics.ListCreateAPIView):
    """
    get:
    Get user bills list

    post:
    Create new user bill and bill items
    """
    permission_classes = (IsAuthenticated,)
    serializer_class = BillSerializer

    def get(self, request):
        bills = Bill.objects.filter(user_id=request.user.id)
        serializer = self.serializer_class(bills, many=True)

        return Response(serializer.data)

    def post(self, request):
        serializer = self.serializer_class(
            data=request.data,
            context={'request': request}
        )
        validate(serializer)

        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class UserBillDetail(generics.RetrieveAPIView):
    """
    get:
    Get selected user bill detail
    """
    permission_classes = (IsAuthenticated,)
    serializer_class = BillSerializer

    def get(self, request, bill_id):
        bill = get_object_or_404(Bill, pk=bill_id)

        if bill.user_id != request.user.id:
            raise ParseError(settings.MSG_FORBIDDEN_USER_BILL)

        serializer = self.serializer_class(bill)

        return Response(serializer.data)
