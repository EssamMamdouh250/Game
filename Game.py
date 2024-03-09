# File : cs112_A1_T2_Game_3_20230626.py
# purpose : This is a two-player mathematical game of strategy. It is played by two people with a pile of coins (or other tokens) between them. The players take turns removing coins from the pile, always removing a non-zero square number of coins (1, 4, 9, 16, …). The player who removes the last coin wins.
# Author : Essam Mamdouh Saad Abdelzaheh
# ID : 20230626
# represnting the rules of the game
import math
import random
print("to start the game please enter the number of coins")
print("the player must take a perfect square numbers like(1,4,9....)")
print("the last player take coins is won")
print("good luck")
while True:
    number = random.randint(1,1001)
    if math.sqrt(number) / math.floor(math.sqrt(number))!=1:
        print(number)
        break
player1iswin = False
player2iswin = False
while True:
    while number > 1:
        player1_choice = input("please enter your choice: ")
        if player1_choice.isdigit() and math.sqrt(int(player1_choice)) / math.floor(math.sqrt(int(player1_choice))) == 1 and int(player1_choice) > 0 and int(player1_choice) <= number:
            number -= int(player1_choice)
            if number != 0:
                print (number)
            if number == 0:
                player1iswin = True
                break
            else:
                break
        else:
            print("wrong, please try again")
    while number > 0:
        player2_choice = input("please enter your choice: ")
        if player2_choice.isdigit() and math.sqrt(int(player2_choice)) / math.floor(math.sqrt(int(player2_choice))) == 1 and int(player2_choice) > 0 and int(player2_choice) <= number:
            number -= int(player2_choice)
            if number != 0:
                print(number)
            if number == 0:
                player2iswin = True
                break
            else:
                break
        else:
            print("wrong, please try again")
    if player1iswin:
        print("player1 is win")
        break
    if player2iswin:
        print("player2 is win")
        break


