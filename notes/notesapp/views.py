from django.shortcuts import redirect, render  # yahan par import redirect

from django.http import HttpResponse
from .models import Note

# Create your views here.

def home(request):
    return HttpResponse("Hello to Notes App")

def note_list(request):
    notes = Note.objects.all()
    return render(request, "note_list.html", {"notes": notes})

#{"notes": notes} means when we connect the python variables to html file
#left side "notes" mens used in html and right side notes means in python
# if i remove this the loop in html file will not work


def add_note(request):
    notes = Note.objects.all()
    if request.method =="POST":
        
        content = request.POST.get("content")
        title = request.POST.get("title")

        if title and content:
            Note.objects.create(title=title, content=content)
            return redirect("/notes/")   # ✅ redirect after save
    return render(request,"add_note.html",{"notes": notes})
    