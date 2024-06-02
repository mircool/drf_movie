from django.contrib import admin

from .models import Card


class CardAdmin(admin.ModelAdmin):
    list_display = ['card_name', 'card_price', 'duration']
    search_fields = ['card_name']
    list_filter = ['card_name', 'card_price', 'duration']


admin.site.register(Card, CardAdmin)
