from email.mime import image
from django.shortcuts import render, redirect
from .models import College, Student
from django.contrib.auth import authenticate, login
from django.http import Http404


# Create your views here.
def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('reg')
        else:
            raise Http404("Bad Credentials")
            
    return render(request, "core/login.html")

def reg(request):
    college = College.objects.all()
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        phone =request.POST['phone']
        address = request.POST['address']
        division = request.POST['division']
        address = request.POST['address']
        date = request.POST['date']
        id = request.POST.get('col')
        college_name = College.objects.get(id=id)
        profile = request.FILES["image"]
        myuser = Student.objects.create(first_name=fname, last_name=lname, phone=phone, Address=address, college=college_name,division=division, date=date, image=profile )
        myuser.save()
 
        return redirect("idcard", myuser.id)

    return render(request, "core/reg.html", {
        "college":college
    })

def idcard(request, id):
    student = Student.objects.get(pk=id)
    return render(request, "core/make_id.html", {
        "first_name":student.first_name,
        "last_name":student.last_name,
        "phone":student.phone,
        "college":student.college,
        "Address": student.Address,
        "division": student.division,
        "date":student.date,
        "image": student.image
    })