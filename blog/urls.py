from django.conf.urls import url
from blog.views import archive
urlpatterns = [
    url(r'^$', archive),
    #url(r'^exit$', views.LoginOutView.as_view(), name='exit'),
    #url(r'^thanks$', views.ThanksView.as_view(), name='thanks'),
    # ex: /polls/5/
    #url(r'^(?P<pk>[0-9]+)/$', DetailView.as_view(), name='detail'),
    # ex: /polls/5/results/
    #url(r'^(?P<pk>[0-9]+)/results/$', ResultsView.as_view(), name='results'),
    # ex: /polls/5/vote/
    #url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]