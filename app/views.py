from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from app.forms import *

def topic_model(request):
    form=TopicForm()
    if request.method=='POST':
        form_data=TopicForm(request.POST)
        if form_data.is_valid():
            form_data.save()
            return HttpResponse('Record inserted Sucessfully')
    return render(request,'first.html',context={'form':form})

def webpage_model(request):
    form=WebpageForm()
    if request.method=='POST':
        form_data=WebpageForm(request.POST)
        if form_data.is_valid():
            form_data.save()
            return HttpResponse('Record inserted Sucessfully')
    return render(request,'second.html',context={'form':form})

def access_model(request):
    form=AccessForm()
    if request.method=='POST':
        form_data=AccessForm(request.POST)
        if form_data.is_valid():
            form_data.save()
            return HttpResponse('Record inserted Sucessfully')
    return render(request,'third.html',context={'form':form})
