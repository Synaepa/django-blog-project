from django.db import models
from django.contrib import admin

# Create your models here.
class Post(models.Model):
	title= models.CharField(max_length=60)
	body= models.TextField()
	created= models.DateField()
	updated= models.DateField()
	def __unicode__ (self):
		return self.title

class PostAdmin(admin.ModelAdmin):
	list_display= ('title','created','updated')
	search_fields= ('title','body')
	list_filter= ('created',)	

class Comment(models.Model):
	body= models.TextField()
	author= models.CharField(max_length=60)
	created= models.DateField()
	updated= models.DateField()
	def __unicode__ (self):
		return self.author

class CommentAdmin(admin.ModelAdmin):
	list_filter= ('created','author')
	search_fields= ('author','body') 
	list_display= ('author','created','updated')

class CommentInline(admin.TabularInline):
	model= Comment



admin.site.register(Post,PostAdmin)
admin.site.register(Comment,CommentAdmin)


