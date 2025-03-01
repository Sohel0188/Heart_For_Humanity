from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('all_blog', views.BlogViewSet)
router.register('blog_category', views.BlogCategoryViewSet)
router.register('blog_comments', views.BlogCommentViewSet)



# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]