from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("forumApp.posts.urls")),
    path("", include("forumApp.accounts.urls"))
]
