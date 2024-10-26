
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("exam_preparation_1.world_of_speed.urls"))
]
