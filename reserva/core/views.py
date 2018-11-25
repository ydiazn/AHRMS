from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'profile/profile.html'