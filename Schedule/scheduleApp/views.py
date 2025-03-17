from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django import forms
from .models import Schedule, Group, Subject, Teacher  
from .forms import ScheduleForm 

class ScheduleFilterForm(forms.Form):
    group = forms.ModelChoiceField(
        queryset=Group.objects.all(),
        required=False,
        label="Группа",
        empty_label="Все группы"
    )
    day = forms.ChoiceField(
        choices=[('', 'Все дни')] + Schedule.day_shoices,
        required=False,
        label="День недели"
    )

def home(request):
    form = ScheduleFilterForm(request.GET or None)
    schedules = Schedule.objects.all().order_by('day', 'group__name')
    if form.is_valid():
        group = form.cleaned_data['group']
        day = form.cleaned_data['day']
        if group:
            schedules = schedules.filter(group=group)
        if day:
            schedules = schedules.filter(day=day)

    return render(request, 'home.html', {'schedules': schedules, 'form': form})

def login_teacher(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Вы успешно вошли в систему!")
            return redirect('home')
        else:
            messages.error(request, "Ошибка входа. Проверьте логин и пароль.")
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    messages.success(request, "Вы вышли из системы.")
    return redirect('home')

@login_required
def add_schedule(request):
    if request.method == 'POST':
        form = ScheduleForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Расписание добавлено!")
            return redirect('home')
    else:
        form = ScheduleForm()
    return render(request, 'add_schedule.html', {'form': form})

@login_required
def update_schedule(request, pk):
    schedule = get_object_or_404(Schedule, id=pk)

    if request.method == 'POST':
        form = ScheduleForm(request.POST, instance=schedule)
        if form.is_valid():
            form.save()
            messages.success(request, "Расписание успешно обновлено!")
            return redirect('home')
    else:
        form = ScheduleForm(instance=schedule)

    return render(request, 'update_schedule.html', {'form': form})

@login_required
def delete_schedule(request, pk):
    schedule = get_object_or_404(Schedule, id=pk) 
    schedule.delete()
    messages.success(request, "Расписание удалено!")
    return redirect('home')