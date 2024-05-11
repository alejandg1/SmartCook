from django import models 

class TempImg(models.Model):
    imgID = models.AutoField(primary_key=True)
    imgID = models.models.IntegerField(null=True, blank=True)
    url = models.CharField(max_length=255)
    
    def getImg(self):
        return self.url
    
    def setImg(self, url):
        self.url = url