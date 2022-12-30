from rest_framework.viewsets import ModelViewSet
from transactions.serializers import PaymentUserSerializer, ServiceSerializer, UserSerializer, ExpiredPaymentSerializer
from .models import Service, User, PaymentUser, ExpiredPayment
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import UserRateThrottle
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from datetime import datetime
import random

# Create your views here.

class ServiceView(ModelViewSet):
    #recibe dos cosas el queryset y dos serializer
    permission_classes = [IsAuthenticated]
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

    throttle_scope = 'others'

    def create(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return super().create(request, *args, **kwargs)
        else:
            response = {'message': 'Esta vista está protegida'}
            return Response(response, status=status.HTTP_403_FORBIDDEN)

    def update(self, request, pk=None, *args, **kwargs):
        if request.user.is_superuser:
            return super().update(request, pk, *args, **kwargs)
        else:
            response = {'message': 'Esta vista está protegida'}
            return Response(response, status=status.HTTP_403_FORBIDDEN)

    def partial_update(self, request, pk=None, *args, **kwargs):
        if request.user.is_superuser:
            return super().partial_update(request, pk, *args, **kwargs)
        else:
            response = {'message': 'Esta vista está protegida'}
            return Response(response, status=status.HTTP_403_FORBIDDEN)

    def destroy(self, request, pk=None, *args, **kwargs):
        if request.user.is_superuser:
            return super().destroy(request, pk, *args, **kwargs)
        else:
            response = {'message': 'Esta vista está protegida'}
            return Response(response, status=status.HTTP_403_FORBIDDEN)


class UserView(ModelViewSet):
    #recibe dos cosas el queryset y dos serializer
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer

    throttle_scope = 'others'


class PaymentUserView(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = PaymentUser.objects.all()
    serializer_class = PaymentUserSerializer
    filter_backends =  [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['paymentDate','expirationDate']
    search_fields = ['paymentDate','expirationDate']

    throttle_scope = 'paymentuser'

    def create(self, request, *args, **kwargs):
        new_payment_user = super().create(request, *args, **kwargs)
        payment_date = datetime.strptime(request.data['paymentDate'], '%Y-%m-%d')
        expiration_date = datetime.strptime(request.data['expirationDate'], '%Y-%m-%d')
        if payment_date > expiration_date:
            new_expired_payment = ExpiredPayment()
            new_expired_payment.penalty_fee_amount = random.randint(50, 1000)
            new_expired_payment.pay_user_id_id = new_payment_user.data['id']
            new_expired_payment.save()
        return new_payment_user


class ExpiredPaymentView(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = ExpiredPayment.objects.all()
    serializer_class = ExpiredPaymentSerializer

    throttle_scope = 'others'

    def update(self, request, pk=None, *args, **kwargs):
        if request.user.is_superuser:
            return super().update(request, pk, *args, **kwargs)
        else:
            response = {'message': 'Esta vista está protegida'}
            return Response(response, status=status.HTTP_403_FORBIDDEN)

    def partial_update(self, request, pk=None, *args, **kwargs):
        if request.user.is_superuser:
            return super().partial_update(request, pk, *args, **kwargs)
        else:
            response = {'message': 'Esta vista está protegida'}
            return Response(response, status=status.HTTP_403_FORBIDDEN)

    def destroy(self, request, pk=None, *args, **kwargs):
        if request.user.is_superuser:
            return super().destroy(request, pk, *args, **kwargs)
        else:
            response = {'message': 'Esta vista está protegida'}
            return Response(response, status=status.HTTP_403_FORBIDDEN)
