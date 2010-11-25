from django.conf import settings
from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from django.utils.translation import ugettext as _

from django.contrib import admin
admin.autodiscover()


handler500 = "pinax.views.server_error"

import forms

urlpatterns = patterns("",
    url(r"^$", 'fanzine.views.current_fanzine_details', {
    }, name="home"),
    url(r"^admin/", include(admin.site.urls)),
    url(r"^planet/", include("planet.urls")),
    #url(r"^fanzine/", include("fanzine.urls")),
    url(
        r'^(?P<year>[0-9]+)/(?P<month>[0-9]+)/(?P<day>[0-9]+)/(?P<slug>\w+)/$',
        'fanzine_details',
        name='fanzine_details',
    ),
    url(r'^admin_tools/', include('admin_tools.urls')),
    url(
        r"^subscription/$", 
        "views.form", 
        {
            'form_class': forms.SubscriptionForm,
            'success_message': _('your subscription is done! thanks for choosing yourlabs'),
        }, 
        name="subscription_form"
    ),
)


if settings.SERVE_MEDIA:
    urlpatterns += patterns("",
        url(r"", include("staticfiles.urls")),
    )
