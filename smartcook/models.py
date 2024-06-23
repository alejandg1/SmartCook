from django.db import models
from security.models import User


class Historial(models.Model):
    histID = models.AutoField(primary_key=True)
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE,
                                null=True,
                                blank=True)


class DetHistorial(models.Model):
    detHistID = models.AutoField(primary_key=True)
    histID = models.ForeignKey(Historial, on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
    Recipe = models.CharField(max_length=300, null=True, blank=True)
    Instructions = models.TextField(null=True, blank=True)
    Ingredients = models.TextField(null=True, blank=True)

    def getDate(self):
        return self.date
