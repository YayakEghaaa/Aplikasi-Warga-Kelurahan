from django.contrib import admin
from django.urls import path
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('warga/', include('warga.urls')),
    path('api/', include('warga.api_urls')),
    path('api/auth/token/', obtain_auth_token, name='api-token-auth'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
