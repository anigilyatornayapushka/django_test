from django.contrib import admin
from django.urls import path

from apps.main.views import log_in


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', log_in)
]
