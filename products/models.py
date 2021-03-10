from django.db import models
from django.urls import reverse
from django.dispatch import receiver
from django.db.models import signals
from django.utils.text import slugify

from company.models import Company


class Product(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, default='na')
    description = models.TextField()
    url = models.CharField(max_length=500)
    cta = models.CharField(max_length=200)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('company', kwargs={'slug': self.slug})


@receiver(signals.pre_save, sender=Product)
def populate_slug(sender, instance, **kwargs):
    slug = slugify(instance.name)
    counter = 0
    try:
        while Product.objects.get(slug=slug):
            slug = slug + '_' + str(counter)
            counter = +1
    except:
        instance.slug = slug
