from __future__ import unicode_literals

from django.db import models


class Student(models.Model):
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    email = models.EmailField(max_length=20)
    password = models.CharField(max_length=10)
    phone = models.IntegerField(max_length=10,null=True)

    class Meta:
        db_table = "score"
