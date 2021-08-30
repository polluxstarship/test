from django.db import models
from django.urls import reverse

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=1000,decimal_places=2)
    summary = models.TextField(default='this is cool!')
    featured = models.BooleanField(default=False, null=False)

    def get_detail_url(self):
        return reverse('product-detail', kwargs={"my_id": self.id})
    def get_delete_url(self):
        return reverse('product-delete', kwargs={"my_id": self.id})
    def get_edit_url(self):
        return reverse('product-edit', kwargs={"my_id": self.id})