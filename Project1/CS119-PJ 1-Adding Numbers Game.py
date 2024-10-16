# Author: Yaowei Lei
# Date:    10/01/2021
# Purpose: CS119-PJ1: To play an adding-three-number game and earn/lose points for each win/lose. 


def testAdd(s1, s2, s3) : # Define a function testAdd to add 3 numbers from user
    points = 10 # 10 points for each game 
    sum = int(input("Please enter the sum of these 3 numbers: " )) # get 3 numbers from the user
    if sum == ( int(s1)+int(s2)+int(s3) ) :  # is sum really correct? must use int() to convert str to integer
        print("Congratulations! You are right! You earn " + str(points) + " points now." )
        list[0] += points   # add points to total for win, list[0] is a global variable
        # print("Therefore, you have " + str(list[0]) + " points in your account!" ) 
    else : # incorrect answer from the user
        print("Sorry, it is not correct! You lose " + str(points) + " points now." )
        list[0] -= points   # deduct points from total for loss, list[0] is a global variable  
        # print("Therefore, you have " + str(list[0]) + " points in your account!" )

# MAIN PROGRAM :
total_points = 0 # variable to track total number of points for the player
list = [total_points]  # one-element list to make list[0] a global variable for all functions to update  
print ("Welcome to the Super Numbering game of Yaowei Lei !!!") 
your_name = input("Please enter your full name: ")
print ( your_name + ": Thank you for playing this number game. You have " + str(list[0]) + " points to start. ")
while True: # keep running until the user says "no"
    s1 = input("Enter first number: ")    #string s1
    s2 = input("Enter second number: ")   #string s2
    s3 = input("Enter third number: ")    #string s3
    print ("You just entered 3 numbers: ", s1, s2, s3) # show three numbers in strings
    testAdd(s1, s2, s3) # calling function testAdd to check and give award or penalty 
    print("Now, you have " + str(list[0]) + " points in your account!" )
    play_again = input("Would you like to continue this game? 'yes' or 'no': ")  #get player's input for continuation
    if play_again == "no" :  # only "no" will stop this game
        break  # to leave this while loop and exit the game
print("Thank you for playing this wonderful game designed by Yaowei Lei !!!") 
x = input("Press Ctrl+Alt+PrtScn to get a snapshot of this console, then ENTER to exit: ")
# End of MAIN PROGRAM