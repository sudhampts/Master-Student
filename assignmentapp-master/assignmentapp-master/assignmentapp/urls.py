from django.urls import path

from assignmentapp import views

urlpatterns = [
    #redirecting urls
    path('',views.home,name='home'),
    path('slogin',views.stud_login,name='slog'),
    path('sregister',views.stud_register,name='sreg'),
    path('mlogin',views.master_login,name='mlog'),
    path('mregister',views.master_register,name='mreg'),
    path('taskview',views.task_view,name='taskview'),
    path('taskassign',views.task_assign,name='taskassign'),
    #redirecting urls end here

    path('readslogin',views.read_student_login),
    path('readmlogin',views.read_master_login),
    path('readsdata',views.read_student_register),
    path('readmdata',views.read_master_register),
    path('createtask',views.create_task),
    path('log_out',views.log_out,name='log_out'),

    path('solve/<int:id>',views.solve,name='solve' )




    ]