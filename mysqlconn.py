from pymysql import *


try:
    conn=connect(host="localhost",user="root",password="computer",db="pythondb")
    try:
        cu=conn.cursor()
        name=input("please enter the name:")
        age=int(input("please enter the age:"))
        email=input("please enter the email:")
        cu.execute('''insert into student values('%s',%d,'%s')'''%(name,age,email))
        conn.commit()
        print("Data inserted successfully...")
        cu.close()
        conn.close()
    except:
        print("Data insertion Fail...")
except:
    print("server not connected.......")
