from django.urls import path

from blog.views import *
app_name = "blog"
urlpatterns = [

    path('single-<int:pid>/', blog_single ,name="single"),
    path('test-<int:pid>/',test , name="test"),
    path('pop/',pop , name="pop"),
    path('', blog ,name="index"),
    path('category/<str:cat_name>',blog , name="category"),  
    path('author/<str:author_name>',blog , name="author"),  
    path('search/',blog_search , name="search")  
]
