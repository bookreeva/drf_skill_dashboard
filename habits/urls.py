"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
"""
from django.urls import path

from habits.apps import HabitsConfig
from habits.views import (HabitCreateAPIView, HabitListAPIView,
                          HabitRetrieveAPIView, HabitUpdateAPIView,
                          HabitDestroyApiView, HabitUserListAPIView)

app_name = HabitsConfig.name

urlpatterns = [
    path('habit-create/', HabitCreateAPIView.as_view(), name='habit-create'),
    path('habits/', HabitListAPIView.as_view(), name='habit-list'),
    path('my-habits/', HabitUserListAPIView.as_view(), name='my-habits'),
    path('habits/<int:pk>/', HabitRetrieveAPIView.as_view(), name='habits'),
    path('habits/<int:pk>/update/', HabitUpdateAPIView.as_view(), name='habit-update'),
    path('habits/<int:pk>/delete/', HabitDestroyApiView.as_view(), name='habit-delete'),

]
