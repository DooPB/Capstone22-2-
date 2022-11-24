from django.urls import path
from . import views

urlpatterns = [
    path('reETH',views.ETH_refresh),
    path('reBTC',views.BTC_refresh),
    path('reXRP',views.XRP_refresh),
    #path('reDKA',views.DKA_refresh),
    #path('reDOGE',views.DOGE_refresh),
]