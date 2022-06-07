from django import views
from django.http import HttpResponseRedirect
from django.urls import reverse
from acc.forms.user import NewUserRegForm
from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout,decorators
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

from acc.models.user import Profile
# Create your views here.
class Signup(views.View):
  def get(self, request):
    form = NewUserRegForm()
    print("get")
    return render(request, 'registration/registration_form.html', {'form':form})
  
  def post(self, request):
    form = NewUserRegForm(request.POST)
    print(form.errors)
    if form.is_valid():
       
       user = form.save()
       username = User.objects.filter(username=form.cleaned_data['username'])[0]
       newProfile = Profile.objects.create(user=username)
       newProfile.save()
       login(request, user)
       return HttpResponseRedirect(reverse('home',kwargs={'username':username}))
    messages.error(request, "Unsuccessful registration.")
    return render(request, 'registration/registration_form.html', {'form':form})



class Login(views.View):
    
    def get(self, request):
      form = AuthenticationForm()
      return render(request, 'registration/login.html', {'form':form})
   
    def post(self, request):
      
      form = AuthenticationForm(data=request.POST)
      print(form.is_valid)
      if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if user is not None:
          login(request, user)
          username = user.username
          return HttpResponseRedirect(reverse('home',kwargs={'username':username}))
        else:
          errors = "Invalid username or password."
          messages.error(request, messages.INFO, 'username or password is not known')
          form = AuthenticationForm()
          return render(request,"registration/login.html", {"form":form, 'errors':errors})
      messages.error(request, messages.INFO, 'username or password is not known')
      return render(request,"registration/login.html",{"form":form})
				
		
@decorators.login_required(login_url='login')
def logsout(request):
  logout(request)
  messages.info(request,"Logged Out Successfully")
  return redirect('login')



@decorators.login_required(login_url='')
def four_four(request,exception):
  return render(request, 'registration/404.html')

