from django.urls import path
from . import views  # Import views from the same directory

urlpatterns = [
    path('', views.index, name='accounts_index'),
    # Add additional URL patterns here as needed
]
