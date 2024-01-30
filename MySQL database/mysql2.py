import mysql.connector

mydb= mysql.connector.connect(host='localhost',user='root',passwd='',database='project')
mycursor=mydb.cursor()
mycursor.execute("CREATE TABLE 12A( S_NO VARCHAR(3) NOT NULL,\
NAME VARCHAR(30) NOT NULL, ADMN_NO VARCHAR(10) PRIMARY KEY, PHYSICS  INTEGER(2) NOT NULL, \
CHEMISTRY INTEGER(3) NOT NULL,MATHS INTEGER(3) NOT NULL,CS INTEGER(3),BIOLOGY INTEGER(3),TOTAL INTEGER(5) NOT NULL)")
mycursor.execute("ALTER TABLE 12A CHANGE TOTAL ENGLISH INTEGER(3)")
mycursor.execute("ALTER TABLE 12A ADD(TOTAL INTEGER(5) NOT NULL)")
