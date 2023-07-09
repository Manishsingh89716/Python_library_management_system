#Task 3(Golden Project):- Library management system

#import mysql.connector module which connects to the mysql server.

import mysql.connector

#create database for library management
db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "libmanagement"
)

#create function & sql queries for inserting the books into the table
def addbook():
    bname = input("Enter book name: ")
    bcode = input("Enter book code:")
    total = input("Total books:")
    sub = input("Enter subject:")
    data = (bname,bcode,total,sub)
    sql = "insert into book_list(bname,bcode,total,subject) values(%s,%s,%s,%s)"
    c = db.cursor()
    c.execute(sql,data)
    db.commit()
    print(".............")
    print("Data entered successfully")
    main()

#create function & sql queries for issuing the books
def issueb():
    name = input("Enter name:")
    rno  = input("Enter rno:")
    code = input("Enter book code:")
    date = input("Enter date:")
    sql  = "insert into book_issue(name,regno,bcode,idate) values(%s,%s,%s,%s)"
    data =(name,rno,code,date)
    c = db.cursor()
    c.execute(sql,data)
    db.commit()
    print("...............")
    print("Book issued to :",name)
    main()
    bookup(code,-1)

#create function & sql queries for the submission of books
def submitb():
    name = input("Enter name:")
    regno  = input("Enter rno:")
    code = input("Enter book code:")
    sdate = input("Enter date:")
    sql = "insert into book_submit(name,regno,bcode,sdate) values(%s,%s,%s,%s)"
    data = (name,regno,code,sdate)
    c = db.cursor()
    c.execute(sql,data)
    db.commit()
    print("...............")
    print("Book submitted from :",name)
    bookup(code,1)

#create function & sql queries for the updation of table after changes
def bookup(co,u):
    sql = "select TOTAL from book_list where BCODE = %s"
    data = (co,)
    c = db.cursor()
    c.execute(sql,data)
    myresult = c.fetchone()
    t = myresult[0] + u
    sql = "update book_list set TOTAL = %s where BCODE = %s"
    d = (t,co)
    c.execute(sql,d)
    db.commit()
    main()

#create function & sql queries for the deletion of books
def dbook():
    ac = input("Enter book code:")
    sql = "delete from book_list where BCODE = %s"
    data = (ac,)
    c = db.cursor()
    c.execute(sql,data)
    db.commit()
    main()

#create function & sql queries for displaying of books or whole schema
def dispbook():
    sql = "select * from book_list"
    c = db.cursor()
    c.execute(sql)
    myresult = c.fetchall()
    for i in myresult:
        print("Book name:",i[0])
        print("Book code:",i[1])
        print("Total:",i[2])
        print("................")
    main()

#create function for choices i.e. add book, issue book, submit book, delete book, display book
def main():
    print("""........LIBRARY MANAGEMENT........
    1.Add book
    2.Issue book
    3.Submit book
    4.Delete book
    5.Display book
    """)

#to make the choices(if choice is 1:- task is to add book)
#if choice is 2:- task is to issue book)
#if choice is 3:- task is to submit book)
#if choice is 4:- task is to delete book
#if choice is 5:- task is to display book
#if choice is none of given, then print 'wrong choice'

    choice = input("Enter task no:")
    print("............................")
    if(choice == '1'):
        addbook()
    elif(choice == '2'):
        issueb()
    elif(choice == '3'):
        submitb()
    elif(choice == '4'):
        dbook()
    elif(choice == '5'):
        dispbook()
    else:
        print("wrong choice")
        main()

#create function for password and user name
def password():
    import random
    ps = random.randint(0,1000)
    user = input("Enter Username: ")
    print("Your password is:",ps)
    verify = input("Enter password:")

#if entered password is correct, then move to next step and if wrong then not
    if verify == str(ps):
        main()
    else:
        verify != str(ps)
        print("wrong password")
        password()
password()

