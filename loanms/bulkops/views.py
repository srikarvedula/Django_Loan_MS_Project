from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse
from mysql.connector import errors
import logging
from loanms.Connpool import getConn,db
import pymysql as sql

def upload_csv(request):
    data = {}
    getConn()
    if "GET" == request.method:
        return render(request, "upload_testing.html", data)
    try:
        csv_file = request.FILES["csv_file"]
        if not csv_file.name.endswith('.csv'):
            messages.error(request, 'File is not CSV type')
            return HttpResponseRedirect(reverse("bulkops:upload_csv"))
        if csv_file.multiple_chunks():
            messages.error(request, "Uploaded file is too big (%.2f MB)." % (csv_file.size / (1000 * 1000),))
            return HttpResponseRedirect(reverse("bulkops:upload_csv"))

        file_data = csv_file.read().decode("utf-8")
        new_file_data=[]
        lines = file_data.split("\n")
        for i in lines:
            list1=list(i.split(','))
            new_file_data.append(list1)
        conn = sql.connect(host='localhost', port=3306, user='root', password='Dirtydula1$', db='loan_proj')
        try:
            cursor = conn.cursor()
            sql_script = "INSERT INTO loan_table_lookup( loan_mdm_lookup_id, CreditScoreMin, CreditScoreMax, LoanAmountMin, LoanAmountMax, InterestRatePct, DurationMonths, eff_from_date, eff_to_date) VALUES"
            for row in new_file_data:
                row_str = row[0] + "," + row[1] + "," + row[2] + "," + row[3] + "," + row[4] + "," + row[5] + "," + row[6] + "," + "str_to_date('"+row[7]+"','%m/%d/%Y')" + "," + "str_to_date('"+row[8]+"','%m/%d/%Y')"
                print(sql_script + "(" + row_str + ");")
                cursor.execute(sql_script + "(" + row_str + ");")
            dict = {'completed': "The data has successfully been uploaded to MySQL database."}
            conn.commit()
        except errors.Error as e:
            print(e)
        finally:
            cursor.close()
        return render(request, 'upload_testing.html', context=dict)
    except Exception as e:
        logging.getLogger("error_logger").error("Unable to upload file. " + repr(e))
        messages.error(request, "Unable to upload file. " + repr(e))

    return HttpResponseRedirect(reverse("bulkops:upload_csv"))