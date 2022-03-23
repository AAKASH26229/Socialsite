import uuid
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import login
from django.contrib import messages

from .forms import CustomUserCreationForm
# Create your views here.
def signUpView(request):
    form = CustomUserCreationForm()
    
    if request.method == "POST":
        
        form = CustomUserCreationForm(request.POST)
        
        if form.is_valid():
            user = form.save(commit=False)
            
            username = "{}{}{}".format(user.first_name, user.last_name, uuid.uuid4())
            user.username = username

            user.save()
            
            login(request,user)
            messages.success(request, 'User registered and logged in successfully')
            return redirect("/")
        else:
            # Do something in case if form is not valid
            raise Http404     
       

    return render(request, 'registration/signup.html', {
        "form": form
    })