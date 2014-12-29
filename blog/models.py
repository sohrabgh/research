from django.db import models
from django.contrib.auth.models import  User

# Create your models here.

class   Category(models.Model):

        title = models.CharField(max_length=50)


class   State(models.Model):

        title = models.CharField(max_length=20)


class   Post(models.Model):

        title = models.CharField(max_length=100)
        create_datetime = models.DateTimeField()
        publish_datetime = models.DateTimeField()
        update_time = models.DateTimeField()
        post_state = models.ForeignKey(State, db_column='state_id')
        category = models.ForeignKey(Category, db_column='cat_id')
        body = models.CharField(max_length=1000)
        create_user = models.ForeignKey(User, db_column='uid')


class   Comment(models.Model):

        body = models.CharField(max_length=50)
        post = models.ForeignKey(Post, db_column='post_id')
        email = models.EmailField();
        create_datetime = models.DateTimeField()
        create_user = models.ForeignKey(User, db_column='uid')





