# apps/pages/urls.py
from django.urls import path
from .views import landing_view, login_view, log_hours_view

urlpatterns = [
    path('', landing_view, name='landing'),           # e.g. /pages/
    path('login/', login_view, name='login'),         # e.g. /pages/login/
    path('log-hours/', log_hours_view, name='log_hours'),
]
