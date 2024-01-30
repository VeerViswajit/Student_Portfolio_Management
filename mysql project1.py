def menu():
    c='y'
    while c=='y':
        print('-'*165)
        print("\t\t\tMenu Choices")
        print("\t\t\t1.DISPLAY TABLES")
        print("\t\t\t2.DISPLAY RECORDS")
        print("\t\t\t3.DISPLAY AVERAGE MARKS")
        print("\t\t\t4.ADD RECORD")
        print("\t\t\t5.DELETE RECORD")
        print("\t\t\t6.UPDATE RECORD")
        print("\t\t\t7.EXIT")
        print('-'*165)
        ch=int(input("ENTER YOUR CHOICE: "))
        if ch==1:
            disp_tab()
        elif ch==2:
            disp_rec()
        elif ch==3:
            disp_avg()
        elif ch==4:
            add_rec()
        elif ch==5:
            del_rec()
        elif ch==6:
            upd_rec()
        elif ch==7:
            print("Exiting")
            break
        else:
            print("Enter correct choice")
        c=input("Do you want to continue(y/n): ")

def disp_tab():
    import mysql.connector
    try:
        mydb=mysql.connector.connect(host='localhost',user='root',passwd='',database='PROJECT')
        mc=mydb.cursor()
        mc.execute("SHOW TABLES")
        tab=mc.fetchall()
        for i in tab:
            print(i)
    except:
        print("Error unable to show tables")

def disp_rec():
    import mysql.connector
    try:
        mydb=mysql.connector.connect(host='localhost',user='root',passwd='',database='PROJECT')
        mc=mydb.cursor()
        a=input("ENTER THE TABLE TO BE DISPLAYED: ")
        mc.execute("SELECT * FROM  "+str(a))
        rec=mc.fetchall()
        for i in rec:
            print(i)
    except:
        print("ERROR:unable to display records")

def disp_avg():
    import mysql.connector
    try:
        mydb=mysql.connector.connect(host='localhost',user='root',passwd='',database='PROJECT')
        mc=mydb.cursor()
        mc.execute("SELECT AVG(TOTAL) FROM 12A")
        a1=mc.fetchall()
        print("CLASS AVERAGE OF12A: ",a1)
        mc.execute("SELECT AVG(TOTAL) FROM 12B")
        a2=mc.fetchall()
        print("CLASS AVERAGE OF 12B: ",a2)
    except:
        print("ERROR:unable to show average")

def add_rec():
    import mysql.connector
    try:
        mydb=mysql.connector.connect(host='localhost',user='root',passwd='',database='PROJECT')
        mc=mydb.cursor()
        c=input("Enter the class: ")
        record=eval(input("Enter The Record: "))
        if c=='12a':
            query= "INSERT INTO 12A  (S_NO, NAME, ADMN_NO, PHYSICS, CHEMISTRY, MATHS,CS, BIOLOGY, ENGLISH, TOTAL)VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            mc.execute(query, record)
            mydb.commit()
            print("Record successfully added")
        elif c=='12b':
            query= "INSERT INTO 12B (S_NO, NAME, ADMN_NO, PHYSICS, CHEMISTRY, MATHS,CS, BIOLOGY, ENGLISH, TOTAL)VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            mc.execute(query, record)
            mydb.commit()
            print("Record successfully added")
    except:
        print("ERROR:unable to add record")

def del_rec():
    import mysql.connector
    try:
        mydb=mysql.connector.connect(host='localhost',user='root',passwd='',database='PROJECT')
        mc=mydb.cursor()
        c=input("Enter the class: ")
        rec=input("Enter the admission number: ")
        if c=='12a':
            query= "DELETE FROM 12A WHERE ADMN_NO=  %s"
            mc.execute(query, (rec,))
            mydb.commit()
            print("Record sucessfully deleted")
        elif c=='12b':
            query1= " " "DELETE FROM 12B WHERE ADMN_NO= %s" " "
            mc.execute(query1, (rec,))
            mydb.commit()
            print("Record sucessfully deleted")
    except:
        print("ERROR:unable to delete record")

def upd_rec():
        import mysql.connector
        try:
            mydb=mysql.connector.connect(host='localhost',user='root',passwd='',database='PROJECT')
            mc=mydb.cursor()
            c=input("Enter the class: ")
            NO=input("Enter the admission number: ")
            change=input("Enter the change in which column: ")
            change1=eval(input("Enter the change in value: "))
            if c=='12a':
                if change=='NAME':
                    query="UPDATE 12A SET NAME=%s WHERE ADMN_NO=%s"
                    rec=(change1, NO)
                    mc.execute(query, rec)
                elif change=='PHYSICS':
                    total=int(input("Enter the change in total: "))
                    query="UPDATE 12A SET PHYSICS=%s, TOTAL=%s WHERE ADMN_NO=%s"
                    rec=(change1,total, NO)
                    mc.execute(query, rec)
                elif change=='CHEMISTRY':
                    total=int(input("Enter the change in total: "))
                    query="UPDATE 12A SET CHEMISTRY=%s, TOTAL=%s WHERE ADMN_NO=%s"
                    rec=(change1,total, NO)
                    mc.execute(query, rec)
                elif change=='MATHS':
                    total=int(input("Enter the change in total: "))
                    query="UPDATE 12A SET MATHS=%s, TOTAL=%s WHERE ADMN_NO=%s"
                    rec=(change1,total, NO)
                    mc.execute(query, rec)
                elif change=='CS':
                    total=int(input("Enter the change in total: "))
                    query="UPDATE 12A SET CS=%s, TOTAL=%s WHERE ADMN_NO=%s"
                    rec=(change1,total, NO)
                    mc.execute(query, rec)
                elif change=='BIOLOGY':
                    total=int(input("Enter the change in total: "))
                    query="UPDATE 12A SET BIOLOGY=%s, TOTAL=%s WHERE ADMN_NO=%s"
                    rec=(change1,total, NO)
                    mc.execute(query, rec)
                elif change=='ENGLISH':
                    total=int(input("Enter the change in total: "))
                    query="UPDATE 12A SET ENGLISH=%s, TOTAL=%s WHERE ADMN_NO=%s"
                    rec=(change1,total, NO)
                    mc.execute(query, rec)
            elif c=='12b':
                if change=='NAME':
                    query="UPDATE 12B SET NAME=%s WHERE ADMN_NO=%s"
                    rec=(change1, NO)
                    mc.execute(query, rec)
                elif change=='PHYSICS':
                    total=int(input("Enter the change in total: "))
                    query="UPDATE 12B SET PHYSICS=%s, TOTAL=%s WHERE ADMN_NO=%s"
                    rec=(change1,total, NO)
                    mc.execute(query, rec)
                elif change=='CHEMISTRY':
                    total=int(input("Enter the change in total: "))
                    query="UPDATE 12B SET CHEMISTRY=%s, TOTAL=%s WHERE ADMN_NO=%s"
                    rec=(change1,total, NO)
                    mc.execute(query, rec)
                elif change=='MATHS':
                    total=int(input("Enter the change in total: "))
                    query="UPDATE 12B SET MATHS=%s, TOTAL=%s WHERE ADMN_NO=%s"
                    rec=(change1,total, NO)
                    mc.execute(query, rec)
                elif change=='CS':
                    total=int(input("Enter the change in total: "))
                    query="UPDATE 12B SET CS=%s, TOTAL=%s WHERE ADMN_NO=%s"
                    rec=(change1,total, NO)
                    mc.execute(query, rec)
                elif change=='BIOLOGY':
                    total=int(input("Enter the change in total: "))
                    query="UPDATE 12B SET BIOLOGY=%s, TOTAL=%s WHERE ADMN_NO=%s"
                    rec=(change1,total, NO)
                    mc.execute(query, rec)
                elif change=='ENGLISH':
                    total=int(input("Enter the change in total: "))
                    query="UPDATE 12B SET ENGLISH=%s, TOTAL=%s WHERE ADMN_NO=%s"
                    rec=(change1,total, NO)
                    mc.execute(query, rec)
            mydb.commit()
            print("Record successfully updated")
        except:
            print("ERROR:unable to update record")

import pickle
dict1={'teacher1':'pass123','teacher2':'pass321'}
f=open('bin_project.dat','wb')
pickle.dump(dict1,f)
f.close()
def login():
    print("\t\t\tLogin Portal")
    username=input("Enter Username: ")
    password=input("Enter Password: ")
    dict2={username:password}
    if username=='teacher1':
        if dict1.get('teacher1')==dict2.get('teacher1'):
            print("login successful")
            menu()
        else:
            print("Incorrect password")
            login()
    elif username=='teacher2':
        if dict1.get('teacher2')==dict2.get('teacher2'):
            print("login successfull")
            menu()
        else:
            print("Incorrect password")
            login()
    else:
        print("Login unsuccessfull")
login()
                
                
                    
                    


        
        
        
    
   





































