"""Coderspace URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))

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
from cgitb import handler
from django.contrib import admin
from django.urls import path, include

urlpatterns = [

    path('',include('problemstack.urls')),
    path('admin/', admin.site.urls),
]

handler404 = "Coderspace.views.page_not_found"