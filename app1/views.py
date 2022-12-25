from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from app1.models import *

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
        if "userid" in request.COOKIES:
            cookie_user_id = request.COOKIES["userid"]
            user_id = User.objects.get(user_id=cookie_user_id)

            #ログインしている状態で匿名でログインIDで投稿する場合
            if request.POST["userID"] == "loginUserID":
                login_or_anonymous = 1

            #ログインしている状態で匿名IDで投稿する場合
            else:
                login_or_anonymous = 0

            article = Article(
                    user_id = user_id,
                    article_data = request.FILES["articleData"],
                    title = request.POST["title"],
                    content = request.POST["content"],
                    login_or_anonymous = login_or_anonymous,
                    answer = request.POST["answer"],
                )         
        
        #匿名で投稿する場合
        else:
            login_or_anonymous = 0

            article = Article(
                    article_data = request.FILES["articleData"],
                    title = request.POST["title"],
                    content = request.POST["content"],
                    login_or_anonymous = login_or_anonymous,
                    answer = request.POST["answer"],
                )
        article.save()
        return HttpResponse("get uploaded")
            
def share_platform_search(request):
    if "userid" in request.COOKIES:
        context = {
            "answered": UserAnsweredArticle.objects.filter(answer_user_id=request.COOKIES["userid"]),
            "articles": Article.objects.all(),
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

def articles_search(request): 
    search_text = request.GET.get("search")

    try:
        articles = Article.objects.filter(title__contains=search_text)
    except ValueError:
        articles = None

    if "userid" in request.COOKIES:
        context = {
            "articles": articles,
            "userid" : request.COOKIES["userid"],
            "password" : request.COOKIES["password"],
        }

        return render(request, "sharePlatformSearch.html", context)
    context = {
            "articles": articles,
        }

    return render(request, "sharePlatformSearch.html", context)

def get_answer(request):
    posted_article_id = request.POST["articleId"]
    correct_answer = list(Article.objects.filter(article_id=posted_article_id).values())[0]['answer']
    answer = request.POST["answer"]

    if correct_answer == answer:
        result = "正解です"
        if "userid" in request.COOKIES:
            cookie_user_id = request.COOKIES["userid"]

            #主キーを参照
            user_id = User.objects.get(user_id=cookie_user_id)
            article_id = Article.objects.get(article_id=posted_article_id)
            
            #ユーザの回答履歴を保存
            check_data = UserAnsweredArticle.objects.filter(
                answer_user_id = user_id,
                article_id = article_id,
            )
            if not check_data:
                user_answer_data = UserAnsweredArticle(
                    answer_user_id = user_id,
                    article_id = article_id,
                )
                user_answer_data.save()
    else:
        result = "不正解です"
    return HttpResponse(result)