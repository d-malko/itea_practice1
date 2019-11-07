from django.shortcuts import render
from .models import Post, Comment


def post_list(request):
    ctx = {}
    ctx['post_list'] = Post.objects.all()
    return render(request, 'blog/post_list.html', ctx)


def post_detail(request, slug):
    ctx = {}
    post = Post.objects.filter(slug=slug).first()
    # category = get_object_or_404(Category, pk=pk)
    if post:
        ctx['post'] = post.title.title()
        ctx['comment_list'] = post.comment_set.all()
    return render(request, 'blog/post.html', ctx)
