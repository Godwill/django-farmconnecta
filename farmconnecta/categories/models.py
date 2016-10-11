from django.core.urlresolvers import reverse
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Categories(MPTTModel):
    name = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True)
    slug = models.SlugField(blank=True)
    images = models.ImageField(upload_to='categories', blank=True)
    description = models.TextField(blank=True)

    class MPTTMeta:
        order_insertion_by = ['name']

    def get_absolute_url(self):
        return reverse('category', kwargs={'path': self.get_path()})

    class Meta:
        unique_together = ('slug', 'parent')
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name
