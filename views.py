# Python Imports
from datetime import date

import json
from decimal import Decimal
from itertools import chain
from operator import attrgetter, index

# Django Imports
from django.contrib.auth import login
from django.shortcuts import render, redirect, get_object_or_404
from django.template import RequestContext
from django.views.generic.list import ListView
from django.views.generic import DetailView
from django.views import View, generic
from django.http import Http404
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.sessions.backends.db import SessionStore
from django.contrib import messages

# 3rd Party Imports
from rest_framework.response import Response

# App Imports

from bo.forms import *
from bo.views import genealogy_build, user_register
from account.models import *
from .forms import *
from shop.models import ShopOrder, Payments
from account.decorator import admin_required
from django.shortcuts import render, redirect
from .forms import AddLessons


# Create your views here.
def admin_session(request):
    s = SessionStore()
    admin_last_login = User.objects.get(id=1).last_login.second
    print(admin_last_login)
    s['admin_last_login'] = admin_last_login
    s.create()
    s.save()




@method_decorator([admin_required], name='dispatch')
class UserIdView(View):
    template_name = 'user.html'

    def get(self, request):
        return render(request, self.template_name)


@method_decorator([admin_required], name='dispatch')
class ManageSitingView(View):
    template_name = 'admin-manage-siting.html'

    def get(self, request):
        Siting_report = AddSiting.objects.all()
        context = {
            'report': lessons_report
        }
        return render(request, self.template_name, context=context)


@method_decorator([admin_required], name='dispatch')
class SitingAddView(View):
    template_name = 'admin-add-siting.html'

    def get(self, request):
        return render(request, self.template_name, {"res": True})

    def post(self, request):
        if request.method == "POST":
            siting = Addsiting()
        animal = request.POST.get('animal')
        breed = request.POST.get('breed')

        siting, _ = AddSiting.objects.update_or_create(animal=animal,
                                                        breed=breed,
                                                        )
        siting.save()

        if _:
            context = {
                'submission': True,
                'message': "User Successfully Added "
            }
            return render(request, 'admin-distributor-success.html', context=context)
        else:
            context = {
                'submission': False,
                'message': " Submission Failed"
            }
            return render(request, self.template_name, context=context)


class SitingEditView(View):
    template_name = "admin-edit-lessons.html"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def get(self, request, **kwargs):
        _id = kwargs.get('id')
        request.session['id'] = siting_id
        siting_obj = AddSiting.objects.get(id=siting_id)
        context = {
            'siting_get': siting_obj
        }
        return render(request, self.template_name, context=context)

    def post(self, request, id):
        siting_obj = AddSiting.objects.get(id=id)
        if request.method == "POST":
            animal = request.POST.get('animal')
            breed = request.POST.get('breed')

            siting_obj.animal = animal
            siting_obj.breed = breed


            siting_obj.save()

        return redirect("office:manage_siting")
        context = {
            'siting_get': siting_obj
        }
        return render(request, self.template_name, context=context)


class SitingDeleteView(View):

    def get(self, request, id):
        Siting_obj = AddSiting.objects.get(id=id)
        Siting_obj.delete()

        return redirect("office:manage_siting")
        context = {
            'siting_get': siting_obj
        }
        return render(request, self.template_name, context=context)
