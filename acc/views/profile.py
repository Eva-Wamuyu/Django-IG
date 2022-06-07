from django.shortcuts import render
from django import views
from acc.forms.image import PostImage,PostComment
from acc.forms.profile import ProfileForm
from django.contrib.auth.models import User
from acc.models.user import Image, Profile, Comment
from django.contrib.auth.decorators import login_required
from .acc import *
# # Create your views here.


@login_required(login_url='')
def home(request,username):
  form = PostImage()
  posts = Image.objects.all()
  people = User.objects.filter(is_superuser=False)
  context = {'posts':posts,"form": form,'people':people}
  if request.method == 'POST':
    form = PostImage(data=request.POST,files=request.FILES)
    print(form.errors)
    if form.is_valid():
      user = User.objects.filter(username=username)[0]
      poster = Profile.objects.filter(user=user.id)[0]
      #img = add_pic(form.cleaned_data['img'],request.FILES['img'])
      #print(img)
      photo = Image.objects.create(
        img=form.cleaned_data['img'],
        profile_id=user.id,
        img_name=form.cleaned_data['img_name'],
        caption=form.cleaned_data['caption']
      )
      photo.save()
      form = PostImage()
      return render(request, 'acc/home.html', context=context) 
  return render(request, 'acc/home.html', context=context)


@login_required(login_url='')
def add_pic(name,file):
    url=f'media/images/{name}.jpg'
    with open(url,'wb+') as dest:
        for chunk in file.chunks():
            dest.write(chunk)

    
@login_required(login_url='')
def edit(request,username):
  print(username)
  user = User.objects.get(username=request.user)
  print(user)
  form = ProfileForm(initial={'bio':user.profile.bio, 'profile_photo':user.profile.profile_photo})
  context = {"form": form}
  if request.method == 'POST':
    form = ProfileForm(data=request.POST,files=request.FILES)
    print(form.errors)
    if form.is_valid():
      user = User.objects.get(username=request.user)
      poster = Profile.objects.filter(user=user.id)[0]
      print(poster)
      new_profile = Profile(profile_photo=form.cleaned_data['profile_photo'], bio=form.cleaned_data['bio'],user=user)
      new_profile.profile_photo = form.cleaned_data['profile_photo']
      new_profile.bio = form.cleaned_data['bio']
      new_profile.save()
      print(new_profile.bio)
      form = ProfileForm(initial={'profile_photo': new_profile.profile_photo,'bio': new_profile.bio})
      context = {"form": form}
      return render(request, 'acc/edit.html', context=context)
  return render(request, 'acc/edit.html', context=context)


@login_required(login_url='')
def acc(request,username):
  try:
   user = User.objects.get(username=username)
  except User.DoesNotExist:
    error = "User does not exist"
    return render(request, 'acc/acc.html', {'error': error})
  else:
   pp = Profile.objects.get(user=user)
   posts = Image.objects.filter(profile=pp)
   context = {'user': user,'posts': posts}
   return render(request, 'acc/acc.html', context=context)
  

@login_required(login_url='')
def follow(request,username):
  user = User.objects.get(username=username)
  print(user)
  #user.save()
  user2 = User.objects.get(username=request.user)
  print(user2)
  user.profile.followers.set([user2])
  user2.profile.following.set([user])
  user.save()
  user2.save()
  

  return HttpResponseRedirect(reverse('acc',kwargs={'username':user}))

@login_required
def image(request,id):
  form = PostComment()
  
  image = Image.objects.get(id=id)
  
  try: 
   comments = Comment.get_Comments(id)
   #comments = Comment.objects.get(image=image.id)
   
  except Comment.DoesNotExist:
    comments = ["",""]
  context = {'image':image, 'comments':comments, 'form':form}

  if request.method == 'POST':
    user = User.objects.get(pk=3)
    print(user)
    print(form.is_valid())
    form = PostComment(request.POST)
    if form.is_valid():
      print(user)
      profile = Profile.objects.get(user=user)
      
      newComment = Comment.objects.create(image=image,profile=profile,comment=form.cleaned_data['comment'])
      newComment.save()
      print(newComment)
      form = PostComment()
      return render(request, 'acc/image.html',context=context)
    return render(request, 'acc/image.html',context=context)
  return render(request, 'acc/image.html',context=context)


def search(request):
  if 'username' in request.GET and request.GET['username']:
    people = Profile.objects.filter(name__unaccent__icontains= request.GET.get('category'))
    print(people)
    return render(request, 'acc/search.html',{'people':people})

  return render(request, 'acc/search.html',{'heading':'xx'})
  

  
