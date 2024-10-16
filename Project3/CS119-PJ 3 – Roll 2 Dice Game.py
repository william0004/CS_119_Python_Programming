#-------------------------------------------------------------------------------------------------.
# Author: Yaowei Lei
# Date:    10/24/2021
# Purpose: To play a game of rolling 2 dice between dealer and you, and win/lose money.
# MAIN PROGRAM: ====== Python does not use main( ) to start the main program.
#-------------------------------------------------------------------------------------------------.

import random   # import library to use random.randint( ) 

n = 1  # line number for each separator line in sequence
print ("Welcome to the Rolling 2 Dice Game of Yaowei Lei!\n ")  #   must use your name
print(n,"=========================================================."); n+=1; # increment n by 1
yourMoney = 100      # you have 100 dollars to start.
dealerMoney = 100   # dealer also has 100 dollars to start.
print( "Now, you have ", yourMoney, "dollars to play the game. Dealer also has ", dealerMoney, " dollars.")
bet = int(input("Enter your bet to roll 2 dice for this complete game (enter 0 to quit): "))  # convert to integer for bet
if bet == 0 :
    exit( ) # to stop this game and exit immediately
while True:  # keep running forever until break is encountered.
    dealer = random.randint(1, 6) + random.randint(1, 6)  # dealer rolls the dice twice to get 2 numbers
    you = random.randint(1, 6) + random.randint(1, 6) # you roll the dice twice to get another 2 numbers 
    print(n,"=========================================================."); n=n+1; 
    print("Roll 2 dice twice: Dealer got ", dealer , ", and you got ", you , "." )
    resaultWords = ["You won.", "You lost.", "It's tie."]
    resault = " "
 
    # if dealer > you:  # dealerMoney will be increased by the bet, yourMoney will be deducted by the bet
    if dealer > you :
        yourMoney -= bet
        dealerMoney += bet
        resault = resaultWords[1]
    # elif you > dealer:   # - - -
    elif dealer < you :
        yourMoney += bet
        dealerMoney -= bet
        resault = resaultWords[0]
    # else :      # you == dealer      # It is a tie.
    else :
        resault = resaultWords[2]
    print(resault,"Now, You have ", yourMoney, " dollars, and dealer has ", dealerMoney, " dollars. ")
    if dealerMoney <= 0 or yourMoney <= 0 :   # either side has no money to play
        break # time to exit the while loop and stop this game now.  Game is really over. 
    # end of while True loop 
print(n,"=========================================================."); n+=1;
print("Game ends. You have ", yourMoney, " dollars, and dealer has ", dealerMoney, " dollars. ") 
print(n,"=========================================================."); n+=1;
print("Thank you for playing this Rolling 2 Dice Game of Yaowei Lei! ")     # < < - - must use your name
print(n,"=========================================================."); n+=1;
x = input("Press Ctrl+Alt+PrtScn to get a snapshot of this console, then ENTER to exit: ")
# End of MAIN PROGRAM ============================================.


