from django.shortcuts import render, redirect
import pymysql
# Create your views here.
def print_report(request):
    conn = pymysql.connect(host='localhost', port=3306, user='root', password='Dirtydula1$', db='loan_proj')
    cursor = conn.cursor()
    cursor.execute("select * from loan_table_lookup;")
    l_data = []
    for loan_mdm_lookup_id, CreditScoreMin, CreditScoreMax, LoanAmountMin, LoanAmountMax, InterestRatePct, DurationMonths, eff_from_date, eff_to_date in cursor.fetchall():
        l_data.append({"loan_mdm_lookup_id": loan_mdm_lookup_id
                          , "CreditScoreMin": CreditScoreMin
                          , "CreditScoreMax": CreditScoreMax
                          , "LoanAmountMin": LoanAmountMin
                          , "LoanAmountMax": LoanAmountMax
                          , "InterestRatePct": InterestRatePct
                          , "DurationMonths": DurationMonths
                          , "eff_from_date": eff_from_date
                          , "eff_to_date": eff_to_date})
    cursor.close()
    conn.close()
    return render(request,'mdm_report.html',{'l_data': l_data})