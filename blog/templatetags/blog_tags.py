from django import template
from blog.models import Post,Categories
register = template.Library()

@register.simple_tag(name="count")
def func():
    p = Post.objects.filter(status=1).count()
    return p


@register.simple_tag(name="all")
def func():
    p = Post.objects.filter(status=1)
    return p

@register.filter
def snippet(value,args=20):
    return value[:args] +" ... "


@register.inclusion_tag("popular-posts.html")
def popular():
    posts = Post.objects.filter(status=1).order_by("created_date")
    return {"pp":posts}


@register.inclusion_tag("blog/latest-posts.html")
def latest(arg=3):
    posts = Post.objects.filter(status=1).order_by("-published_date")[:arg]
    return {"posts":posts}


@register.inclusion_tag("blog/post-category-widget.html")
def postCategories():
    posts = Post.objects.filter(status=1)
    categories = Categories.objects.all()
    cat_dict = {}
    for name in categories:
        cat_dict[name]= posts.filter(category=name).count()
    return {"categories":cat_dict}



@register.inclusion_tag("blog/tag-cloud-widget.html")
def postCategoriesCount():
    posts = Post.objects.filter(status=1)
    categories = Categories.objects.all()
    cat_dict = {}
    for name in categories:
        cat_dict[name]= posts.filter(category=name).count()
    return {"categories":cat_dict}