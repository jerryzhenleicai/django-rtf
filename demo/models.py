from rich_text import RichTextField
from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=64)
    resume = RichTextField(blank=True, null=True)
