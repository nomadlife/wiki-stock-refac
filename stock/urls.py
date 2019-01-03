from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='stock-home'),

    url(r'^cbvtest/$', views.HomePageView.as_view()),

    url(r'^list/$', views.stock_list_page, name='stock-list'),
    url(r'^list5/$', views.StockListPage.as_view()),
    url(r'^list6/$', views.StockListPage2.as_view()),

    url(r'^search/$', views.stock_search, name='stock-search'),

    url(r'^detail/(?P<ticker_id>.+?)/', views.stock_detail, name='stock-detail'),
    url(r'^detail_am_demo/(?P<ticker_id>.+?)/', views.stock_detail_am_demo, name='stock-detail-amdemo'),
    url(r'^detail_am/(?P<ticker_id>.+?)/', views.stock_detail_am, name='stock-detail-am'),
    
    url(r'^detail_2/(?P<ticker_id>.+?)/', views.stock_detail_2, name='stock-detail-2'),

    url(r'^api/test/data/',views.testapi, name='api-test-data'),
    url(r'^api/chart/data/(?P<ticker>.+?)/',views.ChartData.as_view(), name='api-chart-data'),
    url(r'^api/minichart/data/(?P<ticker>.+?)/',views.miniChartData.as_view(), name='api-minichart-data'),
    url(r'^api/minichartpredict/data/(?P<ticker>.+?)/',views.miniChartData_predict.as_view(), name='api-minichartpredict-data'),
    url(r'^api/amchart/data/(?P<ticker>.+?)/',views.amChartData4.as_view(), name='api-amchart-data'),
    url(r'^api/amchart/json/(?P<ticker>.+?)/',views.amChartData_json.as_view(), name='api-amchart-json'),
    url(r'^api/amchart/json2/(?P<ticker>.+?)/',views.amChartData_json2.as_view(), name='api-amchart-json2'),
    url(r'^api/stocklist/data/',views.stockList, name='api-stocklist-data'),
    url(r'^api/autocomplete/data/(?P<ticker>.+?)/',views.AutoComplete.as_view(), name='api-autocomplete-data'),

]
