from django.conf import settings
from django.http import HttpResponseServerError
from django.template import loader
from django.template.context import RequestContext
from django.views.decorators.csrf import requires_csrf_token
from django.shortcuts import render
from django.utils.decorators import method_decorator
from wiki.views.article import ArticleView
from wiki.models.article import Article
from wiki.decorators import get_article

from django.http import HttpResponse

##
from wiki.views.mixins import ArticleMixin
from wiki.views.accounts import Login
from django.utils.translation import gettext as _
from django.contrib.auth import get_user_model as auth_login

@requires_csrf_token
def server_error(request, template_name='500.html', **param_dict):
    # You need to create a 500.html template.
    t = loader.get_template(template_name)
    return HttpResponseServerError(t.render(RequestContext(
        request,
        {
            'MEDIA_URL': settings.MEDIA_URL,
            'STATIC_URL': settings.STATIC_URL,
            'request': request,
        },
    )))


def page_not_found(request, template_name='404.html', exception=None):
    response = server_error(
        request,
        template_name=template_name,
        exception=exception
    )
    response.status_code = 404
    return response

def test1(request):
    return render(request, 'wiki/test1.html', {'wiki_pagetitle':'pagetitle', 'string':'param test'})  

def test2(request):
    return render(request, 'wiki/test2.html', {'title':'Test'})  
    
def hello_fn(request, name="World"):
    return HttpResponse("Hello {}!".format(name))

from django.views.generic import View
class HelloView(View):
    def get(self, request, name="World"):
        return HttpResponse("Hello {}!!".format(name))

class GreetView(View):
    greeting = "Hello {}!!!"
    default_name = "World"
    def get(self, request, **kwargs):
        name = kwargs.pop("name", self.default_name)
        return HttpResponse(self.greeting.format(name))

class GreetView2(View):
    greeting = "Hello {}!!!"
    default_name = "World"
    def get(self, request, **kwargs):
        name = kwargs.pop("name", self.default_name)
        return HttpResponse(self.greeting.format(name))

class GreetView3(View):
    template_name = 'wiki/test3.html'
    greeting = "Hello {}!!!"
    default_name = "World"
    def get(self, request, **kwargs):
        name = kwargs.pop("name", self.default_name)
        return HttpResponse(self.greeting.format(name))

class SuperVillainView(GreetView):
    greeting = "We are the future, {}. Not them. "
    default_name = "my friend"

def myhome(request):
    return render(request, 'base.html', {'title':'HOME'})  



class WikiListView(ArticleView):
    # template_name = 'wiki/test3.html'
    # model = Article
    # revision = current_revision
#     date = created
    # context_object_name = 'posts'
    # ordering = ['-date_posted']
    # @method_decorator(get_article(can_read=True))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        kwargs['path'] = ''
        return ArticleMixin.get_context_data(self, **kwargs)

# class MyLoginView(Login):
#     def form_valid(self, form, *args, **kwargs):
#         auth_login(self.request, form.get_user())
#         messages.info(self.request, _("로그인 성공!"))
#         if self.request.GET.get("next", None):
#             return redirect(self.request.GET['next'])
#         if django_settings.LOGIN_REDIRECT_URL:
#             return redirect(django_settings.LOGIN_REDIRECT_URL)
#         else:
#             if not self.referer:
#                 return redirect("wiki:root")
#             return redirect(self.referer)
