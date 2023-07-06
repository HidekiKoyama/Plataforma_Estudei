from django.shortcuts import render
from .models import categorie_curses
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .db_connection import conn_bd


class admin_space():
    def home_admin(request):
        return render(request, 'sytem_admin/admin_main_control.html')

    def cad_categories_curse(request):
        buttom_click = request.POST.get('buttom')

        if request.method == 'GET':
            return_data = conn_bd.conn('SELECT name, description FROM sistema_categorie_curses')
            return render(request, 'system_admin/curses_categories_add.html', {'return_data': return_data})
        elif request.method == 'POST' and buttom_click == 'buttom_save_categorie':
            new_curse_name = request.POST.get('name_categorie')
            new_curse_description = request.POST.get('desc_categorie')
            conn_bd.conn('INSERT INTO sistema_categorie_courses () VALUES ()')

            return_data = conn_bd.conn('SELECT name, description FROM sistema_categorie_curses')
            return render(request, 'system_admin/curses_categories_add.html', {'return_data': return_data})
        else:
            print("deu ruim meu nobre")
            return render(request, 'login/index.html')

    @login_required
    def delete_categories_curse(request, id):
        if request.method == 'POST':
            
            return render(request, 'system_admin/curses_categories_add.html', {'return_data': return_data})
        else:

            return_data = categorie_curses.objects.all()
            return render(request, 'system_admin/curses_categories_add.html', {'return_data': return_data})

    @login_required
    def update_cad_categories_curse(request, id):
        if request.method == 'POST':
            up_name = request.POST.get('name_categorie')
            up_desc = request.POST.get('desc_categorie')
            update_cad_categories = categorie_curses.objects.filter(
                id=id).update(name=up_name, description=up_desc)
            return_data = categorie_curses.objects.all()
            return render(request, 'system_admin/curses_categories_add.html', {'return_data': return_data})
        else:
            update_cad_categories = categorie_curses.objects.filter(id=id)
            return render(request, 'system_admin/update_curses_categories_add.html', {'update_cad_categories': update_cad_categories})

    @login_required
    def control_user(request):
        if request.method == 'GET':
            list_users = User.objects.all()
            return render(request, 'system_admin/admin_crud_users.html', {'list_users': list_users})
        else:
            list_users = User.objects.all()
            return render(request, 'system_admin/admin_crud_users.html', {'list_users': list_users})

    '''    elif request.method == 'POST' and request.POST.get('button') == 'delete':
            delete_who = User.objects.filter(id=id)
            delete_who.delete()
            list_users = User.objects.all()
            return render (request, 'system_admin/admin_crud_users.html', {'list_users': list_users})'''
