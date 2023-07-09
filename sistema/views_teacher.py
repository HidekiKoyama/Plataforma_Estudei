from django.shortcuts import render
from .db_connection import ConectionDB
from .scriptSQL import RequestSQL


def add_courses(request):
    conn = ConectionDB(); query = RequestSQL()
    if request.method != 'POST':
        return_data = conn.connConsulta(query.requestCategorieCourses())
        return render(request, 'system/add_courses_system.html', {'return_data': return_data})
    else:
        name = request.POST.get('name-course')
        description = request.POST.get('desc_categorie')
        categorie = request.POST.get('categorie_course')
        user_log = request.user
        conn.connAlter(query.insertCourses(name, description, categorie, user_log))

        return_data = conn.connConsulta(query.requestCategorieCourses())
        return render(request, 'system/add_courses_system.html', {'return_data': return_data})
