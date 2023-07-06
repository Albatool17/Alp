# Example code 1

number = 7
#target
print("I have thought of a number between 1 and 10")
#print statement to tell us to choose 
guess = int(input("Can you guess what it is?"))
#choose an integer from 1 to 10
if guess == number:
  print("Correct!")
# if the guess is equal to the number the print will be given as an answer
elif guess < number:
  print("Too Low!")
# if the guess is smaller than the number the print will be give as an answer
else:
  print("Too High!")
#any number else it will be to high

# Example code 2

number1 = int(input("Please enter a number"))
#to choose an integer
number2 = int(input("Please enter another number"))
# choose an integer
if number1 > number2:
  print("Number 1 is bigger than number 2")
  # if  number1 is larger than 2 than this statement will be given as an answer
elif number2 > number1: 
  print("Number 2 is bigger than number 1")
  # if  number2 is larger than 1 than this statement will be given as an answer
else:
  print("Both numbers are the same")
  
any number else it will be the same
