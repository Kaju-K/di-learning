from typing import Any, Dict
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.views import generic
from django.urls import reverse_lazy

from django.contrib.auth.models import User

from .forms import (
    UserProfileForm
)

from .models import (
    UserProfile
)

# Create your views here.
class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("homepage")
    template_name = "signup.html"

def profile_redirect_view(request):
    user = request.user
    if hasattr(user, "profile"):
        return redirect("homepage")
    else:
        return redirect("create_profile")
    
def update_profile(request):
    user = request.user
    profile = user.profile

    if request.method == "POST":
        filled_form = UserProfileForm(request.POST)

    form = UserProfile(instance=profile)
    context = {"form": form}
    return render(request, "profile_update.html", context)

def create_profile(request):
    user = request.user
    if request.method == "POST":
        
        form = UserProfileForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = user
            profile.save()
            return redirect("profile", profile_id=profile.id)
    form = UserProfileForm()
    context = {"form": form}
    return render(request, "create_profile.html", context)

def profile(request, profile_id):
    profile = UserProfile.objects.get(id = profile_id)
    print(profile)
    context = {"user_profile": profile}
    return render(request, "profile.html", context)