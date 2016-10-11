from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
import views
import mptt_urls


urlpatterns = [
    # url(r'^categories/$',
    #     mptt_urls.view(model='farmconnecta.categories.models.Categories',
    #                    view='farmconnecta.categories.views.category',
    #                    slug_field='slug'),
    #     name='category'),
	# url(r'^categories/$', views.categories_list, name="categories_list"),
    # url(r'^categories/(?P<path>.*)/$', views.category_details, name='category_details'),
	url(r'^categories/(?P<path>.*)',mptt_urls.view(model='farmconnecta.categories.models.Categories',
                       view='farmconnecta.categories.views.category',
                       slug_field='slug'),name='category'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)