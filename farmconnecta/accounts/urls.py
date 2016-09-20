from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic.base import TemplateView
import views
admin.autodiscover()

urlpatterns = [
    # url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^accounts/profile/$', TemplateView.as_view(template_name='account/profile.html')),
	url(r'^accounts/(?P<pk>\d+)/follow/$', views.follow, name="follow_user"),
	url(r'^accounts/(?P<pk>\d+)/unfollow/$', views.unfollow, name="unfollow_user"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)