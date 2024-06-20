from django.shortcuts import render
from django import views
from django.http import Http404
# Create your views here.



# class MainPageView(views.View):
#     template_name = "main/portfolio.html"

def MainPageView(request):
    return render(request, "main/portfolio.html")


