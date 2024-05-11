from django.db import models
from models import TempImg

class User(models.Model):
    userID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    imgID = models.ForeignKey(TempImg)

    def __str__(self):
        return self.Name
    
    def getImg(self):
        return self.imgID
    
    def setPass(self, password):
        self.password = password
    
    def getPass(self):
        return self.password

