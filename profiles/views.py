from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import transaction
from django.shortcuts import render, redirect
from profiles.forms import UserProfileForm, UserForm


def info_is_completed(user):
    # проверяет, заполнил ли пользователь все поля формы при вводе личной информации
    if user.first_name != "" and user.last_name != "" and user.profile.patronymic != "":
        return True


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
        user_form = UserForm(request.POST, request.FILES, instance=request.user)
        if profile_form.is_valid() and user_form.is_valid():
            profile_form.save()
            user_form.save()
            if info_is_completed(request.user):
                messages.success(request, 'Успешное изменение профиля!')
                return redirect('/my_profile/')
            else:
                messages.error(request, 'Необходимо ввести все поля формы')
        else:
            messages.error(request, 'Необходимо ввести корректные значения в поля формы!')
    elif info_is_completed(request.user):
        return redirect('/my_profile/')
    else:
        profile_form = UserProfileForm(instance=request.user.profile)
        user_form = UserForm(instance=request.user)
    heading = "Пожалуйста, введите все свои данные в форму ниже:"
    return render(request, 'data_input.html', {'profile_form': profile_form,
                                               'user_form': user_form,
                                               'heading': heading})


@login_required(login_url='/')
def my_profile(request):
    # рендерит страницу с данными профиля пользователя, либо делает редирект на страницу для их заполнения
    if info_is_completed(request.user):
        return render(request, 'profile.html')
    else:
        return redirect('/add_info/')


@login_required(login_url='/')
@transaction.atomic
def edit_profile(request):
    # метод для изменения информации о пользователе
    # используются две формы, которые отправляются на сервер одной кнопкой
    if request.method == 'POST':
        profile_form = UserProfileForm(request.POST, request.FILES, instance=request.user.profile)
        user_form = UserForm(request.POST, request.FILES, instance=request.user)
        if profile_form.is_valid() and user_form.is_valid():
            profile_form.save()
            user_form.save()
            if info_is_completed(request.user):
                messages.success(request, 'Успешное изменение профиля!')
                return redirect('/my_profile/')
            else:
                messages.error(request, 'Необходимо ввести все поля формы')
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
    if info_is_completed(request.user):
        users = User.objects.all()
        return render(request, 'all_users.html', {'users': users})
    else:
        return redirect('/add_info/')
