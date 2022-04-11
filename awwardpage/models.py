from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.utils import timezone



# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic = CloudinaryField('image', blank=True)
    bio = models.TextField()
    contact = models.TextField
    project = models.TextField()

    def __str__(self):
     return self.user.username

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()  

    def update_profile(cls, id):
        Profile.objects.get(user_id=id)

    @classmethod
    def search_profile(cls, name):
        return cls.objects.filter(user__username__icontains=name).all()
   
        
class Post(models.Model):
    project_image = CloudinaryField('images')
    description = models.TextField()
    title = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    user = models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    profile = models.ForeignKey(Profile,on_delete = models.CASCADE, null=True)
    date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.title

    def save_post(self):
        return self.save()

    def delete_post(self):
        self.delete()
    @classmethod
    def get_post_by_id(cls,id):
        post=cls.objects.filter(id=id).get()
        return post

    @classmethod
    def search_by_project(cls, searched_project):
        project = cls.objects.filter(title__icontains=searched_project)
        return project
    


class Rates(models.Model):
    RATE_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
        (9, '9'),
        (10, '10'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    post = models.ForeignKey(Post, null=True, on_delete=models.CASCADE)
    design = models.IntegerField(choices=RATE_CHOICES, default=0, blank=False)
    usability = models.IntegerField(choices=RATE_CHOICES, default=0, blank=False)
    content = models.IntegerField(choices=RATE_CHOICES, default=0, blank=False)
    average = models.DecimalField(default=1, blank=False, decimal_places=2, max_digits=40)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.post.title


