from django.contrib import admin
from . models import Post, Author, Tag, Comment

# Register your models here.

admin.site.site_header="My Blog"

class AdminPost(admin.ModelAdmin):
	prepopulated_fields={"slug":("title",)}


class CommentPost(admin.ModelAdmin):
	list_display=("name","email","post")


admin.site.register(Author)
admin.site.register(Post, AdminPost)
admin.site.register(Tag)
admin.site.register(Comment, CommentPost)