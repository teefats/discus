from django.shortcuts import render, redirect
from .models import Forum, Discussion
from .forms import *
# Create your views here.

def main_view(request):
    forums =Forum.objects.all()
    count = forums.count()
    discussions =[]
    for i in forums:
        discussions.append(i.discussion_set.all())

    context = {'forums':forums, 'count':count, 'discussions':discussions}
    return render(request, 'talk/main_view.html', context)


def addInForum(request):
    form = CreateInForum()
    if request.method == 'POST':
        form = CreateInForum(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context ={'form':form}
    return render(request,'talk/addInForum.html',context)

def addInDiscussion(request):
    form = CreateInDiscussion()
    if request.method == 'POST':
        form = CreateInDiscussion(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context ={'form':form}
    return render(request,'talk/addInDiscussion.html',context)
 