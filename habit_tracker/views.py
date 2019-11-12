from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from habit_tracker.models import User, Habit, Entry, Comment
from habit_tracker.forms import HabitForm, EntryForm
from django.utils import timezone
from datetime import datetime

def home_page(request):
  user = request.user
  return render(request, 'home_page.html', {'user': user})

@login_required
def profile_page(request, pk):
  if request.method == "POST":
    form = HabitForm(request.POST)
    if form.is_valid():
      habit = form.save(commit=False)
      habit.user = request.user
      habit.created_at = timezone.now()
      habit.save()
      return redirect('profile_page', pk=pk)
  else:
    form = HabitForm()

    habits = Habit.objects.filter(user=User.objects.get(pk=pk))
  return render(request, 'profile_page.html', {'habits': habits, 'form': form})

@login_required
def habit_detail(request, pk):
  habit = Habit.objects.get(pk=pk)
  if request.method == 'POST':
    form = EntryForm(request.POST)
    if form.is_valid():
      entry = form.save(commit=False)
      entry.user = request.user
      entry.habit = habit
      entry.save()
      return redirect(to='habit_detail', pk=pk)
  else:
    form = EntryForm()
    records = Entry.objects.filter(habit=habit)
  return render(request, 'habit_detail.html', {'form': form, 'habit': habit, 'records': records})

# def delete_habit(request, pk):
#   habit = get_object_or_404(Habit, pk=pk)
#   if request.method == "POST":
#     habit.delete()
#     return redirect(to='profile_page')

#   return render(request, 'habit_tracker/profile_page.html', {'habit': habit})

