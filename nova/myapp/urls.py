from django.urls import path

from . import views


urlpatterns = [
    path('nova/', views.FileView.as_view())
]
