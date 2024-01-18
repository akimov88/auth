from django.contrib import admin
from django.urls import path

from core.views import KeycloakCallbackAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('keycloak_callback/', KeycloakCallbackAPIView.as_view()),
]

admin.site.login_template = 'admin/custom_login.html'
admin.site.site_header = 'Custom django administration'
