from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse
#from .models import Employee, Project, DocumentModel, LdProj, Subject
#from .forms import ProjectForm, LdProjForm #, SubjectForm, PageTypeForm, DocTypeForm, PageformatForm, DocumentModelForm, EmployeeForm, StatusDocForm, ActionForm #, LdProjForm, CotationForm
from django.contrib import messages

@login_required
def index(request):
    return render(request, 'rotine/index.html')

@login_required
def home(request):
    return render(request, 'rotine/home.html')

@login_required
def isa(request):
    return render(request, 'rotine/isa5-1.html')

@login_required
def calc_tension(request):
    return render(request, 'rotine/calc-tension.html')

