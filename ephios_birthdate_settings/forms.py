from django import forms

class BirthdateForm(forms.Form):
    birthdate = forms.DateField(
        label='Geburtstag',
        widget=forms.DateInput(attrs={'type': 'date'}),
    )