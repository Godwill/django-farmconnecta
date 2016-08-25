from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
import views


urlpatterns = [
	url(r'^products/$', views.product_list, name="product_list"),
	url(r'^product/new/$', views.new_product, name="new_product"),
	url(r'^product/(?P<pk>\d+)/$', views.product_details, name="product_details"),
	url(r'^product/(?P<pk>\d+)/edit/$', views.edit_product, name="edit_product"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)