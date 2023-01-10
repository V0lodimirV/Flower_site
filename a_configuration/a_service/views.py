from django.shortcuts import render
from django.views import View



class ServicesView(View):
    def get(self, reuest):
        return render(reuest, "service/service.html")
