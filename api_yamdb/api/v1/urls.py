from django.urls import include, path
from rest_framework import routers

from .views import (
    CategoryViewSet,
    GenreViewSet,
    TitleViewSet,
    ReviewViewSet,
    CommentViewSet,
)

router_v1 = routers.DefaultRouter()

router_v1.register(r'title', TitleViewSet, basename="title")
router_v1.register(r'genres', GenreViewSet, basename="genres")
router_v1.register(r'categories', CategoryViewSet, basename="categories")
router_v1.register(
    r'title\/(?P<title_id>\d+)/reviews',
    ReviewViewSet, basename='reviews'
)
router_v1.register(
    r'title\/(?P<title_id>\d+)/reviews\/(?P<review_id>\d+)/comments',
    CommentViewSet, basename='comments'
)


urlpatterns = [
    path('v1/', include(router_v1.urls))]
