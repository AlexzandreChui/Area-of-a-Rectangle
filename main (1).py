# Created By: Alex.Chui
# Created On: 2022/10/05
# This program tells the user to enter the length and width of the reactangle and calculate the area. The computer will tell the user if they are correct or not.
print("\"Let's calculate the area of a rectangle.\"")
l = int(input("Enter the length:"))
w = int(input("Enter the width:"))
area = int(input("Enter the area:"))
a = l*w 

if area == a:
  print("That is correct: %d" %(a))
else:
  print("That is incorrect, the correct answer is: %d" %(a))
  