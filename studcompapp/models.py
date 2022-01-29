from django.db import models

# Create your models here.
class student(models.Model):
    name = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100, null=True)
    complaint_subject = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=600, null=True)
    date_created = models.DateTimeField(auto_now_add=True)


    # def __str__(self):
    #     return self.name