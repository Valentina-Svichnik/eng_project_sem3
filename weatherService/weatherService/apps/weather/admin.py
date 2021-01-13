from django.contrib import admin
from django.urls import reverse
from django.utils.http import urlencode
from django.utils.html import format_html

from .models import Country, City, District, Temperature, Humidity, Pressure, Wind, Precipitation, Precipitation_icon, Cloud, Cloudy_icon, Day



# admin.site.register(Temperature)
# admin.site.register(Humidity)
# admin.site.register(Pressure)
# admin.site.register(Wind)
# admin.site.register(Precipitation)
# admin.site.register(Precipitation_icon)
# admin.site.register(Cloud)
# admin.site.register(Cloudy_icon)

@admin.register(Day)
class Weather(admin.ModelAdmin):
    list_display = ("date", "id_district", "average_temperature", "average_humidity", "name_precipitation", "average_cloud", "average_pressure", "average_wind")
    list_filter = ("average_temperature", "date" )
    search_fields = ("name_precipitation", "id_district__name" )
    actions = ['unsett','sett']

    def sett(self, request, queryset):
        """Обнулить значение влажности"""
        row_update = queryset.update(average_humidity=0)
        if row_update == 1:
            message_bit = "1 запись была обновлена"
        else:
            message_bit = f"{row_update} записей были обновлены"
        self.message_user(request, f"{message_bit}")

    def unsett(self, request, queryset):
        """Обнулить значение облачности"""
        row_update = queryset.update(average_cloud=0)
        if row_update == 1:
            message_bit = "1 запись была обновлена"
        else:
            message_bit = f"{row_update} записей были обновлены"
        self.message_user(request, f"{message_bit}")

    unsett.short_description = "Обнулить значение облачности"
    unsett.allowed_permissions = ('change', )

    sett.short_description = "Обнулить значение влажности"
    sett.allowed_permissions = ('change',)

@admin.register(District)
class Districtes(admin.ModelAdmin):
    list_display = ("name", "id_city", "popolation", "square")
    list_filter = ("id_city", )    

@admin.register(City)
class Cities(admin.ModelAdmin):
    list_display = ("name", "id_country", "popolation", "square", "view_districtes_link")
    list_filter = ("id_country", )

    def view_districtes_link(self, obj):
        count = obj.district_set.count()
        url = (
            reverse("admin:weather_district_changelist")
            + "?"
            + urlencode({"districtes_id": f"{obj.id}"})
        )
        return format_html('<a href="{}">{} districtes</a>', url, count)
        view_districtes_link.short_description = "districtes"

@admin.register(Country)
class Country(admin.ModelAdmin):
    list_display = ("name", "popolation", "square", "view_cities_link")

    def view_cities_link(self, obj):
        count = obj.city_set.count()
        url = (
            reverse("admin:weather_city_changelist")
            + "?"
            + urlencode({"cities_id": f"{obj.id}"})
        )
        return format_html('<a href="{}">{} cities</a>', url, count)
        view_cities_link.short_description = "cities"

@admin.register(Temperature)
class Temperature(admin.ModelAdmin):
    list_display = ("id_district", "date", "t_morning", "t_day", "t_evening", "t_night","t_average")

@admin.register(Cloud)
class Cloud(admin.ModelAdmin):
    list_display = ("id_district", "date", "c_morning", "c_day", "c_evening", "c_night","c_average")    
          

@admin.register(Humidity)
class Humidity(admin.ModelAdmin):
    list_display = ("id_district", "date", "h_morning", "h_day", "h_evening", "h_night","h_average")   

@admin.register(Pressure)
class Pressure(admin.ModelAdmin):
    list_display = ("id_district", "date", "pressure_morning", "pressure_day", "pressure_evening", "pressure_night","pressure_average")  

@admin.register(Wind)
class Wind(admin.ModelAdmin):
    list_display = ("id_district", "date", "w_morning", "w_day", "w_evening", "w_night","w_average")  

@admin.register(Precipitation)
class Precipitation(admin.ModelAdmin):
    list_display = ("id_district", "date", "p_morning", "p_day", "p_evening", "p_night","p_average")   

@admin.register(Precipitation_icon)
class Precipitation_icon(admin.ModelAdmin):
    list_display = ("name", "icon")       