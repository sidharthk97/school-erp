from django.shortcuts import render

# Create your views here.

def sa_home(request):
    return render(request,'school_admin_templates/home.html')

def sa_view_student(request):
    return render(request,'school_admin_templates/viewstudent.html')

def sa_add_student(request):
    return render(request,'school_admin_templates/addstudent.html')

def sa_view_attendance(request):
    return render(request,'school_admin_templates/attendance.html')