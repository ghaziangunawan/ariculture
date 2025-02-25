from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Advertisement(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.TextField()
    title = models.TextField()
    description = models.TextField()
    ad_type = models.TextField(default="FARMLAND")
    username = models.TextField(default="NULL")
