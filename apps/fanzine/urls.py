from django.conf.urls.defaults import *

urlpatterns = ('fanzine.views',
    url(
        r'^(?P<year>[0-9]+)/(?P<month>[0-9]+)/(?P<day>[0-9]+)/(?P<slug>\w+)/$',
        'fanzine_details',
        name='fanzine_details',
    )
)
