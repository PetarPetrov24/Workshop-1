from django.shortcuts import render
from django.views.generic import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from profiles.forms import ProfileUpdateForm
from profiles.models import Profile
from django.urls import reverse_lazy


# Create your views here.
class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = ProfileUpdateForm
    template_name = 'users/update_profile.html'
    success_url = reverse_lazy('home')

    def get_object(self, queryset=None):
        return self.request.user.profile