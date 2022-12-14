from django.urls import path
from app1 import views

urlpatterns = [
    path("", views.index, name="index"),
    path("createAccount", views.create_account, name="createAccount"),
    path("storeCookie", views.store_cookie, name="storeCookie"),
    path("login", views.login, name="login"),
]