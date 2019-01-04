from django.shortcuts import render
from django.db.models import Q
from users.models import CustomUser
from django.views.generic import TemplateView, DetailView, ListView
from users.models import CustomUser
from taggit.models import Tag
from functools import reduce

# Create your views here.

def search_users(request):
    if request.method == 'GET':
        query= request.GET.get('q')
        submitbutton= request.GET.get('submit')
        if query is not None:
            lookups = Q(skills__name__icontains=query) | Q(software_hardware__icontains=query)
            results = CustomUser.objects.filter(lookups).distinct()
            context={'results': results, 'submitbutton': submitbutton}
            return render(request, 'search.html', context)
        else:
            return render(request, 'search.html')
    else:
        return render(request, 'search.html')



 