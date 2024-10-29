from django.urls import path

from common.views import Index, Catalogue

urlpatterns = [
    path("", Index.as_view(), name="index"),
    path("catalogue/", Catalogue.as_view(), name="catalogue")
]