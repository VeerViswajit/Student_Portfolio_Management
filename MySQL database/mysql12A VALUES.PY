import mysql.connector
mydb=mysql.connector.connect(host="localhost",user='root',passwd='',database='PROJECT')
mycursor=mydb.cursor()
mycursor.execute("INSERT INTO 12A VALUES('1','ARYAN','S01',93,95,84,92,NULL,95,459)")
mycursor.execute("INSERT INTO 12A VALUES('2','BALA','S02',90,96,87,93,NULL,90,456)")
mycursor.execute("INSERT INTO 12A VALUES('3','SHIRYA','S03',92,93,96,NULL,87,95,463)")
mydb.commit()
