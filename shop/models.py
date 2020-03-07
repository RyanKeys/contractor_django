from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.


class Listing(models.Model):
    title = models.CharField(max_length=50, help_text="Name of your listing:")
    publisher = models.ForeignKey(User,on_delete=models.PROTECT)
    slug = models.CharField(max_length=50, blank=True, editable=False,
                            help_text="Unique URL path to access this page. Generated by the system.")
    created = models.DateTimeField(
        auto_now_add= True, help_text="Date and time model was created")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """ Returns path for a listing """
        path_components = {'slug': self.slug}
        return reverse('shop-details-page', kwargs=path_components)

    def save(self, *args, **kwargs):
        """ Creates a URL safe slug automatically when a new a page is created. """
        if not self.pk:
            self.slug = slugify(self.title, allow_unicode=True)

        # Call save on the superclass.
        return super(Listing, self).save(*args, **kwargs)
