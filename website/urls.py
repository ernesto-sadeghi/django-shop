from django.contrib.sitemaps.views import sitemap
from django.urls import path

from .sitemaps import StaticViewSitemap
from website.views import *
from blog.sitemaps import BlogSitemap

sitemaps = {
    "static": StaticViewSitemap,
    "blog": BlogSitemap
}


app_name = "website"
urlpatterns = [

    path('', index ,name="index"),
    path('contact/', contact ,name="contact"),
    # path('blog/', blog ,name="blog"),
    path('about/', about ,name="about"),
    path('elements/', elements ,name="elem"),
    path('newsteller/', newstellerView ,name="newsteller"),
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps},name="django.contrib.sitemaps.views.sitemap"),
]
