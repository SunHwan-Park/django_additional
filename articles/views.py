from django.shortcuts import render

# Create your views here.

def article_list(request):
    
    context = {

    }
    return render(request, 'articles/article_list.html', context)