from django.urls import path
from . views import index, admin_dashboard

urlpatterns = [
    path("", index, name="index"),
    path("admin-dashboard", admin_dashboard, name="admin-dashboard"),
]
