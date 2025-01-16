from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('info', views.ContactViewSet)
router.register('form', views.ContactFormViewSet)

urlpatterns = [
    path('', include(router.urls)),
]