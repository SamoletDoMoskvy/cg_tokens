from django.contrib.admin import (
    ModelAdmin,
    register,
)

from .models import Token


@register(Token)
class TokenModelAdmin(ModelAdmin):
    fields = (
        'id',
        'address',
        'name',
        'symbol',
        'price_in_dollars',
        '_created_at',
        '_updated_at',
    )
    list_display = (
        'id',
        'address',
        'name',
        'symbol',
        'price_in_dollars',
    )
    readonly_fields = (
        'id',
        '_created_at',
        '_updated_at'
    )