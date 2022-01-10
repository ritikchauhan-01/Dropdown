from django.db import models

# Create your models here.
class DropDownList(models.Model):
  name = models.CharField(max_length=250,null=True)

  def __str__(self):
    return self.name
