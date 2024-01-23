from django import forms

class CalcIncomeForm(forms.Form):
    monney = forms.IntegerField()
    
