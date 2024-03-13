from django.db import models

# Create your models here.


class Weapon(models.Model):
    smg = models.IntegerField(max_length=60)
    heavygun = models.IntegerField(max_length=150)
    pistol = models.IntegerField(max_length=30)
    knfie = models.Empty()



# a funtion to call my class wiht all infos in a line , but to use it in command line with : python manage.py  shell
    def __str__(self):
        return f"{self.id} - {self.smg} and {self.heavygun} and {self.pistol} are Guns for a shooting game"

