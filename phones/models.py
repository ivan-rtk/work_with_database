from django.db import models
from django.db.models import BooleanField


class Phone(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    price = models.FloatField()
    image = models.URLField()
    release_date = models.DateField()
    lte_exists: BooleanField = models.BooleanField()
    slug = models.SlugField()

    def __str__(self):
        return f"{self.id}; {self.name}; {self.price}; {self.image}; {self.release_date}; {self.lte_exists}; {self.slug}"
