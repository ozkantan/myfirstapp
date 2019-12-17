from django.db import models
from django.urls import reverse

# Create your models here.

class TodoAppTheme(models.Model):  
    title = models.CharField(max_length=50, verbose_name="Başlık")
    completed = models.BooleanField(verbose_name="Durum")

    class Meta:
        verbose_name = ("")
        verbose_name_plural = ("Todo List")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})

