"""
URL configuration for ecommerce_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.http import JsonResponse

# Root API homepage to avoid 404
def home(request):
    return JsonResponse({"message": "Project Nexus API is live!"})

# Swagger/OpenAPI schema view
schema_view = get_schema_view(
    openapi.Info(
        title="Project Nexus API",
        default_version='v1',
        description="E-commerce Backend API",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),

    # Root homepage
    path('', home, name='api-home'),

    # Core app APIs (products + categories via router)
    path('api/', include('core.urls')),

    # JWT auth endpoints
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Future apps (users, cart, orders)
    # path('api/', include('users.urls')),   # user registration & profile
    # path('api/', include('cart.urls')),    # cart endpoints
    # path('api/', include('orders.urls')),  # orders endpoints

    # Swagger/OpenAPI UI
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
