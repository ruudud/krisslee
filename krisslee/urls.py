from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'krisslee.frontpage.views.front', name='frontpage'),
    (r'^admin/', include(admin.site.urls)),
    url(r'^jukebox/', 'django.views.generic.simple.direct_to_template', {
            'template': 'jukebox.html',
        }, name='jukebox'),
    url(r'^snuscalc/', 'django.views.generic.simple.direct_to_template', {
            'template': 'snuscalc.html',
        }, name='snuscalc'),
)
#Hack to get testserver to serve media
if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',
                {'document_root': settings.MEDIA_ROOT}),
    )
