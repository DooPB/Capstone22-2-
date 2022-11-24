from django.urls import path
from . import views

urlpatterns = [
    path('reETH',views.ETH_refresh),
    path('reBTC',views.BTC_refresh),
    path('reXRP',views.XRP_refresh),
    path('XRP',views.XRP_view),
    path('BTC',views.BTC_view),
    path('ETH',views.ETH_view),
]