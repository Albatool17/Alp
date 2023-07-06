# Example Code 1

def say_hi():
  print("Why hello there!")
#define for subroutine

def offer_drink():
  print("Would you care for a spot of tea?")
#define for subroutine

def offer_food():
  print("Biscuit?")
#define for subroutine

def say_bye():
  print("Cheerio then.")
#define for subroutine

offer_drink()
say_hi()
offer_food()
# calls function name

# Example code 2
def maths1():
  num1 = 50
  num2 = 5
  return num1 + num2
#defines maths1 and return solves equation

def maths2():
  num1 = 50
  num2 = 5
  return num1 - num2
#defines maths2 and return solves equation

def maths3():
  num1 = 50
  num2 = 5
  return num1 * num2
#defines maths3 and return solves equation

outputNum = maths2()
print(outputNum)
#calls function name (math2) the equation will be printed solved
# Example Code 3

def location(country):
  print("I am from " + country)
# defines location

location("Brazil")
#calls the location and printing it to the sentence that has been written