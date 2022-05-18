from rest_framework.serializers import ModelSerializer
from rest_framework.fields import FloatField

from tokens_app.models import Token


class TokenModelSerializer(ModelSerializer):
    priceInDollars = FloatField(source='price_in_dollars')

    class Meta:
        model = Token
        fields = (
            'address',
            'name',
            'symbol',
            'priceInDollars',
            'network',
        )
