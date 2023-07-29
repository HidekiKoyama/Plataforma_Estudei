from django.contrib.auth.models import User
from django.shortcuts import render
from .views_admin import Conection


class FunctionsUser():
    def add_friend(request, id):
        conn = Conection()

        if request.method == 'POST':
            conn.getConect().connAlter(conn.getQuery().addFriend(request.user.id, id))
            list_users = conn.getConect().connConsulta(conn.getQuery().isFriend(request.user.id))
            return render(request, 'system/add_friend_system.html', {'list_users': list_users})
        else:
            list_users = conn.getConect().connConsulta(conn.getQuery().isFriend(request.user.id))
            return render(request, 'system/add_friend_system.html', {'list_users': list_users})

    def list_courses(request):
        conn = Conection()
        # after add "order by"
        list_curses = conn.getConect().connConsulta(conn.getQuery().rankCourses())
        return render(request, 'system/rank_dos_cursos.html', {'list_curses': list_curses})

    def profile_user(request):
        load_user = User.objects.filter(username=request.user)
        return render(request, 'system/profile_user_system.html', {'oload_user': load_user})