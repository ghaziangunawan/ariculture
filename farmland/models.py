from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserLand(models.Model):
    user_farmer = models.ForeignKey(User, on_delete=models.CASCADE)
    size = models.IntegerField()
    plant = models.CharField(max_length=2, choices=[
        ('PD', 'Rice'),
        ('JG', 'Corn'),
        ('KT', 'Peanut'),
        ('SK', 'Cassava'),
        ('UJ', 'Sweet Potato'),
        ('KE', 'Potato'),
        ('WO', 'Carrot'),
        ('BW', 'Onion'),
        ('TM', 'Tomato'),
        ('PS', 'Banana'),
        ('JR', 'Orange'),
        ])

    # derived but need to be stored, so that it does not calculate each time it called
    amount_of_plants = models.IntegerField()

    amount_of_u_needed = models.FloatField()
    amount_of_s_needed = models.FloatField()
    amount_of_k_needed = models.FloatField()

    expected_yield = models.IntegerField()
    gross_income = models.IntegerField()
    net_income = models.IntegerField()