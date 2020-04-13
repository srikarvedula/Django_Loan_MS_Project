from django import forms

class CustomerForm(forms.Form):
    customer_name=forms.CharField()
    CreditScore=forms.IntegerField()
    LoanAmount=forms.IntegerField()