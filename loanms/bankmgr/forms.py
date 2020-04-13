from django import forms

class AddRecordForm(forms.Form):
    loan_mdm_lookup_id=forms.IntegerField()
    CreditScoreMin=forms.IntegerField()
    CreditScoreMax=forms.IntegerField()
    LoanAmountMin=forms.IntegerField()
    LoanAmountMax=forms.IntegerField()
    InterestRatePct=forms.IntegerField()
    DurationMonths=forms.IntegerField()
    eff_from_date=forms.DateField()
    eff_to_date=forms.DateField()
