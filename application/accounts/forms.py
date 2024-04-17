from django import forms  
from django.contrib.auth.models import User, Group, Permission  
from django.contrib.auth.forms import UserCreationForm  
from django.core.exceptions import ValidationError  
from django.forms.fields import EmailField  
from django.forms.forms import Form  
from .apps import puzzlePerms
from django.contrib.contenttypes.models import ContentType
    
class SignupUserCreationForm(UserCreationForm):  
    username = forms.CharField(label='username', min_length=5, max_length=150)  
    email = forms.EmailField(label='email')  
    password1 = forms.CharField(label='password', widget=forms.PasswordInput)  
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)  
    
    def username_clean(self):  
        username = self.cleaned_data['username'].lower()  
        new = User.objects.filter(username = username)  
        if new.count():  
            raise ValidationError("User Already Exist")  
        return username  
    
    def email_clean(self):  
        email = self.cleaned_data['email'].lower()  
        new = User.objects.filter(email=email)  
        if new.count():  
            raise ValidationError(" Email Already Exist")  
        return email  
    
    def clean_password2(self):  
        password1 = self.cleaned_data['password1']  
        password2 = self.cleaned_data['password2']  
    
        if password1 and password2 and password1 != password2:  
            raise ValidationError("Password don't match")  
        return password2  
    
    def save(self, commit = True):  
        user = User.objects.create_user(  
            self.cleaned_data['username'],  
            self.cleaned_data['email'],  
            self.cleaned_data['password1']  
        )
        user.user_permissions.add(puzzlePerms[0])
        if commit:
            user.save()
        return user
    




class SignupEmployerCreationForm(UserCreationForm):  
    username = forms.CharField(label='username', min_length=5, max_length=150)  
    email = forms.EmailField(label='email')  
    password1 = forms.CharField(label='password', widget=forms.PasswordInput)  
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)
    verifier = forms.CharField(label='Employer code')  
    
    def username_clean(self):  
        username = self.cleaned_data['username'].lower()  
        new = User.objects.filter(username = username)  
        if new.count():  
            raise ValidationError("User Already Exist")  
        return username  
    
    def email_clean(self):  
        email = self.cleaned_data['email'].lower()  
        new = User.objects.filter(email=email)  
        if new.count():  
            raise ValidationError(" Email Already Exist")  
        return email  
    
    def clean_password2(self):  
        password1 = self.cleaned_data['password1']  
        password2 = self.cleaned_data['password2']  
    
        if password1 and password2 and password1 != password2:  
            raise ValidationError("Password don't match")  
        return password2  
    
    def save(self, commit = True):  
        verifierCode = self.cleaned_data['verifier']
        if verifierCode == "test1":
            user = User.objects.create_user(  
                self.cleaned_data['username'],  
                self.cleaned_data['email'],  
                self.cleaned_data['password1']  
            )
            user.user_permissions.add(puzzlePerms[0])
            employerGroup = Group.objects.get_or_create(name="Employer")[0]
            employerGroup.permissions.set([Permission.objects.get_or_create(
                name="Is Employer",
                content_type=ContentType.objects.get_for_model(User),
                codename="is_employer"  
                )[0]])
            user.groups.add(employerGroup)
            if commit:
                user.save()
            return user
        else:
            raise ValidationError("Employer code is incorrect")