from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from blog.forms import *


# Create your views here.


def addCategory(request):

    if(request.method == 'POST'):
        form = CategoryForm(request.POST)
        if(form.is_valid()):
            form.save(commit=True)
            HttpResponseRedirect('blog/add_category')
    else :
        form = CategoryForm()
        return render(request, 'add_category.html',{'title':'add_category','form':form})
