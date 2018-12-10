from django.conf import settings
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.http.response import HttpResponse
from django.views.static import serve as static_serve
from wiki.compat import include, url
from testproject import views
from testproject import mysites as sites
##
from .my_views.article import ArticleView
from django.views.generic.base import View

##
from .my_views import accounts

admin.autodiscover()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^robots.txt', lambda _: HttpResponse('User-agent: *\nDisallow: /')),
    url(r'^test1/', views.test1, name='wikitest1'),
    # url(r'^test2/', views.test2, name='wikitest2'),
]

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', static_serve, {'document_root': settings.MEDIA_ROOT}),
    ]


urlpatterns += [
    url(r'^notify/', include('django_nyt.urls')),
    url(r'^_test/', views.hello_fn),
    url(r'^_test1/', views.HelloView.as_view()),
    url(r'^_test2/', views.SuperVillainView.as_view()),
    url(r'^_test3/', views.GreetView.as_view()),
    url(r'^_test4/', views.GreetView2.as_view(),kwargs={'name':'test4'}),
    url(r'^_test5/', views.GreetView3.as_view(),kwargs={'name':'test5-GreetView3'}),
    url(r'^_test11/', ArticleView.as_view(), name='myArticleView',kwargs={'path': ''}),
    url(r'^_test12/', ArticleView.as_view(template_name='wiki/dir.html'), name='myArticleView2',kwargs={'path': ''}),
    url(r'^_test13/', ArticleView.as_view(template_name='wiki/test3.html'), name='myArticleView3',kwargs={'path': '', 'string':'stirng'}),
    url(r'^_test21/', views.WikiListView.as_view(), name='myWikiListView',kwargs={'path': ''}),
    url(r'^_test22/', views.WikiListView.as_view(), name='myWikiListView2',kwargs={'path': ''}),
    url(r'^_test23/', views.WikiListView.as_view(template_name='wiki/test3.html'), name='myWikiListView3',kwargs={'path': ''}),
    url(r'^_accounts/login/$',accounts.Login.as_view(),name='login'),
    url(r'^_accounts/logout/$',accounts.Logout.as_view(),name='logout'),
    url(r'^_accounts/sign-up/$',accounts.Signup.as_view(),name='signup'),
    url(r'^stock/', include('stock.urls')),
    url(r'', include('testproject.myurls')),
]

handler500 = 'testproject.views.server_error'
handler404 = 'testproject.views.page_not_found'
