from django import forms
from . models import todomodel
class todo_form(forms.ModelForm):
    class Meta:
        model=todomodel
        fields=['name','priority','date']