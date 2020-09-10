from django.contrib import admin
from readers.models import Reader, ReaderPhone, ReaderAddress, ReaderTicket


@admin.register(Reader)
class ReaderAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'birthday']
    search_fields = ['fisrt_name', 'last_name']


@admin.register(ReaderPhone)
class ReaderPhoneAdmin(admin.ModelAdmin):
    list_display = ['reader', 'phone_format', 'is_active']
    search_fields = ['phone_number', 'reader__first_name', 'reader__last_name']

    def phone_format(self, obj):
         phone = str(obj.phone_number)
         return f'{phone[0:2]}({phone[2:5]}) {phone[5:8]}-{phone[8:10]}-{phone[10:12]}'


@admin.register(ReaderAddress)
class ReaderAddressAdmin(admin.ModelAdmin):
    list_display = ['city_reader', 'street_reader', 'house_reader', 'is_active']


@admin.register(ReaderTicket)
class ReaderTicketAdmin(admin.ModelAdmin):
    list_display = ['ticket_number', 'valid_until', 'is_active']



# это делает наш декоратор когда мы его на вешиваем
# admin.site.register(Reader, ReaderAdmin)
