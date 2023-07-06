'''
Task - Which Room?
----------------------

Write a program that asks the user for their name and which subject they are studying.
The program should output a message telling the student by name which room to go to for that class (make up the room numbers if you need to).  You should include at least 3 subjects and have a message such as 'I don't know which room that class is in' for any you don't include.
 Example - an input of 'Ben' and 'Computing' might get an output of 'Hi Ben, go to room 401 for Computing'


You may use any method taught in class that is appropriate for this task. There is room for interpretation.

'''
#Start coding below
name=int(input("what's your name? "))

subject=int(input("what's your subject? "))

if subject=="computing":
 print("Hi"+name+", " + "go to room 1")

elif subject=="Art":
 print("Hi"+name+", " + "go to room 2")

elif subject=="Science":
 print("Hi"+name+", " + "go to room 3")

else:
  print("I don't know which room that class is in")

