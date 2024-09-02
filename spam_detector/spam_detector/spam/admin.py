from django.contrib import admin
from .models import NewUser, UserSpamNumber, GlobalSpamNumber

# Register your models here.
@admin.register(NewUser)
class NewUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'phone_number')
    search_fields = ('email', 'first_name', 'last_name')

@admin.register(UserSpamNumber)
class UserSpamNumberAdmin(admin.ModelAdmin):
    list_display = ('user', 'spam_number', 'pub_date')
    search_fields = ('spam_number',)
    ordering = ('-pub_date',)

@admin.register(GlobalSpamNumber)
class GlobalSpamNumberAdmin(admin.ModelAdmin):
    list_display = ('spam_number', 'pub_date')
    search_fields = ('spam_numbers',)
    ordering = ('-pub_date',)