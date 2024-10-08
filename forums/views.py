from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Forum, Post, User
# Create your views here.
share_forum_id = None

def index(request):
    print("*** in forums.index)")
    if request.user.is_authenticated:
        user_id = request.user.id
    else:
        return redirect('/')

    if request.method == 'POST':
        # prepare forum data
       
        if 'postmsg' in request.POST:
            postmsg = request.POST['postmsg']
            print("*** postmsg=", postmsg)

        else:
            print("*** no value")
        if postmsg:
            Forum.objects.create(
                created_by = request.user,
                message = postmsg,
            )

    forums = Forum.objects.order_by('-created_at')
    context = {
                'forums': forums,
    }
   # print("*** FORUM=", forums[1].message, " size=", forums.__sizeof__)
    return render(request, 'forums/index.html', context)
    
    
def forums(request, forum_id):
    if request.user.is_authenticated:
        user_id = request.user.id
    else:
        return redirect('/')
    global share_forum_id
    print("***in forums: id=", forum_id)
    forum = get_object_or_404(Forum, pk=forum_id)
    share_forum_id = forum_id
    post = Post.objects.order_by('-created_at').filter(forum_id=forum_id, posted_by_id=user_id)

    if post:
        context = {'forum':forum, 'post':post}
    else:
        context = {'forum':forum, 'post':{}}
    return render(request, 'forums/detail.html', context )


def search(request):
    queryset_list = Forum.objects.order_by('-created_at')
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(keywords__icontains=keywords)
            
    if 'title' in request.GET:
        title = request.GET['title']
        if title:
            queryset_list = queryset_list.filter(title__icontains=title)
            
    if 'message' in request.GET:
        message = request.GET['message']
        if message:
            queryset_list = queryset_list.filter(message__iexact=message)        


    context = {
        'forums': queryset_list,
        'total': len(queryset_list)
    }
    return render(request, 'forums/search.html', context)



def post(request):
    global share_forum_id
    print("### in forum:post ")
    # write record to Post
    context={}
    if request.user.is_authenticated:
        user_id = request.user.id
    else:
        return redirect('/')

    if request.method == 'POST':
        if 'postmsg' in request.POST:
            postmsg = request.POST['postmsg']
            print("*** postmsg=", postmsg)
        else:
            print("*** no value")
        if  share_forum_id:
            print("*** share_forum =", share_forum_id)

        obj_forum = Forum.objects.get(id=share_forum_id)
        obj_user = User.objects.get(id=user_id)
        post = Post(forum=obj_forum, posted_by=obj_user, content=postmsg)
        post.save()

        #update forum counter
        obj_forum.post_count += 1
        obj_forum.save()

#        if postmsg:
#            Post.objects.create(
#                forum = Forum,
#                posted_by = request.user,
#                content = postmsg,
#            )
#    post = Post.objects.order_by('-created_at')
#    context = {
#                'post': post,
#    }
#    return render(request, 'forums/detail.html', context)
    forum = get_object_or_404(Forum, pk=share_forum_id)
    post = Post.objects.order_by('-created_at').filter(forum_id=share_forum_id, posted_by_id=user_id)
    #post = get_object_or_404(Post, pk=forum_id)
    if post:
        context = {'forum':forum, 'post':post}
    else:
        context = {'forum':forum, 'post':{}}
    return render(request, 'forums/detail.html', context )

def add(request):
    context={}
    return render(request, 'forums/detail.html', context)