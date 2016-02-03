from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^price/', include('price.urls')),
    url(r'^admin/', admin.site.urls),
]