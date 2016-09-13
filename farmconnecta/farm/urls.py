from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
import views


urlpatterns = [
	url(r'^farm/new/$', views.new_farm, name="new_farm"),
	url(r'^farm/(?P<pk>\d+)/$', views.farm_details, name="farm_details"),
	url(r'^farm/(?P<pk>\d+)/edit/$', views.edit_farm, name="edit_farm"),
	url(r'^farm/(?P<pk>\d+)/delete/$', views.delete_farm, name="delete_farm"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)