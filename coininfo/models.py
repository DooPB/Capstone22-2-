from django.db import models

# Create your models here.
class CoinInfoETH(models.Model):    #이더리움
    cd = models.CharField(max_length=10)
    tp = models.IntegerField()
    scr = models.FloatField()
    tv = models.FloatField()

class CoinInfoBTC(models.Model):    #비트코인
    cd = models.CharField(max_length=10)
    tp = models.IntegerField()
    scr = models.FloatField()
    tv = models.FloatField()

class CoinInfoXRP(models.Model):    #리플
    cd = models.CharField(max_length=10)
    tp = models.IntegerField()
    scr = models.FloatField()
    tv = models.FloatField()

class CoinInfoDKA(models.Model):    #디카르고
    cd = models.CharField(max_length=10)
    tp = models.IntegerField()
    scr = models.FloatField()
    tv = models.FloatField()

class CoinInfoDOGE(models.Model):    #도지코인
    cd = models.CharField(max_length=10)
    tp = models.IntegerField()
    scr = models.FloatField()
    tv = models.FloatField()