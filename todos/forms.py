from django import forms
from .models import todo


class TodoForm(forms.ModelForm):
    class Meta:
        model = todo
        fields = ['title','description']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'w-full bg-slate-700 border-2 border-slate-600 rounded-lg py-3 px-4 text-white focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-transparent transition duration-300'
            }),
            'description': forms.Textarea(attrs={
                'class': 'w-full bg-slate-700 border-2 border-slate-600 rounded-lg py-3 px-4 text-white focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-transparent transition duration-300',
                'rows': 3
            }),
        }