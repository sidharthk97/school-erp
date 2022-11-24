from django.urls import path

from . import views
app_name='student'

urlpatterns=[
    path('home', views.student_home, name='student_home'),
    path('profile', views.student_profile, name='student_profile'),
    path('password', views.student_password, name='student_password'),
    path('attendance', views.student_view_attendance, name='student_attendance'),

]