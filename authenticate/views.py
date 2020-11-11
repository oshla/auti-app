from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib import messages
from authenticate.forms import RegistrationForm, EditProfileForm
from django.contrib.auth.models import User



def home(request):
    return render(request,'authenticate/home.html', {})


def user_login(request):
    if request.method=="POST":
        username= request.POST['username']
        password= request.POST['password']
        user=authenticate(request,username=username, password=password)
        if user is not None:
            login(request,user)
            messages.success(request, ('You have been successfully logged in.'))
            return redirect("home")
        else:
            messages.success(request, ('Error logging in-please try again...'))
            return redirect("Login")
    else:
        return render(request,'authenticate/login.html', {})
        
def user_logout(request):
    logout(request)
    messages.success(request, ('you have been successfully logged out.')) 
    return redirect("home")

# def user_registration(request):
#     if request.method=='POST':
#         form=SignUpForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username= form.cleaned_data['username']
#             password= form.cleaned_data['password1']
#             user= authenticate(username=username, password=password)
#             login(request,user)
#             messages.success(request, ("you have been registered. Welcome!"))
#             return redirect('home')

#     else:
#         form=SignUpForm()

#     context={'form':form}
#     return render(request,'authenticate/register.html', context)

#  fields=('username','first_name','last_name','email','password1','password2', )
    
def user_registration(request):
    if request.method=='POST':
        form=RegistrationForm(request.POST)
        if form.is_valid():
            
            username= form.cleaned_data['username']
            first_name=form.cleaned_data['first_name']
            last_name=form.cleaned_data['last_name']
            email=form.cleaned_data['email']
            
            # new_user=User(first_name=first_name, username=username, last_name=last_name, email=email)
            form=RegistrationForm(request.POST,)
            form.save()
            # user= authenticate(username=username, password=password)
            # login(request,user)
            messages.success(request, ("you have been registered. Welcome!"))
            return redirect('home')
        else:
            messages.error(request, ("sorry! error submitting form"))
            form=RegistrationForm()
            print(form.errors)
              

    else:
        
        form=RegistrationForm()
        print(request)

    context={'form':form}
    return render(request,'authenticate/register.html', context)

def edit_profile(request):
    if request.method=='POST':
        form=EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            # new_user=User(first_name=first_name, username=username, last_name=last_name, email=email)
            form.save()
            # user= authenticate(username=username, password=password)
            # login(request,user)
            messages.success(request, ("profile has been successfully edited!"))
            return redirect('home')
        else:
            messages.error(request, ("sorry! error submitting form"))
            form=EditProfileForm()
            print(form.errors)
              

    else:
        
        form=EditProfileForm(instance=request.user)
        print(request)

    context={'form':form}
    
    return render(request,'authenticate/edit_profile.html', context)

def change_password(request):
    if request.method=='POST':
        form=(request.POST)
        if form.is_valid():
            # new_user=User(first_name=first_name, username=username, last_name=last_name, email=email)
            form=PasswordChangeForm(data=request.POST, user=request.user)
            form.save()
            # user= authenticate(username=username, password=password)
            # login(request,user)
            messages.success(request, ("Password has been changed!"))
            return redirect('home')
        else:
            messages.error(request, ("sorry! error submitting form"))
            form=PasswordChangeForm()
            print(form.errors)
    
    else:

        
        form=PasswordChangeForm(user=request.user)
        print(request)

    context={'form':form}
    
    return render(request,'authenticate/change_password.html', context)

def about_us(request):
    return render(request,'authenticate/about_us.html', {})





    

