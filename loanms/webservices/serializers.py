from rest_framework import serializers
from .model_loan_table_lookup import LoanTableLookup

class LoanTableLookupSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanTableLookup
        fields = ('loan_mdm_lookup_id', 'creditscoremin', 'creditscoremax', 'loanamountmin','loanamountmax','interestratepct','durationmonths','eff_from_date','eff_to_date')