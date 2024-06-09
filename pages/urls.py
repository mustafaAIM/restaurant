from django.urls import path
from .views import HomePageView, AboutPageView,PostViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("posts",PostViewSet)
urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("about/", AboutPageView.as_view(), name="about"),
]
urlpatterns = router.urls