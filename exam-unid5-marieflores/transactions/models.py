from django.db import models
from authapp.models import User

# Create your models here.

class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    logo = models.URLField()

    class Meta:
        db_table = "Service"

    def __str__(self):
        return self.name


class PaymentUser(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.PROTECT) 
    service_id = models.ForeignKey(Service, on_delete=models.PROTECT)
    amount = models.FloatField()
    paymentDate = models.DateField()
    expirationDate = models.DateField()
    
    class Meta:
        db_table = "PaymentUser"
    
    def __str__(self):
        return str(self.user_id)

class ExpiredPayment(models.Model):
    pay_user_id = models.ForeignKey(PaymentUser, on_delete=models.PROTECT) 
    penalty_fee_amount = models.FloatField()

    class Meta:
        db_table = "ExpiredPayment"

