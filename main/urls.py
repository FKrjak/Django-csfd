from django.urls import include, path

urlpatterns = [
    path("", include("csfd.urls")),
]
