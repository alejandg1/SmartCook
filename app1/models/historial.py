from django import models
from models import User

class Historial(models.Model):
    histID = models.AutoField(primary_key=True)
    userID = models.models.ForeignKey(User)


class DetHistorial(models.Model):
    detHistID = models.AutoField(primary_key=True)
    histID = models.models.ForeignKey(Historial)
    date = models.DateField(auto_now=True)
    Recipe = models.CharField(max_length=255)
    Instructions = models.CharField(max_length=255)

    def getDate(self):
        return self.date

