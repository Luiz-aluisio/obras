from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'autores', views.AutorViewSet)
router.register(r'obras', views.ObraViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
