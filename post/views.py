from django.shortcuts import render,redirect 
from .forms import PostForm
from .models import Post
from dsuser.models import Dsuser
from tag.models import Tag

# Create your views here.
def post_write(request):
    if not request.session.get('user'):
        return redirect('/user/login')

    if request.method=='POST':
        form=PostForm(request.POST)
        if form.is_valid():
            user_id=request.session.get('user')
            dsuser=Dsuser.objects.get(pk=1)
            tags=form.cleaned_data['tags'].split(',')

            post=Post()
          
            post.contents=form.cleaned_data['contents']
            post.img_url=form.cleaned_data['img_url']
            post.name=dsuser
            post.save()

            for tag in tags:
                if not tag:
                    continue

                _tag,_=Tag.objects.get_or_create(name=tag)
                post.tag.add(_tag)

            return redirect('/post/list/')
    else:
        form=PostForm()

    return render(request,'post_write.html',{'form':form})