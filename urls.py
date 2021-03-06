from django.conf import settings
from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from django.utils.translation import ugettext as _

from django.contrib import admin
admin.autodiscover()

import views

handler500 = "pinax.views.server_error"

from feeds import BlogFeedAll, BlogFeedUser
blogs_feed_dict = {"feed_dict": {
    "all": BlogFeedAll,
    "only": BlogFeedUser,
}}

urlpatterns = patterns("",
    url(r"^$", 'fanzine.views.current_fanzine_details', {
    }, name="home"),
    url(r"^admin/", include(admin.site.urls)),
    url(r'^planet/posts/(?P<post_id>\d+)/$', views.planet_post_detail, name="planet_post_detail"),
    url(r"^planet/", include("planet.urls")),
    #url(r"^fanzine/", include("fanzine.urls")),
    url(
        r'^(?P<year>[0-9]+)/(?P<month>[0-9]+)/(?P<day>[0-9]+)/(?P<slug>[a-zA-Z0-9-]+)/$',
        'fanzine.views.fanzine_details',
        name='fanzine_details',
    ),
    url(r'^admin_tools/', include('admin_tools.urls')),
    url(r"^announcements/", include("announcements.urls")),
    url(r"^account/", include("pinax.apps.account.urls")),
    url(r"^notices/", include("notification.urls")),
    url(r"^comments/", include("threadedcomments.urls")),
    url(r"^i18n/", include("django.conf.urls.i18n")),
    url(r"^announcements/", include("announcements.urls")),
    url(r"^blog/", include("pinax.apps.blog.urls")),
    url(r"^feeds/posts/(.*)/$", "django.contrib.syndication.views.feed", blogs_feed_dict),
)


if settings.SERVE_MEDIA:
    urlpatterns += patterns("",
        url(r"", include("staticfiles.urls")),
    )
