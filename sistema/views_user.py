from django.contrib.auth.models import User
from django.shortcuts import render
def add_friend(request):
    if request.method == 'POST':
        return render(request, 'system/add_friend_system.html')
    else:
        list_users = User.objects.filter(is_superuser=False, )
        return render(request, 'system/add_friend_system.html', {'list_users': list_users})