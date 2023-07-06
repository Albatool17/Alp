'''
Task - Predict and Run
This task contains three code examples.

Look at each example , study it carefully. Write a prediction of what it will do when it runs. Your prediction should be added to the code as comments. You should use the key terms selection, condition and branch in your prediction.
'''

# Example code 1

age = 18 
 
if age > 18: 
 print("You are old enough to drive") 
#if the the digit written is greater than 18 then the text You are old enough to drive will be be given as an answer
# Example code 2

num1 = 1337 
 
if num1 == 10: 
  print("This text is output because the condition was true") 
else:
  print("This text is output because the condition was false") 
#from 1337 numbers a random one will be guessed if the answer is true than the first statement will show up otherwise its the other statement
# Example code 3

number = 5
print("I have thought of a number between 1 and 10")
guess = int(input("Can you guess what it is?"))

if guess == number:
  print("Correct!")
if guess < number:
  print("Too Low!")
if guess > number:
  print("Too High!")
it will guessing random number from 1- 10 and if you guessed the target right the first string will show up other than that the statements will show up depending wether your answer is higher or lower