import mysql.connector
from tabulate import tabulate
import time 

con=mysql.connector.connect(host='localhost',user='root',password='JSkc11@*',database='dsce')


res=con.cursor()

def insert(id,name,deptname):
    sql='INSERT INTO students_details (regno,name,deptname) values (%s,%s,%s)'
    data=(id,name,deptname)
    res.execute(sql,data)
    con.commit()
  
    print('Inserted successfully')

def update(regno,name,deptname):
    data=(regno,name,deptname)
    sql='update students_details set name=%s,deptname=%s where regno=%s'
    res.execute(sql,data)
    con.commit()
    print('Update Successfully')
    


def select():
    sql='select * from students_details'
    res.execute(sql)
    result=res.fetchall()
    print(tabulate(result,headers=['regno','name','deptname']))
    

def delete(id):
    dt=(id,)
    sql='delete from student where ID=%s'
    res.execute(sql,dt)
    con.commit()
    print('Deleted successfully')

while True:
     
    print("""
          1)Insert data
          2)Update data
          3)Select data
          4)Delete data
          5)Exit
          """)
    
    choice=int(input('Enter the choice:'))
    if choice ==1:
        regno=input('Enter the regno:')
        name=input('Enter the name:')
        deptname=input('Enter the deptname:')
        insert(regno,name,deptname)

    elif choice ==2:
        regno=input('Enter the regno:')
        name=input('Enter the name:')
        deptname=input('Enter the deptname:')
        update(regno,name,deptname)
    elif choice ==3:
        select()

    elif choice ==4:
        id=int(input('Enter the Delete ID:'))
        delete(id)
    elif choice ==5:

        quit()
    else:
        print('Wrong Choice ,Try again')
