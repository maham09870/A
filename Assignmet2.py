print("<=====Question:1====")
print("Twinkel twinkel little star")
print("\tHow i wonder what you are")
print("\t\t\tUp above the once so high")
print("\t\t\tlike a diamond in the sky")
print("Twinkel twinkel little star")
print("\tHow i wonder what you are\n")

print("<=========Question:2==============>\n")
import sys
python_version= sys.version
print("python version:",python_version)
print("<=====Question:3======>")
import datetime

print("current date and time",datetime.datetime.now())
print("<====Question:4==>")

radius=int((input("enter the radius:\n")))
area=3.142*(radius*radius)
print(area)
print("<====Question:5===>")
firstname=input("enter your first name:\n")
lastname=input("enter your last name:\n")
# reversed_string=firstname[::-1]+' '+lastname[::-1]

print(lastname+" "+firstname)

print("<=====Question:6===>")
first_num=int(input("enter your first number"))
second_num=int(input("enter your second number"))
add=first_num+second_num
print("your result is" ,add)


print("<===Question:7=====>\n")
Eng =int(input("Subject 1:")) 
Maths=int(input("Subject 2:"))
Isl=int(input("Subject 3:"))
comp=int(input("Subject 4:"))
urdu=int(input("Subject 5:"))


total =500
Obt=Eng+Maths+Isl+comp+urdu
percentage = (Obt/total)*100
print ( percentage)
if   percentage < 100 and percentage >= 80:
     print("A+ passed")
elif percentage < 80 and percentage >=70:
     print("A passed")
elif percentage < 70 and percentage >= 60:
     print ("B passed")
elif percentage <= 60 and percentage >= 50:
     print ("C passed")
else:
     print ("failed")


print("<==========3==Quserion:8========>")
x=int(input("enter the number"))
if x%2==0:
    print("given number is even")
else:
    print("given number is odd")