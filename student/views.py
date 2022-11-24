from django.shortcuts import render

# Create your views here.


def student_home(request):
    return render(request,'student_templates/home.html')

def student_profile(request):
    return render(request,'student_templates/profile.html')

def student_password(request):
    return render(request,'student_templates/password.html')

def student_view_attendance(request):
    return render(request,'student_templates/attendance.html')