from django.contrib import admin
from .models import CoinInfoETH, CoinInfoBTC, CoinInfoDKA, CoinInfoXRP, CoinInfoDOGE
# Register your models here.

admin.site.register(CoinInfoETH)
admin.site.register(CoinInfoBTC)
admin.site.register(CoinInfoDKA)
admin.site.register(CoinInfoXRP)
admin.site.register(CoinInfoDOGE)