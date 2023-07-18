from django.http import HttpResponse
import datetime

from django.shortcuts import render
def home(request):
    isActive = True
    if request.method == "POST":
        check = request.POST.get("check")
        if check == "on":
            isActive = True
        else:
            isActive = False

    date=datetime.datetime.now()
    name = "John"
    list_of_programs = [
        "Python", 
        "Django", 
        "Flask"
        ]
    
    student = {
        'student_name': "John",
        'student_age': 20,
        'student_college': "ABC",
        'student_branch': "IT",
    }
    # return HttpResponse("<h1>Hello World</h1>" + str(date))
    data={
        'date': date,
        'isActive': isActive,
        'name': name,
        'list_of_programs': list_of_programs,
        'student': student
    }
    return render(request, "home.html", data)
def about(request):
    # return HttpResponse("<h1>About</h1>")
    return render(request, "about.html", {})

def services(request):
    # return HttpResponse("<h1>Services</h1>")
    return render(request, "services.html", {})