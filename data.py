name = "rajan"
age = 23 
is_student = True 


marks = int(input("Enter your marks: " ))

if marks >= 90 :
  print("A+")
elif marks >=80 and marks < 90 :
  print("B+") 
elif marks >= 60 and marks < 80 : 
  print("C+") 
elif marks >= 33 and marks < 60 : 
  print("D")
else: 
  print("fail") 
