from django.db import models

# Create your models here.
class paitents(models.Model):
    paitent_ID = models.IntegerField()
    Name = models.CharField(max_length=200)
    Age = models.IntegerField()
    Disease = models.CharField(max_length=200)
    Location = models.CharField(max_length=100,blank=True)
    def __str__(self):
        return self.Name

                        