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
    if request.method == "GET":
        if "userid" in request.COOKIES:
            return render(request, "createAccount.html", request.COOKIES)
    
        return render(request, "createAccount.html")
    else:
            userid = request.POST["userid"]
            password = request.POST["password"]

            #ユーザidとパスワードをデータベースに保存
            user_data = User(user_id=userid, password=password)
            user_data.save()
            return redirect(index)

def login(request):
    
    if "userid" in request.COOKIES:
        return render(request, "login.html", request.COOKIES)
    
    return render(request, "login.html")

def share_platform_post(request):
    if request.method == "GET":

        if "userid" in request.COOKIES:
            return render(request, "sharePlatformPost.html", request.COOKIES)

        return render(request, "sharePlatformPost.html", request.COOKIES)
    
    else:
        if request.POST["userID"] == "loginUserID":
            article = Article(
                article_id = str(uuid.uuid4()),
                user_id = request.COOKIES["userid"],
                article_data = request.FILES["articleData"],
                title = request.POST["title"],
                content = request.POST["content"]
            )
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
    context = {
        "articles": Article.objects.all()
    }
    
    if "userid" in request.COOKIES:
        return render(request, "sharePlatformSearch.html", {request.COOKIES, context})
    
    return render(request, "sharePlatformSearch.html", context)