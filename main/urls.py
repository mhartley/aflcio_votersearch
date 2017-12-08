from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.returnindex, name='index'),
    url(r'votes/([0-9]{1,3})', views.vote_table),
    url(r'elements', views.elements),
    url(r'welcomematdev', views.welcomemat),
    url(r'legislatorhandle', views.legislatorhandle),
    url(r'error', views.error),
    url(r'emailinputhandle', views.welcomemathandle),
]




