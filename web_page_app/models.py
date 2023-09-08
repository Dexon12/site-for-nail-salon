from django.db import models
from django.utils import timezone
from django.urls import reverse

import datetime

class Registration(models.Model):
    user_nickname = models.CharField(max_length=100)
    user_name = models.CharField(max_length=150)
    user_surname = models.CharField(max_length=150)
    user_password = models.CharField(max_length=150)
    time_create_profile = models.DateTimeField(auto_now_add=True)




# _____________________________________________________________________________

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text  # Почему без создания конструктора к переменным можно обратиться через self


    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
    
class Women(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id':self.pk})
    


class Category(models.Model):
    name = models.CharField(max_length=100, db_index = True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_id':self.pk})
    