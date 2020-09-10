from django.contrib import admin

from property_book.models import Property_Publishing_house, Property_book, Property_Status

@admin.register(Property_Publishing_house)
class Admin_Property_Publishing_house(admin.ModelAdmin):
    list_display = ['title']
@admin.register(Property_Status)
class Admin_Property_Status(admin.ModelAdmin):
    list_display = ['title']
@admin.register(Property_book)
class Admin_Property_book(admin.ModelAdmin):
    list_display = ['title', 'property_Publishing_house', 'serial_number', 'year', 'rack', 'shelf', 'property_status']


# это делает наш декоратор когда мы его на вешиваем
# admin.site.register(Property_Publishing_house, Admin_Property_Publishing_house)






