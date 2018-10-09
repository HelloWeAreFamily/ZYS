from math import ceil

from django.shortcuts import render, redirect

from post.models import Post
# Create your views here.

# 创建帖子
def create_post(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        post = Post.objects.create(title=title,content=content)
        return redirect('/post/read/?post_id=%d'%post.id)
    else:
        return render(request,'create_post.html')

# 修改帖子
def edit_post(request):
    if request.method == 'POST':
        post_id = int(request.POST.get('post_id'))
        post = Post.objects.get(pk=post_id)
        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        post.save()
        return redirect('/post/read/?post_id=%d' % post.id)
    else:
        post_id = int(request.GET.get('post_id'))
        post = Post.objects.get(pk=post_id)
        return render(request,'edit_post.html',{'post':post})

# 读帖子
def read_post(request):
    post_id = int(request.GET.get('post_id'))
    post = Post.objects.get(pk=post_id)
    return render(request, 'read_post.html', {'post': post})

# 删除帖子
def delete_post(request):
    post_id = int(request.GET.get('post_id'))
    Post.objects.get(pk=post_id).delete()
    return redirect('/')

# 搜索功能
def search(request):
    keyword = request.POST.get('keyword')
    posts = Post.objects.filter(content__contains=keyword)
    return render(request, 'search.html', {'posts': posts})

# 分页
def post_list(request):
    page = int(request.GET.get('page', 1))  # 当前页码
    total = Post.objects.count()         # 帖子总数
    per_page = 10                        # 每页帖子数
    pages = ceil(total / per_page)       # 总页数

    start = (page - 1) * per_page  # 当前页开始的索引
    end = start + per_page         # 当前页结束的索引
    posts = Post.objects.all()[start:end]

    return render(request, 'post_list.html',
                  {'posts': posts, 'pages': range(pages)})
