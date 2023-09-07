from django.db import models

from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.utils.text import slugify



# Create your models here.

class ManagerUser(BaseUserManager):
    def create_user(self, username, password, is_active=True, is_superuser=False, is_staff=False, *args, **kwargs):
        user = self.model(username=username,
                          password=password,
                          is_active=is_active,
                          is_staff=is_staff,
                          is_superuser=is_superuser,
                          **kwargs)
        user.set_password(password)
        user.save()
        return user
# hgjhgjhgjhgjhgjhgjhghjgj
    def create_superuser(self, username, password, **kwargs):
        return self.create_user(username, password, is_superuser=True, is_staff=True, **kwargs)

class Style(models.Model):
    name = models.CharField(max_length=128, unique=True, blank=False, null=False)

    def __str__(self):
        return self.name
class Category(models.Model):
    name = models.CharField(max_length=128)
    key = models.SlugField(max_length=128, blank=True)
    is_menu = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.key:
            self.key = slugify(self.name)
        return super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Products(models.Model):
    product_id = models.CharField(max_length=128)
    ctg = models.ForeignKey(Category, on_delete=models.CASCADE)
    style = models.ForeignKey(Style, on_delete=models.CASCADE)
    material = models.CharField(max_length=128, blank=False, null=False, default="MDF")
    color = models.CharField(max_length=128)
    img = models.ImageField()

    def __str__(self):
        return self.product_id, self.ctg, self.style

class Contact(models.Model):
    name = models.CharField(max_length=128)
    phone = models.CharField(max_length=128)
    def __str__(self):
        return self.name



class Basket(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    create_date = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        return super(Basket, self).save(*args, **kwargs)

    def __str__(self):
        return self.product



