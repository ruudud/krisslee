from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^krisslee/', include('krisslee.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^$', 'krisslee.frontpage.views.front'),
    (r'^admin/', include(admin.site.urls)),
    (r'^registration/', 'django.views.generic.simple.direct_to_template', {
            'template': 'registration.html', 
        }),
    (r'^jukebox/', 'django.views.generic.simple.direct_to_template', {
            'template': 'jukebox.html', 
        }),
    (r'^joern.jpg', 'django.view.generic.simple.redirect_to', {
            'url': '/',
        }),
)
#Hack to get testserver to serve media
if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',
                {'document_root': settings.MEDIA_ROOT}),
    )
