from django.shortcuts import render
from coininfo.models import CoinInfoETH, CoinInfoBTC, CoinInfoXRP
import csv

def ETH_refresh(request):
    path = 'C:\projects\mysite\static\ETH.csv'
    file = open(path)
    ETH_reader = csv.reader(file)
    list = []
    for row in ETH_reader:
        if row[0] != 'cd':
            list.append(CoinInfoETH(cd=row[0],
                                    tp=row[1],
                                    scr=row[2],
                                    tv=row[3]))
    CoinInfoETH.objects.bulk_create(list)
    ETH_data = CoinInfoETH.objects.all()
    return render(request,'home.html',context={'ETH_data':ETH_data})

def BTC_refresh(request):
    path = 'C:\projects\mysite\static\BTC.csv'
    file = open(path)
    BTC_reader = csv.reader(file)
    list = []
    for row in BTC_reader:
        if row[0] != 'cd':
            list.append(CoinInfoBTC(cd=row[0],
                                    tp=row[1],
                                    scr=row[2],
                                    tv=row[3]))
    CoinInfoBTC.objects.bulk_create(list)
    BTC_data = CoinInfoBTC.objects.all()
    return render(request,'home.html',context={'BTC_data':BTC_data})

def XRP_refresh(request):
    path = 'C:\projects\mysite\static\XRP.csv'
    file = open(path)
    XRP_reader = csv.reader(file)
    list = []
    for row in XRP_reader:
        if row[0] != 'cd':
            list.append(CoinInfoXRP(cd=row[0],
                                    tp=row[1],
                                    scr=row[2],
                                    tv=row[3]))
    CoinInfoXRP.objects.bulk_create(list)
    XRP_data = CoinInfoXRP.objects.all()
    return render(request,'home.html',context={'XRP_data':XRP_data})

def ETH_view(request):
    return render(request,'chartpage.html')

def BTC_view(request):
    return render(request,'chartpage.html')

def XRP_view(request):
    return render(request,'chartpage.html')

