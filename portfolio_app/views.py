from django.shortcuts import render

def my_cv(request):
    return render(request,"portfolio_app/portfolio.html")
