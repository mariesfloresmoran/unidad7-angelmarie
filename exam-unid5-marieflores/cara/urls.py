
from django.urls import path

from cara.views import login, pagos

urlpatterns = [
    path("login", login, name="login"),
    path("lista", pagos, name="pagos"),
]