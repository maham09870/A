Eng = 67
Maths=90
Isl=80
total =300
Obt=Eng+Maths+Isl
percentage = (Obt/total)*100
print ( percentage)
if   percentage < 100 and percentage >= 80:
     print("A+ passed")
elif percentage < 80 and percentage >=70:
     print("A passed")
elif percentage < 70 and percentage > 60:
     print ("B passed")
elif percentage < 60 and percentage > 50:
     print ("C passed")
else:
     print ("failed")