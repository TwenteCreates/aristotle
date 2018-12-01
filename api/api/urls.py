from django.urls import path, include
from django.conf.urls import url
from rest_framework import routers
from analytics.viewsets import PupilView, ConceptView
from django.contrib import admin


router = routers.DefaultRouter()
router.register(r'pupils', PupilView)
router.register(r'concepts', ConceptView)


urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
