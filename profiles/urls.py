from django.urls import path

from profiles import views

urlpatterns = [
    path('profile/', views.ProfileUpdateView.as_view(), name='profile_update'),
]