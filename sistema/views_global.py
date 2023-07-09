from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.hashers import make_password

class RequestGlobal():
    
    def index(request):
        return render(request, 'login/index.html')

    def cad_user(request):
        if request.method == 'GET':
            return render(request, 'login/cad_new_user.html')
        else:
            new_user = User()
            new_user.username = request.POST.get('user')
            new_user.password = make_password(request.POST.get('password'))
            new_user.save()
            login(request, new_user)
            return render(request, 'login/index.html')

    def login_is_valid (request):
        try:
            submit_user_name = request.POST.get('user')
            submit_user_password = request.POST.get('password')
            rec_user_tb = authenticate(request, username=submit_user_name, password=submit_user_password)
            login(request, rec_user_tb)
            if request.user.is_superuser:
                return render(request, 'system_admin/admin_main_control.html')
            else:
                return render(request, 'system/index_system.html')
        except:
            return render(request, 'login/index.html')