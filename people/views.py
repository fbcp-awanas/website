from django.shortcuts import render
from django.http import HttpResponse
from .models import Child

def view_child(request, id):
    if id:
        child = Child.objects.get(id=id)
        name = child.full_name
    else:
        name = "No child specified"
    html = '<html><body>{}</body></html>'.format(name)
    return HttpResponse(html)

def view_children(request, data):
    # Return a list of all children
    pass