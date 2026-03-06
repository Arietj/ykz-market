"""
URL configuration for ykz_market project.

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
from django.urls import path, include
from rest_framework import routers
from apps.product.urls import router as product_router
from apps.cart.urls import default_router as cart_router
from apps.orders.urls import default_router as orders_router
from apps.accounts.views import RegisterAPIView
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView


main_router = routers.DefaultRouter()

main_router.registry.extend(product_router.registry)
main_router.registry.extend(cart_router.registry)
main_router.registry.extend(orders_router.registry)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/v1/", include(main_router.urls)),
    path("api/v1/register/", RegisterAPIView.as_view(), name="register"),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]