from django.urls import path
from app1 import views

urlpatterns = [
    path("", views.index, name="index"),
    path("createAccount", views.create_account, name="createAccount"),
    path("login", views.login, name="login"),
    path("sharePlatformPost", views.share_platform_post, name="sharePlatformPost"),
    path("sharePlatformSearch", views.share_platform_search, name="sharePlatformSearch"),
]