from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import Blog
from .models import Ministry
from .models import GalleryImage


def home(request):
    return render(request, 'menonight/index.html')

def about(request):
    return render(request, 'menonight/about.html')

def events(request):
  
    return render(request, 'menonight/events.html')

def gallery(request):
    category = request.GET.get('category', 'all')

    if category == 'all':
        images = GalleryImage.objects.all().order_by('-id')
    else:
        images = GalleryImage.objects.filter(category=category).order_by('-id')

    paginator = Paginator(images, 8)  # 8 images per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'menonight/gallery.html', {
        'page_obj': page_obj,
        'selected_category': category,
    })

def prayer_request(request):
    return render(request, 'menonight/prayer_request.html')

# blog posts
def blog(request):
    post_list = Blog.objects.all().order_by('-created_at')  # newest first
    paginator = Paginator(post_list, 6)  # 6 posts per page

    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)

    # Create compact pagination range
    current_page = posts.number
    total_pages = paginator.num_pages

    if total_pages <= 7:
        page_range = range(1, total_pages + 1)
    else:
        if current_page <= 4:
            page_range = list(range(1, 6)) + ['...', total_pages]
        elif current_page >= total_pages - 3:
            page_range = [1, '...'] + list(range(total_pages - 4, total_pages + 1))
        else:
            page_range = [1, '...'] + list(range(current_page - 1, current_page + 2)) + ['...', total_pages]

    return render(request, 'menonight/blog.html', {'posts': posts, 'page_range': page_range})

def blog_detail(request, pk):
    post = get_object_or_404(Blog, pk=pk)
    return render(request, 'menonight/blog_detail.html', {'post': post})



def contact(request):
    return render(request, 'menonight/contact.html')

def donate(request):
    return render(request, 'menonight/donate.html')

def membership(request):
    return render(request, 'menonight/membership.html')

def ministries(request):
    ministries = Ministry.objects.all()
    return render(request, 'menonight/ministries.html', {'ministries': ministries})

def sermons(request):
    return render(request, 'menonight/sermons.html')

def testimonies(request):
    return render(request, 'menonight/testimonies.html')

def live_stream(request):
    return render(request, 'menonight/live_stream.html')

def visit(request):
    return render(request, 'menonight/visit.html')