from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect

from . import forms

# Create your views here.


def index(request):
    return HttpResponse('hello there')

def template(request):
    d_var = {'any_var':"I'm value of any_variables"}
    return render(request,'appone/index.html',context = d_var)

def detail(request, question_id):
    return HttpResponse('You are looking at question %s.' % question_id)

def result(request, question_id):
    response = "you are looking at the result of question %s"
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

def form_view(request):
    form = forms.FormName()
    if request.method =="POST":
        form = forms.FormName(request.POST)
        if form.is_valid():
            post = form.save(commit = False)
            post.save()
            return redirect('/admin/appone/signup/', pk=post.pk)
    else:
        form = forms.FormName()

    return render(request,'appone/form.html',{'form1':form})

