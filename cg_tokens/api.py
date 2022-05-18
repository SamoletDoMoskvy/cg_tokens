from django.urls import(
    include,
    path,
)


urlpatterns = [
    path('tokens', include('tokens_app.urls')),
]