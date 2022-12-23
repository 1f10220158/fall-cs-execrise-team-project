from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from app1.models import *
import uuid

def index(request):

    #cookieにユーザデータがあったらindex.htmlの"ログイン"のところをユーザIDに変える
    if "userid" in request.COOKIES:
        return render(request, "index.html", request.COOKIES)
    
    #ない場合は"ログイン"のまま返す
    return render(request, "index.html")

def create_account(request):

    #GETの場合
    if request.method == "GET":
        if "userid" in request.COOKIES:
            return render(request, "createAccount.html", request.COOKIES)
    
        return render(request, "createAccount.html")
    
    #POSTの場合
    else:
        userid = request.POST["userid"]
        password = request.POST["password"]

        #ユーザidとパスワードをデータベースに保存
        user_data = User(user_id=userid, password=password)
        user_data.save()
        return render(request, "createAccountEnd.html", request.COOKIES)

def login(request):
    
    if "userid" in request.COOKIES:
        return render(request, "login.html", request.COOKIES)
    
    return render(request, "login.html")

def share_platform_post(request):
    #GETの場合
    if request.method == "GET":

        if "userid" in request.COOKIES:
            return render(request, "sharePlatformPost.html", request.COOKIES)

        return render(request, "sharePlatformPost.html", request.COOKIES)
    
    #POSTの場合
    else:

        #ログインしているuseridで投稿する場合
        if request.POST["userID"] == "loginUserID":
            article = Article(
                article_id = str(uuid.uuid4()),
                user_id = request.COOKIES["userid"],
                article_data = request.FILES["articleData"],
                title = request.POST["title"],
                content = request.POST["content"]
            )
        
        #匿名で投稿する場合
        else:
            article = Article(
                article_id = str(uuid.uuid4()),
                article_data = request.FILES["articleData"],
                title = request.POST["title"],
                content = request.POST["content"]
            )
        article.save()
        return HttpResponse("uploaded")
            
def share_platform_search(request):
    if "userid" in request.COOKIES:
        context = {
            "articles": list(Article.objects.all().values()),
            "userid" : request.COOKIES["userid"],
            "password" : request.COOKIES["password"],
        }

        return render(request, "sharePlatformSearch.html", context)
    context = {
            "articles": Article.objects.all(),
        }

    return render(request, "sharePlatformSearch.html", context)

def share_platform_post_end(request):
        if "userid" in request.COOKIES:
            return render(request, "sharePlatformPostEnd.html", request.COOKIES)

        return render(request, "sharePlatformPostEnd.html", request.COOKIES)
    
def create_account_end(request):
        if "userid" in request.COOKIES:
            return render(request, "createAccountEnd.html", request.COOKIES)

        return render(request, "createAccountEnd.html", request.COOKIES)

def Article_search(request):
    #記事検索用関数
    #try,exceptは空欄で検索するときのエラー回避のため
    try:
        #URLのパラメータから検索ワードを取得
        searchword = request.GET["searchbox"]

        if "userid" in request.COOKIES:
            #context内の記事をfilterで絞る
            context = {
                "articles": list(Article.objects.filter(title__contains=searchword).values()),
                "userid" : request.COOKIES["userid"],
                "password" : request.COOKIES["password"],
            }

            return render(request, "sharePlatformSearch.html", context)

        context = {
            "articles": list(Article.objects.filter(title__contains=searchword).values()),
        }
        return render(request, "sharePlatformSearch.html", context)

    except:
        if "userid" in request.COOKIES:
            context = {
                "articles": list(Article.objects.all().values()),
                "userid" : request.COOKIES["userid"],
                "password" : request.COOKIES["password"],
            }

            return render(request, "sharePlatformSearch.html", context)

        context = {
            "articles": list(Article.objects.all().values()),
        }
        return render(request, "sharePlatformSearch.html", context)