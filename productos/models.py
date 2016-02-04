#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.postgres.fields import JSONField
from django.db.models.signals import pre_save, post_save
from django.utils.text import slugify

# Create your models here.


class Categoria(models.Model):
    name = models.CharField(max_length=50)  # Auto, Beauty, etc.

class SubCategoria(models.Model):
    category = models.ForeignKey(Categoria)
    name = models.CharField(max_length=50)


class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    slug = models.SlugField(blank=True)#(unique=True)
    foto = models.ImageField(upload_to='prod/')
    categoria = models.ForeignKey(SubCategoria)
    precio_flete = models.SmallIntegerField(null=True)
    caracteristicas = JSONField()


def product_pre_save_reciever(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.nombre)+ "-"+ slugify(instance.id)

pre_save.connect(product_pre_save_reciever, sender=Producto)

