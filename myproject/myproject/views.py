"""
To render web pages
"""
from django.http import HttpResponse
from articles.models import Article
from django.template.loader import render_to_string




HTML_STRING = render_to_string("home-view.html",)
def Home_View(request, *args, **kwargs):
    print(args,kwargs)
    return HttpResponse(HTML_STRING)
    