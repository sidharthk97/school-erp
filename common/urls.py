from django.urls import path

from . import views
app_name='common'

urlpatterns=[
    path('', views.common_home),
    path('teacherlogin', views.common_teacher, name='teacher_login'),
    path('studentlogin', views.common_student, name='student_login'),
    path('adminlogin', views.common_schooladmin, name='admin_login'),
    
]