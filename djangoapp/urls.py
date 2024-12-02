from django.urls import path
from . import views  # Import views from the same app

urlpatterns = [
    path('', views.index, name='index'),  # Add a default view for testing
]
