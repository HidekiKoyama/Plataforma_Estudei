from django.contrib.auth.models import User
from django.shortcuts import render
from .models import courses

def add_friend(request):
    if request.method == 'POST':
        return render(request, 'system/add_friend_system.html')
    else:
        list_users = User.objects.filter(is_superuser=False).exclude(username=request.user)
        return render(request, 'system/add_friend_system.html', {'list_users': list_users})
    
def list_courses(request):
    list_curses = courses.objects.all()
    return render(request, 'system/rank_dos_cursos.html', {'list_curses': list_curses})

def profile_user(request):
    load_user = User.objects.filter(username=request.user)
    return render(request, 'system/profile_user_system.html', {'oload_user': load_user})

def add_friend(request  ):
    load_user = User.objects.filter(username=request.user)
    return render(request, 'system/profile_user_system.html', {'oload_user': load_user})