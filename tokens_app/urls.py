from django.urls import path

from .views import TokenModelViewSet


urlpatterns = [
    path(
        '',
        TokenModelViewSet.as_view(
            {
                'get': 'get_all_tokens',
            }
        )
    ),
    path(
        'update',
        TokenModelViewSet.as_view(
            {
                'get': 'update_tokens',
            }
        )
    )
]