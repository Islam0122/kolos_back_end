from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
from .drf_yasg import urlpatterns as urls_swagger

urlpatterns = [
                  path('api/v1/distributor/', include('distributor.urls')),
                  path('admin/', admin.site.urls),
                  path('api/v1/product/', include("product.urls")),
                  # users
                  path('api/v1/users/', include('users.urls')),

              ] + urls_swagger

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [path("__debug__/", include(debug_toolbar.urls))]
