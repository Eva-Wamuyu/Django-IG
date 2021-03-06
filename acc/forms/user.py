from django.forms import CharField
from django.contrib.auth import models, forms
from django.contrib.auth.hashers import make_password

class NewUserRegForm(forms.UserCreationForm):

  email = CharField(max_length=120, required=True)
  fullname = CharField(max_length=120)
  #password1 = CharField(widget=PasswordInput())
  class Meta:
    model = models.User
    fields = [
      "username",
      "email",
      "password1",
      "password2"
    ]

    def save_user(self, commit=True):
      user = super(NewUserRegForm, self).save(commit=False)
      user.email = self.cleaned_data["email"]
      user.fullname = self.cleaned_data["fullname"]
      user.password = make_password(self.cleaned_data['password1'])
      if commit:
        user.save()
        print("Saved")
      return user

