from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class User(AbstractUser):
  
  def __str__(self):
    return self.username  

class Habit(models.Model):
  #user
  user = models.ForeignKey(to=User, on_delete=models.CASCADE, blank=True, related_name="author", null=True)
  #name of habit
  habit_name = models.CharField(max_length=100)
  measurement = models.CharField(max_length=50)
  #description of goal
  description = models.TextField(max_length=255)
  #goal
  target_goal = models.IntegerField(default=0)
  #date time of goal
  created_at = models.DateTimeField(default=timezone.now)
  #habit end
  ended_at = models.DateTimeField(blank=True, null=True)

  def __str__(self):
    return self.habit_name

class Entry(models.Model):
  #foreign key to habit
  habit = models.ForeignKey(to='Habit', on_delete=models.CASCADE, blank=True, related_name="entry", null=True)
  #quantity (what user enters)(video @ 11:09am)
  actual = models.IntegerField(default=0)
  #ratio / met goal?
  met_goal = models.BooleanField(default=False)
  #date-time (when goal was completed)
  time_complete = models.DateTimeField(default=timezone.now)
  comment = models.TextField(max_length=255)

  def __str__(self):
    return self.habit

class Comment(models.Model):
  #user
  author = models.ForeignKey(to='User', on_delete=models.CASCADE, blank=True, related_name="comments", null=True)
  #habit being commented on
  habit = models.ForeignKey(to='Habit', on_delete=models.CASCADE, blank=True, related_name="comments", null=True)
  #comment-text
  comment = models.TextField(max_length=255)

  created_at = models.DateTimeField(default=timezone.now)
  updated_at = models.DateTimeField(blank=True, null=True)

  def __str__(self):
    return self.comment
