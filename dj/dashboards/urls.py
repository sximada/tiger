from django.urls import include, path

from . import api


urlpatterns = [
    path('api/ping/', api.PingPoingAPIView.as_view()),
    path('api/balance/', api.BalanceAPIView.as_view()),
]
