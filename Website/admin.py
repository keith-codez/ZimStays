from django.contrib import admin
from .models import Home, City, HomeImage, Amenity, Reservation, Contact


class HomeImageInline(admin.TabularInline):
    model = HomeImage
    extra = 1  # Number of extra forms to display

class HomeAdmin(admin.ModelAdmin):
    inlines = [HomeImageInline]
    list_display = ('title', 'city', 'available_from', 'available_to', 'price_per_night')
    list_filter = ('city', 'available_from', 'available_to')
    search_fields = ('title', 'city__name')

# Register your models here.

admin.site.register(Home, HomeAdmin)
admin.site.register(City)
admin.site.register(Amenity)
admin.site.register(Reservation)
admin.site.register(Contact)