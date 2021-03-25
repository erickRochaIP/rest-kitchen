from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from kitchen.views import ReceitaViewSet

router = routers.DefaultRouter()
router.register(r'receitas', ReceitaViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth', include('rest_framework.urls'))
]
