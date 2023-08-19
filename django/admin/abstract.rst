Admin Abstract
==============

>>> # doctest: +SKIP
... from django.contrib import admin
... from django.http import HttpRequest
... from django.utils.translation import gettext_lazy as _
...
...
... admin.site.site_header = _('Project Name')
... admin.site.index_title = _('Dashboard')
... admin.site.site_title = _('Project Name')
...
...
... class BaseAdmin(admin.ModelAdmin):
...     def get_readonly_fields(self, request: HttpRequest, obj: admin.ModelAdmin | None = None):
...         readonly_fields = super().get_readonly_fields(request, obj)
...         readonly_fields += ('uuid', 'created_date', 'created_user',  'modified_date', 'modified_user', 'is_deleted')
...         return readonly_fields
...
...     def save_model(self, request: HttpRequest, obj: admin.ModelAdmin, form, change: bool):
...         if not change:
...             obj.created_user = request.user
...         obj.modified_user = request.user
...         return super().save_model(request, obj, form, change)
...
