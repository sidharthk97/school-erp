from django.shortcuts import render

# Create your views here.


def teacher_home(request):
    return render(request,'teacher_templates/home.html')

def teacher_profile(request):
    return render(request,'teacher_templates/profile.html')

def teacher_view_student(request):
    return render(request,'teacher_templates/viewstudent.html')

def teacher_add_attendance(request):
    return render(request,'teacher_templates/attendance.html')