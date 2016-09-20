from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
import views


urlpatterns = [
	url(r'^vendor_products/$', views.vendor_product_list, name="vendor_product_list"),
	url(r'^vendor_product/new/$', views.new_vendor_product, name="new_vendor_product"),
	url(r'^vendor_product/(?P<pk>\d+)/$', views.vendor_product_details, name="vendor_product_details"),
	url(r'^vendor_product/(?P<pk>\d+)/edit/$', views.edit_vendor_product, name="edit_vendor_product"),
	url(r'^vendor_product/(?P<pk>\d+)/delete/$', views.delete_vendor_product, name="delete_vendor_product"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)