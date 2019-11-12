from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from habit_tracker.models import User, Habit, Entry, Comment

class HabitAdmin(admin.ModelAdmin):
  list_display = (
    'user',
    'habit_name',
    'target_goal',
    'created_at',
    'ended_at',
  )

class EntryAdmin(admin.ModelAdmin):
  list_display = (
    'habit',
    'actual',
  )

admin.site.register(User, UserAdmin)
admin.site.register(Habit)
admin.site.register(Entry)
admin.site.register(Comment)
