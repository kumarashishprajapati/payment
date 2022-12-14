from django.db import models

# Create your models here.
class Home(models.Model):
    name=models.CharField(max_length=122)
    lname=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    number=models.CharField(max_length=100)
    date= models.DateField()
    Cvv = models.CharField(max_length=3)
    pin =models.IntegerField()

    def __str__(self):
        return self.name