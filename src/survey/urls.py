from django.urls import path
from survey import views

urlpatterns = [
    path('', views.base),
]