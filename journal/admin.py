from django.contrib import admin
from journal.models import Journal, JournalEmployee

@admin.register(Journal)
class AdminJournal(admin.ModelAdmin):
    list_display = ['ticket', 'book_property', 'check_int','check_out']

@admin.register(JournalEmployee)
class AdminJornalEmployee(admin.ModelAdmin):
    list_display = ['first_name', 'last_name']

# это делает наш декоратор когда мы его на вешиваем
# admin.site.register(Journal,AdminJournal)

