from django.db import models

# Create your models here.

class c_todo(models.Model):
    Todoid = models.AutoField(primary_key=True)
    Todotext = models.TextField()
    Tododone = models.BooleanField()
    
    def __str__(self):
        return self.Todotext
        #return f"{self.Todoid} {self.Todotext}"