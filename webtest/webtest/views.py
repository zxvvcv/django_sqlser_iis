from unittest import result
from django.shortcuts import render
from webtest.models import sqlserverconn
import pyodbc

def connsql(request):
    conn=pyodbc.connect('DRIVER={SQL Server};SERVER=DBSRV\AAI;DATABASE=AAI;UID=a5;PWD=1111')
    cursor=conn.cursor()
    cursor.execute("""
    DECLARE	@return_value int
    EXEC	@return_value = [dbo].[Proc_INVDataByY]
		    @yy = 2022

     SELECT	'Return Value' = @return_value
    
    
    """)
    result=cursor.fetchall()
    return render(request,'Index.html', {'sqlserverconn' : result})

def table2(request):
    return render(request, 'table2.html')


    