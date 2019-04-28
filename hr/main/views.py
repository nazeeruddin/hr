# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from .models import application

from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'index.html')


def main(request):
    First_Name = request.GET.get('firstname', False)
    Last_Name = request.GET.get('lastname', False)
    db_object = application(first_name=First_Name, last_name=Last_Name, status='0')
    db_object.save()
    return HttpResponse('Hi {},Application submitted successfully.'.format(First_Name))


def hr(request):
    context = {'name': 'nazeer'}
    status_from_url = request.GET.get('status', False)
    record_id = request.GET.get('id', False)
    if record_id is not False:
        ddd = application.objects.filter(id=record_id)[0]
        return render(request, 'details.html', {'app': ddd})
    if status_from_url == '1':
        all_applications = application.objects.filter(status='1').order_by('-id')
        return render(request, 'accepted.html', context={'todaymatch_list': all_applications})
    elif status_from_url == '2':
        all_applications = application.objects.filter(status='2').order_by('-id')
        return render(request, 'rejected.html', context={'todaymatch_list': all_applications})
    elif status_from_url == '0':
        all_applications = application.objects.filter(status='0').order_by('-id')
        return render(request, 'all.html', context={'todaymatch_list': all_applications})
    return render(request, 'main.html', context)


def accept(request):
    record_id = request.GET.get('id', False)
    application.objects.filter(id=record_id).update(status='1')
    return HttpResponse('Application Accepted. Check Accepted List')


def reject(request):
    record_id = request.GET.get('id', False)
    application.objects.filter(id=record_id).update(status='2')
    return HttpResponse('Application Rejected. Check Rejected List')


"""
from django.views import generic


class ApplicationListView(generic.ListView):
    model = application


class ApplicationDetailView(generic.DetailView):
    model = application



from django.shortcuts import get_object_or_404

def Todaymatch_detail_view(request, primary_key):
match = get_object_or_404(Todaymatch, pk=primary_key)
return render(request, 'cricket/todaymatch_detail.html', context={'match': match})"""
