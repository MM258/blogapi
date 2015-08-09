from django.db import models

# Create your models here.
class Case(models.Model):
    title = models.CharField(max_length=256)
    content = models.TextField(default=None,blank=True)
    tag = models.TextField(default=None,blank=True)
    create_by = models.CharField(max_length=256,blank=True)
    create_time = models.DateField()
     # picture = models.ImageField(upload_to="upload")


class Contact_us(models.Model):
    name = models.CharField(max_length=256)
    email = models.EmailField()
    content = models.TextField(default=None,blank=True)
    weibo = models.CharField(max_length = 30)
    telephone = models.IntegerField(max_length=11)

    def __unicode__(self):
        return self.name

class About_us(models.Model):
    name = models.CharField(max_length=256)
    email = models.EmailField()
    content = models.TextField(default=None,blank=True)
    weibo = models.CharField(max_length = 30)
    telephone = models.IntegerField(max_length=11)

    def __unicode__(self):
        return self.name
