from django.shortcuts import render
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

class Teacher():

    def returnHand(request):
        conn = Conection()
        return_data = conn.getConect().connConsulta(conn.getQuery().requestCategorieCourses())
        return render(request, 'system/add_courses_system.html', {'return_data': return_data})

    def add_courses(request):
        conn = Conection()
        if request.method != 'POST':
            return Teacher.returnHand(request)
        else:
            name = request.POST.get('name-course')
            description = request.POST.get('desc_categorie')
            categorie = request.POST.get('categorie_course')
            user_log = request.user
            conn.getConect().connAlter(conn.getQuery().insertCourses(name, description, categorie, user_log))
            return Teacher.returnHand(request)