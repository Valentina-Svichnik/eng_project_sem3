from django.contrib import admin

from .models import Country, City, District, Temperature, Humidity, Pressure, Wind, Precipitation, Precipitation_icon, Cloud, Cloudy_icon, Day

admin.site.register(Country)
admin.site.register(City)
admin.site.register(District)
admin.site.register(Temperature)
admin.site.register(Humidity)
admin.site.register(Pressure)
admin.site.register(Wind)
admin.site.register(Precipitation)
admin.site.register(Precipitation_icon)
admin.site.register(Cloud)
admin.site.register(Cloudy_icon)
admin.site.register(Day)

# @admin.register(SaleSummary)
# class SaleSummaryAdmin(ModelAdmin):
#     change_list_template = 'admin/sale_summary_change_list.html'
#     date_hierarchy = 'created'