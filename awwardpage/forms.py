from django import forms
from awwardpage.models import Rates, Post, Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
class NewPostForm(forms.Form):
    title = forms.CharField(max_length=200)
    project_image = forms.ImageField()
    description =forms.CharField(max_length=500)
    url=forms.CharField(max_length=200)
# class ratesForm(forms.Form):
#     design=IntegerField()
#     usability=IntegerField()
#     content=IntegerField()
class SignUpForm(UserCreationForm):
    full_name = forms.CharField(max_length=50, required=False)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )

class UpdateUserForm(forms.ModelForm):
    email = forms.EmailField(max_length=254, help_text='Required.')

    class Meta:
        model = User
        fields = ('username', 'email')


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['user','profile_pic', 'bio']

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['user', 'profile', 'date']

class RatingsForm(forms.ModelForm):
    class Meta:
        model = Rates
        fields = ['design', 'usability', 'content']