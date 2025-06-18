from django.urls import path
from profiles.views import ProfileUpdateView
from users import views

urlpatterns = [
    path('', views.home, name='home'),
    path('post/', views.create_post, name='create-post'),
    path('profile/', ProfileUpdateView.as_view(), name='profile'),
    path('trip/', views.trip_journal, name='trip-journal'),
    path('register/', views.AppUserRegisterView.as_view(), name='register'),
    path('login/', views.AppUserLoginView.as_view(), name='login'),
    path('logout/', views.AppUserLogoutView.as_view(), name='logout'),
    path('profile/update/', ProfileUpdateView.as_view(), name='update-profile'),
]