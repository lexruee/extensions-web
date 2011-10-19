
from django.conf.urls.defaults import patterns, url

from errorreports import views

urlpatterns = patterns('',
    url(r'^report/(?P<pk>\d+)',
        views.report_error_view, name='errorreports-report'),

    url(r'^view/(?P<pk>\d+)',
        views.view_error_report_view, name='errorreports-view'),
)
