"""
URL configuration for realestate project.

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
from django.urls import path
from store import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add/',views.RealEstateCreate.as_view(),name="create-property"),
    path('list/',views.RealEstateList.as_view(),name="property-list"),
    path("realestate/<int:pk>/update",views.RealEstateUpdate.as_view(),name="property-update"),
    path("realestate/<int:pk>/delete",views.RealEstateDelete.as_view(),name="property-delete"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)