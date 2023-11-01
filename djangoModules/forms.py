from django import forms
from djangoModules.models import Student


class Wanafunzi(forms.Form):
    class Meta:
        model = Student
        fields = "all"
