from django.shortcuts import render
from .models import categorie_curses

def home_admin(request):
    return render (request, 'sytem_admin/admin_main_control.html')


def cad_categories_curse(request):  
    buttom_click = request.POST.get('buttom')
    
    if request.method == 'GET':
        return_data = categorie_curses.objects.all()
        return render (request, 'system_admin/curses_categories_add.html', {'return_data': return_data})
    elif request.method == 'POST' and buttom_click == 'buttom_save_categorie':
        new_curse = categorie_curses()
        new_curse.name = request.POST.get('name_categorie')
        new_curse.description = request.POST.get('desc_categorie')
        new_curse.save_base()
        return_data = categorie_curses.objects.all()
        return render (request, 'system_admin/curses_categories_add.html', {'return_data': return_data})
    else: 
        print("deu ruim meu nobre")
        return render(request, 'login/index.html')

def delete_categories_curse(request, id):      
    if request.method == 'POST':
        categorie_curses.objects.filter(id=id).delete()
        return_data = categorie_curses.objects.all()
        return render (request, 'system_admin/curses_categories_add.html', {'return_data': return_data})
    else: 
        print("deu ruim meu nobre")
        return render(request, 'login/index.html')
    
def update_cad_categories_curse(request, id):
        if request.method == 'POST':
            up_name = request.POST.get('name_categorie')
            up_desc = request.POST.get('desc_categorie')
            update_cad_categories = categorie_curses.objects.filter(id=id).update(name=up_name, description=up_desc)
            return_data = categorie_curses.objects.all()
            return render (request, 'system_admin/curses_categories_add.html', {'return_data': return_data})
        else:
            update_cad_categories = categorie_curses.objects.filter(id=id)
            return render (request, 'system_admin/update_curses_categories_add.html', {'update_cad_categories': update_cad_categories})