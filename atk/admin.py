from .models import ATKResult
from django.contrib import admin


class ATKResultAdmin(admin.ModelAdmin):
    model = ATKResult
    list_display = ('user', 'result', 'image')


admin.site.register(ATKResult, ATKResultAdmin)
