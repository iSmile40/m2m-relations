from django.shortcuts import render

from articles.models import Article, ScopesInArticle


def articles_list(request):
    template = 'articles/news.html'
    object_list = Article.objects.all()
    article_tags = ScopesInArticle.objects.all()
    context = {'object_list': object_list, 'scopes': article_tags}

    return render(request, template, context)
