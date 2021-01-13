from django.contrib import admin

from .models import New, Advertice

from import_export.admin import ImportExportActionModelAdmin
from import_export import resources
from import_export import fields
from import_export.widgets import ForeignKeyWidget

# admin.site.register(New)
admin.site.register(Advertice)

class NewResource(resources.ModelResource):
    id = fields.Field(column_name='id', attribute='id')
    date = fields.Field(column_name='date', attribute='date')
    subject = fields.Field(column_name='subject', attribute='subject')
    heading = fields.Field(column_name='heading', attribute='heading')
    picture = fields.Field(column_name='picture', attribute='picture')
    description = fields.Field(column_name='description', attribute='description')
    source = fields.Field(column_name='source', attribute='source')

@admin.register(New)
class NewAdmin(ImportExportActionModelAdmin):
    resource_class = NewResource
    list_display = ("id", "date", "subject", "heading", "picture", "description", "source")
    list_filter = ("subject", ) 