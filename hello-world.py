from time import sleep
from pygame import mixer
mixer.init()
mixer.music.load('explosion.mp3')
love = 0
alist = ["a", "A"]
blist = ["B", "b"]
clist = ["C", "c"]
#hello world eindopdracht
#speelt af in een pokemon wereld
#trainer name and Eevee name can be chosen
while True: 
    print("^Hello, i am professor Goei and welcome to the world of pokemon^")
    sleep(.5)
    print("^What is your name pokemon trainer?^")
    name = input()
    print("^Hello " + name + "^")
    print("^What is your Eevees name?^")
    Eevee = input()
    print("^You and " + Eevee + " are no longer safe in Saffron city!^")
    sleep(1)
    print("^There is a pokemon war going on right this second and i advice you to go to lavender town^")
    sleep(1)
    print("^Lavender town is taking people in at the moment^")
    sleep(1)
    print("^Goodluck on your journey...^")
    sleep(2)
    print("*you and Eevee are going on a journey to Lavender town*")
    sleep(1)
    print("*you come across a path that splits in 2")
    sleep(1)
    print('The left path looks dark and ominoous, the right path looks safe and well lit')
    sleep(1)
    while True:
        print("Which path wil you chose?")
        sleep(1)
        print("Left (dark and ominous) or right (safe and bright)")
        answer = input()
        if answer == "left":
            #safe choice, story continues
            print("You and eevee go on the left path")
            sleep(.5)
            print("you walk along the path casious...")
            sleep(2)
            print("You hear something rumble in the distance")
            sleep(.5)
            print("The bushes next to you start shaking, you and " + name + " start preparing for battle")
            sleep(1)
            print("Something jumps out of the bush!")
            sleep(1)
            print("Its a bunnelby!")
            sleep(1)
            print("Eevee and bunnelby start sniffing eachother...")
            sleep(1)
            print("*" + Eevee + " made a friend!*")
            print("Your eevee's love has increased by 10")
            love = love + 10
            # continue story
            sleep(1)
            print("You and " + Eevee + " come across another split path")
            sleep(1)
            print("The paths are labelled")
            print("a. Safe route lavender town    b. Short route lavender town    c. Unicorn forest")
            sleep(.5)
            print("which path will you choose? a/b/c")
            answer2 = input()
            if answer2 in alist:
                print("You go on the safe path")
                #story continues to all the eevee endings
                #your eevee will gain love
            if answer2 in blist:
                print("You go on the short path")
                sleep(1)
                print("The path is difficult and your eevee gets very stressed")
                sleep(1)
                print("Eevee gets stuck and you free her")
                sleep(1)
                print("*your eevee didnt gain love*")
                sleep(1)
                print("-you arrive in lavender town-")
                sleep(1)
                print("After a long and hard journey you and eevee can finally rest on a bench")
                sleep(2)
                print("A townsperson walks up to you...")
                sleep(1)
                print("^Hello my name is Lila^")
                sleep(1)
                print("^I saw your Eevee over there and i was wondering if she would like to play with my pikachu?^")
                sleep(1)
                print("Do you want " + Eevee + " to play with pikachu? yes/no")
                answer3 = input()
                if answer3 == "yes":    
                    print("^Great!^")
                    sleep(1)
                    print("Eevee and pikachu have a great time")
                    sleep(1)
                    print(Eevee + " has made a friend!")
                    sleep(1)
                    print("Eevee gained +10 love")
                    sleep(1)
                    print("^It seems like pikachu and Eevee get along great!^")
                    print("^would you like to go to the towns bonfire with me an pikachu?")
                    print("A. accept the invitation    B. Ask her out on a walk in the moonlight instead  a/b")
                    answer4 = input()
                    if answer4 in alist:
                        print("^Lovely! I cant wait for you to meet all the others!^")
                        sleep(1)
                        print("You and Lila go to the towns bonfire and she introduces you to all the people there")
                        sleep(1)
                        print("Your Eevee is getting along great with all the other pokemon!")
                        sleep(.5)
                        print(Eevee + " has made a bunch of friends!")
                        sleep(1)
                        print("*+10 love*")
                        sleep(1)
                        print("Oh? Eevee is evolving!")
                        sleep(1)
                        print("Eevee has evolved into a Sylveon!")
                        sleep(1)
                        print("She must have been so filled with love from the bonfire she evolved into a fairy type!")
                        sleep(2)
                        print("some time later...")
                        sleep(1)
                        print('You and ' + Eevee + " made a bunch of friends!")
                        sleep(1)
                        print("You two fit right in with the lavender town people")
                        sleep(1)
                        print("Congratulations! You have made it to the Sylveon bonfire ending!")
                        sleep(1)
                        print("I am so proud of you " + name)
                        sleep(1)
                    if answer4 in blist:
                        #pikachu and eevee kiss, eevee turns into umbreon
                        print("^Oh! uhmm sure, i would love too! :o ^")
                        sleep(1)
                        print("You and Lila go on a walk in the moonlight...")
                        sleep(2)
                        print("Pikachu and Eevee are playing together")
                        sleep(1)
                        print("oh? Pikachu kisses Eevee, +10 love")
                        sleep(1)
                        print("Eevee is filled with love under the moon")
                        sleep(1)
                        print(Eevee + " is evolving!")
                        sleep(.5)
                        print("Eevee has evolved into an umbreon!")
                        sleep(1)
                        print("-some time later-")
                        sleep(1)
                        print("You and " + Eevee + " have settled in into lavender town!")
                        sleep(1)
                        print(Eevee + " and Pikachu got married")
                        sleep(3)
                        print("Congratulations! You got the umbreon love ending")
                        sleep(1)
                        print("I am proud of you " + name)
                        sleep(2)
                if answer == "no":
                        print("^Thats a shame :(")
            if answer2 in clist:
                #you will die
                print("You go into the unicorn forest")
                #a unicorn will kill you
        if answer == "right":
            #bad choice, you die
            #there is a cliff and you slip and die
            print("You go on the right safe path...")
            sleep(1)
            print("You look at the beautiful view of the cliff and river to your right")
            sleep(2)
            print("Suddenly you slip and fall")
            sleep(1)
            print("You fell off the cliff, you have died")
            sleep(1)
            break
        else:
         print("Sorry thats not a viable answer, try again")
         sleep(1)
    while True:
        print("Would you like to play again? yes/no")
        if answer == "yes":
            print("goodluck!")
            sleep(2)
        if answer == "no":
            print("goodbye!")
            break
        else: 
            print("Sorry thats not a valid answer, try again!")
