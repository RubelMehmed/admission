from django import forms
from .models import *


# class ApplicantForm(forms.Form):
#     applicant_id = forms.IntegerField()
#     name = forms.CharField(label='Name', max_length=100)
#     father_name = forms.CharField(label='Father Name', max_length=100)
#     district = forms.CharField(label='District', max_length=100)
#     email = forms.EmailField(label='Email')
#     father_contact = forms.CharField(label='Father Contact', max_length=100)
#     selected_course = forms.CharField(label='Selected Course', max_length=100)

class ApplicantForm(forms.ModelForm):
    class Meta:
        model = Applicant
        fields = '__all__'
