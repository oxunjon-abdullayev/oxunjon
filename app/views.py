from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from app.form import ContactModelForm
from app.models import Blog, Skills


def index_view(request):
    skills = Skills.objects.all()
    blogs = Blog.objects.all()
    return render(request=request,
                  template_name="app/index.html",
                  context={'blogs': blogs,
                           "skills":skills})


def contact_view(request):
    if request.method == "POST":
        form = ContactModelForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")

    form = ContactModelForm()
    return render(request=request,
                  template_name="app/index.html",
                  context={"form": form})



