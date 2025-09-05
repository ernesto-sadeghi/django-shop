from django.contrib import admin

# Register your models here.
from blog.models import Post,Categories,Comment

class PostAdmin(admin.ModelAdmin):
    date_hierarchy="created_date"
    empty_values_display="--!@---empty---@!--"
    list_display=("title","author","views_count","status","created_date")
    list_filter=("status","author")
    ordering=["-created_date"]
    search_fields=["title","content"]
class CommentAdmin(admin.ModelAdmin):
    date_hierarchy="created_date"
    empty_values_display="--!@---empty---@!--"
    list_display=("subject","name","approach","created_date")
    list_filter=("name","approach")
    ordering=["-created_date"]
    # search_fields=["title","content"]

admin.site.register(Post,PostAdmin)
admin.site.register(Categories)
admin.site.register(Comment,CommentAdmin)
