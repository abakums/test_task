from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import transaction
from django.shortcuts import render, redirect
from profiles.forms import UserProfileForm, UserForm


def home_page(request):
    # рендеринг пользователю начальной страницы сайта
    return render(request, 'home.html')


def log_out(request):
    # разлогинизация пользователя, выход из системы с последующим редиректом на стартовую страницу
    logout(request)
    return redirect('/')


@login_required(login_url='/')
@transaction.atomic
def add_info(request):
    # функция, выводящая форму для ввода информации о пользователе
    # или перенаправляющая на страницу профиля при повторной авторизации пользователя
    if request.method == 'POST':
        profile_form = UserProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if profile_form.is_valid():
            profile_form.save()
            request.user.first_name = request.POST['first_name']
            request.user.last_name = request.POST['last_name']
            request.user.save()
            messages.success(request, 'Успешное изменение профиля!')
            return redirect('/my_profile/')
        else:
            messages.error(request, 'Необходимо ввести корректные значения в поля формы!')
    elif request.user.profile.patronymic != "":
        return redirect('/my_profile/')
    else:
        profile_form = UserProfileForm(instance=request.user.profile)
    heading = "Пожалуйста, введите свои данные в форму ниже:"
    return render(request, 'data_input.html', {'profile_form': profile_form,
                                               'heading': heading})


@login_required(login_url='/')
def my_profile(request):
    # рендерит страницу с данными профиля пользователя, либо делает редирект на страницу для их заполнения
    if request.user.profile.patronymic != "":
        return render(request, 'profile.html')
    else:
        return redirect('/')


@login_required(login_url='/')
@transaction.atomic
def edit_profile(request):
    # метод для изменения информации о пользователе
    # используются две формы, которые отправляются на сервер одной кнопкой
    # одна форма для ввода поля 'email' экземпляров User, вторая - для изменения полей у экземпляров UserProfile
    if request.method == 'POST':
        profile_form = UserProfileForm(request.POST, request.FILES, instance=request.user.profile)
        user_form = UserForm(request.POST, request.FILES, instance=request.user)
        if profile_form.is_valid() and user_form.is_valid():
            profile_form.save()
            user_form.save()
            request.user.first_name = request.POST['first_name']
            request.user.last_name = request.POST['last_name']
            request.user.email = request.POST['email']
            request.user.save()
            messages.success(request, 'Успешное изменение профиля!')
            return redirect('/my_profile/')
        else:
            messages.error(request, 'Необходимо ввести корректные значения в поля формы!')
    else:
        profile_form = UserProfileForm(instance=request.user.profile)
        user_form = UserForm(instance=request.user)
    heading = "Здесь Вы можете изменить личную информацию профиля:"
    return render(request, 'data_input.html', {'profile_form': profile_form,
                                               'user_form': user_form,
                                               'heading': heading})


@login_required(login_url='/')
def all_users(request):
    # рендеринг страницы со вписком всех пользователей
    # для пользователей, не вводивших свои данные после регистрации - перенаправление на страницу для их ввода
    if request.user.profile.patronymic != '':
        users = User.objects.all()
        return render(request, 'all_users.html', {'users': users})
    else:
        return redirect('/add_info/')
