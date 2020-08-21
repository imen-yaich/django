from django.shortcuts import render
import pandas as pd 
from pandas import DataFrame
import sqlite3
import sys
import MySQLdb
def index(request):
	connection = MySQLdb.connect(host = "172.17.0.2",
                             user = "imen",
                             passwd = "imen",
                             db = "test")

	crsr = connection.cursor()
	crsr.execute("SELECT * FROM table_name ;")
	rowss = crsr.fetchall()
	crsr.execute("SELECT COUNT(*) FROM table_name ;")
	#row = pd.DataFrame(crsr.fetchall())
	#row.columns = resoverall.keys()
	t = crsr.fetchall()
	print (t)
	row = list( rowss )
	for r in row:
		print(r[0])
	i = "ahmed"
        
	return render(request,'index.html',{'row':row,'i':i} )
