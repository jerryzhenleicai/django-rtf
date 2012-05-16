from django.conf.urls.defaults import *
from django.conf import settings
import views

urlpatterns = patterns('',
    (r'^$', views.edit_form),
    (r'^show/', views.show_candidate),
)


if settings.DEBUG:
    from django.views.static import serve

    urlpatterns += patterns('',
        (r'^' + settings.MEDIA_URL.lstrip('/') + '(?P<path>.*)$', serve,
            {'document_root': settings.MEDIA_ROOT}),
        )
