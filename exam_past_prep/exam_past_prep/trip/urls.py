from django.urls import path

from exam_past_prep.trip import views

urlpatterns = [
    path('create/', views.create, name='create-trip'),
    path('<int:pk>/details/', views.trip_details, name='trip-details'),
    path('<int:pk>/delete/', views.trip_delete, name='trip-delete'),
    path('<int:pk>/edit/', views.trip_edit, name='trip-edit'),
]