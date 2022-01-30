from django import forms

class DateForm(forms.Form):
    date1 = forms.DateField(input_formats=['%d/%m/%Y'], label='Date')
    date2 = forms.DateField(input_formats=['%d/%m/%Y'], label='Until')