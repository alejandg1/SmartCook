from django.db import models
from security.models import User


class TempImg(models.Model):
    imgID = models.AutoField(primary_key=True)
    url = models.CharField(max_length=255)
    data = models.BinaryField(blank=True, null=True)
    userID = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True)

    def getImg(self):
        return self.url

    def setImg(self, url):
        self.url = url


class Historial(models.Model):
    histID = models.AutoField(primary_key=True)
    userID = models.ForeignKey(User, on_delete=models.CASCADE)


class DetHistorial(models.Model):
    detHistID = models.AutoField(primary_key=True)
    histID = models.ForeignKey(Historial, on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
    Recipe = models.CharField(max_length=255)
    Instructions = models.CharField(max_length=255)

    def getDate(self):
        return self.date
