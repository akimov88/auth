from django.contrib import admin
from django.urls import path
from core.authentication import CustomAdminSite


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('admin/', CustomAdminSite().urls),
]
