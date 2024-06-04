from django.shortcuts import render, redirect, get_object_or_404
from .models import Article, Comment
from .forms import ArticleForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse


# Create your views here.
@login_required(login_url="user:login")
def articles_list(request):
    keyword = request.GET.get('keyword')

    if keyword:
        articles = Article.objects.filter(title__contains=keyword)
    else:
        articles = Article.objects.all()
    return render(request, 'articles_list.html', { 'articles': articles })


@login_required(login_url="user:login")  
def my_articles(request):
    articles = Article.objects.filter(author = request.user)
    return render(request, 'dashboard.html', {'articles': articles})  


@login_required(login_url="user:login") 
def article_detail(request, id):
    article = get_object_or_404(Article, id=id)
    comments = article.comments.all

    context = {
        'article': article,
        'comments': comments,
    }
    return render(request, 'article-detail.html', context)


@login_required(login_url="user:login")  
def article_create(request):
    form = ArticleForm(request.POST or None, request.FILES or None)
    context = {'form': form}

    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()

        messages.success(request, 'Article created successfully')
        return redirect('article:dashboard')
    
    return render(request, 'article-create.html', context)


@login_required(login_url='user:login')
def article_update(request, id):
    article = get_object_or_404(Article, id=id)
    form = ArticleForm(request.POST or None, request.FILES or None, instance=article)
    context = {"form": form}

    if form.is_valid():
        article.save()
        messages.success(request, 'Article updated successfully')
        return redirect('article:dashboard')

    return render(request, "article-update.html", context)


@login_required(login_url='user:login')
def article_delete(request, id):
    article = get_object_or_404(Article, id=id)
    article.delete()
    messages.success(request, 'Article deleted successfully')
    return redirect('article:dashboard')


@login_required(login_url='user:login')
def comment_create(request, id):
    article = get_object_or_404(Article, id=id)

    if request.method == "POST":
        comment_author = request.POST.get('comment_author')
        comment_content = request.POST.get('comment_content')

        comment = Comment(author = comment_author, content = comment_content)
        comment.article = article
        comment.save()
        messages.success(request, "Comment added successfully")

    return redirect(reverse("article:detail", kwargs={"id":id}))