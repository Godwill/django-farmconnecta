from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin
from .models import Categories


admin.site.register(
    Categories,
    DraggableMPTTAdmin,
    list_display=(
        'tree_actions',
        'indented_title',
    ),
    list_display_links=(
        'indented_title',
    ),
)