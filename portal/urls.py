"""portal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from django_rest_passwordreset import urls as reset_urls
from profiles import views as profile_views

urlpatterns = [
    path("activate/<slug:uidb64>/<slug:token>/", profile_views.activate, name="activate"),
    path("api/token/auth/", obtain_jwt_token),
    path("api/token/refresh/", refresh_jwt_token),
    path("api/password_reset/", include("django_rest_passwordreset.urls", namespace="password_reset")),
    path("api/", include(("api.urls", "api"), namespace="api")),
    path("admin/", admin.site.urls),
    re_path("^", TemplateView.as_view(template_name="index.html"), name="index"),
]
