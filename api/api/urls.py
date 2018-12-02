from django.urls import path, include
from django.conf.urls import url
from rest_framework import routers
from django.contrib import admin
from analytics.admin import teacher_admin
from analytics.viewsets import *



router = routers.DefaultRouter()
router.register(r'pupils', PupilView)
router.register(r'concepts', ConceptView)
router.register(r'primary_schools', PrimarySchoolView)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', teacher_admin.urls),
]
