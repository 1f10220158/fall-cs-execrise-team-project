from django.urls import path
from app1 import views

urlpatterns = [
    path("", views.index, name="index"),
    path("createAccount", views.create_account, name="createAccount"),
    path("login", views.login, name="login"),
    path("sharePlatformPost", views.share_platform_post, name="sharePlatformPost"),
    path("sharePlatformSearch", views.share_platform_search, name="sharePlatformSearch"),
    path("createAccountEnd", views.create_account_end, name="createAccountEnd"),
    path("sharePlatformPostEnd", views.share_platform_post_end, name="sharePlatformPostEnd"),
    path("articlesSearch", views.articles_search, name="articlesSearch"),
    path("getAnswer", views.get_answer, name="getAnswer"),
    path('api/articles/<int:article_id>/interesting',views.api_interesting),#面白いのURL
    path('api/articles/<int:article_id>/difficult',views.api_difficult),#難しいのURL
    path('api/articles/<int:article_id>/easy',views.api_easy),#解きやすいのURL
]