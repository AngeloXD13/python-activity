import random
import numpy as np
# Demo of basic input in python
# name = input("Enter your name: ")
# print("Hello " + name)

# Demo of a program that computes for an area of a circle
# radius = float(input("Enter the radius: "))
# area = 3.14 * (radius**2)
# print("The area of the Circle is: " + str(area))

# Demo of a program that computes for a volume of a cylinder
# radius = float(input("Enter the Radius: "))
# height = float(input("Enter the Height: "))
# volume = 3.14 *(radius**2 * height)
# print("The Volume of the Cylinder: " + str(volume))

#Demo for array 
# fruits = ["apple", "banana", "cherry", "strawberry", "melon", "watermelon"]
# print(fruits[0])
# print(fruits[1])
# print(fruits[2])

#Demo for for Loop
# for x in fruits:
#     print(x)

# i = 0
# while i < 10:
#     print("Hello World")
#     print(i)
#     i = i + 1



#sample text-based game with simple conditional statement
character_health = 100
item = ""
inventory = np.array([[0, 3],[1,3]])  #[{itemId, amount}]

items = [[0,"Health Pack"], #[{itemID, itemName}]
    [1, "Fish"]]
#posible items in inventory = ["Health Pack",]

name = input("Enter your character's name: ")
print("Hello " + name)

while character_health > 0:
    if character_health != 100 and item == "Fish":
        n = input("You have taken some damage to heal select [1 to heal/ 0 to ignore]")
        if n == "1":
            character_health += 10
            print("Your character's health is back to " + str(character_health))
        else :
             print("Your character's health is back to " + str(character_health))


    v = int(input("Choose 1 if you want to cross the river\nChoose 2 if you want to jump on the ravine\nChoose 3 if you want to fight monster in the dungeon \nInput: "))
   
    #Start of Journey
    if v == 1: 
        choice = input("If you want to go fishing select [1 for yes/ 0 for no]")
        if choice == "1":
            #Fishing minigame
            print("You have chosen Fishing! ")
            chance = random.randint(0,9)
            if chance > 6:
                item = "Fish"
                print("You have catch a Fish!")
                ###TODO in future: find the id of item in inventory to avoid error and conflict in future
                inventory[1][1]+=1

            else:
                print("There is no fish to catch")

        elif choice == "0":
            print("You have crossed the river")


    elif v == 2:
        #damages the player
        print("You have jumped into the ravine")
        print("Your character has taken 10pt of damage")
        character_health = character_health - 10
    elif v == 3:
        #player goes to the dungeon
        print("You have enter the dungeon")
        print(name + " walked and feel creeps around the dark dungeon...")
        input()
        playerInsideDungeon = True
        playerSeeExitoutofDungeon = False
        moonsterhasSpawned = False
        monsterhealth = 100
        lessChanceOfPlayerfindingExitout = 0 
        exitedTheDungeon = False
        #if the player run, the less chance or plus 2 lesschance finding the exit
        #if the palyer walk, he less chance or plus 1 lesschance finding the exit
        #but random number can increase fate of having minus less chance finding the exit
        #and fighthing monster can minus 2 less chance finding the exit

        while playerInsideDungeon == True:
            correctAction = False
            while correctAction == False:
                print("Select actions: ")

                #normal selection// without monster
                print("Choose 1: RUN!")
                print("Choose 2: Walk slowly")
                #special selection 3// with monster
                if moonsterhasSpawned == True: 
                    print("Choose 3: Fight the monster")
                #special selection 4// see way out of dungeon
                if playerSeeExitoutofDungeon == True:
                    print("Choose 4: Go to the dungeon exit")
                #see characters stats/inventory
                print("Choose 5: Inventory")

                choice = input("Your choice: ")

                if choice == "1": #run
                    correctAction = True;
                    print(name + " runned away")
                    input()
                    if moonsterhasSpawned == False: 
                        print(name + " feel someone was following, run for your life!!!")
                        print(name + " run for his life....")
                        lessChanceOfPlayerfindingExitout=+2
                        if playerSeeExitoutofDungeon == True:
                            print(name + " lost his way out of the dungeon...")
                            playerSeeExitoutofDungeon = False
                    elif moonsterhasSpawned == True: 
                        lessChanceOfPlayerfindingExitout=+3
                        if playerSeeExitoutofDungeon == True:
                            print(name + " lost his way out of the dungeon...")
                            input()
                            playerSeeExitoutofDungeon = False
                        fate = random.randint(0,1)
                        if fate == 0:
                            print(name + " lost the monster")
                            moonsterhasSpawned = False
                        else : 
                            print("A monster still following you...")
                            input()

                elif choice == "2": #walk
                    correctAction = True;
                    if moonsterhasSpawned == False:
                        print(name +" walk slowly but heard rustling nearby....")
                        input()
                        lessChanceOfPlayerfindingExitout+1
                        if playerSeeExitoutofDungeon == True:
                            print(name + " lost his way out of the dungeon...")
                            input()
                            playerSeeExitoutofDungeon = False
                    else : 
                        lessChanceOfPlayerfindingExitout=+1
                        if playerSeeExitoutofDungeon == True:
                            print(name + " lost his way out of the dungeon...")
                            input()
                            playerSeeExitoutofDungeon = False
                        fate = random.randint(1,3)
                        #fate 1, player will be atacked by a monster
                        if fate == 1:
                            print("A monster was charging an attack!!!")
                            damagePoints = random.randint(0,80)
                            print("You have been attacked by monster")
                            print(name + " have been damage by " + str(damagePoints))
                            character_health -= damagePoints 
                            print(name + " remaining health is " + str(character_health))
                            lessChanceOfPlayerfindingExitout -= 2
                            if character_health <= 0:
                                print(name + " have been died")
                                break
                        #fate 2, player will still followed by monster but will not attack
                        elif fate == 2:
                            print("A monster still following you")
                            input()

                        #fate 3, the monster leaved the player
                        elif fate == 3:
                            print("The monster become uninterested to " + name)
                            print("The monter walked away")
                            moonsterhasSpawned = False;
                
                elif choice == "3" and moonsterhasSpawned == True: #attck if monster spawed
                    correctAction = True;
                    print(name + " is ready to attack!!!")
                    input()
                    playerAttackPoints = random.randint(0,100)
                    if playerAttackPoints <=20:
                        print("The monster missed "+name+" attack...")
                        input()
                        lessChanceOfPlayerfindingExitout-=1
                    elif playerAttackPoints > 20 and playerAttackPoints < 60:
                        print("The monster sustained " + str(playerAttackPoints) + " damage!")
                        input()
                        monsterhealth -= playerAttackPoints
                        lessChanceOfPlayerfindingExitout-=2
                    elif playerAttackPoints > 60 and playerAttackPoints <=100:
                        print("The monster sustained " + str(playerAttackPoints) +" critical damage points!!!!")
                        input()
                        monsterhealth -= playerAttackPoints
                        lessChanceOfPlayerfindingExitout-=3
                    
                    print("The monster's health is "+ str(monsterhealth))
                    if monsterhealth <= 0:
                        print(name +"killed the monster")
                        input()
                        print(name + " obtained an Health Pack")
                        print(items[0][1]," ",str(inventory[0][1])," +1")
                        inventory[0][1]+=1
                        input();

                        moonsterhasSpawned = False;
                        lessChanceOfPlayerfindingExitout-=5
                    else:
                        fate = random.randint(1,3)
                        #fate 1, player will be atacked by a monster
                        if fate == 1:
                            print("A monster was charging an attack!!!")
                            input()
                            damagePoints = random.randint(0,80)
                            print("You have been attacked by monster")
                            print(name + " have been damage by " + str(damagePoints))
                            character_health -= damagePoints 
                            print(name + " remaining health is " + str(character_health))
                            lessChanceOfPlayerfindingExitout -=2
                            if character_health <= 0:
                                print(name + " have been died")
                                exitedTheDungeon = True
                                break
                        #fate 2, player will still followed by monster but will not attack
                        elif fate == 2:
                            print("A monster did not attack...")
                            input()

                        #fate 3, the monster leaved the player
                        elif fate == 3:
                            print("The monster become uninterested to fight" + name)
                            print("The monter walked away")
                            input()
                            moonsterhasSpawned = False;

                elif choice == "4" and playerSeeExitoutofDungeon == True: #GOTO outside the dungeon
                    correctAction = True;
                    print(name + " exited the dungeon") 
                    
                    input()
                    exitedTheDungeon = True
                    break
            
                elif choice == "5":
                    print("Your inventory is: ")
                    print("Amount| Name")

                    for x in range(len(inventory)):
                    # print["Item: "+ str(inventory[x])+ "Amount" + str(inventory[y])]
                        print(str(inventory[x][1]),"pcs  ",items[x][1])

                    input()
                            


                else: 
                    print("invalid Choice")
                    input()
                    
           
            ### players fate after choicing like spawen monster or see the way out of dungen
            #outof dungeon

            if exitedTheDungeon == True:
                break

            if character_health <= 0:
                break
            #print(lessChanceOfPlayerfindingExitout)
            fateFindingExittoDungeon =random.randint(0,100)
            if fateFindingExittoDungeon <= 60:
                lessChanceOfPlayerfindingExitout-1

            if lessChanceOfPlayerfindingExitout <= 0:
                print(name + " see the way out of dungeon...")
                input()
                playerSeeExitoutofDungeon = True

            #monster has spawed
            if moonsterhasSpawned == False:
                fateMonsterSpawning = random.randint(0,10)
                if fateMonsterSpawning >= 6 :
                    print("A monster has spawned and ready to attack!!!")
                    monsterhealth = 100
                    input()
                    moonsterhasSpawned = True

            
            
#### doSelect actions: 
#Choose 1: RUN!
#Choose 2: Walk slowly
#Choose 4: Go to the dungeon exit
##Your choice: 4
#angeloXd exited the dungeon

#angeloXd see the way out of dungeon...

#Select actions: 
#Choose 1: RUN!
#Choose 2: Walk slowly
#Choose 4: Go to the dungeon exit
#Your choice:
####

            



            



    else:
        print("Invalid input")

    print("Your character's Health: " + str(character_health))

print("Your Character is dead!")