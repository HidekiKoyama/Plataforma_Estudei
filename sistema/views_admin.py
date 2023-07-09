from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .db_connection import ConectionDB
from .scriptSQL import RequestSQL

class Conection():

    def __init__(self):
        self.conect = ConectionDB() 
        self.query = RequestSQL()

    def getConect(self):
        return self.conect
    
    def getQuery(self):
        return self.query

class Admin_space():

    def home_admin(request):
        return render(request, 'sytem_admin/admin_main_control.html')
    
    @login_required
    def cad_categories_curse(request):
        conn = Conection()

        buttom_click = request.POST.get('buttom')
        if request.method == 'GET':
            return_data = conn.getConect().connConsulta(conn.getQuery().requestCourses())
            return render(request, 'system_admin/curses_categories_add.html', {'return_data': return_data})
        
        elif request.method == 'POST' and buttom_click == 'buttom_save_categorie':
            new_name = request.POST.get('name_categorie'); new_description = request.POST.get('desc_categorie')
            conn.getConect().connAlter(conn.getQuery().insertCourses(new_name, new_description))
            return_data = conn.getConect().connConsulta(conn.getQuery().requestCourses())
            return render(request, 'system_admin/curses_categories_add.html', {'return_data': return_data})
        
        else:
            return render(request, 'login/index.html')

    @login_required
    def delete_categories_curse(request, id):
        conn = Conection()
        
        if request.method == 'POST':
            conn.getConect().connAlter(conn.getQuery().dellCourses(id))
            return_data = conn.getConect().connConsulta(conn.getQuery().requestCourses())
            return render(request, 'system_admin/curses_categories_add.html', {'return_data': return_data})
        
        else:
            return_data = conn.conect().connConsulta(conn.getQuery().requestCourses())
            return render(request, 'system_admin/curses_categories_add.html', {'return_data': return_data})

    @login_required
    def update_cad_categories_curse(request, id):
        conn = Conection()
        
        if request.method == 'POST':
            up_name = request.POST.get('name_categorie')
            up_desc = request.POST.get('desc_categorie')
            conn.getConect().connAlter(conn.getQuery().updateCourses(up_name, up_desc, id))
            return_data = conn.getConect().connConsulta(conn.getQuery().requestCourses())
            return render(request, 'system_admin/curses_categories_add.html', {'return_data': return_data})
        
        else:
            print('else')
            return_data = conn.getConect().connConsulta(conn.getQuery().filterCourses(id))
            return render(request, 'system_admin/update_curses_categories_add.html', {'return_data': return_data})

    @login_required
    def control_user(request):
        conn = Conection()

        list_users = conn.getConect().connConsulta(conn.getQuery().requestUser())
        return render(request, 'system_admin/admin_crud_users.html', {'list_users': list_users})