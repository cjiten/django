from django.shortcuts import get_object_or_404, render
from .models import Category, Post, Web
from django.core.paginator import Paginator


# Create your views here.

def home(requst):
    Web1 = get_object_or_404(Web)
    Category2 = Category.objects.all()[0:6]
    data = {
        'Web1': Web1,
        'Category2': Category2
    }
    return render(requst, 'webpages/home.html', data)

def admitcard(requst):
    Web1 = get_object_or_404(Web)
    Category1 = Category.objects.filter(name='Admit Card')
    # set up pagination
    p = Paginator(Post.objects.order_by('-created_date'), 8)
    page = requst.GET.get('page')
    Post1 = p.get_page(page)
    data = {
        'Post1': Post1,
        'Web1': Web1,
        'Category1': Category1
    }
    return render(requst, 'webpages/post-page.html', data)
def answerkey(requst):
    Web1 = get_object_or_404(Web)
    Category1 = Category.objects.filter(name='Answer Key')
    # set up pagination
    p = Paginator(Post.objects.order_by('-created_date'), 8)
    page = requst.GET.get('page')
    Post1 = p.get_page(page)
    data = {
        'Post1': Post1,
        'Web1': Web1,
        'Category1': Category1
    }
    return render(requst, 'webpages/post-page.html', data)
def cutoffmarks(requst):
    Web1 = get_object_or_404(Web)
    Category1 = Category.objects.filter(name='Cut Off Marks')
    # set up pagination
    p = Paginator(Post.objects.order_by('-created_date'), 8)
    page = requst.GET.get('page')
    Post1 = p.get_page(page)
    data = {
        'Post1': Post1,
        'Web1': Web1,
        'Category1': Category1
    }
    return render(requst, 'webpages/post-page.html', data)

def latestjobs(requst):
    Web1 = get_object_or_404(Web)
    Category1 = Category.objects.filter(name='Latest Jobs')
    # set up pagination
    p = Paginator(Post.objects.order_by('-created_date'), 8)
    page = requst.GET.get('page')
    Post1 = p.get_page(page)
    data = {
        'Post1': Post1,
        'Web1': Web1,
        'Category1': Category1
    }
    return render(requst, 'webpages/post-page.html', data)

def result(requst):
    Web1 = get_object_or_404(Web)
    Category1 = Category.objects.filter(name='Result')
    # set up pagination
    p = Paginator(Post.objects.order_by('-created_date'), 8)
    page = requst.GET.get('page')
    Post1 = p.get_page(page)
    data = {
        'Post1': Post1,
        'Web1': Web1,
        'Category1': Category1
    }
    return render(requst, 'webpages/post-page.html', data)

def syllabus(requst):
    Web1 = get_object_or_404(Web)
    Category1 = Category.objects.filter(name='Syllabus')
    # set up pagination
    p = Paginator(Post.objects.order_by('-created_date'), 8)
    page = requst.GET.get('page')
    Post1 = p.get_page(page)
    data = {
        'Post1': Post1,
        'Web1': Web1,
        'Category1': Category1
    }
    return render(requst, 'webpages/post-page.html', data)

def pyqp(requst):
    Web1 = get_object_or_404(Web)
    Category1 = Category.objects.filter(name='Previous Year Question Papers')
    # set up pagination
    p = Paginator(Post.objects.order_by('-created_date'), 8)
    page = requst.GET.get('page')
    Post1 = p.get_page(page)
    data = {
        'Post1': Post1,
        'Web1': Web1,
        'Category1': Category1
    }
    return render(requst, 'webpages/post-page.html', data)

def resentpost(requst):
    Web1 = get_object_or_404(Web)
    Category1 = Category.objects.filter(name='Resent Post')
    # set up pagination
    p = Paginator(Post.objects.order_by('-created_date'), 8)
    page = requst.GET.get('page')
    Post1 = p.get_page(page)
    data = {
        'Post1': Post1,
        'Web1': Web1,
        'Category1': Category1
    }
    return render(requst, 'webpages/post-page.html', data)

def contact(requst):
    Web1 = get_object_or_404(Web)
    Category1 = Category.objects.filter(name='contact')
    # set up pagination
    p = Paginator(Post.objects.order_by('-created_date'), 8)
    page = requst.GET.get('page')
    Post1 = p.get_page(page)
    data = {
        'Post1': Post1,
        'Web1': Web1,
        'Category1': Category1
    }
    return render(requst, 'webpages/contact.html')

def category(requst):
    Web1 = get_object_or_404(Web)
    Category1 = Category.objects.filter(name='name')
    # set up name
    p = Paginator(Post.objects.order_by('-created_date'), 8)
    page = requst.GET.get('page')
    Post1 = p.get_page(page)
    data = {
        'Post1': Post1,
        'Web1': Web1,
        'Category1': Category1
    }
    return render(requst, 'webpages/category.html', data)

def slink(requst, slug, slugcat):
    Web1 = get_object_or_404(Web)
    lpost = get_object_or_404(Post, slug=slug)
    kpost = get_object_or_404(Category, cslug=slugcat)
    Post1 = Post.objects.order_by('?')
    data = {
        'lpost': lpost,
        'Web1': Web1,
        'kpost': kpost,
        'Post1': Post1,
    }
    return render(requst, 'webpages/single-post.html', data)

def shlink(requst, slug, slugcat):
    Web1 = get_object_or_404(Web)
    lpost = get_object_or_404(Post, slug=slug)
    kpost = get_object_or_404(Category, cslug=slugcat)
    data = {
        'lpost': lpost,
        'Web1': Web1,
        'kpost': kpost
    }
    return render(requst, 'webpages/single-post-hi.html', data)

def search(requst):
    Web1 = get_object_or_404(Web)
    Post2 = Post.objects.all()
    Category1 = Category.objects.order_by('name')
    Post1 = Post.objects.order_by('-modified_date')
    
    if 'keyword' in requst.GET:
        keyword = requst.GET['keyword']
        if keyword:
            Post1 = Post1.filter(name__icontains=keyword)

    data = {
        'Post1': Post1,
        'Post2': Post2,
        'Web1': Web1,
        'Category1': Category1,
    }
    return render(requst, 'webpages/search.html', data)

def sitemap(requst):
    Web1 = Web.objects.all()
    Post1 = Post.objects.all()
    Category1 = Category.objects.all()
    data = {
        'Post1': Post1,
        'Web1': Web1,
        'Category1': Category1
    }
    return render(requst, 'webpages/sitemap.xml', data)