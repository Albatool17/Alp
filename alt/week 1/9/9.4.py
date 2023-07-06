def add_c (num1, num2):
  return num1+num2

def subtract_c (num1, num2):
  return num1-num2

def mulitply_c (num1, num2):
  return num1*num2

def divide_c (num1, num2):
  return num1/num2

num1=int(input("insert a number "))
num2=int(input("insert a number "))



print("1. add")
print("2.subtract")
print("3.mulitply")
print("4.divide")

choice=input("choose an operation ")
if choice == "1" :
  ans=add_c(num1, num2)
  print(ans)

elif choice == "2":
  ans=subtract_c(num1, num2)
  print(ans)
elif choice == "3":
  ans=multiply_c(num1, num2)
  print(ans)
elif choice == "4":
  ans=divide_c(num1, num2)
  print(ans)
else:
  print("error")
