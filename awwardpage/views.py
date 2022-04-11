from django.shortcuts import render,redirect,HttpResponseRedirect
from awwardpage.models import Post,Profile,Rates
from .forms import NewPostForm,RatingsForm
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import UserSerializer,ProfileSerializer,PostSerializer
from rest_framework import status
from django.urls import reverse
# Create your views here.
def homepage(request):
    message='WELCOME TO AWWWARDS'
    projects=Post.objects.all()
    return render(request,'homepage.html',{'message':message,'projects':projects})
def more_on_pic(request,id):
    project = Post.objects.get(id=id)
    rate = Rates.objects.filter(user=request.user, post=project).first()
    ratings = Rates.objects.all()
    rating_status = None
    if rate is None:
        rating_status = False
    else:
        rating_status = True
    current_user = request.user
    if request.method == 'POST':
        form = RatingsForm(request.POST)
        if form.is_valid():
            design = form.cleaned_data['design']
            usability = form.cleaned_data['usability']
            content = form.cleaned_data['content']
            review = Rates()
            review.post = project
            review.user = current_user
            review.design = design
            review.usability = usability
            review.content = content
            review.average = (
                review.design + review.usability + review.content)/3
            review.save()
            return HttpResponseRedirect(reverse('more', args=(project.id,)))
    else:
        form = RatingsForm()
    return render(request, 'moreabout.html',{'ratings': rate,'project': project,'form': form,'rating_status': rating_status,'reviews': ratings,})







    # rates=Ratings.objects.filter(Post=id)
    return render(request, 'moreabout.html', { 'more_on_pic': more_on_pic,'message':message})
def profile(request):
    message='profile'
    current_user = request.user
    post = Post.objects.filter(user=current_user.id).all
    return render(request,'profile.html',{'message':message,'post':post})
class ProfileList(APIView):
    
    def get(self, request, format=None):
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(profiles, many=True)
        return Response(serializer.data)

# def rate(request,id):
#     post = Post.objects.get(id=id)
#     rate = Rates.objects.filter(user=request.user, post=post).first()
#     ratings = Rates.objects.all()
#     rating_status = None
#     if rate is None:
#         rating_status = False
#     else:
#         rating_status = True
#     current_user = request.user
#     if request.method == 'POST':
#         form = RatingsForm(request.POST)
#         if form.is_valid():
#             design = form.cleaned_data['design']
#             usability = form.cleaned_data['usability']
#             content = form.cleaned_data['content']
#             review = Rates()
#             review.project = project
#             review.user = current_user
#             review.design = design
#             review.usability = usability
#             review.content = content
#             review.average = (
#                 review.design + review.usability + review.content)/3
#             review.save()
#             return HttpResponseRedirect(reverse('more', args=(project.id,)))
#     else:
#         form = RatingsForm()
#     params = {
#         'project': project,
#         'form': form,
#         'rating_status': rating_status,
#         'reviews': ratings,
#         'ratings': rate

#     }
#     return render(request, 'moreabout.html', params)
    # message='put your ratings'
    # if request.method == 'POST':
    #     form = NewPostForm(request.POST, request.FILES)        
    #     if form.is_valid():
    #         design=form.cleaned_data.get('project')
    #         usability=form.cleaned_data.get('description')
    #         content=form.cleaned_data.get('title')
    #         average =(int(design)+int(usability)+int(content))/3
    #         ratings=Ratings(design=design,usability=usability,content=content,average=average)
    #         ratings.save()  
    #     else:
    #         print(form.errors)
    #     return redirect("homepage")
    # else:
    #     form = ratesForm()
    # return render(request, 'moreabout.html', {"form": form})


def new_post(request):
    current_user = request.user
    # profile = request.GET.get("profile")
    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)        
        if form.is_valid():
            project_image=form.cleaned_data['project_image']
            description=form.cleaned_data['description']
            title=form.cleaned_data['title']
            url=form.cleaned_data['url']
            post = Post(project_image = project_image,description= description, title=title,url=url)
            post.save()  
        else:
            print(form.errors)
        return redirect("homepage")
    else:
        form = NewPostForm()
    return render(request, 'new_post.html', {"form": form})

    # message='place your post'
    # return render(request,'new_post.html',{'message':message})
def updateProfile(request):
    message='update your profile'
    return render(request,'updateProfile.html',{'message':message})
def search(request):
    # message='search here'
    # return render(request,'search.html',{'message':message})
    if 'article' in request.GET and request.GET["article"]:
        search_term = request.GET.get("article")
        searched_articles = Post.search_by_project(search_term)
        message = f"{search_term}"
        return render(request, 'search.html',{"message":message,"searched_articles": searched_articles})
    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})



class PostList(APIView):
   

    def get(self, request, format=None):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)