from django.contrib import admin
from django.urls import path

from send_email.core import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.enviar_email, name="enviar_email"),
]
