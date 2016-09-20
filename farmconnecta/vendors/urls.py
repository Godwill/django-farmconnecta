from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
import views


urlpatterns = [
	url(r'^vendors/$', views.vendor_list, name="vendor_list"),
	url(r'^vendors/new/$', views.new_vendor, name="new_vendor"),
	url(r'^vendors/(?P<pk>\d+)/$', views.vendor_details, name="vendor_details"),
	url(r'^vendors/(?P<pk>\d+)/edit/$', views.edit_vendor, name="edit_vendor"),
	url(r'^vendors/(?P<pk>\d+)/delete/$', views.delete_vendor, name="delete_vendor"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)