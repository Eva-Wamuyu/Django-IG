from django.urls import path,include
from .views import acc,profile

urlpatterns = [
  path("",acc.Login.as_view(), name="login"),
  path("register",acc.Signup.as_view(), name="signup"),
  path("home/<username>",profile.home, name="home"),
  path("edit/<username>",profile.edit, name="edit"),
  path("<username>",profile.acc, name="acc"),
  path("f/<username>",profile.follow, name="follow"),
  path("image/<id>",profile.image, name="image"),
  path("logout",acc.logsout, name="logout"),
  path("results",profile.search, name="search"),
  
]


handler404 = acc.four_four