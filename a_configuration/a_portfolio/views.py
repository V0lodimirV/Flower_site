from django.shortcuts import render
from django.views import View
from .models import Portfolio


class PortfolioView(View):
    def get(self, request):
        portfolio = Portfolio.objects.all()
        return render(request, "portfolio/portfolio.html",
                      {"portfolio_list": portfolio}
                      )



class PortfolioDetail(View):
    """отдельная страница записи"""
    def get(self, request, pk):
        portfolio = Portfolio.objects.get(id=pk)
        return render(request, 'portfolio/portfolio_single.html',
                          {'portfolio': portfolio
                           }
                      )