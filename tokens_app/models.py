from django.db.models import (
    CharField,
    FloatField,
)

from base.models import AbstractBaseModel


class Token(AbstractBaseModel):
    address = CharField(
        max_length=512,
        verbose_name='address',
        null=True,
    )
    name = CharField(
        max_length=512,
        verbose_name='name',
    )
    symbol = CharField(
        max_length=256,
        verbose_name='symbol',
    )
    price_in_dollars = FloatField(
        default=0,
        null=True,
        verbose_name='price in dollars',
    )
    # TODO: Network must be a FK on Network model, but now we dont have it
    network = CharField(
        max_length=256,
        default='Ethereum',
        verbose_name='network',
    )
