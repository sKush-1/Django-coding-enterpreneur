from django.shortcuts import render
from .models import Article
from django.contrib.auth.decorators import login_required
from .forms import ArticleForm

# Create your views here.

def article_detail_view(request, id=None):
    article_obj = None
    if id is not None:
        article_obj = Article.objects.get(id=id)
    context = {
        "object": article_obj,
    }
    return render(request, "articles/detail.html", context=context)

@login_required
def article_create_view(request, id=None):
    form = ArticleForm()
    context = {
        "form": form
    }
    if(request.method == 'POST'):
        form = ArticleForm(request.POST)
        context['form'] = form
        if form.is_valid():
            article_obj = form.save()
            context['form'] = ArticleForm(request.POST or None)
            print(article_obj)
            title = form.cleaned_data.get('title')
            context['form'] = form
            content = form.cleaned_data.get('content')
            article_object = Article.objects.create(title=title, content=content)
            context['object'] = article_object
            context['created'] = True
    
    return render(request,"articles/create.html",context=context)


  

def article_search_view(request):
    try:
        query = int(query_dict.get("query"))
    except: 
        query = None
    query_dict = request.GET
    query = query_dict.get("query")
    if query is not None:
        article_obj = Article.objects.get(id=query)
    context = {
        "object":article_obj
    }
    
    return render(request,"articles/search.html", context=context)

