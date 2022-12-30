from rest_framework.serializers import ModelSerializer
from .models import Service, User, PaymentUser, ExpiredPayment


class ServiceSerializer(ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class PaymentUserSerializer(ModelSerializer):
    class Meta:
        model = PaymentUser
        fields = '__all__'


class ExpiredPaymentSerializer(ModelSerializer):
    class Meta:
        model = ExpiredPayment
        fields = '__all__'