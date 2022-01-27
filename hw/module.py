# HW Exercise 2
#
# 1. Find Area


def findArea():
        length = int(input("What is the length of the room? "))
        width = int(input("What is the width? "))
        area = length * width
        print("The area of your room is: " + str(area))
            
findArea()

# 2. Find Circumference


def findCircumference(): 
    radius = float(input("What is the radius of the circle? "))
    pi = 3.14
    circum = 2 * pi * radius
    print("The circumference of the circle is " + str(circum))
    


findCircumference()
