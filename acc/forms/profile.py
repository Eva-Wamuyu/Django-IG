from django import forms
from acc.models.user import Profile


class ProfileForm(forms.ModelForm):
  class Meta:
    model = Profile
    fields = [
      "profile_photo",
      "bio"

    ]


     