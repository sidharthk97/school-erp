from django.urls import path

from . import views
app_name='teacher'

urlpatterns=[
    path('home', views.teacher_home, name='teacher_home'),
    path('profile', views.teacher_profile, name='teacher_profile'),
    path('viewstudent', views.teacher_view_student, name='teacher_viewstudent'),
    path('attendance', views.teacher_add_attendance, name='teacher_attendance'),

]