from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse
#from .models import Employee, Project, DocumentModel, LdProj, Subject
#from .forms import ProjectForm, LdProjForm #, SubjectForm, PageTypeForm, DocTypeForm, PageformatForm, DocumentModelForm, EmployeeForm, StatusDocForm, ActionForm #, LdProjForm, CotationForm
from django.contrib import messages


#@login_required
def home(request):
    return render(request, 'rotine/home.html')

#@login_required
def isa(request):
    return render(request, 'rotine/isa5-1.html')

#@login_required
def calc_tension(request):
    return render(request, 'rotine/calc-tension.html')

#@login_required
def name_inst(request):
    return render(request, 'rotine/name-inst.html')

#@login_required
def data_sheet(request):
    return render(request, 'rotine/data-sheet.html')

#@login_required
def construction(request):
    return render(request, 'rotine/construction.html')


def open_external_web(request):
    if request.method == 'POST':
        meu_valor = request.POST.get('read')
        print('>>>>>>>>>>>: ', meu_valor)
        return render(request, 'rotine/data-sheet.html')
        
    return render(request, 'rotine/data-sheet.html')


'''
def open_external_web(request):
    url_externa = "https://www.alldatasheet.com/view.jsp?Searchword=${text_data_sheet}`, '_blank'"  # Substitua isso pela URL externa que deseja abrir
    return redirect(url_externa)
'''


 