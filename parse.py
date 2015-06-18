import pyodbc
import mylog

list=list()
try:
	cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=10.1.35.19;DATABASE=REGLAM;UID=du;PWD=53du')
	cursor = cnxn.cursor()
	cursor.execute("select date, pv from RVPROSTOI order by date")
	rows = cursor.fetchall()
	for row in rows:
		list.append({"date":row.date,"pv":row.pv})
except Exception(e):
	print("Бяда: "+str(e))
finally:
	mylog.log("Загрузил из БД "+str(len(list)))

f2 = open('./fileO/rv_prostoi.txt', 'w')
f2.write("date_rvpr pv_rvpr\n")
for index in list:
	f2.write(str(index['date'])+" "+str(index['pv'])+"\n")	
f2.close()
mylog.log("Сформировал файл")