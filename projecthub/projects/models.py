from django.db import models
import uuid

# Create your models here. 


class Project(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField(null=True, blank=True)
    featured_images = models.ImageField(
        blank=True,null=True,default='default.jpg')
    price = models.CharField(max_length=200)
    status = models.CharField(max_length=200)
    brand = models.CharField(max_length=200)
    tags = models.ManyToManyField('Tag',blank=True) 
    key_feature =  models.TextField(null=True, blank=True)
    basic_information =  models.TextField(null=True, blank=True)
    warranty =  models.CharField(max_length=200,null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    project_priority_sl = models.IntegerField(null=True, blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self) -> str:
        return self.title + ' - ' + str(self.project_priority_sl)
        
class Tag(models.Model): 
    name  = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                        primary_key=True, editable=False)   
    def __str__(self) -> str:
        return self.name
