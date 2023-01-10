from django.shortcuts import render
from django.views import View
from .models import Flower


class FlowerView(View):
    def get(self, request):
        flower = Flower.objects.all()
        return render(request, "flower/flower.html",
                      {"flower_list": flower}
                      )



class FlowerDetail(View):
    """отдельная страница записи"""
    def get(self, request, pk):
        flower = Flower.objects.get(id=pk)
        return render(request, 'flower/flower_single.html',
                          {'flower': flower
                           }
                      )


