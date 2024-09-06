from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.views.static import serve
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from .views import home

urlpatterns = [
    path('', home, name='home')

]
#------------add custom media path for production mode-----------
urlpatterns += re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
if settings.DEBUG==False:
    handler404 = "services.views.page_not_found"
    handler500 = "services.views.server_error"
else:
    pass