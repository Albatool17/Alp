'''
Task - Investigate
Use comments to answer the investigate questions on the example code.

'''
# Example Code

number = 5
print("I have thought of a number between 1 and 10")
guess = int(input("Can you guess what it is?"))

if guess == number:
  print("Correct!")
if guess < number:
  print("Too Low!")
if guess > number:
  print("Too High!")

# What happens if you input the guess '2'?
  # Answer: the print too low will show up

# What happens if you input the guess '6'?
  # Answer: the print too high will show up

# What happens if you input the guess '5'?
  # Answer: the print correct! will show uo

# What happens if you input the guess '-5'?
  # Answer:the print too low will show up

# What happens if you input the guess '0'?
  # Answer: the print too low will show up

# What do the symbols '<' and '>' mean on lines 9 and 11?
  # Answer: < means the guess is lower than the target
#> means the guess is higher than the target

# What happens if you change line 5 to if guess = number: ?
  # Answer

# What do you notice about each line that FOLLOWS each IF statement?
  # Answer


