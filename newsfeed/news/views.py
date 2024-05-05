from django.shortcuts import render
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
    context = {
        "news" : news
    }
    return render(request, "news/news_details.html", context)
    