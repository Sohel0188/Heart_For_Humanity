from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('all_capain', views.CampainViewSet)
router.register('category', views.CampainCategoryViewSet)
router.register('donetion', views.DonetionViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
    path('payment/', views.MakePayment),
]