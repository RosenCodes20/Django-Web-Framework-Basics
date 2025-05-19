from django.urls import path

from exam_past_prep.traveler import views

urlpatterns = [
    path('create/', views.create_traveler, name='create-traveler'),
    path('details/', views.traveler_details, name='details-traveler'),
    path('delete/', views.traveler_delete, name='delete-traveler'),
    path('edit/', views.traveler_edit, name='edit-traveler'),
]