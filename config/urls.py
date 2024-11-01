"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static


from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

...

schema_view_v1 = get_schema_view(
   openapi.Info(
      title="Course API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="bunyodbekpirnazarov@425gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
   patterns=[
       path('api/v1/', include('app.urls', namespace = "v1")),
   ]
)

schema_view_v2 = get_schema_view(
   openapi.Info(
      title="Course API",
      default_version='v2',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="bunyodbekpirnazarov@425gmail.com",),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
   patterns=[
       path('api/v2/', include('app.urls', namespace = "v2")),
   ]
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('app.urls')),
    path('api/v1/', include('app.urls', namespace="v1")),
    path('api/v2/', include('app.urls', namespace="v2")),

    path('api-auth/', include('rest_framework.urls')),


   path('swagger/v1<format>/', schema_view_v1.without_ui(cache_timeout=0), name='schema-json-v1'),
   path('swagger/v2<format>/', schema_view_v2.without_ui(cache_timeout=0), name='schema-json-v2'),

   path('swagger/v1/', schema_view_v1.with_ui('swagger', cache_timeout=0), name='schema-swagger-v1'),
   path('swagger/v2/', schema_view_v2.with_ui('swagger', cache_timeout=0), name='schema-swagger-v2'),

   path('redoc/v1', schema_view_v1.with_ui('redoc', cache_timeout=0), name='schema-redoc-v1'),
   path('redoc/v2', schema_view_v2.with_ui('redoc', cache_timeout=0), name='schema-redoc-v2'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
