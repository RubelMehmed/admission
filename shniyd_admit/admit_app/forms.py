from django import forms
from .models import *


class ApplicantForm(forms.ModelForm):
    class Meta:
        model = Applicant
        fields = '__all__'
