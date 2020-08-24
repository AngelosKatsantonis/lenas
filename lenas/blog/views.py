from django.shortcuts import render,get_object_or_404

from .models import Article
from .articlefilter import ArticleFilter

def get_articles(request):
    form = ArticleFilter(request.GET or None)
    # Filter articles based on form (Year,Month,Tag) submitted by user
    if form.is_valid():
        articles = form.get_articles()
    # Otherwise get all articles
    else:
        articles = Article.objects.all()
    context = {
            'articles': articles,
            'form': form
    }
    return render(request, 'blog/archive.html', context)

def get_article(request, id):
    article = get_object_or_404(Article, id=id)
    form = ArticleFilter(None)
    tags = list(article.tags.all())
    # Fetches some articles related to 
    # the tags of the article we display
    articles = form.get_articles(tags=tags)[:4] 
    context = {
            'article': article,
            'articles': articles 
    }
    return render(request, 'blog/article.html', context)
