from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm, CustomAuthenticationForm, UserProfileForm
from .models import CustomUser
from django.shortcuts import redirect
from django.contrib.auth import logout as auth_logout
from manager_task.models import Task
from rest_framework.authtoken.models import Token


class RegisterView(CreateView):
    model = CustomUser
    form_class = CustomUserCreationForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        super().form_valid(form)

        email = form.cleaned_data['email']
        password = form.cleaned_data['password1']
        try:
            user = CustomUser.objects.get(email=email)
            login(self.request, user)
            token, created = Token.objects.get_or_create(user=user)
            if created:
                pass
            else:
                pass
        except CustomUser.DoesNotExist:
            pass

        return super().form_valid(form)


class CustomLoginView(LoginView):
    model = CustomUser
    authentication_form = CustomAuthenticationForm
    template_name = 'accounts/login.html'


class ProfileView(UpdateView):
    model = CustomUser
    form_class = UserProfileForm
    template_name = 'accounts/profile.html'
    success_url = reverse_lazy('profile')

    def get_object(self):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = Task.objects.filter(user=self.request.user)
        return context


class EditProfileView(UpdateView):
    model = CustomUser
    form_class = UserProfileForm
    template_name = 'accounts/edit_profile.html'
    success_url = reverse_lazy('profile')

    def get_object(self):
        return self.request.user


def home(request):
    return render(request, 'accounts/home.html')


def logout(request):
    auth_logout(request)
    return redirect('home')