from django.contrib import admin
from .models import CarMake, CarModel

# Inline class for CarModel to allow editing within CarMake admin
class CarModelInline(admin.TabularInline):
    model = CarModel
    extra = 1  # Number of empty forms to display

# Admin class for CarModel (optional customization)
class CarModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'type', 'year', 'dealer_id', 'car_make']
    list_filter = ['type', 'year']
    search_fields = ['name']

# Admin class for CarMake with inline CarModels
class CarMakeAdmin(admin.ModelAdmin):
    inlines = [CarModelInline]
    list_display = ['name', 'description']
    search_fields = ['name']

# Register the models with their admin classes
admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel, CarModelAdmin)
