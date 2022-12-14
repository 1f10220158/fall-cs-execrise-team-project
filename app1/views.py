from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse

def index(request):
    if request.COOKIES.get("userid", False):
        return render(request, "index.html", request.COOKIES)
    return render(request, "index.html")

def store_cookie(request):
    status = request.POST

    """
    データベースにユーザ情報登録処理
    """

    return render(request, "index.html", status)

def create_account(request):
    return render(request, "createAccount.html")

def login(request):
    return render(request, "login.html")