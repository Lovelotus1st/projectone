from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect

from . import forms
# Create your views here.

def index(request):
    return HttpResponse('hello there from app2')

def template(request):
    d_var = {'any_var':"I'm value of any_variables"}
    return render(request,'apptwo/index.html',context = d_var)

def form_view(request):
    form = forms.FormName()
    if request.method =="POST":
        form = forms.FormName(request.POST)
        if form.is_valid():
            a = form.cleaned_data["password"]
            b = form.cleaned_data["v_password"]
            if a == b:
                post = form.save(commit=False)
                post.save()
            else:
                form = forms.FormName()
                return HttpResponse("Password not matched, try again")
            return redirect('/admin/apptwo/login/', pk=post.pk)
    else:
        form = forms.FormName()

    return render(request,'apptwo/form.html',{'form2':form})