<<<<<<< HEAD
from dataclasses import fields
from pyexpat import model
from socket import fromshare
from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):
    class Meta:
        model= Todo
        fields= "__all__"
=======
from django import forms
from django.forms import fields
from .models import Todo


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = "__all__"
>>>>>>> ed2e2a13759283a08493e70a597620f42af54b99
