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
    image = models.ImageField(null=True, blank=True, default='images/default.png', upload_to='images/profiles')

    def __str__(self):
        return self.user.username

    # def save(self, *args, **kwargs):
    #
    #     super(Profile, self).save(*args, **kwargs)
