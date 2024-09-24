from django.shortcuts import render

# Create your views here.
from django.core.paginator import Paginator
from .models import Demo


_global_per_page = 5


def demo_list(request):
    # получаем все посты
    posts = Demo.objects.order_by('id')

    global _global_per_page
    per_page = request.GET.get('per_page')
    if not per_page:
        per_page = _global_per_page
    else:
        _global_per_page = per_page

    # создаем пагинатор
    paginator = Paginator(posts, per_page)  # 10 постов на странице

    # получаем номер страницы, на которую переходит пользователь
    page_number = request.GET.get('page')

    # получаем посты для текущей страницы
    page_posts = paginator.get_page(page_number)

    print(type(paginator.num_pages))

    # передаем контекст в шаблон
    return render(request, 'homeworks/paginator.html',
                  {'page_posts': page_posts, 'per_page': per_page})
