# Program to calculate the area of a rectangle

# Get input for height & width. Convert to integers and store in variables

# Calculate the area & store the result in the area variable

# Output the area variable (converted to string)
height=int(input("enter a number: "))
width=int(input("enter a number: "))
area = height * width    
print(type(width))
print(str(height) + " multiply " + str(width) + " = " + str(area))
       

'''
Extra Challenges
Perimeter Calc
Create a program that allows the user to enter 2 numbers representing the width and length of a rectangle. The program calculates and displays the perimeter of the rectangle. 
Restaurant Tip Calculator 
Create a program that allows the user to enter the price of a meal at a restaurant. The program calculates the amount of the tip to be paid at 20%. The tip and total price are then displayed separately.
Volume and Surface Calc 
Create a program that allows the user to enter 3 numbers representing the height, width and length of a cuboid. The program calculates and displays the volume and total surface area of the cuboid. 
'''
#chanllenge 1
length=int(input("enter an number: "))
width=int(input("enter a number: "))
print(2*(length+width))

#challenge 2
price=int(input("enter the price"))
tip=0.20*price
print("the tip is "+ str(tip))
print("the total is "+ str(price + tip))

#Challenge 3
height=int(input("enter a number"))
width=int(input("enter a number"))
length=int(input("enter a number"))
print("the volume is " +str(height*length*height))
print("the total surface "+ str(2*(length*width + width*height + height*length)))