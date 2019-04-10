from django.db import models

class Index(models.Model):
    kind = models.CharField(
        max_length=8,
        primary_key=True,
        default='others')

class Text(models.Model):
    text = models.TextField()

class Blog(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=16)
    kind = models.ForeignKey(
        Index,
        on_delete=models.CASCADE)
    year = models.IntegerField()
    mounth = models.IntegerField()
    day = models.IntegerField()
    text = models.OneToOneField(
        Text,
        on_delete=models.CASCADE)
    
