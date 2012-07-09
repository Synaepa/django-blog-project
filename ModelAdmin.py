class PostAdmin(admin.ModelAdmin):
	list_display= ('title','created','updated')
	search_fields= ('title','body')
	list_filter= ('created',)	

class CommentAdmin(admin.ModelAdmin):
	list_filter= ('created','author') 
	list_display= ('author','body(max_length=60)','created','updated')


class CommentInline(admin.TabularInline)
	model= Comment

class PostAdmin(admin.ModelAdmin)
	inlines= [CommentInline]
