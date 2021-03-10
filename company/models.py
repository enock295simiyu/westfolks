from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.dispatch import receiver
from django.db.models import signals
from django.utils.text import slugify


class Company(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, default=1)
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, null=False, default='na')
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('company', kwargs={'slug': self.slug})

    class Meta:
        verbose_name_plural = 'Companies'


@receiver(signals.pre_save, sender=Company)
def populate_slug(sender, instance, **kwargs):
    slug = slugify(instance.name)
    counter = 0
    try:
        while Company.objects.get(slug=slug):
            slug = slug + '_' + str(counter)
            counter = +1
    except:
        instance.slug = slug
