from django.conf.urls import url
from . import views

app_name = 'zip_to_rep'

urlpatterns = [
    #/zip_to_rep/
    url(r'^$', views.index, name='index'),

    #/zip_to_rep/<zipcode>/
    url(r'^(?P<zipcode>[0-9]+)/$', views.zip_detail, name='zipcode_detail'),

    #zip_to_rep/<zipcode>/<rep name>/
#    url(r'^(?P<zipcode>[0-9]+)/<rep_name>/$', views.zip_detail, name='rep_detail'),

    #zip_to_rep/60614/
 #   url(r'^(?P<zipcode>[0-9]+)/(<dist_state,dist_num>[A-Z][A-Z][0-9])/$', views.zip_detail, name='zip_detail'),

    #/zipcode/add/
    url(r'^zipcode/add/$', views.ZipAdd.as_view(), name='zip_add'),

]
