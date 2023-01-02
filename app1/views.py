from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from app1.models import *
import re

def index(request):
    if request.method == "POST":
        answer = request.POST.get("xxInputBox").lower().strip()
        
        if answer == "cryphographies":
            if "userid" in request.COOKIES:
                user_id = request.COOKIES["userid"]
                if not TimeforOfficial.objects.filter(user_id=user_id):
                    correct_data = TimeforOfficial(
                        user_id = User.objects.get(user_id=user_id)
                    )
                    correct_data.save()
            return HttpResponse("true")
        else:
            return HttpResponse("false")

    else:
        #cookieにユーザデータがあったらindex.htmlの"ログイン"のところをユーザIDに変える
        if "userid" in request.COOKIES:
            context = {
                "times": TimeforOfficial.objects.all()[:10],
                "userid": request.COOKIES["userid"],
                "password": request.COOKIES["password"]
            }
            return render(request, "index.html", context)
        context = {
            "times": TimeforOfficial.objects.all()[:10]
        }
    
        #ない場合は"ログイン"のまま返す
        return render(request, "index.html", context)
    if ('sort' in request.GET):
        #いいね順と新着順と難しい順と解きやすい順の並び替え
        if request.GET['sort']=='interesting':
            articles=Article.objects.order_by('-interesting')
        elif request.GET['sort']=='difficult':
            articles=Article.objects.order_by('-difficult')
        elif request.GET['sort']=='easy':
            articles=Article.objects.order_by('-easy')
    else:
        articles=Article.objects.order_by('-posted_at')

def create_account(request):

    #GETの場合
    if request.method == "GET":
        if "userid" in request.COOKIES:
            return render(request, "createAccount.html", request.COOKIES)
    
        return render(request, "createAccount.html")
    
    #POSTの場合
    else:
        user_id = request.POST["userid"].strip()
        password = request.POST["password"].strip()
        dict = {}
        user_id_lst = User.objects.values_list('user_id', flat=True)
        if user_id in user_id_lst:
            dict["existed"] = 1

        if not (user_id and password):
            dict["none_user_id_or_password"] = 1

        if len(password) < 5:
            dict["less_password"] = 1

        if re.search(r"\s", password) or re.search(r"\s", user_id):
            dict["blank_exist"] = 1

        if not re.search(r"\w", password):
            dict["none_number_or_word_in_password"] = 1

        if re.search(r"\W", password):
            dict["inappropriate_letter_exist"] = 1

        if len(dict) == 0:
            user_data = User(
                user_id = request.POST["userid"],
                password = request.POST["password"]
            )
            user_data.save()
            return JsonResponse({"result": 1})
        dict["result"] = 0
        return JsonResponse(dict)

def login(request):
    if request.method == "POST":
        user_id = request.POST.get("userid")
        password = request.POST.get("password")

        if User.objects.filter(user_id=user_id, password=password):
            return HttpResponse("True")
        
        return HttpResponse("False")

    else:
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
            article = Article(
                    article_data = request.FILES["articleData"],
                    title = request.POST["title"],
                    content = request.POST["content"],
                    login_or_anonymous = 0,
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
    correct_answer = list(Article.objects.filter(article_id=posted_article_id).values())[0]['answer'].lower().strip()
    answer = request.POST["answer"].lower().strip()

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
#面白いの関数
def interesting(request,article_id):
    try:
        article=Article.objects.get(pk=article_id)
        article.interesting+=1
        article.save()
    except Article.DoesNotExist:
        raise Http404("Article does not exist")
    return redirect(detail,article_id)
#難しいの関数
def difficult(request,article_id):
    try:
        article=Article.objects.get(pk=article_id)
        article.difficult+=1
        article.save()
    except Article.DoesNotExist:
        raise Http404("Article does not exist")
    return redirect(detail,article_id)
#解きやすいの関数
def easy(request,article_id):
    try:
        article=Article.objects.get(pk=article_id)
        article.easy+=1
        article.save()
    except Article.DoesNotExist:
        raise Http404("Article does not exist")
    return redirect(detail,article_id)