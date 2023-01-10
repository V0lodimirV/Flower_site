from django.shortcuts import render
from .models import News, About
from django.views import View




class NewsView(View):
    def get(self, request):
        news = News.objects.all()
        return render(request, "home/index.html",
                      {"news_list": news}
                      )

class NewsDetail(View):
    def get(self, request, pk):
        news = News.objects.get(id=pk)
        return render(request, 'home/index_news_single.html',
                      {'news': news
                           }
                      )


class AboutUs(View):
    def get(self, request):
        about_us = About.objects.all()
        return render(request, 'home/about.html',
                      {'about': about_us}
                      )