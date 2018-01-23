from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import NewsPost
# Create your views here.


def newsPostList(request):
    """Renders list of all NewsPost's object, has a pagination"""
    news_post_list = NewsPost.objects.order_by('-pub_date')[::-1]
    paginator = Paginator(news_post_list, 10)
    page = request.GET.get('page')
    try:
        current_news_post_list = paginator.page(page)
    except PageNotAnInteger:
        current_news_post_list = paginator.page(1)
    except EmptyPage:
        current_news_post_list = paginator.page(paginator.num_pages)
    num_pages = range(1, paginator.num_pages+1)
    context = {
            'news_post_list': current_news_post_list,
            'num_pages': num_pages
    }
    return render(request, "news/list.html", context)


def newsPost(request, news_post_id):
    """Renders specific NewsPost"""
    news_post = get_object_or_404(NewsPost, pk=news_post_id)
    context = { 'news_post': news_post, }
    return render(request, "news/post.html", context)
