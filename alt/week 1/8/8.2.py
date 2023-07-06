'''
Answer the questions

'''

# Example code:

names = ["Alex","Anita","Patrick","Atif","Sue"]

print("Enter a number for your choice.")
print("1. Show all")
print("2. Add name")
print("3. Show name")
print("4. Exit")
choice = int(input())

if choice == 1:
  print(names)
elif choice == 2:
  name = input("Enter the name")
  names.append(name)
elif choice == 3:
  print("Enter the index of the name")
  index = int(input())
  print(names[index])
else:
  print("Goodbye")


# What is the identifier for the list in this program?
  # Answer: from line 10 to 15

# What would happen if you choose option “3” and entered index “0”? 
  # Answer: alex will show up

# What would happen if you choose option “3” and entered index “7”?
  # Answer: you will get an error

# What would happen if you choose option “2” and entered the name “Stuart”?
  # Answer: the name will be added

# What is the purpose of int(input()) on line 10 ?
  #: the user will choose a numberr from the identifiers

