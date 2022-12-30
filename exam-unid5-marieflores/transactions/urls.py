from rest_framework.routers import DefaultRouter
from .views import PaymentUserView, ServiceView, UserView, ExpiredPaymentView

router = DefaultRouter()

router.register(r'service', ServiceView, basename='service') #esto
router.register('user', UserView, basename='user')
router.register('paymentuser', PaymentUserView, basename='paymentuser')
router.register('expiredpayment', ExpiredPaymentView, basename='expiredpayment')
