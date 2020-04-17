from django.shortcuts import render, redirect
from loanms.Connpool import getConn,db
from .forms import CustomerForm
import pymysql as sql


l_data_show = []
def showTable():
    l_data_show.clear()
    conn = sql.connect(host='localhost', port=3306, user='root', password='Dirtydula1$', db='loan_proj')
    cursor = db.cursor()
    cursor.execute("select * from loan_table_lookup;")
    for loan_mdm_lookup_id, CreditScoreMin, CreditScoreMax, LoanAmountMin, LoanAmountMax, InterestRatePct, DurationMonths, eff_from_date, eff_to_date in cursor.fetchall():
        l_data_show.append({"loan_mdm_lookup_id": loan_mdm_lookup_id
                               , "CreditScoreMin": CreditScoreMin
                               , "CreditScoreMax": CreditScoreMax
                               , "LoanAmountMin": LoanAmountMin
                               , "LoanAmountMax": LoanAmountMax
                               , "InterestRatePct": InterestRatePct
                               , "DurationMonths": DurationMonths
                               , "eff_from_date": eff_from_date
                               , "eff_to_date": eff_to_date})
    master_data=tuple(l_data_show)
    cursor.close()
    return master_data

def show(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            return redirect('/selfserv/first/report')
    else:
        form = CustomerForm()
    return render(request, 'selfserv.html', {'form': form})

def getReport(request):
    master_dat = showTable()
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            cust_name = form.cleaned_data.get("customer_name")
            creditscore = form.cleaned_data.get("CreditScore")
            loanamount = form.cleaned_data.get("LoanAmount")
            resul=[]
            cust_info={'name':cust_name,'score':creditscore,'amount':loanamount}
            for l_data in master_dat:
                if creditscore >= l_data['CreditScoreMin'] and creditscore <= l_data['CreditScoreMax']:
                    if loanamount >= l_data['LoanAmountMin'] and loanamount <= l_data['LoanAmountMax']:
                        resul.append(l_data)
                elif creditscore< 100:
                    print("Loan has been rejected")
    else:
        form = CustomerForm()
    return render(request, 'customerreport.html',{'resul':resul,'cust_info':cust_info})