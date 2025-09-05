from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.generic import UpdateView
from accounts.models import Profile
from accounts.forms import ProfileForm

def registerView(request):
    if request.method == "POST":
        userForm = UserCreationForm(request.POST)
        if userForm.is_valid():
            userForm.save()
            return redirect("login")
    else:
        userForm = UserCreationForm()
    return render(
        request,
        'register.html',
        {'userForm': userForm}
    )

def loginView(request):
    if request.method == "POST":
        loginForm = AuthenticationForm(request, data=request.POST)
        if loginForm.is_valid():
            user = loginForm.get_user()
            login(request, user)
            return redirect("cars_list")
    else:
        loginForm = AuthenticationForm()
    return render(
        request,
        'login.html',
        {'loginForm': loginForm}
    )

def logoutView(request):
    logout(request)
    return redirect("cars_list")

class ProfileUpdateView(UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'profileUpdate.html'
    success_url = '/cars/'

    def get_object(self, queryset=None):
        return Profile.objects.get(user=self.request.user)
    