from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from assignmentapp.models import Student, Master, Task


def home(request):
    return render(request, 'index.html')


def stud_login(request):
    return render(request, 'student_login.html')


def stud_register(request):
    return render(request, 'student_registration.html')


def master_login(request):
    return render(request, 'master_login.html')


def master_register(request):
    return render(request, 'master_registration.html')


def task_view(request):
    tasks = Task.objects.all()
    return render(request, 'task_list.html', {'data': tasks})


def task_assign(request):
    students  = Student.objects.all()
    return render(request, 'assgin_task.html',{'data':students})


def read_student_login(request):
    userName = request.POST['tbsusername']
    userPassword = request.POST['tbspassword']
    if Student.objects.filter(Q(UserNAme=userName) & Q(Password=userPassword)).exists():
        return render(request, 'student_dash.html')
    else:
        return render(request, 'slogin.html')


def read_master_login(request):
    userName = request.POST['tbmusername']
    userPassword = request.POST['tbmpassword']
    if Master.objects.filter(Q(UserNAme=userName) & Q(Password=userPassword)).exists():
        return render(request, 'master_dash.html')
    else:
        return render(request, 'master_login.html')


def read_student_register(request):
    if request.method == 'POST':
        username = request.POST['tbsusername']
        name = request.POST['tbname']
        password = request.POST['tbspassword']
        if Student.objects.filter(Q(UserNAme=username) | Q(Password=password)).exists():
            return render(request, 'student_registration.html')
        else:
            s1 = Student()
            s1.Name = name
            s1.UserNAme = username
            s1.Password = password
            s1.save()
            return render(request, 'student_login.html', {'data': ''})


def read_master_register(request):
    if request.method == 'POST':
        username = request.POST['tbmusername']
        name = request.POST['tbmname']
        password = request.POST['tbmpassword']
        if Master.objects.filter(Q(UserNAme=username) | Q(Password=password)).exists():
            return render(request, 'master_registration.html')
        else:
            s1 = Master()
            s1.Name = name
            s1.UserNAme = username
            s1.Password = password
            s1.save()
            return render(request, 'master_login.html', {'data': ''})


def log_out(request):
    return redirect('home')


def create_task(request):
    t1 = Task()
    t1.Left = request.POST['left']
    t1.Right = request.POST['right']
    t1.Operator = request.POST['operators']
    t1.Student_id = Student.objects.get(Name=request.POST['ddlstudent'])
    t1.save()
    tasks = Task.objects.all()
    return render(request, 'task_list.html', {'data': tasks})


def solve(request,id):
    t1 = Task.objects.get(id=id)
    left = t1.Left
    left = globals()[left]
    right = t1.Right
    right = globals()[right]
    op = t1.Operator
    op = globals()[op]
    print(left,right)

    res = left(op(right()))
    t1.Complete = True
    return  render(request,'task_list.html',{'sol': f'solution is{res}','data':Task.objects.all()})


def make_num(num,func):
    if func == None:
        return num
    else:
        return func(num)


def zero(func= None):
    return make_num(0,func)


def one(func= None):
    return make_num(1,func)


def two(func= None):
    return make_num(2, func)


def three(func= None):
    return make_num(3,func)


def four(func= None):
    return make_num(4,func)


def five(func= None):
    return make_num(5,func)


def six(func= None):
    return make_num(6,func)


def seven(func = None):
    return make_num(7, func)


def eight(func=None):
    return make_num(8, func)

def nine(func= None):
    return make_num(9, func)

def times(right):
  sum = lambda left :  left * right
  return  sum

def plus(right):
  sum = lambda left :  left + right
  return  sum

def minus(right):
  sum = lambda left :  left - right
  return  sum

def divided_by(right):
  sum = lambda left :  left // right
  return  sum





