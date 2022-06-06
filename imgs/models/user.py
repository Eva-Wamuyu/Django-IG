from email.policy import default
from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    profile_photo = CloudinaryField('image', default="/v1653763532/fkx4bmfae7enhta2wfqz.jpg")
    bio = models.CharField(max_length=120, blank=True)
    user = models.OneToOneField(User, primary_key=True)
    followers = models.ManyToManyField(User, related_name="followers")
    following = models.ManyToManyField(User, related_name="following")
    


