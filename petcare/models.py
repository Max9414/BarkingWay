from django.db import models
from django.utils.text import slugify

# Create your models here.

class PetCare(models.Model):
    title = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    excerpt = models.TextField()
    slug = models.SlugField(unique=True, blank=True) #set to blank to allow auto-generation as it was giving error otherwise

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["title"]

    #this autogenerates the slug field for url based on the breed
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)