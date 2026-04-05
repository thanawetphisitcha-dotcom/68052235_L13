from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from myapp.models import Person
from django.db.models import Q

# Create your views here.
def index(request):
    all_Person = Person.objects.all()

    query = request.GET.get('q')

    if query:
        all_Person = all_Person.filter(Q(name__icontains=query) | Q(age__icontains=query))

    return render(request,"index.html",{"all_person":all_Person})

def about(request):
    return render(request,"about.html")

def form(request):
    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")



        person = Person.objects.create(
            name=name,
            age=age
        )


        return redirect("/")
    else:


        return render(request, "form.html")
    
def edit(request, person_id):
    person = get_object_or_404(Person, pk=person_id)
    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")



        person = name=name,
        person = age=age
        person.save()
        


        return redirect("/")
    else:


        return render(request, "form.html")

def delete(request, person_id):
    person = get_object_or_404(Person, pk=person_id)
    person.delete()
    return redirect("/")