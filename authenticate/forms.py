from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm



# class RegistrationForm(forms.ModelForm):
#     username=forms.CharField( max_length=60, required=False)
#     first_name=forms.CharField( max_length=60, required=False)
#     email=forms.EmailField(required=False)


#     class Meta:
#             model= User
#             fields=('username','first_name','last_name','email','password1','password2' )
class EditProfileForm(UserChangeForm):
    password=forms.CharField(label="", widget=forms.TextInput(attrs={'type':'hidden'}))

    class Meta:
        model=User
        fields=('username','first_name','last_name','email','password',)

       

class RegistrationForm(UserCreationForm):
    username=forms.CharField(help_text="<div class='form-text text-muted'><small>Enter a valid username</small></div>",label="", max_length=70, required=True, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter username'}))
    email=forms.EmailField(help_text="<div class='form-text text-muted'><small>Enter a valid E-mail address</small></div>",required=True, label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email address'}))
    first_name=forms.CharField(label="", max_length=100, required=False, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'First name'}))
    last_name=forms.CharField(label="", max_length=100, required=False, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last name'}))
    password1=forms.CharField(help_text="<small><ul class='form-text text-muted'><li>password must be at least 8 characters</li><li>password cannot be all numeric</li><li>password cannot be a commonly used password</li></ul></small>",label="", max_length=20, required=False, widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Enter password'}))
    password2=forms.CharField(label="", max_length=20, required=False, widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Confirm password'}))



    class Meta:
        model= User
        fields=('username','first_name','last_name','email','password1','password2', )

    def _init_(self, *args, **kwargs):
        super(RegistrationForm, self)._init_(*args, **kwargs)  

        self.fields['username'].widget.attrs['class']='form-control'
        self.fields['username'].widget.attrs['placeholder']='Username'
        self.fields['username'].label=""
        


        self.fields['password1'].widget.attrs['class']='form-control'
        self.fields['password1'].widget.attrs['placeholder']='Password'
        self.fields['password1'].label=""
        
        self.fields['password2'].widget.attrs['class']='form-control'
        self.fields['password2'].widget.attrs['placeholder']='Confirm password'
        self.fields['password2'].label=""
    
