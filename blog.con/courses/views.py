from django.shortcuts import render
from.models import Blog
# Create your views here.
def blogg_list(request):
    bloggs = Blog.objects.all()
    context = {
        'bloggs': bloggs
    }
    
    return render(request, 'blogg.html',context)
