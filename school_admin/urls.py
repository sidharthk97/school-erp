from django.urls import path

from . import views
app_name='school_admin'

urlpatterns=[
    path('home', views.sa_home, name='admin_home'),
    path('viewstudent', views.sa_view_student, name='admin_home'),
    path('addstudent', views.sa_add_student, name='admin_home'),
    path('attendance', views.sa_view_attendance, name='admin_home'),

]