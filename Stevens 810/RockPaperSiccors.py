""" this is a program that lets you play Rock Paper Scissors with the computer """

from random import choice
def winner(human):
    """ this function decides and prints the winner and returns the fuction to main"""
    PC = choice(['R', 'P', 'S'])
    if(PC==human):
        print("Tie: we both chose "+('Rock'if PC=='R' else ('Paper' if PC=='P' else 'Scissors')))        
    elif(human=='R' and PC=='P'):
        print("paper beats rock: I Win!!")
    elif(human=='P' and PC=='R'):
        print("paper beats rock: You Win!!")
    elif(human=='S' and PC=='P'):
        print("scissors beats paper: You Win!!")
    elif(human=='S' and PC=='R'):
        print("rock beats scissors: I Win!!")
    elif(human=='P' and PC=='S'):
        print("scissors beats Paper: I Win!!")
    elif(human=='R' and PC=='S'):
        print("rock beats scissors: You Win!!")
    return()


print("Hello welcome to first assignment Rock Paper scissors")
val = input("Enter your choice R for Rock P for Paper S for scissors Q if you want to quit")
val = val.upper()

while val != 'Q':
    if val in ['R','S','P']:
        winner(val)
        val = input("Enter your choice R for Rock P for Paper S for scissors Q if you want to quit")
        val = val.upper()
    else:
        print('You have selected a invalid choice please try again')
        val = input("Enter your choice R for Rock P for Paper S for scissors Q if you want to quit")
        val = val.upper()

print("Thanks for playing! have a good day")

# I will try to do the same with dictionaries!