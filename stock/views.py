import textwrap

from testproject.settings import base

import os
from django.http import HttpResponse, JsonResponse
from django.views.generic.base import View
from django.shortcuts import render, redirect
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib.staticfiles.templatetags.staticfiles import static


from django.shortcuts import render
from django.views.generic import View


def home(request):
    return render(request, 'stock/home.html')

def stock_list_page(request):
    file = open(os.path.join(base.BASE_DIR, 'stock/statics/stock/alltickers_2018.csv'))
    data = [i.split(',') for i in file.readlines()]
    for j in data:
        j[2] = j[2].zfill(6)
    paginator = Paginator(data, 50)
    page = request.GET.get('page')
    data_paged = paginator.get_page(page)
    context = {'file_content': data_paged}
    file.close()
    return render(request, 'stock/stock_list_page.html', context)

def stock_search(request):
    if request.GET and request.GET['q'] != '':
        keyword = request.GET['q'].upper()
        file = open(os.path.join(base.BASE_DIR, 'stock/statics/stock/alltickers_2018.csv'))
        data = [i.split(',') for i in file.readlines()]
        file.close()
        for j in data:
            j[2] = j[2].zfill(6)
        items = [i for i in data if keyword in i[2] or keyword in i[1]]
        if len(items)==1:
            context = {'data':items[0] , 'ticker':items[0][2]}
            return render(request, 'stock/stock_detail.html', context)
        else:
            paginator = Paginator(items, 40)
            page = request.GET.get('page')
            data_paged = paginator.get_page(page)
            context = {'file_content': data_paged , 'keyword':keyword}
            return render(request, 'stock/stock_list_page.html', context)
    else:
        return redirect('stock-home')

def stockList(request):
    file = open(os.path.join(base.BASE_DIR, 'stock/statics/stock/alltickers_2018.csv'))
    data = [i.split(',') for i in file.readlines()]
    data2 = [{'id':j[0],'name':j[1],'ticker':j[2].zfill(6)} for j in data]
    file.close()
    print('data2:',len(data2))
    return JsonResponse(data2, safe=False)

def testapi(request):
    data = [{ 'data1':'test',
    'data2':'test2'}
    ,{ 'data3':'test',
    'data4':'test2'}]
    return JsonResponse(data, safe=False)

class StockListPage(View):
    #hold
    file = open(os.path.join(base.BASE_DIR, 'stock/statics/stock/alltickers_2018.csv'))
    data = [i.split(',') for i in file.readlines()]
    for j in data:
        j[2] = j[2].zfill(6)
    template_name = 'stock/stock_list_page_cbv.html'
    context_object_name = {'file_content': data}
    paginate_by = 5

class StockListPage2(View):
    #hold
    template_name = 'stock/stock_list_page_cbv.html'
    context_object_name = 'posts'
    paginate_by = 5


def stock_detail(request, ticker_id):
    file = open(os.path.join(base.BASE_DIR, 'stock/statics/stock/alltickers_2018.csv'))
    data = [i.split(',') for i in file.readlines()]
    info = []
    for j in data:
        if j[0] == ticker_id:
            info = j
    ticker = info[2].zfill(6)
    print('check',info)
    context = {'data':info , 'ticker':ticker}
    return render(request, 'stock/stock_detail.html', context )

def stock_detail2(request, ticker_id):
    file = open(os.path.join(base.BASE_DIR, 'stock/statics/stock/alltickers_2018.csv'))
    data = [i.split(',') for i in file.readlines()]
    info = []
    for j in data:
        if j[0] == ticker_id:
            info = j
    ticker = info[2].zfill(6)
    
    context = {'data':info , 'ticker':ticker}
    return render(request, 'stock/stock_detail_amchart.html', context )

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime,date

class ChartData(APIView):
    authentication_classes = []
    permission_classes = []
    def get(self, request, format=None,  *args, **kwargs):
        ticker = self.kwargs['ticker']
        print('ticker:',ticker)
        df = pd.read_pickle(os.path.join(base.BASE_DIR, 'stock/statics/stock/data/{}'.format(ticker)))
        labels = df.index.strftime('%Y-%m-%d').tolist()
        value1 = df.y.tolist()
        value2 = df.yhat.tolist()
        print('length:',len(value2))
        content = {
        "labels":labels,
        "value1":value1,
        "value2":value2,
        }
        return Response(content)

class AutoComplete(APIView):
    authentication_classes = []
    permission_classes = []
    def get(self, request, format=None,  *args, **kwargs):
        ticker = self.kwargs['ticker']
        print('ticker:',ticker)
        df = pd.read_pickle(os.path.join(base.BASE_DIR, 'stock/statics/stock/data/{}'.format(ticker)))
        labels = df.index.strftime('%Y-%m-%d').tolist()
        value1 = df.y.tolist()
        value2 = df.yhat.tolist()
        print('length:',len(value2))
        content = {
        "labels":labels,
        "value1":value1,
        "value2":value2,
        }
        return Response(content)

class HomePageView(View):

    def dispatch(request, *args, **kwargs):
        response_text = textwrap.dedent('''\
            <html>
            <head>
                <title>Greetings to the world</title>
            </head>
            <body>
                <h1>Greetings to the world</h1>
                <p>Hello, world!</p>
            </body>
            </html>
        ''')
        return HttpResponse(response_text)