from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'posts', views.PostViewSet, basename='post')

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('api/v1/', include(router.urls)),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]
