from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url="/login/")
def receipes(request):
    if request.method == "POST":    
        data = request.POST
        receipe_name = data.get("receipe_name")
        receipe_description = data.get("receipe_description")
        # receipe_image = request.FILES["receipe_image"] 
        receipe_image = request.FILES.get("receipe_image")

        Receipe.objects.create(
            receipe_name = receipe_name,
            receipe_description = receipe_description,
            receipe_image = receipe_image,

        )
        return redirect('receipes')
    querryset = Receipe.objects.all()

    if request.GET.get('search'):
        search = request.GET.get('search')
        querryset = querryset.filter(receipe_name__icontains = search)
    context = {
        'receipes':querryset
    }

    return render(request,"receipes.html",context)

@login_required(login_url="/login/")
def update_receipe(request,id):
    queryset = Receipe.objects.get(id=id)
    if request.method== "POST":
        data = request.POST
        receipe_name = data.get("receipe_name")
        receipe_description = data.get("receipe_description")
        receipe_image = request.FILES.get("receipe_image")


        queryset.receipe_name = receipe_name
        queryset.receipe_description = receipe_description
        if receipe_image:
            queryset.receipe_image = request.FILES.get("receipe_image")
        
        queryset.save()
        return redirect('receipes')
    context = {
        'receipe':queryset
    }
    return render(request,'update_receipe.html',context)

@login_required(login_url="/login/")
def delete_receipe(request,id):
    querryset = Receipe.objects.get(id=id)
    querryset.delete()
    return redirect('receipes')

def amazone_view(request):
    return render(request,"amazone.html")

def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username = username).exists():
            messages.error(request,"Invalid Username")
            return redirect('/login/')
        
        user=authenticate(username=username ,password= password)

        if user is None:
            messages.error(request,'Invalid Password')
            return redirect('/login')
        else:
            login(request,user)
            return redirect('/receipes/')

    return render(request,'login.html')

def logout_page(request):
    logout(request)
    return redirect('/login/')

def register_page(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('email_id')
        password = request.POST.get('password')

        user = User.objects.filter(username=username)

        if user.exists():
            messages.info(request,"Username already taken")
            return redirect('/register/')

        user = User.objects.create(
            first_name =first_name,
            last_name=last_name,
            username=username,
            # password=password,

        )

        user.set_password(password)
        user.save()
        messages.info(request,"Account created")

        messages.info(request,"Accoubt create sucessfully")
    return render(request,'register.html')

from django.core.paginator import Paginator
from django.db.models import Q,Sum

def get_student(request):
    queryset=Student.objects.all()

    if request.GET.get('search'):
        search = request.GET.get('search')
        print(search)
        queryset = queryset.filter(
            Q(student_name__icontains = search) |
            
            Q(student_id__student_id =search)
        )


    paginator = Paginator(queryset, 25)
  
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj':page_obj,
    }

    return render(request,"report\student.html",context)

def see_marks(request,id):
    queryset = SubjectMarks.objects.filter(student__student_id__student_id = id)
    print(queryset)
    total_marks = queryset.aggregate(total_marks = Sum('marks'))
    context = {
        "queryset":queryset,
        "total_marks":total_marks,
    }

    return render(request,"report\see_marks.html",context)