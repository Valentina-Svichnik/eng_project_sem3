from django.contrib import admin

from .models import Country, City, District, Temperature, Humidity, Pressure, Wind, Precipitation, Precipitation_icon, Cloud, Cloudy_icon, New, Day, User, Advertice

admin.site.register(Country)
# class CountryAdmin(admin.ModelAdmin):
#     list_display = ['name', 'population', 'square']
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
admin.site.register(New)
admin.site.register(Day)
admin.site.register(User)
admin.site.register(Advertice)