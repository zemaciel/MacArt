from django.contrib import admin
from .models import FAQEntry


class FAQEntryAdmin(admin.ModelAdmin):
    list_display = (
        'question',
        'answer',
        'updated_on',
        'created_on'
    )

    ordering = ('question',)


admin.site.register(FAQEntry, FAQEntryAdmin)
