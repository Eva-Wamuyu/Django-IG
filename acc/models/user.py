from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    profile_photo = models.ImageField(upload_to="images/", default="/images/avatars.png")
    bio = models.CharField(max_length=120, default="New here")
    user = models.OneToOneField(User, primary_key=True,on_delete=models.CASCADE)
    followers = models.ManyToManyField(User, related_name="followers")
    following = models.ManyToManyField(User, related_name="following")
    
    def save_profile(self):
      self.save()
    

    def search(self,x):
      return Profile.objects.filter(name__unaccent__icontains=x)


class Image(models.Model):
  img = models.ImageField(upload_to="images/")
  img_name = models.CharField(max_length=20)
  caption = models.CharField(max_length=200)
  likes = models.IntegerField(default=0)
  profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
  

  def save_image(self):
    self.save()

  def delete_image(self):
    self.delete()

  def update_caption(self):
    self.update()


class Comment(models.Model):
  profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
  image = models.ForeignKey(Image, on_delete=models.CASCADE)
  comment = models.CharField(max_length=120)

  def get_Comments(x):
    comments = Comment.objects.filter(image=x)
    return comments
  
  def get_profile(self):
    return self.profile.user.username


  def save_comment(self):
    self.save()