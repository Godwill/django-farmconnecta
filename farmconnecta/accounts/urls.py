from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import include, url


urlpatterns = [
    url(r'^accounts/', include('userena.urls')),
    url(r'^messages/', include('userena.contrib.umessages.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)