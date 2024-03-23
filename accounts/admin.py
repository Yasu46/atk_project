from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account


class AccountAdmin(UserAdmin):
    model = Account
    list_display = ('username', 'last_login', 'date_joined', 'is_active')


admin.site.register(Account, AccountAdmin)
