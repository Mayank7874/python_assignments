#1 display difference in date
from datetime import date
import time
import random
import numpy as np
import hashlib
import base64
today=datetime.now()
day=(int(input("\n Enter Day : ")))
mon=(int(input("\n Enter Month : ")))
year=(int(input("\n Enter Year : ")))
udate=datetime(year,mon,day)
diff=today-udate
print(diff)

# 2 Display time since epoch in hours and minutes

epoch= int(time.time())
print("\n Epoch time  : ",epoch)
minutes=int(epoch/60)
hours=int(minutes/60)
print("\n Minutes : ",minutes)
print("\n Hours : ",hours)


#3 Display your age in years, months and days

print("\n Enter your Birth date")
year=int(input("\n Year : "))
mon=int(input("\n Month : "))
day=int(input("\n Day : "))
bdate=date(year,mon,day)
current=date.today()
diff=current-bdate
t_mon=int(diff.days/30)
t_year=int(t_mon/12)
print(type(t_mon))
print("\n total approx days",diff.days)
print("\n total approx months ",t_mon)
print("\n total approx year ",t_year)

#4 Display trigonometric table of sin, cos and tan
angles_deg = np.array([0, 30, 45, 60, 90])
angles_rad = np.deg2rad(angles_deg)
sin_values = np.sin(angles_rad)
cos_values = np.cos(angles_rad)
tan_values = np.tan(angles_rad)
print("degrees \t radious \t sin \t cos \t tan")
print("-" * 55)

for i in range(len(angles_deg)):
    if angles_deg[i] == 90:
        tan_val = "Undefined"
    else:
        tan_val = f"{tan_values[i]:.4f}"
        
    print(f"{angles_deg[i]:<10}{angles_rad[i]:<15.4f}{sin_values[i]:<10.4f}{cos_values[i]:<10.4f}{tan_val:<10}")





#5 Generate 10 random numbers

for i in range(0,10):
    print("\n ",i+1,random.randint(-9999,9999))

#6 Authentication: Ask username, password and compare

uname=input("\n Enter usesrname : ")
upass=input("\n Enter password : ")
if(uname == "user123" and upass =="123@abc"):
    print("\n Welcome user123")
else:
    print("\n Wrong login information")

#7 Authentication: Ask username, password and compare with encryption

uname=hashlib.sha1("user1".encode()).hexdigest()
upass=hashlib.sha1("123a".encode()).hexdigest()
n_name=input("\n Enter usesrname : ")
n_pass=input("\n Enter password : ")
n_name=hashlib.sha1(n_name.encode()).hexdigest()
n_pass=hashlib.sha1(n_pass.encode()).hexdigest()
print(n_name)
print(uname)

if(uname==n_name and upass==n_pass):
    print("\n welcome user")
else:
    print("\n invalid user credencials")

#8) Authentication: Ask username, password and compare with hashing

user="jassi@123".encode()
passwd="js@abc".encode()
user=hashlib.md5(user).hexdigest()
passwd=hashlib.md5(passwd).hexdigest()
u_user=input("\n Enter username : ")
u_pass=input("\n Enter password : ")
u_user=hashlib.md5(u_user.encode()).hexdigest()
u_pass=hashlib.md5(u_pass.encode()).hexdigest()
if(user==u_user and passwd==u_pass):
    print("\n Welcome admin Jassi")
else:
    print("\n !!! Invalid user detail")


#9) Convert string "Hello$World" into Base64

st="Hello$World"
print("\n before Base64 ",st)
st=base64.b64encode(st.encode())
print("\n After encode : ",st)


#10) Code for String Manipulation 

st="jack of all, master of none"
print(st)
print("reversed",st[::-1])
print("upper case : ",st.upper())
print("capitalize : ",st.capitalize())
print("find 'of' position string : ",st.find("of"))
print("spllit words",st.split())
print("replace 'master' with 'blaster' :",st.replace("master","blaster"))
print("count 'e' : ",st.count('e'))





