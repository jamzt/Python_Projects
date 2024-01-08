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




def start():
    print("Hello, {}!".format(get_name()))


def get_name():
    name = input("What's your name? ")
    return name



if __name__ == "__main__":
    start()
    


