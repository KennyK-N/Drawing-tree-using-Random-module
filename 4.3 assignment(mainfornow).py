# Assignment 4.3: A program that draws a recursive tree
# October 28, 2020
# Kenny Kwan
# Description: A program that draws an autumn tree using recursion. It uses randomly generated Angles and branch lengths that uses random.randint. It uses a dictionary for the color of the branch, and the leaves for the tree.

# import turtle package into python file
import turtle

# import random into python file
import random

# Create the turtle
tree = turtle.Turtle()

# Dictionary containing the color for the leaves
color = {"autumn1": "#FFB533", "autumn2": "#FF853F", "autumn3": "#F79762", "autumn4": "#F05133"}

# 1st random choice: Randomly chooses one of the color for the leaves from the color dictionary for the leaves of the tree 
randomname, randomcolor = random.choice(list(color.items()))
# 2nd random choice: Randomly chooses one of the color for the leaves from the color dictionary for the leaves of the tree 
randomname2, randomcolor2 = random.choice(list(color.items()))
# 3rd random choice: Randomly chooses one of the color for the leaves from the color dictionary for the leaves of the tree 
randomname3, randomcolor3 = random.choice(list(color.items()))

# Dictionary containing the color for the branches
treecolor = {"tree1": "#704241", "tree2": "#A0522D", "tree3": "#CD853F", "tree4": "#B46F50"}

# Randomly chooses the color for the branch for the tree from the color dictionary for the branch of the tree
random_treename, random_treecolor = random.choice(list(treecolor.items()))

# Adjusts the pen speed
tree.speed(0)
# Brings the pen up
tree.penup()
# Moves the pen to 0, 290 on the screen
tree.goto(0, -290)
# Turns the pen 90 degrees to the left
tree.left(90)
# puts the pen down
tree.pendown()
# chooses a random tree color for the branch for the color of the pen
tree.color(random_treecolor)
# Adjusts the pen width
tree.width(7)
# Change the pen stamps into triangles
tree.shape("triangle")

# Creates a function that draws the bottom branch of the tree
def draw_main_tree(branch_length):
    # Stamps the bottom branch of the tree and draws the bottom branch
    tree.stamp()
    tree.forward(branch_length)
    
# creates a function that draws the upper branches, and leaves for the tree
def draw_tree(level, branch_lengths):
    # Make it so that the branch lengths will choose a random number from random number range of 55-130
    branch_lengths = random.randint(55,130)
    # Make it so that the branch length divide will choose a random number from a range of 1-9 
    branch_length_divide = random.randint(1, 9)
    # Make it so that the branch angle will choose a random number from a range of 20-37
    branch_angle_random = random.randint(20, 37)
    # if we're not on the leaf level
    if level > 0:
        # Draw a branch
        tree.forward(branch_lengths)
        # Turn left using 1 random angle number and draw another branch at level -1 and divide the branch length by a random number from branch_length_divide, and change the pen width to 7, change the pen color to the 3rd random leaves color, stamp the leaves, and change the pens color back to the branches color.
        tree.width(7)
        tree.left(branch_angle_random)
        draw_tree(level-1, branch_lengths/branch_length_divide)
        tree.color(randomcolor3)
        tree.stamp()
        tree.color(random_treecolor)
        
        # Turn right using 2 random angle numbers and draw another branch at level -1 and divide the branch length by a random number from branch_length_divide, and set the pen width to 4.
        tree.right(branch_angle_random + branch_angle_random)
        draw_tree(level-1, branch_lengths/branch_length_divide)
        tree.width(4)
        
        # Turn Left using 1 random angle number, and go back 
        tree.left(branch_angle_random)
        tree.back(branch_lengths)
        tree.pendown()
        
        # change the color pen color to the 2nd random leaves color and stamp it, and then pen up
        tree.color(randomcolor2)
        tree.stamp()
        tree.penup()
        
        # change the color of the pen back to the branch color and then pen down
        tree.color(random_treecolor)
        tree.pendown()
        
    # Otherwise if we're at the leaf level
    else:
        # Change the color of the pen to the 1st leave color, and draw a circle in the middle of the leaf level, and stamp the leaves, and change the pens color back to the branches color
        tree.color(randomcolor)
        tree.begin_fill()
        tree.circle(3)
        tree.end_fill()
        tree.stamp()
        tree.color(random_treecolor)
        
# Make it so that the branch number will choose a random number from random number range of 4-6   
random_branch_number = random.randint(4,6)
        
# draw a long tree branch at the bottom
draw_main_tree(60)
# randomly draws either small, medium or big tree using the random_branch_number
draw_tree(random_branch_number, 110)