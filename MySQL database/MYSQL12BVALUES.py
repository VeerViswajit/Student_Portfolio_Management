import mysql.connector
mydb=mysql.connector.connect(host="localhost",user='root',passwd='',database='PROJECT')
mycursor=mydb.cursor()
mycursor.execute("INSERT INTO 12B VALUES('1','MICHAEL','S04',95,93,90,86,NULL,93,457)")
mycursor.execute("INSERT INTO 12B VALUES('2','SANTOSH','S05',86,96,89,NULL,93,96,460)")
mycursor.execute("INSERT INTO 12B VALUES('3','EMMA','S06',93,95,84,NULL,87,96,455)")
mydb.commit()
