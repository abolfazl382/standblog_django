from django.contrib.auth.models import User
from django.db import models

choices = [
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Other'),
    ]

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=10, choices=choices)
    age = models.IntegerField()
    image = models.ImageField(null=True, blank=True, default='default.jpg', upload_to='images/profiles')

    def __str__(self):
        return self.user.username
