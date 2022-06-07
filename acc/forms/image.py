from django import forms
from acc.models.user import Comment, Image


class PostImage(forms.ModelForm):
  class Meta:
    model = Image
    fields = ['img','img_name','caption']

    labels = {
      'img': 'Upload Image',
      'img_name': 'Add image name',
      'caption': 'Add A Caption',
    }


class PostComment(forms.ModelForm):
  class Meta:
    model = Comment
    fields = ['comment']

    labels = {
      'comment': 'Add A Comment'
    }