import mysql.connector


from mysql.connector import errors
import time
db = mysql.connector.connect(user='root',
                                 password='yourpassword',
                                 host='127.0.0.1',
                                 database='loan_proj',
                                 pool_name='LoanDBConnPool',
                                 pool_size=10)

db2 = mysql.connector.connect(pool_name='LoanDBConnPool')
db3 = mysql.connector.connect(pool_name='LoanDBConnPool')
db4 = mysql.connector.connect(pool_name='LoanDBConnPool')
db5 = mysql.connector.connect(pool_name='LoanDBConnPool')
#pip install mysql-connector-python
def getConn():

    for i in range(7):
        if i ==6:

            #db2.close()
            pass
        try:
            db6=mysql.connector.connect(pool_name='LoanDBConnPool')
            return db6

        except mysql.connector.errors.PoolError:
            db2.close()
            print("Connection pool is maxed out")
            time.sleep(5)
        else:
            break
