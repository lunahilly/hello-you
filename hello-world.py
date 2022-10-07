from time import sleep
#hello world eindopdracht
#speelt af in een pokemon wereld
#trainer name and Eevee name can be chosen
print("Hello, i am professor Goei and welcome to the world of pokemon")
print("What is your name pokemon trainer?")
name = input()
print("Hello " + name)
print("What is your Eevees name?")
Eevee = input()
print("You and " + Eevee + " are no longer safe in Saffron city!")
print("There is a pokemon war going on right this second and i advice you to go to lavender town")
print("Lavender town is taking people at the moment")
print("Goodluck on your journey...")
sleep(2)
print("*you and Eevee are going on a journey to Lavender town*")
print("*you come across a path that splits in 2")
print('The left path looks dark and ominoous, the right path looks safe and well lit')
while True:
    print("which path wil you chose?")
    print("left (dark and ominous) or right (safe and bright)")
    answer = input()
    if answer == "left":
        print("you walk along the path casious...")
        break
    if answer == "right":
        print("you go on the right safe path...")
        break
    else:
        print("sorry thats not a viable answer, try again")
print("test")