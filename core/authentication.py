from django.contrib import admin


class CustomAdminSite(admin.AdminSite):
    login_template = "admin/custom_login.html"
