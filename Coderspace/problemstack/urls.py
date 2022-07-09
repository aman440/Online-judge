"""
All Paths for routing :- 
    1. domain/ ->Homepage [public]
    2. domain/problem/problem_id -> Problem Page [public]
    3. domain/login -> Login Page [public]
    4. domain/register -> Registration Page [public]
    5. domain/leaderboard -> Leaderboard [public]
    6. domain/problem/problem_id/submit -> CodingBling for that problem [private]
    7. domain/about -> About the developers of this site [public]
    8. domain/any_other_route_not_mentioned_above -> Page Not found with an angry gorilla image

"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('login', views.login),
    path('register', views.register),
    path('leaderboard/', views.leaderboard),
    path('about/', views.about),
]