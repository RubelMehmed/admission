from django.http import HttpResponse
from django.shortcuts import redirect, render

from .forms import *
from .models import *
from .models import Applicant

# Create your views here.

#----------------home page----------------#


def home(request):
    return render(request, 'home.html', {})


# -------------------> course details page

def course(request):
    return render(request, 'course.html', {})


def course_list(request):
    course_list = Course.objects.all()
    return render(request, 'course_list.html', {
        'course_list': course_list
    })


def contact(request):
    return render(request, 'contact.html', {})


def about(request):
    return render(request, 'about.html', {})


def approved(request):
    return render(request, 'approved.html', {})


def admit_form(request):
    return render(request, 'admit_form.html', {})


def admit(request):
    return render(request, 'admit.html', {})


def apply(request):
    return render(request, 'apply.html', {})


# ------------------>input data funcction for user input
def input_data(request):
    if request.method == 'POST':
        form = ApplicantForm(request.POST)
        if form.is_valid():
            applicant = form.save(commit=False)
            applicant.save()
            return redirect('data_display')
    else:
        form = ApplicantForm()
    return render(request, 'input_data.html', {'form': form})


# =============================>query db for  data-display & pass it to the ui/template:
# -------------<as per admin selection>------------------------------------------------


def data_display(request):
    data = Applicant.objects.filter(show=True)
    return render(request, 'data_display.html', {'data': data})


# ------------>Apply Custom permissions to the view


def update(request):
    if request.method == "POST":
        # match_obj = Applicant.objects.get(id=id)
        aForm = ApplicantForm(request.POST)
        if aForm.is_valid():
            aForm.save()
            return redirect(data_display)
        else:
            return redirect(HttpResponse('Error'))


# def remove(request, id):
#     var = Teacher.objects.get(id=id)
#     var.delete()
#     return redirect('home')


# def addnew(request):
#     varForm = TeacherForm()
#     return render(request, "addnew.html", {"TeacherForm": varForm})


# def update(request, id):
#     if request.method == "POST":
#         tForm = TeacherForm(request.POST)
#         if tForm.is_valid():
#             tForm.save()
#             return redirect(home)
#         else:
#             return redirect(HttpResponse('Error'))


# def edit(request, id):
#     match_obj = Teacher.objects.get(id=id)
#     tForm = TeacherForm(instance=match_obj)
#     return render(request, "edit.html", {"tForm": tForm, "match_obj": match_obj})
