from django.shortcuts import render,get_object_or_404
from blog.models import Post,Comment
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
# Create your views here.

# -----------------------------------------------------------------
def blog(request,**kwargs):
    # p = Post.objects.all()

    p = Post.objects.filter(status=True).order_by("-published_date")
    if kwargs.get("cat_name"):
        p = Post.objects.filter(category__name=kwargs["cat_name"],status=True)
    if kwargs.get("author_name"):
        p = Post.objects.filter(author__username=kwargs["author_name"])
    
    
    p = Paginator(p, 3)
    try:
        page_number=request.GET.get("page")
        p=p.get_page(page_number) 
        
    except PageNotAnInteger:
        # If the page number is not an integer, deliver the first page.
        p = Paginator.page(1)
    except EmptyPage:
        # If the page is out of range (e.g., 9999), deliver the last page.
        p = Paginator.page(Paginator.num_pages)

  
    context = {"posts":p}
    return render(request,"blog/blog-home.html",context)
# -----------------------------------------------------------------
def blog_single(request,pid):
    p = get_object_or_404(Post,pk=pid,status=1 )
    p.views_count+=1
    p.save()
    comments = Comment.objects.filter(post=p.id,approach=True)
    context = {"post":p,"n":pid+1,"p":pid-1,"comments":comments}
    return render(request,"blog/blog-single.html",context)

# -----------------------------------------------------------------
def test(request,pid):
    # p = Post.objects.all()
    # p = Post.objects.get(id=pid)
    p = get_object_or_404(Post,pk=pid)
    context = {"posts":p}
    return render(request,"test.html",context)

# -----------------------------------------------------------------
def pop(request):
    return render(request,"popular-posts.html")
# -----------------------------------------------------------------
# def blog_category(request,cat_name):

#     p = Post.objects.filter(status=True)
#     p = Post.objects.filter(category__name=cat_name)
#     context = {"posts":p}
#     return render(request,"blog/blog-home.html",context)
# -----------------------------------------------------------------


def blog_search(request):
    p = Post.objects.filter(status=True)
    if request.method =="GET":
        print(request.GET.get("s"))
        if s := request.GET.get("s"):
            p=p.filter(content__contains=s)
    
    context = {"posts":p}
    return render(request,"blog/blog-home.html",context)















