from django.shortcuts import render

from Board.forms import Form
from Board.models import *

# Get data from database(Article)
def getAllArticles():
    try:
        articles = Article.objects.all()
    except Article.DoesNotExist:
        articles = None
    return articles


def getArticle(num):
    try:
        article = Article.objects.get(id=num)
    except Article.DoesNotExist:
        article = None
    return article


# Create write, list, view, update, delete
def write(request):
    if request.method == 'POST':
        form = Form(request.POST)  # request POST 내용을 form 에 넣음
        if form.is_valid():  # form의 데이터가 유효하면 저장
            form.save()
    else:
        form = Form()

    return render(request, 'write.html', {'form': form})  # write.html 에 form 을 전달


def list(request):
    articles = getAllArticles()
    return render(request, 'list.html', {'articles': articles})


def view(request, num):
    article = getArticle(num)
    return render(request, 'view.html', {'article': article})


def update(request, num):
    article = getArticle(num)
    if request.method == "POST":
        form = Form(request.POST, instance=article)
        if form.is_valid():
            form.save()
            print("saved")
            # return HttpResponseRedirect("/#editado")
    else:
        if article:
            form = Form(instance=article)
        else:
            print("Error")
            # return HttpResponseRedirect("/#no-existe-ese-articulo")

    return render(request, "update.html", {'form':form})


def delete(request, num):
    pass