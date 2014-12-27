from django.db import models

# Create your models here.

class   Category(models.Model):
        title = models.CharField(max_length=50)


class   Post(models.Model):
        title = models.CharField(max_length=100)
        add_datetime = models.DateTimeField()
        publish_datetime = models.DateTimeField()
        category = models.ForeignKey(Category, db_column='cat_id')
        body = models.CharField(max_length=1000)



