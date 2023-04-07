from django.shortcuts import render

def index(request):
    context = {}
    return render(request, 'erp/index.html', context)