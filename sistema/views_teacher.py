from django.shortcuts import render
from .models import categorie_curses, courses
import os


def add_courses(request):
    if request.method != 'POST':
        return_data = categorie_curses.objects.all()
        return render (request, 'system/add_courses_system.html', {'return_data': return_data})
    else:
        print(request.user)
        new_course_user_log = request.user
        new_course_name = request.POST.get('name-course')
        new_course_description = request.POST.get('desc_categorie')
        new_course_categorie = request.POST.get('categorie_course')
        new_cuerse_image = request.POST.get('banner-course')
        courses.objects.create(
                user_log=new_course_user_log,
                name=new_course_name,
                description =new_course_description, 
                categorie_couse=new_course_categorie, 
                image=new_cuerse_image).save_base()
        
        return_data = categorie_curses.objects.all()
        return render (request, 'system/add_courses_system.html', {'return_data': return_data})
