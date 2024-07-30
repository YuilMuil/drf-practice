import os

from django.urls import include, path, re_path
from django.conf import settings
from django.contrib import admin

from rest_framework import permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from common.statics import static
from common.environments import get_env


# Directory : ../api/versions
directory = os.path.join(  # Join filename and directory paths.
    os.path.dirname(  # ../
        os.path.dirname(  #  Current directory.
            os.path.realpath(__file__)  # Current file name with absolute path.
        )
    ), 'api', 'versions'
)

api_urls = []
version_map_dict = {}

for _path, _, _files, in os.walk(directory):
    depth = _path[len(directory) + len(os.path.sep):].count(os.path.sep)
    if _path != directory and depth == 1 and 'urls.py' in _files:
        version, api_name = _path.split(os.path.sep)[-2:]

        if not version_map_dict.get(version, None):
            version_map_dict[version] = []

        _include = 'api.versions.{}.{}.urls'.format(version, api_name)

        api_urls.append(path(f"{version}/", include(_include)))


urlpatterns = [
  path('api/', include(api_urls))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if "test" in get_env("DJANGO_SETTINGS_MODULE"):
    urlpatterns.append(
        path('admin/', admin.site.urls),
    )

schema_view = get_schema_view(
    openapi.Info(
        title="DRF Practice Backend API",
        default_version='v1',
        description=f"DRF Practice Backend Swagger.",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="rootsik1221@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

if settings.DEBUG:
    urlpatterns += [
        re_path(r'swagger(?P<format>\.json|\.yaml)$',
                schema_view.without_ui(cache_timeout=0), name='schema-json'),
        re_path(r'swagger/$',
                schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
        re_path(r'redoc/$',
                schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    ]
