from rest_framework import serializers
# from .models import ProfileSerializer
from .models import Profile,Post,Rates
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','email']
    
class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False, read_only=True)
    class Meta:
        model = Profile
        fields = ['id','user', 'profile_pic', 'bio', ]

class PostSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False, read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'user', 'title', 'project_image', 'url','description','date']