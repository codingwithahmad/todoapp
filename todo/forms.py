from django import forms
from .models import Note

class NoteForm(forms.ModelForm):
	class Meta:
		model = Note
		fields = "__all__"
		time = forms.DateTimeField(
        input_formats=['%d/%m/%Y %H:%M'],
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control datetimepicker-input',
            'data-target': '#datetimepicker1'
        })
    )