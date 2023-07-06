from django.shortcuts import render

class system_login():
    def index(request):
        return render(request, 'login/index.html')