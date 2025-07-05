from django.contrib import admin
from django.urls import path

from django.urls import include
from django.conf import settings
from django.conf.urls.static import static

from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda request: redirect('admin/', permanent=True)),

    # LOCAL APPS
    path('api/v1/store/', include('store.urls')),
    path('api/v1/cart/', include('cart.urls')),
    path('api/v1/blog/', include('blog.urls')),
    path('api/v1/common/', include('common.urls')),
    path('api/v1/accounts/', include('accounts.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
