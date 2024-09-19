from django.shortcuts import render

# Create your views here.

from .forms import UserRegister
from .models import Buyer, Game


def platform_view(request):
    return render(request, 'first_task/platform.html')


def games_view(request):
    context = {'games': Game.objects.all()}
    return render(request, 'first_task/games.html', context)


def cart_view(request):
    return render(request, 'first_task/cart.html')


ACCEPTABLE_AGE = 18


def data_verification(username, password, repeat_password, age):
    answer = {}
    buyers = Buyer.objects.all()
    if list(buyers.filter(name=username)):
        answer['error'] = 'Пользователь уже существует'
    elif password != repeat_password:
        answer['error'] = 'Пароли не совпадают'
    elif age < ACCEPTABLE_AGE:
        answer['error'] = f'Вы должны быть старше {ACCEPTABLE_AGE}'
    else:
        answer['success'] = f'Приветствуем, {username}!'

    return answer


def sign_up_by_django(request):
    info = {}
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            repeat_password = form.cleaned_data["repeat_password"]
            age = form.cleaned_data["age"]

            info = data_verification(username, password, repeat_password, age)

            if 'success' in info:
                Buyer.objects.create(name=username, age=age, balance=0)
        else:
            form = UserRegister()
            info['form'] = form
        return render(request, 'first_task/registration_page.html', context=info)

    return render(request, 'first_task/registration_page.html', context=info)  # если это GET запрос, то выводим форму
