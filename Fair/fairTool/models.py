from django.db import models

class Input(models.Model):
    user = models.CharField(max_length= 25)
    var1 = models.IntegerField(default=0)
    var2 = models.IntegerField(default= 0)
    var3 = models.IntegerField(default= 0)
    var4 = models.IntegerField(default= 0)
    var5 = models.IntegerField(default= 0)
    var6 = models.IntegerField(default= 0)
    var7 = models.IntegerField(default= 0)
    var8 = models.IntegerField(default= 0)
    var9 = models.IntegerField(default= 0)
    var10 = models.IntegerField(default= 0)
    var11 = models.IntegerField(default= 0)
    var12 = models.IntegerField(default= 0)
    input_date = models.DateTimeField('Date Entered')
    comments = models.TextField(blank = True, default = None)