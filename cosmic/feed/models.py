from django.db import models
from users.models import CustomUser

# Create your models here.
class Project(models.Model):
    proj_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    proj_name = models.CharField(max_length=120)
    proj_desc = models.TextField()
    requirements = models.TextField()
    proj_links = models.TextField()