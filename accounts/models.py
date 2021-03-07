from django.contrib.auth.models import User

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    profile_image = models.ImageField(upload_to='profile_images')
    profile_headline = models.CharField(max_length=100)
    profile_description = models.TextField()
    current_employer = models.CharField(max_length=100)
    current_website = models.CharField(max_length=200)
    current_city = models.CharField(max_length=100)
    current_state = models.CharField(max_length=100)
    current_country = models.CharField(max_length=100)
    professional_services = models.CharField(max_length=100)
    professional_specialist = models.CharField(max_length=100)

    def __str__(self):
        return self.user.email+ ' '

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):

    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

