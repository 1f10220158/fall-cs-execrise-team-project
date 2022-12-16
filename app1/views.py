from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
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

    '''
    データベースに保存する処理をここに書く

    userdata = モデル名(idのカラム名=userid, passのカラム名=password)
    userdata.save()

    '''
    
    return redirect(index)

def create_account(request):
    return render(request, "createAccount.html")

def login(request):
    return render(request, "login.html")

def share_platform_post(request):
    return render(request, "sharePlatformPost.html")

def share_platform_search(request):
    return render(request, "sharePlatformSearch.html")