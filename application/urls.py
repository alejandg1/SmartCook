from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('smartcook.urls')),
    path('user/', include('security.urls')),
    path('accounts/', include('django.contrib.auth.urls'))
]
