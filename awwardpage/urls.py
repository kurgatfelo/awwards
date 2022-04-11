from django.urls import path,re_path
from . import views
from django.conf import settings

urlpatterns = [
    path('api/post/', views.PostList.as_view()),
    path('api/profile/', views.ProfileList.as_view()),
    path('',views.homepage,name='homepage'),
    path('more/<int:id>',views.more_on_pic,name='more'),
    path('profile/',views.profile,name='profile'),
    # path('rate/',views.rate,name='rate'),
    path('newpost/',views.new_post,name='new_post'),
    path('updateProfile/',views.updateProfile,name='updateProfile'),
    path('search/',views.search,name='search')
]