from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account


class AccountAdmin(UserAdmin):
    model = Account
    list_display = ('username', 'last_login', 'date_joined', 'is_active')
    # list_filter = ('is_admin', 'is_active')
    # list_display_links = ('username',)
    # readonly_fields = ('last_login', 'date_joined')
    # search_fields = ('username',)
    # ordering = ('username',)

    # fieldsets = (
    #     (None, {'fields': ('username', 'password')}),
    #     ('Permissions', {'fields': ('is_staff', 'is_admin', 'is_active')}),
    # )
    # add_fieldsets = (
    #     (None, {
    #         'classes': ('wide',),
    #         'fields': ('email', 'password1', 'password2', 'is_staff', 'is_admin', 'is_active')}
    #      ),
    # )


admin.site.register(Account, AccountAdmin)
