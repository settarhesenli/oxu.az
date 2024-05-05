from django.urls import path
from .views import home_page_view, news_detail_view

urlpatterns = [
    path("", home_page_view),
    path("news/<int:pk>/", news_detail_view)
]
