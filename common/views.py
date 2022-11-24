from django.shortcuts import render

# Create your views here.


def common_home(request):
    return render(request,'common_templates/home.html')

def common_schooladmin(request):
    return render(request,'common_templates/schooladminlogin.html')

def common_teacher(request):
    return render(request,'common_templates/teacherlogin.html')

def common_student(request):
    return render(request,'common_templates/studentlogin.html')




