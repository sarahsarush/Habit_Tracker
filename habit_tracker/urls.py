from django.contrib import admin
from django.urls import path
from habits import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('habits/', views.habit_list, name='habit_list'),
    path('habits/create/', views.habit_create, name='habit_create'),
    path('habits/<pk>/', views.habit_detail, name='habit_detail'),
    path('habits/<pk>/edit/', views.habit_edit, name='habit_edit'),
    path('habits/<pk>/delete/', views.habit_delete, name='habit_delete'),
    path('habits/<pk>/daily_progress/create/', views.daily_progress_create, name='daily_progress_create'),
]