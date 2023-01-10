from django.shortcuts import render
from django.views import View
from . import models
from .models import Blog
from django.core.paginator import Paginator




class BlogView(View):
    '''вывод записей и пагинация'''
    def get(self, request):
        blog = models.Blog.objects.all()
        p = Paginator(Blog.objects.all(), 3)
        page = request.GET.get('page')
        blogs = p.get_page(page)
        nums = "a" * blogs.paginator.num_pages
        return render(request, "blog/blog.html",
                      {"blog_list": blog,
                       "blogs": blogs,
                       "nums": nums}
                      )