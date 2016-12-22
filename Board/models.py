from django.db import models

# Create your models here.
class Article(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    contents = models.TextField()
    email = models.EmailField()
    reg_date = models.DateTimeField(auto_now_add=True)
    #start_date =
    #end_date =