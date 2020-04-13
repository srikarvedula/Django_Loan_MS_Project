# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#python manage.py inspectdb --database=mysql_db loan_table_lookup > webservices/model_loan_table_lookup.py
from django.db import models


class LoanTableLookup(models.Model):
    loan_mdm_lookup_id = models.IntegerField(primary_key=True)
    creditscoremin = models.IntegerField(db_column='CreditScoreMin', blank=True, null=True)  # Field name made lowercase.
    creditscoremax = models.IntegerField(db_column='CreditScoreMax', blank=True, null=True)  # Field name made lowercase.
    loanamountmin = models.IntegerField(db_column='LoanAmountMin', blank=True, null=True)  # Field name made lowercase.
    loanamountmax = models.IntegerField(db_column='LoanAmountMax', blank=True, null=True)  # Field name made lowercase.
    interestratepct = models.DecimalField(db_column='InterestRatePct', max_digits=4, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    durationmonths = models.IntegerField(db_column='DurationMonths', blank=True, null=True)  # Field name made lowercase.
    eff_from_date = models.DateField(blank=True, null=True)
    eff_to_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'loan_table_lookup'
