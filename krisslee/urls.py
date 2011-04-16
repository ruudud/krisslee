from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', 'krisslee.frontpage.views.front'),
    (r'^admin/', include(admin.site.urls)),
    (r'^jukebox/', 'django.views.generic.simple.direct_to_template', {
            'template': 'jukebox.html', 
        }),
    (r'^joern\.jpg', 'django.views.generic.simple.redirect_to', {
            'url': '/',
        }),
)
#Hack to get testserver to serve media
if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',
                {'document_root': settings.MEDIA_ROOT}),
    )
