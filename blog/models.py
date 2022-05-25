from django.db import models
from pytz import unicode

class UsersNew(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Имя пользователя',max_length=50)
    email = models.CharField('Email пользователя',max_length=150)
    
    def __str__(self):
        return unicode(self.name)