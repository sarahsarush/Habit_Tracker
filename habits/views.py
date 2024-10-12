from django.shortcuts import render, redirect
from . models import Habit, DailyProgress
from . forms import HabitForm, DailyProgressForm

def habit_list(request):
    habits = Habit.objects.all()
    return render(request, 'habits/templates/habit_list.html', {'habits': habits})

def habit_detail(request, pk):
    habit = Habit.objects.get(pk=pk)
    
    daily_progress = habit.dailyprogress_set.all()
    
    dates = [dp.date for dp in daily_progress]
    progress = [dp.progress for dp in daily_progress]

    return render(request, 'habits/templates/habit_detail.html', {'habit': habit})

def habit_create(request):
    if request.method == 'POST':
        form = HabitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('habit_list')
    else:
        form = HabitForm()
    return render(request, 'habits/templates/habit_form.html', {'form': form})

def habit_edit(request, pk):
    habit = Habit.objects.get(pk=pk)
    if request.method == 'POST':
        form = HabitForm(request.POST, instance=habit)
        if form.is_valid():
            form.save()
            return redirect('habit_list')
    else:
        form = HabitForm(instance=habit)
    return render(request, 'habits/templates/habit_form.html', {'form': form})

def habit_delete(request, pk):
    habit = Habit.objects.get(pk=pk)
    habit.delete()
    return redirect('habit_list')

def daily_progress_create(request, pk):
    habit = Habit.objects.get(pk=pk)
    if request.method == 'POST':
        form = DailyProgressForm(request.POST)
        if form.is_valid():
            daily_progress = form.save(commit=False)
            daily_progress.habit = habit
            daily_progress.save()
            return redirect('habit_detail', pk=pk)
    else:
        form = DailyProgressForm()
    return render(request, 'habits/templates/daily_progress_form.html', {'form': form})