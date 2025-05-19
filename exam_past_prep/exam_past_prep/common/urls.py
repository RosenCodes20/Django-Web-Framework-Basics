from django.urls import path

from exam_past_prep.common import views

urlpatterns = [
    path('', views.index, name='index'),
    path('all-trips/', views.all_trips, name='all-trips')
]