from time import sleep
from winsound import PlaySound
import winsound
import os

friend = 0
alist = ["a", "A"]
blist = ["B", "b"]
clist = ["C", "c"]
dlist = ["d", "D"]

#hello world eindopdracht
#speelt af in een pokemon wereld
#trainer name and Eevee name can be chosen
while True: 
    winsound.PlaySound('background.wav', winsound.SND_ASYNC)
    print("^Hello, i am professor Goei and welcome to the world of pokemon^")
    sleep(1)
    print("^What is your name pokemon trainer?^")
    name = input()
    sleep(1)
    print("^Hello " + name + "^")
    sleep(1)
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡴⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣾⡄")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣤⣶⣾⣷⣾⣿⣃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⠟⢹⣧")
    print("⠀⠀⠀⠀⠀⠀⠀⣀⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⠋⠀⢸⣿")
    print("⠀⠀⠀⢀⣠⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⡿⠁⠀⠀⢸⣿")
    print("⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣤⡀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⡿⠁⠀⠀⠀⣿⣿")
    print("⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣍⢤⣬⣥⣾⣿⣶⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⠁⠀⠀⠀⢰⣿⡏")
    print("⣸⣿⣿⣿⣿⣿⣿⡟⠛⠻⠿⠿⠿⠿⣿⡿⠇⢨⣍⣙⣛⣠⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⡏⠀⠀⠀⢀⣾⣿⠁")
    print("⣿⣿⣿⣿⣿⣿⣿⣧⡘⢶⣶⣶⣶⣶⣶⣤⣤⣤⣤⣭⣉⣉⣉⣛⠛⠿⠿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⢀⣠⣴⣦⣤⣶⣶⣿⣿⣧⣤⣤⣄⠉⢻⡇⠀⠀⠀⣼⣿⡏⠀")
    print("⣿⣿⣿⣿⣿⣿⠿⣿⣿⣄⠙⢿⣿⣄⠀⠀⠀⠀⠈⠉⠙⠛⠻⠿⣿⣿⣶⣤⡉⠻⣿⣿⣿⡆⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣥⣤⣭⣁⣀⠀⣸⣿⡟⠀⠀")
    print("⢻⣿⣿⣿⣿⣿⡄⢬⣙⠻⢰⣤⡙⠻⣷⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠻⣿⣷⣌⠻⢿⡇⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣍⡁⠿⠋⠀⠀⠀")
    print("⠸⣿⡏⣉⡻⢿⣿⡜⣿⣿⣿⣿⣿⣶⣄⡙⠻⣷⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⣷⣄⢁⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣛⣛⣛⠛⠂⠀")
    print("⠀⢻⡇⣿⣿⣶⣬⣙⠈⢿⣿⣿⣿⣿⣿⣿⣶⣌⡙⠻⢿⣶⣤⣄⡀⠀⠀⠀⠀⠀⠀⠈⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠀⠀⠀")
    print("⠀⠈⠁⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⣈⠙⠻⢿⣿⣶⣦⣄⣀⣀⣤⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀")
    print("⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠗⢀⣀⣉⠙⠛⠛⠛⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⣉⠻⣿⣿⠀")
    print("⠀⠀⠀⠀⠀⠀⠙⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⢉⣠⣾⣿⣿⠟⣁⣤⣴⣶⣶⢸⣿⣿⣿⣿⣿⣿⣿⢟⣛⠻⣿⣿⣿⣿⣿⣿⣿⣿⠁⣿⠇⠸⣿⡀")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠿⢿⣿⣿⣿⣿⡿⠃⣴⣿⣿⣿⠟⣡⣾⣿⣿⣿⣿⣿⢸⣿⣿⣿⣿⣿⣿⢣⣿⣿⠀⠘⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⣿⡇⠀⠀⠀")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣀⡅⣠⣿⣿⣿⣿⣿⣿⣇⢹⣿⣿⣿⣿⣿⠰⣷⣀⣠⡄⣸⣿⣿⣿⣿⣿⠿⢻⣷⣶⣿⣿⡇")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⢡⣿⣿⣿⣿⣿⣿⣿⣿⡄⢻⣿⣿⣿⣿⣷⣬⣉⣉⣴⣿⣿⣿⣿⣿⣿⣿⠿⢟⣿⣿⠟")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⡇⢸⡇⣿⣿⣿⣿⣿⡿⢹⣿⣦⡙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣛⣋⣭⣶⣾⡿⢟⣡⣾")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣇⢈⣥⢸⣿⣿⣿⣿⡇⣾⣿⣿⣿⣶⣬⣙⠻⠿⣿⣿⣿⣿⣿⣿⠿⠿⢛⣉⣥⣶⣿⡿⠟⠀⠀")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⡿⠈⢿⣿⣿⣿⡀⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣤⣤⣤⣤⣴⣶⣾⣿⣿⢿⣿⣿⠁")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⠡⣿⣌⢻⣿⣿⣧⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢸⣿⠃⠀")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⠇⠀⢿⣿⣷⡙⠛⣿⡇⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠛⠁⠀⠀")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⣿⣿⣿⠀⠀⠈⢿⣿⣿⣶⠈⣰⣷⣬⡻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠟⠀⠀⠀")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠈⠉⠋⢠⣿⣿⣿⣿⣮⡛⢿⠏⠻⢿⣿⣿⣿⣿⢟⣴⣦⠀")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⢿⠆⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⢉⡛⠟⣱⣿⣿⡏⠀")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠁⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⠀⠀⠀⠀⠈⣿⣾⣿⣿⣿⡇⠀⠀")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⢹⣿⣿⣿⣿⣷⠀⠀⠀")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠉⠛⠋⠛⠉⠀")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠿⣿⡟⢿⠟⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    sleep(2)
    print("^Meet your eevee, what wil you name it?^")
    Eevee = input()
    print("^You and " + Eevee + " are no longer safe in Saffron city!^")
    sleep(2)
    print("^There is a pokemon war going on right this second and i advice you to go to lavender town^")
    sleep(2)
    print("^Lavender town is taking people in at the moment^")
    sleep(2)
    print("^Goodluck on your journey...^")
    sleep(3)
    print("*you and Eevee are going on a journey to Lavender town*")
    sleep(2)
    print("*you come across a path that splits in 2")
    sleep(2)
    print('The left path looks dark and ominoous, the right path looks safe and well lit')
    sleep(2)
    print("Which path wil you chose?")
    sleep(2)
    print("left (dark and ominous) or right (safe and bright)")
    answer = input()
    if answer == "left":
            #safe choice, story continues
            print("You and eevee go on the left path")
            sleep(2)
            print("you walk along the path casious...")
            sleep(2)
            print("You hear something rumble in the distance")
            sleep(2)
            print("The bushes next to you start shaking, you and " + Eevee + " start preparing for battle")
            sleep(2)
            print("Something jumps out of the bush!")
            sleep(2)
            print("Its a bunnelby!")
            sleep(2)
            print("Eevee and bunnelby start sniffing eachother...")
            sleep(2)
            print("*" + Eevee + " made a friend!*")
            sleep(2)
            print("Achievement unlocked: Friends")
            friend = friend + 1
            print("Your eevee's love has increased by 10")
            # continue story
            sleep(2)
            print("You and " + Eevee + " come across another split path")
            sleep(2)
            print("The paths are labelled")
            print("a. Safe route lavender town    b. Short route lavender town    c. Unicorn forest")
            sleep(1)
            print("which path will you choose? a/b/c")
            answer2 = input()
            if answer2 in alist:
                print("You go on the safe path")
                sleep(2)
                print("You and " + Eevee + " are walking along the path when you come across a snorlax...")
                sleep(1)
                print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣶⣿⣶⣦⣄⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣤⣶⣾⣿⣿⣷⠀⠀⠀⠀⠀")
                print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⠿⠿⠿⣿⣿⣿⣿⠿⠿⠿⢿⣿⣿⣿⣿⣿⠀⠀")
                print("⠀⠀⠀⠀⠀⢀⡀⣄⠀⠀⠀⠀⠀⠀⠀⣿⣿⠟⠉⠀⢀⣀⠀⠀⠈⠉⠀⠀⣀⣀⠀⠀⠙⢿⣿⣿⠀")
                print("⠀⠀⠀⣀⣶⣿⣿⣿⣾⣇⠀⠀⠀⠀⢀⣿⠃⠀⠀⠀⠀⢀⣀⡀⠀⠀⠀⣀⡀⠀⠀⠀⠀⠀⠹⣿")
                print("⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⣼⡏⠀⠀⠀⣀⣀⣉⠉⠩⠭⠭⠭⠥⠤⢀⣀⣀⠀⠀⠀⢻⡇⠀")
                print("⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⣿⠷⠒⠋⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠑⠒⠼⣧")
                print("⠀⠀⠀⢹⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⣦⣀")
                print(" ⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣷⣦⣀⠀")
                print("⠀⠀⠀⠈⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣷⣄")
                print("⠀⠀⠀⠀⢹⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣷⣄")
                print("⠀⠀⠀⠀⠀⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣧")
                print("⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣶⣤⣄⣠⣤⣤⣶⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣶⣶⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀")
                print("⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀")
                print("⠀⠀⣀⠀⢸⡿⠿⣿⡿⠋⠉⠛⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠉⠀⠻⠿⠟⠉⢙⣿⣿⣿⣿⣿⣿⡇")
                print("⠀⠀⢿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠈⠻⠿⢿⡿⣿⠳")
                print("⠀⠀⡞⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣇⡀")
                print("⢀⣸⣀⡀⠀⠀⠀⠀⣠⣴⣾⣿⣷⣆⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⣰⣿⣿⣿⣿⣷⣦⠀⠀⠀⠀⢿⣿⠿⠃")
                print("⠘⢿⡿⠃⠀⠀⠀⣸⣿⣿⣿⣿⣿⡿⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⢻⣿⣿⣿⣿⣿⣿⠂⠀⠀⠀⡸⠁")
                print("⠀⠀⠳⣄⠀⠀⠀⠹⣿⣿⣿⡿⠛⣠⠾⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠿⠿⠳⣄⠙⠛⠿⠿⠛⠉⠀⠀⣀⠜⠁")
                print("⠀⠀⠀⠈⠑⠢⠤⠤⠬⠭⠥⠖⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠒⠢⠤⠤⠤⠒⠊⠁⠀")
                sleep(2)
                print("The Snorlax seems agitated...")
                sleep(1)
                print("Be carefull... ")
                sleep(1)
                print("*Your Eevee walks over to the Snorlax and gives it a hug!")
                sleep(2)
                print("Snorlax seems happier, i guess it was just having a bad day")
                sleep(2)
                print("Snorlax and Eevee become friends, + 1 friend, + 10 love")
                friend = friend + 1
                print("You and " + Eevee + " continue your journey to lavender town...")
                sleep(2)
                #story continues to all the eevee endings
                #your eevee will gain love
                print("You come across another split...")
                sleep(2)
                print("The paths are labelled yes and no?? Which idiot thought of that...")
                sleep(2)
                print("The path that is labelled yes looks quite safe and the path that is labelled no is very closed off, you cannot see what is going on on path no")
                sleep(3)
                print("Which path are you choosing? yes/no")
                answer5 = input()
                if answer5 == "yes":
                    print("You go onto path yes...")
                    #path yes = death
                    sleep(2)
                    print("There is a funny looking Gengar there")
                    print("⠀⠀⠀⠀⠀⢸⠓⢄⡀⠀⠀⠀⠀")
                    print("⠀⠀⠀⠀⠀⢸⠀⠀⠑⢤⡀")
                    print("⠀⠀⠀⠀⠀⢸⡆⠀⠀⠀⠙⢤⡷⣤⣦⣀⠤⠖⠚⡿⠁⠀")
                    print("⣠⡿⠢⢄⡀⠀⡇⠀⠀⠀⠀⠀⠉⠀⠀⠀⠀⠀⠸⠷⣶⠂⠀⠀⠀⣀⣀⠀⠀")
                    print("⢸⣃⠀⠀⠉⠳⣷⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠉⠉⠉⠉⢉⡭⠋")
                    print("⠀⠘⣆⠀⠀⠀⠁⠀⢀⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠋⠀⠀")
                    print("⠀⠀⠘⣦⠆⠀⠀⢀⡎⢹⡀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⡀⣠⠔⠋⠀")
                    print("⠀⠀⠀⡏⠀⠀⣆⠘⣄⠸⢧⠀⠀⠀⠀⢀⣠⠖⢻⠀⠀⠀⣿⢥⣄⣀")
                    print("⠀⠀⢸⠁⠀⠀⡏⢣⣌⠙⠚⠀⠀⠠⣖⡛⠀⣠⠏⠀⠀⠀⠇⠀⠀⠀⠀⢙⣣⠄")
                    print("⠀⠀⢸⡀⠀⠀⠳⡞⠈⢻⠶⠤⣄⣀⣈⣉⣉⣡⡔⠀⠀⢀⠀⠀⣀⡤⠖⠚⠀")
                    print("⠀⠀⡼⣇⠀⠀⠀⠙⠦⣞⡀⠀⢀⡏⠀⢸⣣⠞⠀⠀⠀⡼⠚⠋⠁⠀⠀")
                    print("⠀⢰⡇⠙⠀⠀⠀⠀⠀⠀⠉⠙⠚⠒⠚⠉⠀⠀⠀⠀⡼⠁⠀")
                    print("⠀⠀⢧⡀⠀⢠⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣞⠁⠀")
                    print("⠀⠀⠀⠙⣶⣶⣿⠢⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀")
                    print("⠀⠀⠀⠀⠀⠉⠀⠀⠀⠙⢿⣳⠞⠳⡄⠀⠀⠀⢀⡞⠀")
                    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠀⠀⠹⣄⣀⡤⠋⠀")
                    sleep(2)
                    print("OH!") 
                    sleep(1)
                    print("It wants to battle...")
                    sleep(2)
                    print("The Gengar used Shadow ball")
                    sleep(1)
                    print("CRITICAL HIT!")
                    sleep(1)
                    print("Your Eevee fainted")
                    sleep(1)
                    print("You died...")
                    sleep(2)
                    print("You got the Eevee battle ending!")
                    sleep(1)
                    print("You can play again to try and get a different ending")
                    sleep(2)
                
                if answer5 == "no":
                    print("You go on path no....")
                    sleep(2)
                    #you survive
                    print("It looks a bit unsafe.....")
                    sleep(1)
                    print("Are you sure you wanna go on this path? yes/no")
                    answer6 = input()
                    if answer6 == "yes":
                        #you dont die
                        sleep(1)
                        print("You continue walking on this path...")
                        sleep(2)
                        print("A wild Bulbasoar!")
                        sleep(1)
                        print("""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠉⢳⠴⢲⠂⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⠤⠤⠤⠤⠤⠤⠤⠤⠤⠖⠊⠀⣠⠎⠀⡞⢹⠏⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡴⠊⠁⠀⠀⠀⠀⠀⢀⡠⠤⠄⠀⠀⠀⠁⠀⠀⢀⠀⢸⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣠⠤⠤⠄⣀⠀⠀⠀⠀⢀⣌⠀⠀⠀⠀⠀⢀⣠⣆⡁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠘⡄⠀⠀⠀⠀
⠀⠀⠀⠀⡴⠁⠀⠀⠐⠛⠉⠁⠀⠀⣉⠉⠉⠉⠑⠒⠉⠁⠀⠀⢸⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢧⠀⠱⡀⠀⠀⠀
⠀⠀⠀⢰⣥⠆⠀⠀⠀⣠⣴⣶⣿⣿⣿⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⢇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⡆⠀⠑⡄⠀⠀
⠀⠀⢀⡜⠁⠀⠀⢀⠀⠻⣿⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠀⠀⠸⡀⠀
⠀⢀⣮⢖⣧⢠⠀⣿⠇⠀⠀⠁⠀⠀⠀⠠⠀⢀⣠⣴⣤⡀⠀⠀⠀⠈⡗⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⢱⠀
⠀⣼⠃⣼⣿⠘⠀⠀⠀⢠⣶⣿⡆⠀⠀⠁⣠⠊⣸⣿⣿⣿⡄⠀⠀⠀⡇⠀⢑⣄⠀⠀⠀⠀⠀⠀⢠⠃⠀⠀⠸⡆
⠀⣿⢰⣿⣿⠀⠀⠀⠀⠙⠻⠿⠁⠀⠀⠠⠁⠀⣿⣿⣿⣿⡇⠀⠀⠀⠇⠀⢻⣿⣷⣦⣀⡀⣀⠠⠋⠀⠀⠀⢀⡇
⠈⠉⠺⠿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⢿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠈⢿⣿⣿⣿⣿⢦⡀⠀⠀⠀⠀⡸⠀
⠘⣟⠦⢀⠀⠀⢠⠀⠀⡠⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠁⣀⠔⠀⠀⠀⠀⠀⠀⠀⠛⠻⠟⠋⠀⠙⢦⠀⣠⠜⠀⠀
⠀⠈⠑⠤⡙⠳⣶⣦⣤⣤⣤⣤⣤⣤⣤⣤⣴⣶⡶⠞⠁⠀⠀⣠⠖⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠈⢯⠁⠀⠀⠀
⠀⠀⠀⠀⠈⢳⠤⣙⡻⠿⣿⣿⣿⣿⡿⠿⠛⠉⠀⢀⣀⡤⡚⠁⠀⠀⠀⠀⠀⠀⣧⠖⣁⣤⣦⠀⠀⠈⢇⠀⠀⠀
⠀⠀⠀⠀⠀⢸⠀⢀⣩⣍⠓⠒⣒⠒⠒⠒⠒⠊⠉⠁⢀⡟⠀⠀⣾⣷⠀⠀⠀⠀⠏⢴⣿⣿⣿⠀⠀⠀⢸⠀⠀⠀
⠀⠀⠀⠀⠀⠘⣶⣿⣿⣿⠀⠀⠈⠒⢄⣀⡀⠀⠀⠀⣼⣶⣿⡇⠈⠋⠀⠀⠀⡼⠀⠈⠻⣿⡿⠀⠀⠀⢸⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠹⡿⠿⠋⠀⠀⠀⠀⡜⠁⠈⢯⡀⢺⣿⣿⣿⠃⠀⠀⠀⢀⣼⣇⠀⠀⠀⠀⠀⠀⠀⠀⡞⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣿⣦⣄⣠⣀⣠⠞⠀⠀⠀⠈⠛⣿⡛⠛⠁⠀⠀⠀⣠⠊⠀⠈⢦⣄⣀⣀⣀⣀⢀⡼⠁⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠛⠉⠀⠀⠀⠀⠀⠀⠘⠛⠿⣿⠷⡾⠗⠊⠁⠀⠀⠀⠈⠉⠙⠛⠛⠛⠉⠀⠀⠀⠀⠀""")
                        sleep(1)
                        print("Bulbasoar challenges you...")
                        sleep(1)
                        print("Bulbasoar used Tackle")
                        sleep(1)
                        print("Eevee dodged the attack")
                        sleep(1)
                        print("Eevee used quick attack")
                        sleep(1)
                        print("critical hit!")
                        sleep(1)
                        print("Bulbasoar fainted...")
                        sleep(1)
                        print("You and eevee continue walking to lavender town")
                        winsound.PlaySound(None, winsound.SND_PURGE)
                        sleep(2)
                        winsound.PlaySound('lavender-.wav', winsound.SND_ASYNC)
                        #play lavender town music
                        #put lavender town music file in the same map as this code file!!!!!!!!!
                        print("Lavender town reached")
                        sleep(1)
                        #doors question
                        print("You and eevee are walking around town in hopes to meet some people...")
                        sleep(2)
                        print("The streets are empty")
                        sleep(1)
                        print("What will you do?")
                        sleep(1)
                        print("A. knock on door yellow     B. knock on door pink    C. knock on door green    d. knock on door blue")
                        answer7 = input()
                        if answer7 in alist:
                            #Jolteon of Flareon evolution
                            print("You knock on the yellow door...")
                            sleep(2)
                            print("A man opens the door, it's pokemon trainer Sparky!")
                            sleep(2)
                            print("^Oh hello! You must be the new trainer in town everyone is talking about! " + name + " right?^")
                            sleep(2)
                            print("^If you like i could show you around town?^")
                            sleep(2)
                            print("^Great! where do you wanna go first?^")
                            sleep(2)
                            print("^We can go to one of my favorite place, the racetrack!^")
                            sleep(2)
                            print("^Or if you want we can go to the towns bonfire!^")
                            sleep(2)
                            print("A. racetracks    B. bonfire")
                            answer8 = input()
                            if answer8 in alist:
                                #jolteon evolution
                                print("^Lets go to the racetracksssssss!!!!!^")
                                sleep(2)
                                print("You arrive at the racetracks. There are some cars on the tracks")
                                sleep(2)
                                print("Sparky shows you the car he races with from time to time")
                                sleep(2)
                                print("You and " + Eevee + " meet some racers")
                                sleep(2)
                                print("You and your eevee have a great time")
                                sleep(2)
                                print("Eevee gains +10 love!")
                                sleep(2)
                                print("Oh? Your eevee is evolving!")
                                sleep(2)
                                print("""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢱⡄⠀⠀⠀⠀⠀⠀⠀⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣦⡀⠀⠀⢀⠀⢠⣿⣷⠀⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣄⠀⠀⠀⠀⠀⠀⢢⣸⣿⣷⣄⠀⠸⡄⢸⣿⣿⡆⣿⡀⠀⠘⡢⡀⠀⠀⠀⠀⠀⠀⡿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠈⢻⣶⣤⡀⠀⠀⠀⢻⣿⣿⣿⣧⡀⣿⣾⣿⣿⣿⣿⣧⠀⠀⢃⠈⠢⡀⠀⢰⡀⢰⠀⢳⠀⠀⠀⡀⠀⠀⣠⠀⣴⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠹⣿⣿⣷⣦⣄⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⠙⢷⣦⣘⡀⠀⠈⠢⣸⠐⠌⠀⠀⢇⠀⡔⡇⢀⠜⣧⡾⠃⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠈⢻⣿⣿⣿⣿⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⠈⠻⣷⣄⡀⠀⠈⠀⠀⣆⠀⠘⠜⠀⡧⠁⣰⡟⠁⢰⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠈⠻⣷⣄⠀⠀⠀⣿⣦⠀⠀⠀⠀⢀⡟⠀⠀⣼⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣀⣀⣀⣈⣑⣲⣬⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⣿⣆⠀⠀⠀⠈⢿⡆⢦⡀⢸⣿⣧⢸⣆⠀⣸⠃⠀⣸⢋⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠉⠛⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠉⠳⣦⡀⠀⠈⣿⣾⣿⣾⣿⣿⣿⣿⣿⣏⢀⣜⠉⠌⠀⢂⠜⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⣉⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣉⠙⠛⠛⠓⠀⠀⠈⢿⣦⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡯⠀⠀⡠⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠈⠉⢉⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣀⠀⠀⠀⢈⣽⣿⣿⡿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⢀⠞⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣀⣠⣾⣿⣿⣿⣿⣿⣿⣿⡟⠛⣿⣿⣿⣿⣯⣍⣉⡁⠀⠀⣰⢿⣿⣿⣧⠀⠈⠙⢿⣿⣿⣿⣿⠏⠁⡏⠓⠒⢀⡠⠄⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⠋⠀⠀⣿⣿⣿⣿⡿⠟⠋⣀⡀⠀⢁⣿⣿⣿⣿⣶⣤⣤⣼⣿⣿⣿⣿⣤⣼⡇⠀⠘⢧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣼⣿⣿⣿⣿⣿⠿⠟⠛⠁⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⠏⠀⠀⠸⠟⡽⣿⣿⣿⣿⣿⣿⣿⣿⣯⣿⣿⣿⠃⠀⠀⠀⠉⠢⣄⠀⠀⠀⠀⠀⠀⠀
⠀⢀⣿⣿⣿⡿⠁⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⡿⠁⠀⢀⣠⠄⠀⠁⠟⠋⠛⠻⣿⣿⣿⣿⣿⣿⠟⠁⢠⡬⠽⠯⠭⠉⠉⠁⠀⠀⠀⠀⠀⠀
⠀⣼⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⢏⣠⣴⠾⢋⡦⡾⠀⠀⠀⠀⡀⠀⠈⠉⠛⠛⠛⢁⠀⠀⠀⠳⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢠⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⠀⠊⢠⠃⠀⢀⠄⠺⡰⡇⠀⡰⠣⡀⣸⣮⣿⣶⣦⣄⡱⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢸⣿⣿⣿⣿⣷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⣿⣿⣿⠀⠀⡜⡠⠒⠁⠀⠋⠀⣇⡜⠀⠀⠱⡏⠙⠻⢿⣿⣿⣿⣿⣷⣦⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠙⠛⠛⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢼⣿⣿⣿⣷⡀⠐⠁⠀⠀⠀⠀⠀⠀⠟⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⢿⣿⣿⣿⣿⣷⣤⣀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣿⣿⣿⣿⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⢿⣿⣿⣿⣿⣿⣶⣦⡀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⢿⣿⠿⠿⠛⠁""")
                                sleep(1)
                                print("Your eevee has evolved into a Jolteon!")
                                sleep(2)
                                print(Eevee + " must've loved the racetracks a lot for it to evolve!")
                                sleep(3)
                                print("in the future")
                                sleep(2)
                                print("You and " + Eevee + " have made friends with the people from the tracks and visit it a lot")
                                sleep(2)
                                print("You and Jolteon have settled in well in lavender town")
                                sleep(3)
                                print("Congratulations! You got the Jolteon ending!")
                                sleep(2)
                                print("You can play again if you want to try and get a different ending")
                                sleep(2)
                                print("Good job " + name)
                                sleep(3)
                            if answer8 in blist:
                                #flareon evolution
                                print("^Great! Lets go to the towns bonfire! Maybe you can meet some people!^")
                                sleep(2)
                                print("^This towns bonfires are so fun, everyone comes to it^")
                                sleep(2)
                                print("^Maybe you can meet some of the townspeople and get to know them^")
                                sleep(2)
                                print("^That way you will have some friends here^")
                                sleep(2)
                                print("-You arrive at the towns bonfire with sparky and " + Eevee)
                                sleep(2)
                                print("Sparky introduces you to some townspeople")
                                sleep(2)
                                print("You make some friends, while eevee plays near the fire")
                                sleep(2)
                                print("You notice your eevee is playing with charmeleon and he is showing her some fire tricks")
                                sleep(2)
                                print("Eevee made a friend!")
                                friend = friend + 1
                                sleep(2)
                                print("Eevee gains +10 love and +10 arsonist")
                                sleep(2)
                                print("Oh? Eevee is evolving!")
                                sleep(2)
                                print("""⠐⢦⣰⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣤⡖⠀
⠀⠈⣿⣿⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣾⣿⡟⠀⠀
⠀⠀⠘⣿⣇⠉⠻⢷⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⠿⠛⢁⣿⡿⠀⠀⠀
⠀⠀⠀⠸⣿⡄⠀⠀⠉⠻⣷⣾⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠀⠀⠀⠀⠀⠀⠀⠀⣶⣶⡿⠋⠁⠀⠀⣸⣿⠁⠀⠀⠀
⠀⠀⠀⠀⢻⣧⠀⠀⠀⠀⠈⠻⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠘⡿⣦⡀⠀⠀⠀⢀⣴⡿⠋⠀⠀⠀⠀⢀⣿⠇⠀⠀⠀⠀
⠀⠀⠀⠀⠈⣿⡆⠀⠀⠀⠀⠀⠈⢿⣧⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⢳⡀⠀⢠⣾⠟⠀⠀⠀⠀⠀⠀⣼⡿⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢹⣷⠀⠀⠀⠀⠀⠀⠈⢿⣧⠀⠀⠀⠀⠀⣀⣴⠏⠀⠀⢷⢠⣿⠏⠀⠀⠀⠀⠀⠀⢰⣿⠃⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢿⣧⠀⠀⠀⠀⠀⠀⠈⣿⣇⠀⡤⠚⠉⠁⠀⠀⠀⠀⢸⣿⡟⠀⠀⠀⠀⠀⠀⢠⣿⡏⠀⠀⢀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⠻⢿⣶⣄⣀⠀⢀⡀⣻⣿⡞⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⡇⢀⠀⢀⣀⣤⣾⠿⠛⠀⠀⢀⣿⡎⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠻⢿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⣶⣿⣿⣿⣿⣿⡿⠛⠉⠀⠀⠀⠀⠀⢼⣿⣿⡀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡄⣠⣾⠿⣿⣿⣿⣷⣄⠀⠀⠀⠀⢀⣼⣿⣿⣿⣿⠟⠛⢿⣆⡆⠀⠀⠀⠀⢶⣾⣿⣿⣿⡀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣝⠟⠃⠀⠀⣿⣿⣿⣿⣿⣶⣶⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠁⡇⠀⠀⠀⠀⢸⣿⣿⣿⣿⡇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣷⣿⠀⠀⠀⢸⡁⠀⠀⠙⣿⣿⣿⣿⣿⡟⠁⠀⠀⢹⠀⠀⠀⠀⢻⣤⣤⣤⣴⣿⣿⣿⣿⣿⠃
⠀⠀⠀⠀⠀⠀⠀⠐⢦⣾⠁⠀⠀⠀⠸⣧⣀⠀⠀⣹⣿⣿⣿⣿⡇⠀⢀⣠⣿⠁⠀⠀⠀⠀⢹⣿⣿⣿⣿⣿⣿⣿⠏⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠘⡆⠀⠀⠀⠀⠀⠻⣿⣿⣿⣿⣿⠿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿⣟⣀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣧⠀⠀⠀⠀⠀⠀⠈⠛⠿⢿⣿⣿⣿⣿⡿⠟⠋⠀⠀⠀⠀⠀⠀⠐⣽⣿⣿⣿⣿⣿⣿⠟⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠘⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⢫⣿⣿⣿⣿⡟⠁⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⣿⣿⣿⣿⣿⣶⡤⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢼⡃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⢾⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠒⢮⣁⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣴⣾⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⣷⣶⣤⠄⣀⣀⣀⣀⠀⢀⣦⣄⣀⣀⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⡏⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠿⠿⠄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⡿⠿⣿⡋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢴⣿⣿⣿⣿⣿⣿⣿⣿⡇⢿⣿⣿⣿⣿⣿⣿⣿⣷⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠉⠸⢿⣿⠿⠋⠀⠈⠻⢿⣿⠿⠋⠙⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀""")
                                sleep(1)
                                print("Eevee has evolved into a Flareon!")
                                sleep(2)
                                print("Guess she really liked the fire huh")
                                sleep(2)
                                print("-in the future-")
                                sleep(2)
                                print("You and " + Eevee + " have settled in nicely in lavender town")
                                sleep(2)
                                print("You made friends at the bonfire and Flareon hangs out with some other fire types")
                                sleep(2)
                                print("Congratulations! You got the Flareon ending!")
                                sleep(2)
                                print("You can play again to get different endings!")
                                sleep(2)
                                print("Im proud of you " + name)
                                sleep(3)
                        if answer7 in blist:
                            #Espeon or Sylveon evolution
                            print("You knock on the pink door...")
                            sleep(2)
                            print("A man opens the door, it's doctor Heart!")
                            sleep(2)
                            print("^Oh hello! You must be the new trainer in town everyone is talking about! " + name + " right?^")
                            sleep(2)
                            print("^If you like i could show you around town?^")
                            sleep(2)
                            print("^Great! where do you wanna go first?^")
                            sleep(2)
                            print("^We can go to a fortune teller or the local daycare?^")
                            sleep(2)
                            print("A. fortune teller     B. daycare")
                            answer9 = input()
                            if answer9 in alist:
                                #Espeon evolution
                                print("^Great, my wife is actually the fortune teller, i love her!^")
                                sleep(2)
                                print("You and Dr. Heart go to his wife")
                                sleep(2)
                                print("Her name is Willow")
                                sleep(2)
                                print("She offers you a pokemon reading and you gladly accept")
                                sleep(2)
                                print("Eevee is very interested in the reading...")
                                sleep(2)
                                print("+10 love, + 30 phsycic")
                                sleep(2)
                                print("Oh? Eevee is evolving!")
                                print("""⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛🟪⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛🟪🟪🟪⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛⬜⬜⬜🟪⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛🟪🟪🟪🟪🟪⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛🟪⬜⬜⬜⬜⬛⬛⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛🟪⬛⬛🟪🟪🟪🟪🟪🟪⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛🟪🟪⬜🟪⬜⬜⬜⬛🟪⬛
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛🟪⬛⬛⬛⬛🟪🟪🟪🟪🟪🟪⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛🟪🟪🟪⬜🟪⬜🟪⬜⬛⬛🟪⬛
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛🟪⬛⬛⬛⬛⬛🟪🟪🟪🟪🟪🟪⬛⬛⬜⬜⬜⬜⬛⬛🟪🟪🟪⬛🟪🟪🟪🟪🟪⬜🟪⬜🟪⬛⬛⬛⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛🟪⬛⬛⬛⬛⬛🟪🟪🟪🟪🟪🟪🟪⬛🟪⬛⬛🟪🟪⬜⬜⬜🟪🟪🟪🟪🟪🟪🟪🟪🟪⬛⬛🟪⬛⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛🟪⬛⬛⬛⬛⬛⬛🟪🟪🟪🟪🟪🟪🟪⬛🟪🟪🟪🟪🟪🟪⬜⬜⬜🟪🟪🟪🟪🟪🟪⬛⬛⬛🟪⬛⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛🟪⬛⬛⬛⬛⬛⬛⬛🟪🟪⬜🟪🟪🟪⬛🟪🟪🟪🟪🟪🟪🟪⬜⬜⬜🟪🟪🟪🟪⬛⬛⬛🟪⬛⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛🟪⬛⬛⬛⬛⬛⬛⬛🟪🟪⬜🟪⬜🟪⬛🟪🟪🟪🟪🟪⬛⬛⬜⬜⬜🟪🟪⬛⬛⬛⬛🟪🟪⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛🟪⬛⬛⬛⬛⬛⬛⬛⬛🟪🟪⬜🟪⬜⬛🟪🟪🟪🟪⬛🟪⬜⬛⬜⬜🟪🟪⬛⬛⬛🟪⬛⬜⬜⬜
⬜⬜⬜⬜⬛🟪🟪⬜⬜⬜⬜⬜⬛🟪⬛⬛⬛⬛⬛⬛⬛⬛🟪🟪⬜🟪🟪🟪🟪🟪🟪⬛🟪🟪⬛⬜⬜⬜⬛⬛⬛🟪⬛⬜⬜⬜⬜
⬜⬜⬜⬛⬜⬜⬜🟪⬜⬜⬜⬜⬜⬛🟪⬛⬛⬛⬛⬛⬛⬛⬛🟪🟪🟪🟪🟪🟪🟪🟪🟪⬛⬛⬜⬜⬜🟪⬛⬛🟪⬛⬜⬜⬜⬜⬜
⬜⬜⬜⬛🟪⬜⬜⬛⬜⬜⬜⬜⬜⬜⬛🟪⬛⬛⬛⬛⬛⬛⬛🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪⬜⬜⬜🟪⬛⬛⬛⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬛🟪🟪🟪⬛⬜⬜⬜⬜⬜⬜⬜⬛🟪⬛⬛⬛⬛⬛🟪🟪🟪⬛⬛🟪🟪⬜🟪🟪🟪🟪⬜⬜🟪⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬛🟪🟪🟪🟪⬛⬜⬜⬜⬜⬜⬜⬜⬜⬛🟪🟪⬛⬛⬛🟪🟪🟪⬛⬜⬛⬛⬜⬜🟪🟪🟪🟪⬜⬛⬜🟪⬛⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬛🟪🟪🟪⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛🟪🟪🟪🟪🟪🟪🟪⬛⬛⬛🟪⬜🟪🟪🟪🟪⬜⬛🟪🟪🟪⬛⬜⬜⬜⬜⬜⬜
⬜⬜⬛🟪🟪🟪⬛⬜⬜⬜⬜⬛⬛🟪⬜⬜⬜⬜⬜⬛🟪🟪🟪🟪🟪🟪🟪🟪⬛⬛🟪🟪🟪🟪🟪⬜⬛⬛🟪🟪🟪⬛⬜⬜⬜⬜⬜
⬜⬛🟪🟪🟪🟪⬛⬜⬜⬜⬛🟪⬜⬜🟪⬜⬜⬜⬛🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪⬛🟪🟪🟪⬛⬜⬜⬜⬜⬜
⬜⬛🟪🟪🟪⬛⬜⬜⬜⬛🟪⬜⬜⬜⬛⬜⬜⬜⬛🟪🟪🟪🟪🟪⬛🟪🟪🟪🟪🟪🟪🟪🟪🟪⬛🟪🟪⬛🟪🟪🟪🟪⬛⬜⬜⬜⬜
⬜⬛🟪🟪🟪⬛⬜⬜⬛🟪🟪🟪⬜🟪⬛⬜⬜⬛🟪🟪🟪🟪🟪⬛🟪🟪⬛⬛🟪🟪🟪🟪🟪🟪🟪🟪⬛🟪🟪⬛⬛🟪⬛⬜⬜⬜⬜
⬛🟪🟪🟪🟪⬛⬜⬜⬛🟪🟪🟪🟪⬛⬜⬜⬜⬛🟪🟪🟪🟪🟪⬛🟪🟪🟪🟪⬛⬛🟪🟪🟪🟪⬛⬜⬜⬜⬛⬜⬜⬛⬛⬜⬜⬜⬜
⬛🟪🟪🟪⬛⬜⬜⬛🟪🟪🟪🟪⬛⬜⬜⬜⬜⬜⬛🟪🟪⬛⬜⬛🟪🟪🟪🟪🟪🟪⬛⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬛🟪🟪🟪⬛⬜⬜⬛🟪🟪🟪⬛⬜⬜⬜⬜⬜⬜⬛🟪⬛⬜⬜⬛🟪🟪🟪🟪🟪🟪🟪🟪⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬛🟪🟪🟪⬛⬜⬛🟪🟪🟪🟪⬛⬜⬜⬜⬜⬜⬜⬜⬛⬜⬜⬜⬛🟪🟪🟪🟪🟪🟪🟪🟪⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬛🟪🟪🟪⬛⬜⬛🟪🟪🟪⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛🟪🟪🟪🟪🟪🟪🟪🟪🟪⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬛🟪🟪🟪🟪⬛🟪🟪🟪🟪⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛🟪🟪🟪🟪🟪🟪🟪🟪🟪⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬛🟪🟪🟪⬜🟪🟪🟪🟪⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬛🟪🟪⬜🟪🟪🟪🟪⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬛🟪🟪⬜🟪🟪🟪⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬛🟪🟪⬜⬜🟪🟪⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬛🟪🟪⬜🟪⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜🟪🟪🟪🟪🟪🟪🟪🟪⬜🟪🟪🟪🟪🟪🟪⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬛🟪🟪⬜🟪⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛🟪🟪🟪🟪🟪🟪🟪⬜🟪⬛🟪🟪🟪🟪🟪⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬛🟪🟪🟪⬜⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛🟪🟪🟪🟪🟪🟪🟪🟪🟪⬜⬛🟪🟪⬛🟪🟪⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬛🟪🟪⬜⬜⬛⬜⬜⬜⬜⬜⬜⬛🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪⬜🟪⬛🟪🟪⬛🟪🟪⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬛🟪🟪🟪⬜⬛⬜⬜⬜⬜⬜⬛🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪⬜⬛🟪⬛🟪🟪🟪⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬛🟪🟪🟪🟪⬛⬜⬜⬜⬛🟪🟪🟪🟪🟪🟪🟪🟪⬛🟪🟪🟪🟪🟪⬛⬛🟪🟪🟪⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬛🟪🟪🟪🟪🟪⬛⬛⬜⬛🟪🟪🟪🟪🟪🟪⬛🟪⬛🟪🟪🟪🟪🟪⬛⬛🟪🟪🟪⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬛🟪🟪🟪🟪🟪🟪⬛🟪🟪🟪🟪🟪⬜⬜⬜🟪⬛⬛🟪🟪🟪🟪⬛🟪🟪🟪🟪⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬛🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪⬜⬜⬜⬜⬜🟪⬛🟪🟪🟪🟪⬛🟪🟪🟪⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬛⬛🟪🟪🟪⬛🟪🟪🟪🟪🟪⬜⬜⬜⬜🟪⬛🟪🟪🟪🟪⬛🟪🟪🟪⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛⬛🟪🟪🟪🟪🟪🟪⬜⬜🟪🟪⬛⬛🟪🟪🟪⬛🟪🟪⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛🟪🟪🟪🟪🟪🟪🟪🟪🟪⬛⬛⬛🟪🟪🟪⬛🟪🟪⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛🟪🟪🟪🟪🟪🟪🟪⬛⬛🟪⬛🟪🟪🟪⬛🟪🟪🟪⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛🟪🟪🟪⬜🟪🟪⬛⬛⬛🟪🟪⬜⬛🟪🟪⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛⬛⬜⬜⬛🟪🟪🟪⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜""")
                                sleep(2)
                                print(Eevee + " has evolved into an Espeon!")
                                sleep(2)
                                print("-some time later in the future")
                                sleep(2)
                                print("You and Espeon have made friends with dr. Heart and his wife Willow")
                                sleep(2)
                                print("You got a job as a nurse in the hospital and " + Eevee + " goes with Willow while youre at work")
                                sleep(2)
                                print("You two settled in lavendertown really well")
                                sleep(3)
                                print("Congratulations! You got the Espeon ending!")
                                sleep(2)
                                print("You can try and get a different ending by playing again")
                                sleep(2)
                                print("good job " + name)
                                sleep(3)
                            if answer9 in blist:
                                #sylveon evolution
                                print("^Really? Usually nobody wants to go to the daycare, i personally love kids^")
                                sleep(2)
                                print("^The daycare usually needs help, theyre understaffed...^")
                                sleep(2)
                                print("You and eevee go to the daycare with dr. Heart")
                                sleep(2)
                                print("Eevee helps with taking care of the pokemons that get dropped there while poeple are at work")
                                sleep(2)
                                print("You help with the little children")
                                sleep(2)
                                print("Eevee gains +30 love +20 fairy")
                                sleep(2)
                                print("Oh? Eevee is evolving!")
                                sleep(3)
                                print("Eevee has evolved into a Sylveon!")
                                sleep(2)
                                print("- some time later in the future -")
                                sleep(2)
                                print("You got a job at the daycare taking care of the children while sylveon helps with the pokemons")
                                sleep(3)
                                print("You have settled in lavendertown nicely")
                                sleep(3)
                                print("Congratulations! You got the Sylveon ending!")
                                sleep(2)
                                print("You can try and get a different ending by playing again")
                                sleep(2)
                                print("Good job " + name)
                                sleep(3)
                        if answer7 in clist:
                            #Leafeon or Umbreon evolution
                            print("You knock on the green door...")
                            sleep(2)
                            print("A woman opens the door, it's trainer Gardenia!")
                            sleep(2)
                            print("^Oh hello! You must be the new trainer in town everyone is talking about! " + name + " right?^")
                            sleep(2)
                            print("^If you like i could show you around town?^")
                            sleep(3)
                            print("^Great! where do you wanna go first?^")
                            sleep(2)
                            print("^Personally my favorite place is the botanical garden, but some people prefer the disco nearby^")
                            sleep(2)
                            print("A. botanical garden    B. disco")
                            answer10 = input()
                            if answer10 in alist:
                                #leafeon evolution
                                print("^Awesome! Lets go!^")
                                sleep(2)
                                print("^The botanical garden is my favorite place in town!^")
                                sleep(2)
                                print("^Its so pretty in there!^")
                                sleep(2)
                                print("You spend the day at the garden with Gardenia while she tells you about all kinds of different flowers")
                                sleep(2)
                                print("Eevee has taken an interest in the flowers")
                                sleep(2)
                                print("Gardenia gives eevee a rose!")
                                sleep(2)
                                print("Eevee gains +20 love and +30 grass")
                                sleep(2)
                                print("""⬜⬜⬜🟩🟩🟩🟩⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬛🟩🟩🟩🟩🟩⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬛🟩🟩🟩🟩🟩🟩⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬛🟩🟩🟩🟩🟩🟩⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬛🟩🟩🟩🟩🟩🟩⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜🟩🟩🟩⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬛🟩🟩🟩🟩🟩🟩⬛🟩⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜🟩🟩🟩🟩🟩⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬛🟩🟩🟩🟩🟩🟩🟩🟩⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜🟩🟩🟩🟩🟩⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬛🟩🟩🟩🟩🟩🟩🟩🟩🟩⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛⬜🟩🟩🟩🟩🟩🟩⬜⬜
⬜⬜⬜⬜⬜⬜🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩⬛⬜⬜⬜⬜⬜⬜⬜⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜🟩🟩🟩🟩🟩⬛⬛🟩🟩🟩🟩🟩🟩⬜
⬜⬜⬜⬜⬜⬛🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩⬛⬜⬜⬜⬜⬜⬜⬛🟩⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜🟩🟩🟩🟩🟩🟩🟩🟩⬛🟩🟩🟩🟩🟩🟩
⬜⬜⬜⬜⬜⬛🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩⬛⬜⬜⬜⬜⬜⬜⬛🟩🟩⬛⬜⬜⬜⬜⬜⬜⬜🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩⬛🟩🟩🟩🟩⬜
⬜⬜⬜⬜⬜⬛🟩🟩🟩🟩🟩🟩🟩🟩🟩⬛⬜⬜⬜⬜⬜⬜⬜⬛🟩🟩🟩🟩🟩⬜⬜⬜⬜⬜🟩🟩🟩🟩🟩🟩⬛⬛⬛🟩⬛🟩🟩🟩🟩🟩
⬜⬜⬜⬜⬜⬛🟩🟩🟩🟩🟩🟩🟩🟩🟩⬛⬜⬜⬜⬜⬜⬜⬜⬛🟩🟩🟩🟩🟩🟩⬜⬜⬜⬛🟩🟩🟩🟩🟩⬛🟩🟩🟩⬛⬛🟩🟩🏿🟩🟩
⬜⬜⬜⬜⬜🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩⬛⬜⬜⬜⬜⬜⬜⬜⬛🟩🟩🟩🟩🟩🟩⬜⬜⬜⬛🟩🟩🟩🟩⬛🟫🟩🟩🟫🟩🟩🟩🟩🏿🟩🟩
⬜⬜⬜⬜⬛🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩⬛⬜⬜⬜⬜⬜⬜⬜⬛🟩🟩🟩🟩🟩🟩🟩🟩⬜⬛🟩🟩🟩🟩⬛🏻🟫🟫🏻🟫🟩🟩🟩🏿🏿🟩
⬜⬜⬛⬛🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩⬛⬜⬜⬜⬜⬜⬜⬜⬜⬛🟩🟩🟩🟩🟩🟩🟩🟩⬛⬜⬛🟩🟩🟩⬛🏻🏻🟧🏻🏻🟫🟩🟩🏿🏿🟩
⬜⬛🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛🟩🟩🟩🏿🟩🟩🟩🟩⬛⬜⬛🟩🟩🟩🟩⬛🏻🏻🟧🏻🏻🟧🏿🟫🏿🟩
⬛🟩🟩🟩🟩🟩🟩🟩🟩⬛⬛🟩🟩⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛🟩🟩🟫🏿🏿🟩🟩🟩⬛🟧🟩🟩🟩🟩🟩🟩🟩🏻🟧🏻🏻🏿🟫🏿🏻
⬛🟩🟩🟩🟩🟩🟩🟩🟩⬛⬜⬜⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛🟩🟫🟧🟫🏿🟩🟩🟩🟫🟧🏻🟩🟩🟩🟩🟩🟩🟧🟧🏻🏿🟫🏿🏻
⬛🟩🟩🟩🟩🟩🟩🟩🟩🟩⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛🟩🟩🟩🟧🟧🟫🏿🟩🏻🟫🏻🏻🟧🏻🟩🟩🟩🟩🟩🟧🏻🏻🏿🏻🏻
⬜⬛🟩🟩🟩🟩🟩🟩⬛🟩⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛🟩🟩🟩🟫🟧🟫🏿🏻🏻🟧🟧🏻🏻🟧🏻🏻🟩🟩🟩🏻🏻🏻🏿🏻🏻
⬜⬛🟩🟩🟩🟩🟩🟩🟩⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛🟩🟩🟩🟧🟫🟫🏿🏻🏻🟫🏻🏻🟧🏻🏻🏻🟩🏻🏻🏻🏻🏻🏻🟫
⬜⬜⬛🟩🟩🟩🟩🟩🟩🟩🟫⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛🟩🏻🏻🏻🟧🏿🟧🏻🟫🏻🏻🏻🏻🏻🏻🏻🏻🏻🏻🏻🏻🏻🟧
⬜⬜⬛🟩🟩🟩🟩🟩🟩🟩🟫⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛🏻🏻🏻🏻🟧🏻🟧🏻🏻🏻🏻🏻🏻🏻🏻🏻🏻🏻🏻🟧🟫
⬜⬜⬜⬛⬛⬛🟩🟩🟩🟩🟩🟫⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛🏻🏻🏻🏻🏻🏻🏻🏻🏻🏻🏻🏻🏻🏻🏻🏿🏻🟧⬛
⬜⬜⬜⬜⬜⬜⬛🟩🟩🟩🟩🟩🟫⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛🏿🏻🏻🏻🏻🏿🏿🏻🏻🏻🏻🏻🏻🏻⬜🏿⬛⬜
⬜⬜⬜⬜⬜⬛🟩🟩🟩🟩🟩🏻🏻🟫🟫⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜🟩⬜⬜🟫🟧🟧🏻🏻🏻🏿🟫⬜🏿🏻🏻🏻🏻🏻🏻🟫🏿⬛⬜
⬜⬜⬜⬜⬜⬛⬛🟩🟩🟩🏻🟧🟧🏻🏻🟫🟫⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛🟩🟩⬜⬜⬛⬛🟧🏻🏻🟫🟫🟫🟫🏿🏻🏻🏻🏻🏻🟫🏻⬛⬜
⬜⬜⬜⬜⬜⬜⬜⬛⬛🏻🏻🏻🏻🟫🟫🟧🟧🟫⬜⬜⬜⬜⬜⬜⬜⬜⬛🟩🟩🟩🟩⬜⬜⬛🏿🏻🏻🟫🟫🟫🟧🏻🏻🏻🏻🏻🏻⬛⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛🟫🟧🟧🟫🟧🟫⬜⬜🟫🟫🟫🟫⬜⬜⬜⬛🟩🟩🟩🟩🏿🟧🟧🏿🏻🏻🏻🏻🏻🏻🏻🏻🟫🏻🟧⬛⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛🟧🟧🟫🟧🟫🟫🏻🏻🏻🏻🟧🟫🟫🟫🟫🟫🟧🟧🟧🟧🟧🟧🏿🟫🟧🏻🏻🏻🏻🟧🟧⬛⬛⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛🟫🟫🏻🏻🏻🏻🏻🏻🏻🏻🏻🏻🏻🏻🏻🟧🟧🟧🟧🟧🟧🟧🟫🟫🟫⬛⬛⬛⬛⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛🏻🏻🏻🏻🏻🏻🏻🏻🏻🏻🏻🏻🏻🏻🏻🏻🟧🟧🟧🟧🟧🟧⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛🏻🏻🏻🏻🏻🏻🏻🏻🏻🏻🏻🏻🏻🏻🏻🏻🏻🏻🟧🟧🟧⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛🟧🟧🏻🏻🏻🏻🏻🏻🏻🏻🏻🏻🏻🏻🏻🏻🏻🏻🏻🏻🏻🏻⬛🟩🟩⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛🏻🟧🟧🟧🟧🏻🏻🏻🏻🏻🏻🏻🏻🏻🏻🏻🏻🏻🏻🏻🏻🟩🟩🟩🟩🟩⬜🟩🟩⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛🟧🏻🟧🟧🟧🟧🟧🟫🟧🟧🏻🏻🏻🏻🏻🏻🏻🏻🏻🏻🟩🟩🟩🟩🟩🟩🟩🟩🟩⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛🟧🏻🟧🏻🟧🟧🟧🟫🟧🟧🟧🟧🟧🟧🟧🟫🏻🏻🏻🏻🏻🟩🟩🟩🟩🟩🟩🟩⬛⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛🏻🟧🏻🟧🟧🟧🟧🏽🏽🏽🏽🏽🏽🏽🟧🟧⬛🏻🏻🏻🏻🟧⬛🟩🟩⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛🟧🟧🟧🟧🟧🟧🟧🏿🟧🟧🟧🟧🏿⬜⬜🏽🏽⬛🟧🏻🏻🏻🏻🏿⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛🟧🟧🟧🟧🟧🟧🟫🏿🟧🟧🟧🟧🏿⬜⬜⬜⬜⬜⬜⬛🏻🏻🏻🏻🏿⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛🟧🟧🟧🟧🟫🏿🟫🟧🟧🟧🟧🏿🏿⬜⬜⬜⬜⬜⬜🏿🟧🏻🏻🏻🏻🟩⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛🟩🟧🟧🟧⬛⬜⬜🏿🟧🟧🟧⬛⬜⬜⬜⬜⬜⬜🏿🏿⬛🏻🏻🏻🟩🟩🟩🟩⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜🟩🟩🟩🟩🟩🟧🟧⬛⬜⬜🏿🟧🟧🟧⬛⬜⬜⬜⬜⬜⬜⬛🏿⬛🟩🏻🏻🟩🟩🟩🟩🟩⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜🟩🟩⬛🟧🟧🟧⬛⬜⬜⬜⬛🏿🏿🟫⬜⬜⬜⬜⬜⬜⬛🏿🏿🟩🟩🟧🟧🟩🟩🟩⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛🟫🟧🟧⬛⬜⬜⬜⬛🏿🏿🏿⬛⬜⬜⬜⬜⬜⬜⬛🟩🟩⬛🟧🟧🟧🏿⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛🟫🟫⬛⬜⬜⬜⬜⬛🏿🏿⬛⬜⬜⬜⬜⬜⬜⬛🏿🏿🏿🟫🟫🟫🟫🏿⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛🟫🟫🟫⬛⬜⬜⬜⬜⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜⬛⬛⬜⬛🟫🟫🟫🏿🏿⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛🟫🟫⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛🟫🏿🟫🏿⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜""")
                                sleep(1)
                                print("Oh? Eevee is evolving!")
                                sleep(3)
                                print("Eevee has evolved into a Leafeon!")
                                sleep(2)
                                print("-some time later in the future-")
                                sleep(2)
                                print("You and Gardenia are friends now and you have a job at the towns garden with leafeon")
                                sleep(2)
                                print("You and " + Eevee + " have settled into lavendertown nicely")
                                sleep(3)
                                print("Congratulations! You got the leafeon ending!")
                                sleep(2)
                                print("You can try to get a different ending by playing again")
                                sleep(2)
                                print("Good job " + name)
                                sleep(3)
                            if answer10 in blist:
                                #Umbreon
                                print("^Alright! It is a great place to meet people!^")
                                sleep(2)
                                print("Gardenia takes you to the disco")
                                sleep(2)
                                print("She introduces you to some of her friends")
                                sleep(2)
                                print("You dance the night away")
                                sleep(2)
                                print("Eevee has taken an interest into the neon lights")
                                sleep(2)
                                print(Eevee + " likes the disco")
                                sleep(2)
                                print("+10 love, +40 darkness")
                                sleep(2)
                                print("Oh? Eevee is evolving!")
                                sleep(3)
                                print("""⡏⠀⠀⠀⠀⠱⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢡⣠⣶⣾⣿⣿⡇⠀⣀⣀⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣀⣀
⠈⣿⣿⣿⡿⠟⣋⢝⣋⠒⡄⠀⠀⠈⠉⠒⢤⣀⣀⠤⠐⠒⠫⣍⠀⠀⠈⢫⡘⢿
⠀⠈⣻⠋⠀⡜⡱⠋⡜⠀⡇⠀⠀⠀⠀⠀⠙⠁⠀⠀⠀⠀⠀⠈⢦⠀⠀⠀⢳⣾
⠀⢰⢋⡀⢸⡀⠧⠊⢀⠜⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡄⠀⠀⢸⣿
⠀⣧⣿⣻⡀⠑⠒⠊⠁⠀⢀⣤⣶⢦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣁⡠⠤⠛⠁
⠀⣿⠻⢿⠁⠀⠀⠀⠀⢠⣾⣿⣿⣶⣿⣆⠀⠀⢹⠏⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀
⢸⡿⠿⠿⠀⠄⠀⠀⠀⢸⢉⣙⡟⢻⣥⡾⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠘⢧⠀⠀⠀⠀⣀⠀⠀⠈⠓⠒⠒⠚⠋⠁⠒⢆⠎⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠈⠳⢄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠔⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠈⠉⣲⠆⠀⠀⠀⠀⠀⠀⠛⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡠⠴
⠀⠀⠀⠀⠀⠰⣿⡄⠀⠀⠀⠀⠀⠀⠀⠘⢦⡀⠀⠀⠀⠀⠀⠀⠀⣠⠴⣍⣀⠀
⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠓⢤⣀⠤⠤⢄⡞⠅⠁⠀⢩⣿
⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢈⣳⣤⣎⣠⡀⣀⣴⣿⣿
⠀⠀⠀⠀⠀⠀⠎⡇⠀⠀⠀⠀⠀⢠⣠⣤⣤⣶⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿""")
                                print("Eevee has evolved into an Umbreon!")
                                sleep(2)
                                print("- some time later in the future -")
                                sleep(2)
                                print("You and Gardenia are good friends and go out often")
                                sleep(2)
                                print("You got a job at the disco with umbreon")
                                sleep(2)
                                print("You and " + Eevee + " have settled into lavendertown nicely")
                                sleep(3)
                                print("Congratulations! You got the Umbreon ending!")
                                sleep(2)
                                print("You can try and get a different ending by playing again")
                                sleep(2)
                                print("Good job " + name)
                                sleep(3)
                        if answer7 in dlist:
                            #Vaporeon or Glaceon evolution
                            print("You knock on the blue door...")
                            sleep(2)
                            print("A girl opens the door, it's aqua!")
                            sleep(2)
                            print("^Oh hello! You must be the new trainer in town everyone is talking about! " + name + " right?^")
                            sleep(2)
                            print("^If you like i could show you around town?^")
                            sleep(2)
                            print("^Great! where do you wanna go first?^")
                            sleep(2)
                            print("^I love the waterpark and the ice rink! They are the best places in town!^")
                            sleep(2)
                            print("A. waterpark     B. ice rink")
                            answer11 = input()
                            if answer11 in alist:
                                #vaporeon evolution
                                print("^YAY! I havent been there in such a long time!^")
                                sleep(2)
                                print("^I absolutely love the waterpark! I go there with Magicarp a lot!")
                                sleep(2)
                                print("You and Aqua go to the waterpark")
                                sleep(2)
                                print("Eevee seems to like the water")
                                sleep(2)
                                print("You and eevee go down the waterslide")
                                sleep(2)
                                print("Eevee gains +10 love and +50 water")
                                sleep(2)
                                print("""⬜⬜⬜⬜⬜⬜⬜⬜⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜🟦⬛⬜⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬛⬜⬜⬛⬜⬛⬜⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜🟦⬛⬜⬜🟦⬛⬜⬛🟦🟦⬛⬛⬛⬜⬛⬛🟦⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬛⬜⬜🟦⬜⬜⬜⬛🟦🟦🟦🟦⬛⬛⬜⬜⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜🟦⬛⬜⬜🟦⬜⬜🟦⬛🟦🟦🟦⬛⬛⬜⬜⬜⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬛⬜⬜🟦⬜⬜🟦⬛🟦🟦⬛⬛⬛⬜⬜⬜🟦⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜🟦⬛⬜⬜🟦⬜🟦⬜⬛🟦🟦⬛⬛⬜⬜⬜🟦⬛🟦⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬛⬛⬜🟦⬜⬜⬛⬛⬛⬛⬛⬛⬜⬜⬜⬜🟦⬛🟦🟦⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜🟦⬛⬜⬜🟦⬛⬛🟦🟦⬛⬛⬛🟦⬜⬜⬜🟦⬜⬛🟦🟦🟦⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬛⬛⬜⬛⬛⬛⬛⬛⬛⬛⬛⬛⬜⬜⬜🟦⬜⬜⬛⬜⬜⬜⬛⬛⬛⬛⬜⬜⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬛⬛⬛⬛⬛⬛🟦🟦🟦⬛⬛🟦⬜⬜⬜⬜⬜🟦⬛⬜⬜⬜⬛🟦⬛🟦⬛🟦⬛🟦⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬛⬛⬛⬛⬛⬛🟦🟦🟦🟦🟦⬛⬜⬜⬜⬜⬜🟦🟦⬜⬛🟦⬛🟦⬛🟦⬛🟦⬛🟦⬛🟦⬛🟦⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬛🟦⬛⬛⬛🟦🟦🟦🟦🟦🟦🟦⬜⬜⬜⬜🟦⬜⬜⬛🟦🟦⬛⬛🟦⬛🟦⬛⬛⬛⬛⬛⬛⬛🟦⬛⬛⬜⬜⬜⬜⬜⬜⬜
⬜🟦🟦⬛⬛🟦🟦🟦🟦⬛⬛🟦🟦⬜⬜⬜🟦⬜⬜⬛🟦🟦🟦⬛⬛⬛⬛⬛🟦🟦🟦🟦🟦🟦⬛⬛🟦⬛⬛⬜⬜⬜⬜⬜⬜
⬛🟦🟦⬛⬛🟦🟦🟦⬛⬛⬛🟦🟦🟦⬜⬜⬜⬜⬜⬛⬜⬜⬛🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦⬛🟦⬛⬛⬜⬜⬜⬜⬜
⬛🟦🟦⬛🟦🟦🟦⬛⬜⬛⬛🟦🟦🟦🟦⬜⬛⬛⬛🟦⬜⬜⬛🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦⬛⬛⬛⬜⬜⬜⬜⬜
⬜⬛⬛⬛🟦🟦🟦⬛⬛⬛🟦🟦🟦🟦🟦⬛🟦🟦🟦🟦🟦🟦⬛🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦⬛⬜⬜⬜⬜
⬜⬛⬜⬛🟦🟦🟦⬛🟦🟦🟦🟦🟦🟦🟦⬛🟦🟦⬜⬜⬜⬛⬛🟦🟦🟦🟦🟦🟦🟦🟦⬛🟦🟦🟦🟦🟦🟦🟦🟦🟦⬛⬜⬜⬜
⬜⬛⬜⬜⬜🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦⬛🟦🟦⬜⬜⬜⬛🟦🟦🟦🟦🟦🟦🟦🟦🟦⬛🟦🟦🟦🟦🟦🟦🟦🟦🟦⬛⬜⬜⬜
⬜⬜⬛⬜⬜🟦🟦🟦🟦🟦🟦🟦🟦🟦⬛🟦🟦🟦🟦🟦⬛🟦⬛🟦🟦🟦🟦🟦🟦🟦🟦⬛🟦🟦🟦🟦🟦🟦🟦⬛🟦🟦⬛⬜⬜
⬜⬜⬛⬛🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦⬛🟦🟦🟦⬜⬜🟦⬛🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦⬛🟦🟦🟦🟦🟦🟦⬛🟦🟦⬛⬜⬜
⬜⬜⬛🟦🟦⬛⬛🟦🟦🟦🟦🟦🟦⬛🟦🟦🟦🟦⬛⬛⬛🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦⬛🟦🟦🟦🟦🟦🟦⬛🟦🟦🟦⬛⬜
⬜⬜⬜⬛⬛🟦🟦🟦🟦🟦🟦⬛⬛🟦🟦🟦⬛⬛🟦🟦🟦🟦🟦🟦🟦⬛🟦🟦🟦🟦🟦🟦🟦⬛🟦🟦🟦🟦🟦🟦⬛🟦🟦⬛⬜
⬜⬜⬜🟦⬜⬛⬛⬛⬛⬛⬛⬜🟦🟦🟦⬛🟦🟦🟦🟦🟦🟦🟦🟦⬛🟦🟦🟦🟦🟦🟦🟦🟦⬛⬛🟦🟦🟦🟦🟦⬛🟦🟦⬛⬜
⬜⬜⬜⬜🟦⬜⬜⬜⬜🟦⬜⬜⬜🟦⬛🟦⬛🟦🟦🟦🟦⬛⬛⬛⬛⬛⬛⬛🟦🟦🟦⬛⬛⬜⬛🟦🟦🟦🟦🟦⬛🟦🟦⬛⬜
⬜⬜⬜⬜⬜🟦🟦⬜⬜🟦⬜⬜⬜⬜⬛🟦🟦⬛⬛⬛⬛⬜⬜⬛⬛⬛⬛⬛⬛⬛⬛⬛⬜⬜⬜⬛🟦🟦🟦🟦⬛🟦🟦🟦⬛
⬜⬜⬜⬜⬜⬜⬛⬛⬜⬜⬛⬛⬜⬜🟦⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛⬛⬛⬜⬜⬜⬛🟦🟦🟦🟦⬛🟦🟦🟦⬛
⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛🟦🟦⬛⬛⬛🟦🟦⬛⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛⬛🟦🟦⬛⬜⬜⬜⬛🟦🟦🟦🟦⬛🟦🟦🟦⬛
⬜⬜⬜⬜⬜⬜⬛🟦🟦🟦🟦🟦🟦🟦🟦⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛🟦🟦🟦🟦⬛⬜⬜⬛🟦🟦🟦🟦⬛🟦🟦🟦⬛
⬜⬜⬜⬜⬜⬛🟦🟦🟦🟦🟦🟦🟦⬛⬛⬜⬜⬜⬜⬜⬛🟦⬛⬜⬜⬜⬜⬛🟦🟦🟦🟦⬛⬜⬜⬛🟦🟦🟦⬛🟦🟦🟦🟦⬛
⬜⬜⬛⬛⬛🟦🟦🟦🟦🟦🟦⬛⬛⬜⬜⬜⬜⬜⬜⬜⬛🟦🟦⬛⬛⬜⬜⬛🟦🟦🟦🟦⬛⬜⬜⬛🟦🟦🟦⬛🟦🟦🟦⬛⬜
⬜🟦🟦🟦🟦🟦🟦🟦🟦🟦⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛🟦🟦🟦🟦⬛⬛🟦🟦🟦🟦⬛⬜⬜⬛🟦🟦🟦🟦⬛🟦🟦🟦⬛⬜
⬛🟦🟦🟦🟦🟦🟦🟦⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛🟦🟦🟦⬛🟦🟦🟦🟦⬛⬜⬜⬜⬛🟦🟦🟦⬛🟦🟦🟦⬛⬜⬜
⬛🟦⬛🟦🟦⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛🟦🟦🟦⬛🟦🟦🟦🟦⬛⬜⬜⬛🟦🟦🟦🟦⬛🟦🟦🟦⬛⬜⬜
⬜⬛⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛🟦🟦🟦⬛🟦🟦⬛⬜⬜⬜⬛🟦🟦🟦🟦⬛🟦🟦⬛⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛🟦🟦🟦⬛⬛⬜⬜⬜⬛⬛🟦⬛🟦⬛🟦🟦⬛⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜🟦🟦🟦🟦🟦🟦🟦⬛⬛⬛🟦🟦⬛⬛⬛🟦⬛⬛⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦⬛⬛⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦⬛⬛⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛🟦🟦🟦🟦🟦🟦⬛⬛⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛🟦🟦🟦🟦⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜""")
                                sleep(1)
                                print("Oh? Eevee is evolving!")
                                sleep(2)
                                print("Eevee has evolved into a Vaporeon!")
                                sleep(3)
                                print("-some time later in the future")
                                sleep(2)
                                print("You got a job at the waterpark with vaporeon")
                                sleep(2)
                                print("You are friends with aqua and give her your employe discount at the waterpark")
                                sleep(2)
                                print("Vaporeon and magicarp are now best friends!")
                                friend = friend + 1

                                sleep(2)
                                print("You and " + Eevee + " have settled into lavedertown nicely")
                                sleep(3)
                                print("Congratulations! You got the Vaporeon ending!")
                                sleep(2)
                                print("You can try and get a different ending by playing again")
                                sleep(2)
                                print("Im proud of you " + name)
                                sleep(3)
                            if answer11 in blist:
                                #glaceon evoluton
                                print("^Good choice, its such a lovely place!^")
                                sleep(2)
                                print("^Me and Cubchoo come here a lot^")
                                sleep(2)
                                print("Aqua shows you around the icerink and you two skate together")
                                sleep(2)
                                print("Eevee skates with Cubchoo and seems to like the ice")
                                sleep(2)
                                print("Eevee gains +10 love and +30 ice")
                                sleep(2)
                                print("Oh? Eevee is evolving!")
                                sleep(2)
                                print("""⠀⣰⣶⣿⣺⣷⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣼⡿⣧⠈⠉⠿⣿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣿⣿⡇⢹⣶⡀⠙⣿⣿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣿⡟⠃⢸⣿⣿⠀⠛⣿⣿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣿⠇⠀⢸⡏⣽⣿⡄⠀⢹⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣿⣆⡀⢸⣿⠉⢿⣷⡀⠈⢹⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠏⣿⣇⣸⣿⣀⠘⣿⡧⣄⣸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⡇⠈⢹⡏⢸⣿⣥⣿⠀⢹⣿⣿⣶⣶⣶⣶⣦⣄⠀⠀⠀⠀⠀⠀⢀⣶⣶⣾⠛⠛⢻⣶⣶⣶⣶⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⡇⠀⠈⣿⣿⠙⣿⡿⣷⣿⣿⣯⣉⠉⠉⠉⠻⠿⢿⣷⣦⣴⣾⡿⠿⠏⠉⠉⣀⣀⡈⠉⠉⠉⠉⠿⠿⠿⣿⣦⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⡇⠀⢀⣽⣿⣶⡛⢷⠉⠉⠉⢻⣿⠘⣶⣆⠀⠀⠈⢉⣹⣿⠏⠁⡀⣰⣶⣶⣿⣿⣷⣶⣶⣶⣦⣀⣀⠀⠘⢉⣹⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⡇⢰⣿⣿⣿⠀⣿⡆⠀⠀⠀⢸⣿⠟⠛⠻⣧⣤⡼⠛⠀⠀⣤⣿⣿⣿⠛⠛⠀⠀⠛⣿⡟⠛⠛⡉⠉⣭⣥⣾⡟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⡇⢸⣿⡏⢸⣿⣅⡀⠀⢠⣼⣿⠁⠀⠀⠀⠹⢿⣇⢀⣠⠿⠋⠀⠀⠹⠿⠿⠿⠿⠋⠉⢡⣤⣠⣿⠿⠛⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⡇⠈⠛⣿⣿⣻⣿⣷⣶⣿⣿⣉⣀⣀⣀⣀⣶⣾⣿⡾⠉⠷⠶⣷⣶⣦⣀⣀⣀⣀⣿⣶⡟⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⡇⠀⠀⢹⣿⣿⠛⣿⣿⣧⡀⡉⣉⣝⣿⣿⣿⣿⣿⡇⠀⠀⠀⣿⡏⠙⠛⠛⠛⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠃⠀⠀⡾⢷⣤⠀⠀⠀⠙⠛⠛⠿⣶⣦⣤⠀⢻⣿⣧⠀⠀⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⡆⠀⠀⢻⡟⠉⣀⡀⠀⠀⢀⣸⣾⣉⣿⣿⡆⣼⡏⢻⣿⣾⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⡇⠀⠀⠘⢿⣦⡛⠁⠀⠀⠈⠙⠛⣿⣿⠛⣳⣿⡗⢸⣿⠛⣿⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣶⣿⣿⣿
⡇⠀⠀⠀⠀⣿⣿⣿⣦⡄⠀⠀⠀⠀⠀⠜⠁⢹⡇⢸⣿⠚⣿⣷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣠⣶⣾⡟⠟⠛⠀⢸⣿
⡇⠀⠀⠀⣤⣿⠿⠏⣿⡿⠿⠷⣶⣤⠀⠀⠀⢻⣧⠸⢿⣄⠈⠿⢿⣶⣤⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⠿⠿⠉⠉⠀⠀⠀⠀⢸⣿
⡇⠀⠀⠀⣿⣿⠀⠀⣿⣧⡄⠀⣾⣿⢤⣤⣶⡞⠉⠀⢸⣿⡀⠀⠈⠉⣽⣿⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⡏⠉⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿
⡇⠀⠀⣾⣿⠛⠀⠀⠀⣼⣧⣿⣿⠛⠀⠀⢸⡇⠀⠀⠈⢻⣷⠄⠀⠀⠘⣿⡿⣿⣿⣶⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿
⡇⠀⣠⣿⣿⠀⣤⣿⣥⡿⢿⣿⣿⠀⠀⠀⢸⡇⢰⣼⣿⣤⣿⡆⠀⠀⠀⠀⠷⣦⠉⠻⠿⢿⣷⣶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⠿⠇⠀⠀⠀⠀⠀⠀⠀⠀⢰⣼⣿
⡃⢸⣿⣏⣹⠿⠃⠀⢻⣇⣸⣿⣿⠀⠀⣿⡏⢿⡿⠃⠉⢿⣍⣿⡆⠀⠀⠀⠀⠹⠷⠤⠶⠮⠭⠉⠿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⡿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿
⡅⢸⣿⣏⠉⠀⠀⠀⠘⣿⣿⣿⣿⢤⡀⣿⣷⣾⠁⠀⠀⠀⠉⠛⢷⣦⠀⠀⠀⠀⠈⠉⠀⠀⠀⠀⠀⠛⢻⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡁⣿⣀⠀⠀⢀⣤⣤⣤⣴⣟⣻⣿⢻
⠀⠘⢿⣷⣄⠀⠀⡀⣤⣿⠏⠛⣿⣤⣿⡀⣹⣏⠀⠀⠀⠀⢀⣶⡟⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⢿⣷⡄⠀⠀⠀⠀⠀⣠⣾⠛⠀⠀⠛⠛⠓⠒⠛⠛⠀⣤⣤⣿⡿⠛⠛
⡀⠀⠀⠙⠿⣿⣾⣿⠛⠁⠀⠀⠙⢿⣍⣷⡋⢹⣇⠀⠀⠀⣿⡉⠁⢠⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡶⠃⢸⣿⡇⠀⣀⣠⡶⠾⠿⠉⠀⠀⠀⣤⣤⣤⣼⣿⣿⠿⠛⠛⠁⠀⠀⠀
⠁⠀⠀⠀⠀⠀⠉⠀⠀⠀⠀⠀⠀⠀⣿⠉⢳⡎⢹⣷⣤⣾⣯⡁⢰⣾⠉⠀⠀⠀⠀⠀⠀⠀⣠⡾⠋⠀⠀⢸⣿⣿⣿⠉⠉⣳⣄⣀⢰⣶⣶⣶⠟⠛⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣦⣾⣧⡤⢸⣿⣦⠀⣿⡿⠇⠀⠀⠀⠀⣤⠤⠾⠉⠉⠀⠀⠀⠀⣸⣷⣦⣤⣴⣦⡿⠿⠟⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⡗⠈⢻⣿⣿⣦⣿⣧⣽⣟⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⢸⣿⣼⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣶⣿⡟⠃⢀⣸⣿⠿⣿⣿⡟⢛⣛⠻⣷⣄⡀⠀⢀⣀⣀⣀⣶⣶⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠿⣿⣷⣶⡾⡏⠁⠀⠘⠻⣷⣿⣿⣿⣾⣿⣷⣶⣾⣿⡿⡿⣿⢉⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀""")
                                sleep(1)
                                print("Eevee has evolved into a Glaceon!")
                                sleep(2)
                                print("-some time later in the future")
                                sleep(2)
                                print("You and aqua became friends")
                                sleep(2)
                                print("You and Glaceon got a job at the ice rink, Glaceon helps keep the ice frozen and you go over the ice with a Zamboni")
                                sleep(2)
                                print("Glaceon is now best friends with Cubchoo")
                                sleep(2)
                                print("You two settled into lavendertown nicely")
                                sleep(3)
                                print("Congratulations! You got the Glaceon ending!")
                                sleep(2)
                                print("You can try and get a different ending by playing again")
                                sleep(2)
                                print("Good job " + name)
                                sleep(3)
                    if answer6 == "no":
                        #you die
                        sleep(2)
                        print("You go back and go on the safe looking path instead...")
                        sleep(2)
                        print("There is a funny looking Gengar there")
                        print("⠀⠀⠀⠀⠀⢸⠓⢄⡀⠀⠀⠀⠀")
                        print("⠀⠀⠀⠀⠀⢸⠀⠀⠑⢤⡀")
                        print("⠀⠀⠀⠀⠀⢸⡆⠀⠀⠀⠙⢤⡷⣤⣦⣀⠤⠖⠚⡿⠁⠀")
                        print("⣠⡿⠢⢄⡀⠀⡇⠀⠀⠀⠀⠀⠉⠀⠀⠀⠀⠀⠸⠷⣶⠂⠀⠀⠀⣀⣀⠀⠀")
                        print("⢸⣃⠀⠀⠉⠳⣷⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠉⠉⠉⠉⢉⡭⠋")
                        print("⠀⠘⣆⠀⠀⠀⠁⠀⢀⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠋⠀⠀")
                        print("⠀⠀⠘⣦⠆⠀⠀⢀⡎⢹⡀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⡀⣠⠔⠋⠀")
                        print("⠀⠀⠀⡏⠀⠀⣆⠘⣄⠸⢧⠀⠀⠀⠀⢀⣠⠖⢻⠀⠀⠀⣿⢥⣄⣀")
                        print("⠀⠀⢸⠁⠀⠀⡏⢣⣌⠙⠚⠀⠀⠠⣖⡛⠀⣠⠏⠀⠀⠀⠇⠀⠀⠀⠀⢙⣣⠄")
                        print("⠀⠀⢸⡀⠀⠀⠳⡞⠈⢻⠶⠤⣄⣀⣈⣉⣉⣡⡔⠀⠀⢀⠀⠀⣀⡤⠖⠚⠀")
                        print("⠀⠀⡼⣇⠀⠀⠀⠙⠦⣞⡀⠀⢀⡏⠀⢸⣣⠞⠀⠀⠀⡼⠚⠋⠁⠀⠀")
                        print("⠀⢰⡇⠙⠀⠀⠀⠀⠀⠀⠉⠙⠚⠒⠚⠉⠀⠀⠀⠀⡼⠁⠀")
                        print("⠀⠀⢧⡀⠀⢠⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣞⠁⠀")
                        print("⠀⠀⠀⠙⣶⣶⣿⠢⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀")
                        print("⠀⠀⠀⠀⠀⠉⠀⠀⠀⠙⢿⣳⠞⠳⡄⠀⠀⠀⢀⡞⠀")
                        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠀⠀⠹⣄⣀⡤⠋⠀")
                        sleep(2)
                        print("OH!") 
                        sleep(1)
                        print("It wants to battle...")
                        sleep(2)
                        print("The Gengar used Shadow ball")
                        sleep(1)
                        print("CRITICAL HIT!")
                        sleep(1)
                        print("Your Eevee fainted")
                        sleep(1)
                        print("You died...")
                        sleep(2)
                        print("You got the Eevee battle ending!")
                        sleep(1)
                        print("You can play again to try and get a different ending")
                        sleep(2)
                
                
            if answer2 in blist:
                print("You go on the short path")
                sleep(2)
                print("The path is difficult and your eevee gets very stressed")
                sleep(2)
                print("Eevee gets stuck and you free her")
                sleep(2)
                print("*your eevee didnt gain love*")
                sleep(2)
                print("-you arrive in lavender town-")
                winsound.PlaySound(None, winsound.SND_PURGE)
                sleep(2)
                winsound.PlaySound('lavender-.wav', winsound.SND_ASYNC)
                sleep(2)
                print("After a long and hard journey you and eevee can finally rest on a bench")
                sleep(2)
                print("A townsperson walks up to you...")
                sleep(2)
                print("^Hello my name is Lila^")
                sleep(2)
                print("^I saw your Eevee over there and i was wondering if she would like to play with my pikachu?^")
                sleep(2)
                print("Do you want " + Eevee + " to play with pikachu? yes/no")
                answer3 = input()
                if answer3 == "yes":    
                    print("^Great!^")
                    sleep(2)
                    print("Eevee and pikachu have a great time")
                    sleep(2)
                    print(Eevee + " has made a friend!")
                    sleep(2)
                    print("Eevee gained +10 love")
                    sleep(2)
                    print("^It seems like pikachu and Eevee get along great!^")
                    sleep(2)
                    print("^would you like to go to the towns bonfire with me an pikachu?")
                    sleep(2)
                    print("A. accept the invitation    B. Ask her out on a walk in the moonlight instead  a/b")
                    answer4 = input()
                    if answer4 in alist:
                        print("^Lovely! I cant wait for you to meet all the others!^")
                        sleep(2)
                        print("You and Lila go to the towns bonfire and she introduces you to all the people there")
                        sleep(2)
                        print("Your Eevee is getting along great with all the other pokemon!")
                        sleep(2)
                        print(Eevee + " has made a bunch of friends!")
                        sleep(2)
                        print("*+10 love*")
                        sleep(1)
                        print("Oh? Eevee is evolving!")
                        sleep(1)
                        print("""⠐⢦⣰⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣤⡖⠀
⠀⠈⣿⣿⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣾⣿⡟⠀⠀
⠀⠀⠘⣿⣇⠉⠻⢷⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⠿⠛⢁⣿⡿⠀⠀⠀
⠀⠀⠀⠸⣿⡄⠀⠀⠉⠻⣷⣾⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠀⠀⠀⠀⠀⠀⠀⠀⣶⣶⡿⠋⠁⠀⠀⣸⣿⠁⠀⠀⠀
⠀⠀⠀⠀⢻⣧⠀⠀⠀⠀⠈⠻⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠘⡿⣦⡀⠀⠀⠀⢀⣴⡿⠋⠀⠀⠀⠀⢀⣿⠇⠀⠀⠀⠀
⠀⠀⠀⠀⠈⣿⡆⠀⠀⠀⠀⠀⠈⢿⣧⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⢳⡀⠀⢠⣾⠟⠀⠀⠀⠀⠀⠀⣼⡿⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢹⣷⠀⠀⠀⠀⠀⠀⠈⢿⣧⠀⠀⠀⠀⠀⣀⣴⠏⠀⠀⢷⢠⣿⠏⠀⠀⠀⠀⠀⠀⢰⣿⠃⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢿⣧⠀⠀⠀⠀⠀⠀⠈⣿⣇⠀⡤⠚⠉⠁⠀⠀⠀⠀⢸⣿⡟⠀⠀⠀⠀⠀⠀⢠⣿⡏⠀⠀⢀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⠻⢿⣶⣄⣀⠀⢀⡀⣻⣿⡞⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⡇⢀⠀⢀⣀⣤⣾⠿⠛⠀⠀⢀⣿⡎⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠻⢿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⣶⣿⣿⣿⣿⣿⡿⠛⠉⠀⠀⠀⠀⠀⢼⣿⣿⡀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡄⣠⣾⠿⣿⣿⣿⣷⣄⠀⠀⠀⠀⢀⣼⣿⣿⣿⣿⠟⠛⢿⣆⡆⠀⠀⠀⠀⢶⣾⣿⣿⣿⡀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣝⠟⠃⠀⠀⣿⣿⣿⣿⣿⣶⣶⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠁⡇⠀⠀⠀⠀⢸⣿⣿⣿⣿⡇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣷⣿⠀⠀⠀⢸⡁⠀⠀⠙⣿⣿⣿⣿⣿⡟⠁⠀⠀⢹⠀⠀⠀⠀⢻⣤⣤⣤⣴⣿⣿⣿⣿⣿⠃
⠀⠀⠀⠀⠀⠀⠀⠐⢦⣾⠁⠀⠀⠀⠸⣧⣀⠀⠀⣹⣿⣿⣿⣿⡇⠀⢀⣠⣿⠁⠀⠀⠀⠀⢹⣿⣿⣿⣿⣿⣿⣿⠏⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠘⡆⠀⠀⠀⠀⠀⠻⣿⣿⣿⣿⣿⠿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿⣟⣀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣧⠀⠀⠀⠀⠀⠀⠈⠛⠿⢿⣿⣿⣿⣿⡿⠟⠋⠀⠀⠀⠀⠀⠀⠐⣽⣿⣿⣿⣿⣿⣿⠟⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠘⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⢫⣿⣿⣿⣿⡟⠁⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⣿⣿⣿⣿⣿⣶⡤⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢼⡃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⢾⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠒⢮⣁⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣴⣾⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⣷⣶⣤⠄⣀⣀⣀⣀⠀⢀⣦⣄⣀⣀⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⡏⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠿⠿⠄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⡿⠿⣿⡋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢴⣿⣿⣿⣿⣿⣿⣿⣿⡇⢿⣿⣿⣿⣿⣿⣿⣿⣷⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠉⠸⢿⣿⠿⠋⠀⠈⠻⢿⣿⠿⠋⠙⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀""")
                        sleep(2)
                        print("Eevee has evolved into a Flareon!")
                        sleep(2)
                        print("She must have loved the bonfire so much she evolved into a fire type!")
                        sleep(2)
                        print("some time later...")
                        sleep(2)
                        print('You and ' + Eevee + " made a bunch of friends!")
                        sleep(2)
                        print("You two fit right in with the lavender town people")
                        sleep(3)
                        print("Congratulations! You have made it to the Sylveon bonfire ending!")
                        sleep(2)
                        print("I am so proud of you " + name)
                        sleep(3)
                    if answer4 in blist:
                        #pikachu and eevee kiss, eevee turns into umbreon
                        print("^Oh! uhmm sure, i would love too! :o ^")
                        sleep(2)
                        print("You and Lila go on a walk in the moonlight...")
                        sleep(2)
                        print("Pikachu and Eevee are playing together")
                        sleep(2)
                        print("oh? Pikachu kisses Eevee, +10 love")
                        sleep(2)
                        print("Eevee is filled with love under the moon")
                        sleep(2)
                        print(Eevee + " is evolving!")
                        print("""⡏⠀⠀⠀⠀⠱⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢡⣠⣶⣾⣿⣿⡇⠀⣀⣀⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣀⣀
⠈⣿⣿⣿⡿⠟⣋⢝⣋⠒⡄⠀⠀⠈⠉⠒⢤⣀⣀⠤⠐⠒⠫⣍⠀⠀⠈⢫⡘⢿
⠀⠈⣻⠋⠀⡜⡱⠋⡜⠀⡇⠀⠀⠀⠀⠀⠙⠁⠀⠀⠀⠀⠀⠈⢦⠀⠀⠀⢳⣾
⠀⢰⢋⡀⢸⡀⠧⠊⢀⠜⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡄⠀⠀⢸⣿
⠀⣧⣿⣻⡀⠑⠒⠊⠁⠀⢀⣤⣶⢦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣁⡠⠤⠛⠁
⠀⣿⠻⢿⠁⠀⠀⠀⠀⢠⣾⣿⣿⣶⣿⣆⠀⠀⢹⠏⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀
⢸⡿⠿⠿⠀⠄⠀⠀⠀⢸⢉⣙⡟⢻⣥⡾⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠘⢧⠀⠀⠀⠀⣀⠀⠀⠈⠓⠒⠒⠚⠋⠁⠒⢆⠎⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠈⠳⢄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠔⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠈⠉⣲⠆⠀⠀⠀⠀⠀⠀⠛⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡠⠴
⠀⠀⠀⠀⠀⠰⣿⡄⠀⠀⠀⠀⠀⠀⠀⠘⢦⡀⠀⠀⠀⠀⠀⠀⠀⣠⠴⣍⣀⠀
⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠓⢤⣀⠤⠤⢄⡞⠅⠁⠀⢩⣿
⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢈⣳⣤⣎⣠⡀⣀⣴⣿⣿
⠀⠀⠀⠀⠀⠀⠎⡇⠀⠀⠀⠀⠀⢠⣠⣤⣤⣶⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿""")
                        sleep(3)
                        print("Eevee has evolved into an umbreon!")
                        sleep(2)
                        print("-some time later-")
                        sleep(2)
                        print("You and " + Eevee + " have settled in into lavender town!")
                        sleep(2)
                        print(Eevee + " and Pikachu got married")
                        sleep(3)
                        print("Congratulations! You got the umbreon love ending")
                        sleep(2)
                        friend = friend + 1
                        print("I am proud of you " + name)
                        sleep(3)
                if answer3 == "no":
                        print("^Thats a shame :(")
                        sleep(2)
                        print("^I guess i'll talk to you some other time...")
                        sleep(2)
                        print("You and Eevee dont make any friends after that and live a lonely life in lavender town")
                        sleep(3)
                        print("You made it to the end!")
                        sleep(2)
                        print("You got the lonely ending...")
                        sleep(2)
            if answer2 in clist:
                #you will die
                print("You go into the unicorn forest")
                sleep(2)
                print("It doesnt look as peaceful as you expected...")
                sleep(2)
                #a unicorn will kill you
                print("Something is rumbling in the bushes...")
                sleep(2)
                print("A unicorn comes running out of the bushes and hit you")
                sleep(2)
                print("Poor thing must have been scared, at least its okay now")
                sleep(2)
                print("You on the other hand...")
                sleep(2)
                print("You are fatally injured and bleeding out")
                sleep(2)
                print("You died, your body couldnt hold on and gave out because of your injuries")
                sleep(2)
                print("Maybe going into a unicorn forest wasn't the smartest bet...")
                sleep(3)
    if answer == "right":
            #bad choice, you die
            #there is a cliff and you slip and die
            print("You go on the right safe path...")
            sleep(2)
            print("You look at the beautiful view of the cliff and river to your right")
            sleep(2)
            print("Suddenly you slip and fall")
            sleep(2)
            print("You fell off the cliff, you have died")
            sleep(2)
            print("You got the death ending")
            sleep(2)
            print("You can play again to try and get a different ending")
            sleep(3)

    while True: 
        print("The amount of friends you obtained:")
        print(friend)
        sleep(1)
        print("Would you like to play again? yes/no")
        answer0 = input()
        if answer0 == "yes":
            sleep(1)
            print("""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡏⡀⠀⢄⠈⢙⢒⠲⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⠶⠚⠃⢣⠀⠸⣶⠋⢈⠇⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣠⠤⢄⡀⠀⠀⢀⣤⣶⢖⣿⣏⡷⠰⠞⠉⠉⢺⣇⠀⢹⠀⢸⡀⠋⢿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣠⠤⠶⣚⣋⡅⠀⠀⠙⣻⡟⠋⡔⠛⠉⠁⠙⣷⠀⠰⣿⡄⠀⢻⡆⠀⢧⠀⠙⢦⠀⡿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢸⣯⡵⠛⠛⠉⠈⣷⠀⠘⠉⠀⠙⢦⡀⠀⣾⣆⠀⢻⣇⠀⢳⣳⡀⠘⣷⣀⣨⠙⢲⣒⣤⢣⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢸⡿⡇⢴⠀⠀⣿⠈⣇⠀⢸⣣⡀⠘⣧⡀⠙⠿⠀⠈⣿⣄⣸⡏⢻⣾⣥⢨⣿⣿⠿⠛⠛⠉⠀⠀⣀⣤⣤⠤⠤⣒⡲⠤⠤⣤⣤⣤⣤⣀⡀⢧⡀⢹⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠙⠻⡆⢧⠀⠹⡄⢹⡄⠘⢏⢧⠀⢸⡷⣤⣤⣶⣚⠋⢸⠛⢳⣿⡅⠘⢇⢷⣿⠀⠀⣤⢔⣻⡯⠶⠛⠛⠋⠉⠉⠉⠉⣉⣉⣛⡛⠓⢲⣬⡝⣷⣤⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢿⡘⡆⠀⢻⠀⢳⣄⣼⠛⢳⣾⢥⣴⠛⠉⠁⠉⢻⡄⠈⢣⢣⠀⠸⡎⠈⣧⣯⡾⠋⠁⠀⣠⣤⣴⣾⣿⣿⣿⣿⠿⢛⣭⣴⣿⡿⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢧⡛⠀⠚⢰⣿⣿⠛⠳⣼⡇⠀⣿⠀⠘⣟⡄⠈⢳⡀⠘⠿⠃⢠⡇⣠⣿⠛⢀⣤⣾⣿⣿⣿⣿⣿⡿⠟⣫⣤⣞⡯⠚⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠉⠛⠪⠖⢻⣝⣦⠀⠘⠇⠀⡟⣦⠀⠛⠿⠀⡼⠓⡦⠤⠴⣫⣤⣿⡁⣠⣿⣿⣿⣿⣿⡿⢿⣡⡴⣿⡭⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢎⠳⡄⠀⠀⡇⢈⣓⣦⡴⢛⡥⣺⡿⠿⢿⣿⣿⠁⣵⣿⣿⣿⡿⠟⣡⣴⣿⣳⣛⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠤⠒⢦⣀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢳⠈⠆⠀⡧⢸⣿⠛⠛⠛⠛⠁⠀⣠⣾⣿⠃⣼⣿⣿⣿⢋⣴⠞⠋⠀⠴⠿⠿⣿⣯⣹⣀⣀⣀⡀⠀⠀⠀⠀⠀⣘⣦⣤⣀⠈⠑⢦⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣇⠀⣴⣃⡬⣿⣁⡀⠀⠀⠀⣼⣿⢿⡇⡴⠋⠀⣻⡿⠛⠁⠀⠀⠀⠀⠀⠀⠉⢙⣶⡿⠿⠿⠭⣍⣒⣶⢤⣀⣏⣀⠉⠓⣝⡄⠈⢧⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠲⢷⡿⠋⢉⣿⠀⢀⣞⡿⠃⠸⠃⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⢦⣤⣀⣀⡀⠈⠉⠳⢮⣝⠯⣶⡀⠈⣿⠦⠼⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀⣰⡟⠀⣰⡿⠋⢹⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⣿⣿⣿⣿⣿⣷⣶⣄⡀⠉⠳⣝⢿⡉⠁⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣾⣽⣿⣿⣏⣿⠀⠀⣿⠁⢠⣿⢻⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣝⠿⣿⣿⣿⣿⣿⣿⣷⣄⠘⢷⣙⣄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣠⣾⡿⠞⠉⠸⢏⣾⡟⠉⢷⡀⣿⣦⣼⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡿⣶⣌⡙⠿⣿⣿⣿⣿⣿⣷⣄⠻⣍⢦⠀⠀⠀⠀
⠀⠀⠀⠀⣠⣾⡿⠋⠀⠀⠀⠀⢸⣿⡇⠀⠈⢉⣿⢿⣿⣫⣿⠀⠀⠀⠀⠀⣀⠀⠀⠀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣱⠁⠙⠯⢿⡶⣤⣉⡻⠿⣿⣿⣿⣦⠙⣮⢦⠀⠀⠀
⠀⠀⠀⣴⣿⠟⠀⠀⠀⠀⠀⠀⠘⣟⣇⣀⣶⡯⠟⠋⠉⠀⢹⣆⠀⠀⠀⠀⠻⣦⣄⣀⣤⡶⠀⠀⠀⠀⠀⢐⠶⢀⣴⣿⠁⠀⠀⠀⠀⠉⠙⠯⢽⣷⡶⣍⣙⠻⣷⠈⢯⣣⡀⠀
⠀⠀⡼⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠹⣾⣿⣋⠀⠀⠀⠀⠀⠀⢻⣆⠀⠀⠀⠀⠈⠉⠉⠁⠀⠀⠀⢀⣀⠀⠘⠷⠛⣿⣹⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠙⠻⢿⣶⣤⣜⢯⣣⡀
⠀⢸⣿⠃⢰⠀⣀⠀⠀⠀⠀⠀⠀⠀⠘⣿⠖⠀⠀⠀⠀⠀⠀⠀⢹⣷⣤⡀⠀⠀⠀⠀⣷⣄⣀⣀⣈⡉⣀⡀⠀⢠⡿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠿⣟⠇⠇
⢀⣿⡟⠀⠀⠀⣿⠀⢰⣇⠀⡴⠂⠀⢰⡏⠀⠀⠀⠀⠀⠀⠀⣰⠏⠀⠉⠛⠶⣤⣤⡀⠀⠉⠉⠁⠈⠙⢋⣠⣴⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠁
⢸⣿⡇⠀⠀⠀⠻⣄⣸⠙⢦⡀⠀⠀⢸⣇⠀⠀⠀⠀⠀⠀⢰⡏⠀⠀⠀⠀⠀⠀⠀⠉⠛⠛⠛⠛⠛⠛⢿⣷⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢸⣿⡇⠀⠀⠀⠀⠙⠋⠀⠀⠹⠀⠀⢸⡿⣦⠀⠀⠀⠀⠀⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡇⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠸⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⠁⠈⢷⣄⢀⣄⢰⣷⢠⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⡟⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢹⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡿⠀⠀⠀⠙⠟⣿⣿⠻⣿⣇⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢷⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠘⣧⠀⠀⠀⠀⠀⠲⣿⠀⠉⠹⣿⣦⠀⠀⠀⠀⠀⠀⢀⡀⢀⣰⣷⠎⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠙⢟⣷⣄⡀⠀⠀⠀⠀⠀⠀⢻⡆⠀⠀⠀⠀⠀⢹⣇⠀⠀⠈⢙⣿⣷⡀⠀⢀⣴⣿⣴⣟⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠙⠿⢟⣶⣤⣄⣀⣀⣀⣨⣿⣦⣀⣀⣀⣀⣀⣿⡄⠀⠀⠈⠉⣿⣿⡶⠛⠉⠀⣾⡝⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠉⠁⠒⠚⠛⠓⠊⠉⠿⣿⣿⡋⢹⡁⣸⢷⡄⠀⠀⠀⠸⣆⣀⠀⠀⣾⣽⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠑⠯⠭⠭⠭⢽⣿⣦⡀⠰⣄⢺⣿⣆⣾⣽⣻⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠚⠛⠲⣻⣛⣿⡿⣿⣾⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀""")
            sleep(1)
            print("goodluck!")
            winsound.PlaySound('lavender-.wav', winsound.SND_ASYNC)
            sleep(3)
            os.system('cls')
            break
        if answer0 == "no":
            print(""""⢀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⣠⣤⣶⣶
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⢰⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣀⣀⣾⣿⣿⣿⣿
⣿⣿⣿⣿⣿⡏⠉⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿
⣿⣿⣿⣿⣿⣿⠀⠀⠀⠈⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⠉⠁⠀⣿
⣿⣿⣿⣿⣿⣿⣧⡀⠀⠀⠀⠀⠙⠿⠿⠿⠻⠿⠿⠟⠿⠛⠉⠀⠀⠀⠀⠀⣸⣿
⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⣴⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⢰⣹⡆⠀⠀⠀⠀⠀⠀⣭⣷⠀⠀⠀⠸⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠈⠉⠀⠀⠤⠄⠀⠀⠀⠉⠁⠀⠀⠀⠀⢿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⢾⣿⣷⠀⠀⠀⠀⡠⠤⢄⠀⠀⠀⠠⣿⣿⣷⠀⢸⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⡀⠉⠀⠀⠀⠀⠀⢄⠀⢀⠀⠀⠀⠀⠉⠉⠁⠀⠀⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿""")
            sleep(1)
            print("Goodbye!")
            sleep(2)
            break
        else: 
            print("Sorry thats not a valid answer, try again!")        
    if answer0 == "no":
        break