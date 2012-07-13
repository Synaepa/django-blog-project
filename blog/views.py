# Create your views here.
"""
This code should be copied and pasted into your blog/views.py file before you begin working on it.
"""

from django.template import Context, loader
from django.http import HttpResponse
from models import Post, Comment 
from django.shortcuts import render_to_response

from django.forms import ModelForm
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect



def post_list(request):
    posts = Post.objects.all()
    t = loader.get_template('blog/post_list.html')
    c = Context({'posts':posts })
    return HttpResponse(t.render(c))


def post_detail(request, id, showComments=False):
    post = Post.objects.get(id = id)
    comments = post.comment_set.all()
    return render_to_response('blog/post_detail.html',{'post':post,'comments':comments})
    
    #print type(post_list)
    #print post_list
    #return HttpResponse('post_list')


 
def post_search(request, term):
    posts =Post.objects.filter(body__contains = term)
    return render_to_response('blog/post_search.html',{'post':posts,'term':term})

def home(request):
    return render_to_response('blog/base.html',{})

   # print 'it works'
    #return HttpResponse('hello world. Ete zene?') 
