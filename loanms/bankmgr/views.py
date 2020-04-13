from django.shortcuts import render, redirect
from django.template import Template, Context, loader
from django.http import HttpResponse, JsonResponse
from mysql.connector import errors
from loanms.Connpool import getConn,db,db2,db3,db4
from .forms import AddRecordForm
import pymysql


conn = pymysql.connect(host='localhost', port=3306, user='root', password='Dirtydula1$', db='loan_proj')
l_data = {}
l_data_show=[]

def showTable():
    l_data_show.clear()
    getConn()
    cursor = conn.cursor()
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
    cursor.close()

def syncTableDict():
    getConn()
    cursor = conn.cursor()
    cursor.execute("select * from loan_table_lookup;")
    for loan_mdm_lookup_id, CreditScoreMin, CreditScoreMax, LoanAmountMin, LoanAmountMax, InterestRatePct, DurationMonths, eff_from_date, eff_to_date in cursor.fetchall():
        l_data[loan_mdm_lookup_id]={"loan_mdm_lookup_id": loan_mdm_lookup_id
                                    , "CreditScoreMin": CreditScoreMin
                                    , "CreditScoreMax": CreditScoreMax
                                    , "LoanAmountMin": LoanAmountMin
                                    , "LoanAmountMax": LoanAmountMax
                                    , "InterestRatePct": InterestRatePct
                                    , "DurationMonths": DurationMonths
                                    , "eff_from_date": eff_from_date
                                    , "eff_to_date": eff_to_date}
    cursor.close()

def show(request):
    showTable()
    return render(request, 'show.html', {'l_data_show': l_data_show})

def edit(request,loan_mdm_lookup_id):
    syncTableDict()
    SingleRowData = l_data[loan_mdm_lookup_id]
    return render(request, 'edit.html',SingleRowData)

def update(request):
    getConn()
    lookupid = request.POST["loan_mdm_lookup_id"]
    creditscoremin = request.POST["CreditScoreMin"]
    creditscoremax = request.POST["CreditScoreMax"]
    loanamtmin = request.POST["LoanAmountMin"]
    loanamtmax = request.POST["LoanAmountMax"]
    interestratepct = request.POST["InterestRatePct"]
    durationmonths = request.POST["DurationMonths"]
    efffromdate = request.POST["eff_from_date"]
    efftodate = request.POST["eff_to_date"]
    sql_update_query = """update   loan_table_lookup
                            set     loan_mdm_lookup_id = '"""+str(lookupid)+"""'
                                    , CreditScoreMin = '"""+str(creditscoremin)+"""'
                                    , CreditScoreMax = '"""+str(creditscoremax)+"""'
                                    , LoanAmountMin = '"""+str(loanamtmin)+"""'
                                    , LoanAmountMax = '"""+str(loanamtmax)+"""'
                                    , InterestRatePct = '"""+str(interestratepct)+"""'
                                    , DurationMonths = '"""+str(durationmonths)+"""'
                                    , eff_from_date = '"""+str(efffromdate)+"""'
                                    , eff_to_date = '"""+str(efftodate)+"""'
                            where loan_mdm_lookup_id = """ + str(lookupid) + ';'
    try:
        cursor = conn.cursor()
        print(sql_update_query)
        cursor.execute(sql_update_query)
        conn.commit()
    except errors.Error as e:
        print(e)
    finally:
        cursor.close()
    return redirect("http://127.0.0.1:8000/bankmgr/first/loanmdm")

def delete(request,loan_mdm_lookup_id):
    getConn()
    syncTableDict()
    try:
        cursor = conn.cursor()
        SingleRowData = l_data[loan_mdm_lookup_id]
        lookup_id = SingleRowData['loan_mdm_lookup_id']
        sql_delete_script='delete from loan_table_lookup where loan_mdm_lookup_id =' + str(lookup_id) + ';'
        print(sql_delete_script)
        cursor.execute(sql_delete_script)
        conn.commit()
    except errors.Error as e:
        print(e)
    finally:
        cursor.close()
    return redirect("/bankmgr/first/loanmdm")

def add_new_record(request):
    getConn()
    if request.method == 'POST':
        print("Add Row Form submit")
        form = AddRecordForm(request.POST)
        if form.is_valid():
            lookupid = form.cleaned_data.get("loan_mdm_lookup_id")
            creditscoremin = form.cleaned_data.get("CreditScoreMin")
            creditscoremax = form.cleaned_data.get("CreditScoreMax")
            loanamtmin = form.cleaned_data.get("LoanAmountMin")
            loanamtmax = form.cleaned_data.get("LoanAmountMax")
            interestratepct = form.cleaned_data.get("InterestRatePct")
            durationmonths = form.cleaned_data.get("DurationMonths")
            efffromdate = form.cleaned_data.get("eff_from_date")
            efftodate = form.cleaned_data.get("eff_to_date")
            try:
                cursor = conn.cursor()
                sql_script = 'insert into loan_table_lookup( loan_mdm_lookup_id, CreditScoreMin, CreditScoreMax, LoanAmountMin, LoanAmountMax, InterestRatePct, DurationMonths, eff_from_date, eff_to_date) VALUES'
                row_str = str(lookupid) + "," + str(creditscoremin) + "," + str(creditscoremax) + "," + str(loanamtmin) + "," + str(loanamtmax) + "," + str(interestratepct) + "," + str(durationmonths) + "," + "str_to_date('" + efffromdate.strftime('%m/%d/%Y') + "','%m/%d/%Y')" + "," + "str_to_date('" + efftodate.strftime('%m/%d/%Y') + "','%m/%d/%Y')"
                sql_insert_script = sql_script + "(" + row_str + ");"
                print(sql_insert_script)
                cursor.execute(sql_insert_script)
                conn.commit()
            except errors.Error as e:
                print(e)
            finally:
                cursor.close()
            return redirect('/bankmgr/first/loanmdm')
    else:
        form = AddRecordForm()
    return render(request, 'addform.html', {'form': form})