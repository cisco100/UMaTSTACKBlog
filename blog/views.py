from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.http import HttpResponse
from blog.forms import CommentForm
from django.template.loader import get_template
from blog.models import Post, Category
from xhtml2pdf import pisa
from django.http import HttpResponse
import feedparser
from django.template.loader import get_template


def feed_view(request):
    feed=feedparser.parse(reverse('post_feed'))
    entries=feed.entries
    return render(request,'main/feed.html',{'entries':entries})



def home_view(request):
	posts = Post.objects.filter(status=Post.ACTIVE)
	return render(request,'main/home.html',{"posts":posts})


def robots_txt(request):
    text = [
        "User-Agent: *",
        "Disallow: /admin/",
    ]
    return HttpResponse("\n".join(text), content_type="text/plain")















def detail(request, category_slug, slug):
    post = get_object_or_404(Post, slug=slug, status=Post.ACTIVE)

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

            return redirect('post_detail', category_slug=category_slug,slug=slug)
    else:
        form = CommentForm()

    return render(request, 'main/detail.html', {'post': post, 'form': form})

def category(request, slug):
    categorys = get_object_or_404(Category, slug=slug)
    posts = categorys.posts.filter(status=Post.ACTIVE)

    return render(request, 'main/category.html', {'categorys': categorys, 'posts': posts})



def search(request):
    query = request.GET.get('query', '')

    posts = Post.objects.filter(status=Post.ACTIVE).filter(Q(title__icontains=query) | Q(intro__icontains=query) | Q(body__icontains=query) | Q(author__icontains=query))

    return render(request, 'main/search.html', {'posts': posts, 'query': query})