# Create your views here.
"""
This code should be copied and pasted into your blog/views.py file before you begin working on it.
"""

from django.template import Context, loader
from django.http import HttpResponse

from models import Post, Comment 
from django.shortcuts import render_to_response


def post_list(request):
    post_list = Post.objects.all()
    posts = Post.objects.all()
    t = loader.get_template('blog/post_list.html')
    c = Context({'posts':posts })
    return HttpResponse(t.render(c))

    
    print type(post_list)
    print post_list
    
    return HttpResponse('post_list')

def post_detail(request, id, showComments=False):
    pass
 
def post_search(request, term):
    pass
   
def home(request):
    return render_to_response('blog/base.html',{})

    print 'it works'
    return HttpResponse('hello world. Ete zene?') 
