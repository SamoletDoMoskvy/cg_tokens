from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK

from .models import Token
from .serializers import TokenModelSerializer
from .filters import TokenFilterPagination
from .services.functions import _get_all_tokens
from base.coingecko_parser import parse_coingecko_tokens


class TokenModelViewSet(ModelViewSet):
    queryset = Token.displayed_objects
    serializer_class = TokenModelSerializer
    pagination_class = TokenFilterPagination

    def get_all_tokens(self, request):
        data = _get_all_tokens(self)
        return Response(
            data=data,
            status=HTTP_200_OK,
        )

    def update_tokens(self, request):
        """
        Мэдскиллз - запуск логики парсера через эндпоинт
        """
        parse_coingecko_tokens()
        return Response(
            data='Updated',
            status=HTTP_200_OK,
        )
