from pyexpat import model
from dataclasses import fields
from tkinter import Widget
from .models import candidate, recruiter, jobs
from django import forms

class CandidateRegisterForm(forms.ModelForm):
    class Meta:
        model = candidate
        fields = ('firstname','lastname','email','phonenumber','username','password')
        widgets = {
            'firstname':forms.TextInput(attrs={'class':'form-control'}),
            'lastname':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
            'phonenumber': forms.TextInput(attrs={'class': 'form-control'}),
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'password':forms.TextInput(attrs={'class':'form-control'}),
        }

class RecruiterRegisterForm(forms.ModelForm):
    class Meta:
        model = recruiter
        fields = ('companyname','companyaddress','email','phonenumber','username','password')
        widgets = {
            'companyname':forms.TextInput(attrs={'class':'form-control'}),
            'companyaddress':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
            'phonenumber': forms.TextInput(attrs={'class': 'form-control'}),
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'password':forms.TextInput(attrs={'class':'form-control'}),
        }

class JobListForm(forms.ModelForm):
    class Meta:
        model = jobs
        fields = ('jobtype','jobname','vacancies')
        widgets = {
            'jobtype':forms.TextInput(attrs={'class':'form-control'}),
            'jobname':forms.TextInput(attrs={'class':'form-control'}),
            'vacancies':forms.TextInput(attrs={'class':'form-control'}),
        }