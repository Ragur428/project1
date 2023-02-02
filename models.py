
from django.db import models
from django.db.models import Count, Avg
from ckeditor.fields import RichTextField
from django import template
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify
from django.core.validators import MaxLengthValidator

import random
from account.models import User
import datetime
import os

register = template.Library()

char = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
        'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
        'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


# Create your models here.



class AddSitings(models.Model):
    animals = models.CharField(max_length=120)
    breed = models.TextField(max_length=500, null=True)
    created_at = models.DateTimeField(_('created_at'), auto_now_add=True, null=True, blank=True)


