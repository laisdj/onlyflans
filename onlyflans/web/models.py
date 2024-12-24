from django.db import models
import uuid
from django import forms

class Flan(models.Model):
    flan_uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)  # Campo UUID correcto
    name = models.CharField(max_length=64)
    description = models.TextField(default="No description")
    image_url = models.URLField()
    slug = models.SlugField(unique=True)
    is_private = models.BooleanField()

def __str__(self):
    return self.name


class ContactForm(models.Model):
    contact_form_uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    customer_email = models.EmailField()
    customer_name = models.CharField(max_length=64)
    message = forms.CharField(label='Tu mensaje', widget=forms.Textarea(attrs={'rows': 5, 'class': 'form-control', 'style': 'resize: none;'}))



