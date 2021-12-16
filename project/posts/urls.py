from django.urls import path
 
from .views import HomePageView, PostsPageView, UserPageView
 
urlpatterns = [
    path('cabinet', UserPageView.as_view(), name='cabinet'),
    path('posts', PostsPageView.as_view(), name='posts'),
    #path('', HomePageView.as_view(), name='home'),
]
