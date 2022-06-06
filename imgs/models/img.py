from .user import *


class Image(models.Model):
  img = CloudinaryField('image')
  img_name = models.CharField(max_length=20)
  caption = models.CharField(max_length=200)
  likes = models.IntegerField(default=0)
  profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
  


class Comment(models.Model):
  profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
  image = models.ForeignKey(Image, on_delete=models.CASCADE)