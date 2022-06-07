from django.test import TestCase
from django.contrib.auth.models import User
from .models.user import Image,Profile,Comment
# Create your tests here.

class CommentTestClass(TestCase):
    def setUp(self):
        self.new_user = User.objects.create_user(username='minaj',password='999999')
        self.poster = Profile.objects.create(user=self.new_user)
        self.image = Image.objects.create(profile=self.poster)
        self.comment = Comment(comment='Comment',profile=self.poster,image=self.image)

    def test_instance(self):
        self.assertTrue(isinstance(self.comment,Comment))

    def tearDown(self):
        Comment.objects.all().delete()

    def test_save_method(self):
        self.comment.save_comment()
        comments = Comment.objects.all()
        self.assertTrue(len(comments)>0)

class ImageTestClass(TestCase):

    @classmethod
    def setUpTestData(self):
        self.new_user = User.objects.create_user(username='minaj',password='999999')
        self.poster = Profile.objects.create(user=self.new_user)
        self.image = Image.objects.create(img_name="funny", caption="wolo",profile=self.poster,img="fancy.png")
       
        

    def test_instance_true(self):
        self.assertTrue(isinstance(self.image, Image))

    def test_save_image_method(self):
        self.image.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) == 1)

    def tearDown(self):
        Image.objects.all().delete()
        Profile.objects.all().delete()
        User.objects.all().delete()              

class Profile(TestCase):
    def setUp(self):
        self.user= User(username='minaj',password='12244')
        self.user.save()
        self.profile = Profile()  
        #profile.save_profile(self)
       
    

    def tearDown(self):
        User.objects.all().delete()
        Image.objects.all().delete()

    def test_is_instance(self):
        self.assertTrue(isinstance(self.user,User))
        self.assertTrue(isinstance(self.profile,Profile))
      

    def test_save_method(self):
        self.profile.save_profile()
        all_profiles = Profile.objects.all()
        self.assertTrue(len(all_profiles)>0)

 

