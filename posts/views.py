from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from .forms import PostCreateForm
from posts import models as PostModel

@login_required
def postListView(request):
    posts = PostModel.Post.objects.filter(Q(viewers=request.user) | Q(author=request.user)).order_by('-posted_on')
    return render(request, 'posts/posts.html', {
        "posts": posts
    })


@login_required
def postCreateView(request):
    form = PostCreateForm(user=request.user)
    
    if request.method == "POST":
        print(request.POST)
        form = PostCreateForm(user=request.user, data=request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()

            post.viewers.set(form.cleaned_data['viewers'])
            
            return redirect(reverse("posts"))
    return render(request, 'posts/new_post.html', {
        "form": form
    })