from django.urls import path, include
from . import views


urlpatterns = [
    path('connections/', views.profileConnectionView, name="connections"),
    path('people/', views.peoplePage, name='people'),
    path("connection/add/<id>/", views.addConnection, name="add_connection"),
    path('connection/confirm/<id>/', views.confirmConnection, name="confirm_connection"),
    path('<id>/', views.profileDetail, name="profile_detail"),
    path('', views.profileView, name="profile"),
]
