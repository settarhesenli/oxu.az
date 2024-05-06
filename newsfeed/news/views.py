from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseForbidden
from .models import News


# Create your views here.

def home_page_view(request):
    news = News.objects.order_by("-id")
    context = {
        "news" : news
    }
    return render(request, "news/index.html", context)


def news_detail_view(request, pk):
    news = News.objects.get(id=pk)
    news.view_counter += 1
    news.save()
    context = {
        "news" : news
    }
    return render(request, "news/news_details.html", context)
    
    
    