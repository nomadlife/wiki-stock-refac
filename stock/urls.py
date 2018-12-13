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
    url(r'^detail2/(?P<ticker_id>.+?)/', views.stock_detail_2, name='stock-detail-2'),

    url(r'^api/test/data/',views.testapi, name='api-test-data'),
    url(r'^api/chart/data/(?P<ticker>.+?)/',views.ChartData.as_view(), name='api-chart-data'),
    url(r'^api/stocklist/data/',views.stockList, name='api-stocklist-data'),
    url(r'^api/autocomplete/data/(?P<ticker>.+?)/',views.AutoComplete.as_view(), name='api-autocomplete-data'),

]
