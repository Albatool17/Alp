# Example code 1

# Add comments to each line to say whehter it is inside or outside the loop and what it does.

# Explain the circumstances in which the loop will run.

print("What is the capital of France?")
# not a part of the loop asks a question
answer = input() 
# not a part  of the loop in lets an answer placed
while answer != "Paris":
  # part of the loop , is that is what it's answered then a print statement will be given
  print("Incorrect! Try again.")
  # part of the loop the print statemnt
  answer = input("What is the capital of France?")
#part of the loop repeats question because the answer is wrong
print("Correct!")
# not a part of the loop tells wether the answer is correct or wrong
# Example code 2

counter = 1
#target
while counter < 5:
  #condition
  
  print("This code is inside the loop")
  #print statement
  counter += 1