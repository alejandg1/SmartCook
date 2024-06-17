from django.db import models
from security.models import User

# me parece mejor no guardar la imagen sino enviarla directo al modelo
# class TempImg(models.Model):
#     imgID = models.AutoField(primary_key=True)
#     image = models.ImageField(upload_to="tempImg/", blank=True, null=True)
#     userID = models.ForeignKey(
#         User,
#         unique=True,
#         on_delete=models.CASCADE,
#         null=True,
#         blank=True)
#
#     def getImg(self):
#         return self.url
#
#     def setImg(self, url):
#         self.url = url


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
    Recipe = models.CharField(max_length=255)
    Instructions = models.CharField(max_length=255)

    def getDate(self):
        return self.date
