from .views import PostViewSet, UserViewSet
from rest_framework import routers
from rest_framework.routers import DefaultRouter

router = routers.DefaultRouter()
router.register(" ", PostViewSet, basename='post-list')
router.register("users", UserViewSet, basename='users ')


urlpatterns = router.urls