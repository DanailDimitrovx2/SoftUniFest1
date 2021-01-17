from django.urls import path
from .views import register, home, user_profile

urlpatterns = [
    path('register/', register, name='register'),
    path('home/', home, name='home'),
    path('home/users/<int:user_id>', user_profile, name='home'),

]