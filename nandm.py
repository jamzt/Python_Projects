#
# Python: 3.11.4
# 
# Author: Jamie Taalai
# 
# Purpose: Python course, creating our first program together with Tech Academy.
#          Demonstrating how to psdd variables from functiion
#          While producing functional game.
# 
#          Remember, function_name(variable) __means that we pass in the varaible. 
#          return varaible means_that we are returning the varaible back to the calling function.



import pygame
import sys

# Initialize Pygame
pygame.init()

# Load sounds
pygame.mixer.init()
nice_sound = pygame.mixer.Sound("Cat.mp3")
mean_sound = pygame.mixer.Sound("Dog.mp3")




def start(nice=0, mean=0,name=""):
    #get user's name
    name = describe_game(name)
    nice,mean,name = nice_mean(nice,mean,name)


def describe_game(name):
    """
        Check if this is a new game or not.
        If it is new, get the user's name.
        If it is not a new game, thank the player for
        playing again and continue with the game
    """
    # meaning, if we do not already have this user's name, then they're are a new player and we need to get their name
    if name != "":
        print("\nThank you for playing again, {}!".format(name))
    else:
        stop = True 
        while stop == True:
            if name == "":
                name = input("\nWhat's your name? \n>>> ").capitalize()
                if name != "":
                    print("\nWelcome, {}!".format(name))
                    print("\nIn this game, you will be greeted \nby several differrent people. \nYou can choose to be nice or mean")
                    print("but at the end of the game your fate \nwill be sealed by your actions.")
                    stop = False

    return name


def nice_mean(nice,mean,name):
    stop = True
    while stop == True:
        show_score(nice,mean,name)
        pick = input("\nA stranger approaches you fom a \nconversation. Will you be nice \nor mean? (N/M) \n>>>: ").lower()
        if pick == "n":
            print("\nThe stranger walks away smiling...")
            nice = (nice + 1)
            nice_sound.play()
            stop = False
        if pick == "m":
            print("\nThe stranger glances at you \nmenacingly and storms off...")
            mean = (mean + 1)
            mean_sound.play()
            stop = False
    score(nice,mean,name) # pass the 3 variables to the score()



def show_score(nice,mean,name):
    print("\n{}, your current total: \n({}, Nice and ({}, Mean)".format(name,nice,mean))



def score(nice,mean,name):
    #score function is being passed the value stored within the 3 variables
    if nice > 2: # if condition is valid, call win function passing in the variables so it can use them
        win(nice,mean,name)
    if mean > 2: # if condition is valid, call lose function passing in the variables so it can use them
        lose(nice,mean,name)
    else:
        nice_mean(nice,mean,name)
    


def win(nice,mean,name):
    #substitute the {} wildcards with our variable valuies
    print("\nNice job {}, you won! \nEveryone loves you and you've \nmade lots of friends along the way!".format(name))
    #call again function and pass in our variables
    nice_sound.stop()
    again(nice,mean,name)

def lose(nice,mean,name):
    #substitute the {} wildcards with our variable valuies
    print("\nAhhh too bad, game over! \n(), you live in a dirty beat-up \nvan by the river, wretched and alone!".format(name))
    #call again function and pass in our variables
    mean_sound.stop()
    again(nice,mean,name)



def again(nice,mean,name):
    stop = True
    while stop == True:
        choice = input("\nDo you want to play again? (y/n):\n>>> ").lower()
        if choice == "y":
            stop = False
            reset(nice,mean,name)
        if choice == "n":
            print("\nOh, so sad, sorry to see you go!")
            stop = False
            quit()
        else:
            print("\nEnter ( Y ) for 'YES', ( N ) for 'NO':\n>>> ")



def reset(nice,mean,name):
    nice = 0
    mean = 0
    #notice, i don't reset the name variable as the same user has electd to play again



if __name__ == "__main__":
    start()
    

    
                