# Starter Code

number = 5
print("I have thought of a number between 1 and 10")
guess = int(input("Can you guess what it is?"))


if guess < number:
  print("Too Low!")
if guess > number:
  print("Too High!")

#the print function will ask for a number that will have to be inserted if the number is higher than the target (5) then too high! will be printed, nd if the number is lower than the target than too low will be printed