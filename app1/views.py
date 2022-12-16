from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from app1.models import Article
#from app1.models import #モデル名

def index(request):

    #cookieにユーザデータがあったらindex.htmlの"ログイン"のところをユーザIDに変える
    if "userid" in request.COOKIES:
        return render(request, "index.html", request.COOKIES)
    
    #ない場合は"ログイン"のまま返す
    return render(request, "index.html")

def store_new_account(request):
    userid = request.POST["userid"]
    password = request.POST["password"]

    #ユーザidとパスワードをデータベースに保存
    user_data = User(user_id=userid, password=password)
    user_data.save()
    
    return redirect(index)

def create_account(request):
    
    if "userid" in request.COOKIES:
        return render(request, "createAccount.html", request.COOKIES)
    
    return render(request, "createAccount.html")

def login(request):
    
    if "userid" in request.COOKIES:
        return render(request, "login.html", request.COOKIES)
    
    return render(request, "login.html")

def share_platform_post(request):
    
    if "userid" in request.COOKIES:
        return render(request, "sharePlatformPost.html", request.COOKIES)
    
    return render(request, "sharePlatformPost.html")

def share_platform_search(request):
    context = {
        'articles' : Article.objects.all()
        }
    
    if "userid" in request.COOKIES:
        return render(request, "sharePlatformSearch.html", {request.COOKIES, context})
    
    #ない場合は"ログイン"のまま返す
    return render(request, "sharePlatformSearch.html", context)
