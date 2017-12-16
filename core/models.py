from django.db import models

# Create your models here.
class Catalogo(models.Model):
    descripcion = models.CharField(max_length=256)

    def __str__(self):
        return self.descripcion

    def __unicode__(self):
        return self.descripcion


class Area(models.Model):
    descripcion = models.CharField(max_length=256)
    name = models.ForeignKeyField('core.Catalogo', related_name='areas', on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.descripcion

    def __unicode__(self):
        return self.descripcion


class Item(models.Model):
    descripcion = models.CharField(max_length=256)
    area = models.ForeignKeyField('core.Area', related_name='items', on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.descripcion

    def __unicode__(self):
        return self.descripcion

