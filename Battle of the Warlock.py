def StartGame():
    print("Welcome to Battle of the Warlock- By Devin Daid")
    print("Your goal is to survive to the very end and save the universe. Good Luck!")
    print("If you are up for this intense and exciting adventure ---> Please type Begin.")
    command = input()
    if command == "Begin":
        Backstory()
    elif command == "Portal":
        UndeadWeapon.append("[The Lightning Blade of the Undead]")
        Burn.append("Drum")
        battleclass.append("Warrior")
        GreenWitchBattle()
    elif command == "skip":
        battleclass.append("Warrior")
        WarriorKnightsWheelSpin()
    else:
        print("Invalid Choice. Try Again")
        StartGame()

######################################################################################################

def Backstory():
    print("")
    print("The Dark Warlock, the epitome of fear and destruction has single handedly defeated the 3 Protectors of our existence.")
    print("By absorbing their powers, The Dark Warlock is now the most powerful being in the universe.")
    print("His goal is to take control of the entire universe by bringing every planet to their knees, starting with Earth.")
    print("However, before the 3 Protectors were destroyed, they created something that could put an end to The Dark Warlock and his goal.")
    print("The 3 Protectors created a spell that would activate when at least one of the protectors are no longer alive.")
    print("The spell activated when The Dark Warlock defeated the 3 Protectors.")
    print("A lightning blast enchanted with their powers would find a worthy being, capable of wielding great power that rivals The Dark Warlock.")
    print("The lightning selected you.")
    print("When you were outside, suddenly a dark cloud covered the sky where lightning struck you, granting you great power.")
    print("It is now up to you to find and defeat The Dark Warlock and save the universe.")
    print("To continue ---> Type Next")
    command = input()
    if command == "Next":
        BattleClass()
    else:
        print("Invalid Choice. Try Again")
        Backstory()

######################################################################################################

def BattleClass():
    import time
    
    print("")
    print("It is time for you to choose your battle class.")
    print("")
    print("1. Warrior Class. (1500 HP)")
    print("- Deals high physical damage")
    print("- Good physical defense")
    print("- Good health")
    print("- Low defence against magic and powers")
    print("- Deals low damage to enemies that use magic and powers")
    print("")
    time.sleep(1)
    print("2. Sorcerer Class. (1250 HP)")
    print("- Deals high magic damage")
    print("- Deals magic effects (Ex. Burn, poison, stun)")
    print("- Good defence against all enemies (Automatically reduces incoming physical damage by 10%)")
    print("- Low Health")
    print("")
    time.sleep(1)
    print("3. Defender Class. (1750 HP)")
    print("- Deals good damage to all enemies")
    print("- Amazing defence against all enemies. (Automatically reduces incoming damage by 10%)")
    print("- High health")
    print("")
    time.sleep(1)
    print("Type 1 to select the Warrior Class")
    print("Type 2 to select the Sorcerer Class")
    print("Type 3 to select the Defender Class")
    command = input()
    if command == "1":
        battleclass.append("Warrior")
        WarriorBegin()
    elif command == "2":
        battleclass.append("Sorcerer")
        SorcererBegin()
    elif command == "3":
        battleclass.append("Defender")
        DefenderBegin()
    else:
        print("Invalid Choice. Try Again")
        BattleClass()


######################################################################################################

def WarriorBegin():
    print("")
    print("You are standing on a street crowded with people.")
    print("Suddenly two portals open in the street.")
    print("Standing before you are two of The Dark Warlock's Knights.")
    print("The people are panicking when suddenly the two Knights grab you by your arms and throw you into a portal.")
    print("It appears that you have entered The Dark Warlock's Dimension.")
    print("It is time to battle.")
    print("Type Fight to battle the two Knights")
    command = input()
    if command == "Fight":
        BattleofTheTwoKnights()
    else:
        print("Invalid Choice. Try Again")
        WarriorBegin()

######################################################################################################

def BattleofTheTwoKnights():
    import time
    from random import randint

    print("")
    print("Main Rules in Battles:")
    print("You cannot attack more than 3 times in a row")
    print("If your dodge is unsuccessful, you must dodge again.")
    time.sleep(3)

    retrycounter = 0
    attackcounter = 0
    dodgecounter = 0
    health = 1500
    knight1 = 500
    knight2 = 500
    while (health > 0 and (knight1>0 or knight2 > 0)) or retrycounter > 0:
        print("")
        print("------------------------------------------------------------------------------")
        print("Your Health: {} HP     ||     Knight 1: {} HP     ||     Knight 2: {} HP".format(health,knight1,knight2))
        print("")
        print("[Lightning Sword] 100 Damage")
        print("[Dodge] 50% chance of successful dodge with chance of a light counter attack 50 Damage. An unsuccessful dodge results in taking double damage.")
        print("")
        print("Type Attack to use your Lightning Sword")
        print("Or type Dodge to try and avoid the two Knight's attacks")
        print("------------------------------------------------------------------------------")
        command = input()

        if command == "Retry":
            retrycounter += 1
            attackcounter = 0
            dodgecounter = 0
            BattleofTheTwoKnights()
            
        if command == "Attack" and attackcounter < 3 and dodgecounter == 0:
            attackcounter += 1
            knight1 -= 100
            knight2 -= 100
            health -= 100
            print("")
            print("You blast both of the Knights with a powerful lightning strike. (Knight 1 and Knight 2 lose 100 health)")
            print("Knight 1 strikes you with his sword. (You lose 50 health)")
            print("Knight 2 strikes you with his sword. (You lose 50 health)")
            time.sleep(3)
        elif command == "Attack" and attackcounter == 3:
            print("")
            print("You cannot attack more than 3 times in a row. Try dodging.")
            time.sleep(2)
        elif command == "Dodge":
            attackcounter = 0
            num = randint(0,1)
            print("The two Knights try to strike you at the same time.")
            if num == 0:
                dodgecounter = 0
                print("You successfully dodge both Knight's attacks and counter with a strike using your Lightning Sword. (Knight 1 and Knight 2 lose 50 health)")
                knight1 -= 50
                knight2 -= 50
                time.sleep(3)
            elif num == 1:
                dodgecounter += 1
                print("You dodged too late and the Knights landed two massive strikes. (You lose 200 health)")
                health -= 200
                time.sleep(3)
        elif command == "Attack" and dodgecounter != 0:
            print("")
            print("You cannot attack after an unsuccessful dodge. Try dodging again.")
            time.sleep(2)
                   
        else:
            print("Invalid Choice. Try Again")
    if health <= 0:
        print("")
        print("Game Over.")
        print("The Two Knights were too powerful and you lose the fight.")
        print("Press Enter to start from the beginning of the fight.")
        command = input()
        if command != 112358:
            BattleofTheTwoKnights()
        
    print("")
    print("Congratulations, you defeated two of The Dark Warlock's Knights")
    print("You tell the Knights to inform you of The Dark Warlock's whereabouts.")
    print("The Knights laugh.")
    print("|Knight 1|: \"If The Dark Warlock is who you seek, death is who you'll meet.\"")
    print("|Knight 2|: \"But if this is the path you desire, The Three Keys to The Gate of Dark Magic is what you must acquire.\"")
    print("|You|: \"What are The Three Keys?\"")
    print("|Knight 2|: \"The Key of the Undead\"")
    print("|Knight 1|: \"The Key of Mystic Power\"")
    print("|Knight 2|: \"And The Key of Monsters\"")
    print("You notice that one of the Knights has a map, so you take it.")
    print("Now to find The Key of the Undead.")
    
    commandcounter = 0
    while commandcounter == 0:
        print("To continue ---> Type Next")
        command = input()
        if command == "Next":
            commandcounter += 1
            WarriorKnightsWheelSpin()
        else:
            print("Invalid Choice. Try Again")

######################################################################################################

def WarriorKnightsWheelSpin():
    import time
    from random import randint
    
    print("")
    print("Before you continue on you adventure, spin a wheel to recieve a new powerful weapon. (10% chance of obtaining a Legendary Weapon)")
    print("Type Spin")
    command = input()
    if command == "Spin":
        time.sleep(1)
        print("...")
        time.sleep(1)
        print("...")
        time.sleep(1)
        print("...")
        time.sleep(1)

        num = randint(0,100)
        if num >= 0 and num < 90:
            print("Congratulations, you got [The Blade of the Lightning Knight] 200 Damage)")
            print("New Ability Unlocked: Stun (When attacking there is a 30% chance to stun enemies preventing them from attacking back)")
            print("You gained 500 additional health")
            print("Dodging now has a 60% success rate")
            KnightsWheelWeapon.append("[The Blade of the Lightning Knight]")
        elif num >= 90:
            print("Wow, you got a Legendary Weapon.")
            print("[Excalibur] 450 Damage)")
            print("Item Ability: Super Effective to All Enemies, 20% Chance to Deal 1.5x Damage")
            print("New Ability Unlocked: Stun (When attacking, there is a 30% chance to stun enemies preventing them from attacking back)")
            print("You gained 500 additional health")
            print("Dodging now has a 60% success rate")
            KnightsWheelWeapon.append("[Excalibur]")
            
    elif command == "Secret":
        print("Wow, you got a Legendary Weapon.")
        print("[Excalibur] 450 Damage)")
        print("Item Ability: Super Effective to All Enemies, 20% Chance to Deal 1.5x Damage")
        print("New Ability Unlocked: Stun (When attacking, there is a 30% chance to stun enemies preventing them from attacking back)")
        print("You gained 500 additional health")
        print("Dodging now has a 60% success rate")
        KnightsWheelWeapon.append("[Excalibur]")
        
    else:
        print("Invalid Choice. Try Again")
        WarriorKnightsWheelSpin()

    nextcounter = 0
    while nextcounter == 0:
        print("To continue ---> Type Next")
        command = input()
        if command == "Next":
            nextcounter += 1
            EasterEggMaze()
        else:
            print("Invalid Choice. Try Again")

######################################################################################################

### NOT NEEDED
def TEMPORARYEasterEggMaze():
    runcounter = 0
    battlecounter = 0
    print("")
    print("ACT 1: THE DEAD END")
    print("-------------------")
    print("")
    print("You figure out that The Key of the Undead is located at, Undead Castle")
    print("As you reach the location, you pass through what looks like a graveyard and you enter the castle.")
    print("You walk up a staircase and enter through the doors.")
    print("Inside is a massive room, about the size of two football fields.")
    print("You walk up another staircase, and through the doors is a long hallway.")
    print("Type Left to go left.")
    print("Or type Right to go right.")
    command = input()
    if command == "Left":
        while command != "Run" and command != "Battle" and runcounter == 0 and battlecounter == 0:
            print("You enter another large room with hundreds of undead warriors.")
            print("Type Run to run away.")
            print("Or type Battle to Battle the army.")
            command = input()
            if command == "Run":
                runcounter += 1
                #UndeadCastleRun()
            elif command == "Battle":
                battlecounter += 1
                #UndeadCastleBattle()
            else:
                print("Invalid Choice. Try Again.")
                print("")
    elif command == "Right":
        while command != "Back" and command != "SEE" and runcounter == 0 and battlecounter == 0:
            print("")
            print("You reach a small dark room with concrete walls and flooring.")
            print("lookS likE you reached a dEad end.")
            print("Type Back to go in the opposite direction.")
            command = input()
            if command == "Back":
                while command != "Run" and command != "Battle" and runcounter == 0 and battlecounter == 0:
                    print("You enter another large room with hundreds of undead warriors.")
                    print("Type Run to run away.")
                    print("Or type Battle to Battle the army.")
                    command = input()
                    if command == "Run":
                        runcounter += 1
                        #UndeadCastleRun()
                    elif command == "Battle":
                        battlecounter += 1
                        #UndeadCastleBattle()
                    else:
                        print("Invalid Choice. Try Again.")
                        print("")
            elif command == "SEE":
                print("You wait.")
                print("As your eyes adjust you notice something unusual.")
                print("You notice that there is one single block sticking out of the wall.")
                print("You take the block out and a floating ball of light appears.")
                print("Congratulations you found Devin Daid's very first Easter Egg.")
                print("As a token of my gratitude take this...")
                print("")
                print("You leave the room and go in the ooposite direction.")
                print("")
                while command != "Run" and command != "Battle" and runcounter == 0 and battlecounter == 0:
                    print("You enter another large room with hundreds of undead warriors.")
                    print("Type Run to run away.")
                    print("Or type Battle to Battle the army.")
                    command = input()
                    if command == "Run":
                        runcounter += 1
                        #UndeadCastleRun()
                    elif command == "Battle":
                        battlecounter += 1
                        #UndeadCastleBattle()
                    else:
                        print("Invalid Choice. Try Again.")
                        print("")
            else:
                print("Invalid Choice. Try Again.")
                print("")
            
    else:
        print("Invalid Choice. Try Again")
        EasterEggMaze()

    if runcounter > 0:
        print(runcounter)
        UndeadCastleRun()
    elif battlecounter > 0:
        print(battlecounter)
        UndeadCastleBattle()
    

######################################################################################################

def EasterEggMaze():
    print("")
    print("You figure out that The Key of the Undead is located at, Undead Castle")
    print("As you reach the location, you pass through what looks like a graveyard and you enter the castle.")
    print("You walk up a staircase and enter through the doors.")
    print("Inside is a massive room, about the size of two football fields.")
    print("You walk up another staircase, and through the doors is a long hallway.")
    print("Type Left to go left.")
    print("Or type Right to go right.")
    command = input()
    if command == "Left":
        LeftEasterEggMaze()
    elif command == "Right":
        RightEasterEggMaze()
    else:
        print("Invalid Choice. Try Again")
        EasterEggMaze()

######################################################################################################

def LeftEasterEggMaze():
    print("")
    print("You enter another large room but now there are hundreds of undead warriors.")
    print("Type Run to run away.")
    print("Or type Battle to Battle the army.")
    command = input()
    if command == "Run":
        UndeadCastleRun()
    elif command == "Battle":
        UndeadCastleBattle()
    else:
        print("Invalid Choice. Try Again.")
        print("")
        LeftEasterEggMaze()

######################################################################################################

def RightEasterEggMaze():
    print("")
    print("You reach a small dark room with concrete walls and flooring.")
    print("lookS likE you reached a dEad end.")
    print("Type Back to go in the opposite direction.")
    command = input()
    if command == "Back":
        BackEasterEggMaze()
    elif command == "SEE":
        SEEEasterEggMaze()
    else:
        print("Invalid Choice. Try Again.")
        print("")
        RightEasterEggMaze()
   
######################################################################################################

def BackEasterEggMaze():
    print("")
    print("You enter another large room with hundreds of undead warriors.")
    print("Type Run to run away.")
    print("Or type Battle to Battle the army.")
    command = input()
    if command == "Run":
        UndeadCastleRun()
    elif command == "Battle":
        UndeadCastleBattle()
    else:
        print("Invalid Choice. Try Again.")
        print("")
        BackEasterEggMaze()

######################################################################################################

def SEEEasterEggMaze():
    print("")
    print("You wait.")
    print("As your eyes adjust you notice something unusual.")
    print("You notice that there is one single block sticking out of the wall.")
    print("You take the block out and a floating ball of light appears.")
    print("Congratulations you found Devin Daid's very first Easter Egg.")
    print("As a token of my gratitude take this...")
    print("")
    print("You leave the room and go in the ooposite direction.")
    BackEasterEggMaze()
        
######################################################################################################

def UndeadCastleRun():
    import time
    red = 0
    blue = 0
    green = 0
    
    print("")
    print("You are running as fast as you can, but the undead warriors are closing in.")
    print("Unfortunately you reach a dead end.")
    print("The undead warriors are now approaching and it appears that this will be the end of the adventure.")
    print("But suddenly when you accidentally put your hand on a block, it pushes inside the wall and the floor below you opens.")
    print("As you fall into a dark room, the floor above you closes. ")

    time.sleep(1)

    print("")
    print("In the room there is a sign that says...")
    time.sleep(1)
    print("-------------------")
    print("| Red Rocks    5  |")
    print("| Blue Rocks   8  |")
    print("| Green Rocks  15 |")
    print("-------------------")
    print("You look around the room, but you only see 3 red rocks, 5 blue rocks, 8 green rocks.")
    print("")
    print("You notice that there are 3 large square holes in the wall, one red, one blue, and one green.")
    print("Each hole will hold the corresponding rock colours.")
    print("You place each of the rocks in their corresponding spots, however, nothing happens.")
    print("You take the rocks out again and think more strategically.")
    
    #print("How many red rocks do you put in the red hole?")
    #redcommand = input()
    #red += redcommand
    #print(redcommand)

    red = int(input("How many red rocks do you put in the red hole?\n"))

    #print("How many blue rocks do you put in the blue hole?")
    #bluecommand = input()
    #blue += bluecommand
    #print(bluecommand)

    blue = int(input("How many blue rocks do you put in the blue hole?\n"))

    #print("How many green rocks do you put in the green hole?")
    #greencommand = input()
    #green += greencommand
    #print(greencommand)

    green = int(input("How many green rocks do you put in the green hole?\n"))

    if red == 2 and blue == 3 and green == 7:
        print("")
        print("The wall starts shaking and begins to open.")
        print("As the walls open, you notice a large room with a throne ahead.")
        print("As you walk in you notice something sitting on the throne.")
        print("The Skeleton King.")
        print("Type Fight to battle The Skeleton King")
        command = input()
        if command == "Fight":
            SkeletonKingBattle()
        else:
            print("Invalid Choice. Try Again")
            UndeadCastleRun()
        
    elif red == 2 and blue != 3 and green != 7:
        print("")
        print("Looks like you have the correct number of red rocks. But the other rocks are incorrect. Try Again.")
        print("Remember, the only information given is that there are 2 different numbers for each of the different rocks. How can you find a number given that information for each rock.")
        print("")
        time.sleep(3)
        UndeadCastleRun() 
        
    elif red != 2 and blue == 3 and green != 7:
        print("")
        print("Looks like you have the correct number of blue rocks. But the other rocks are incorrect. Try Again.")
        print("Remember, the only information given is that there are 2 different numbers for each of the different rocks. How can you find a number given that information for each rock.")
        print("")
        time.sleep(3)
        UndeadCastleRun() 

    elif red != 2 and blue != 3 and green == 7:
        print("")
        print("Looks like you have the correct number of green rocks. But the other rocks are incorrect. Try Again.")
        print("Remember, the only information given is that there are 2 different numbers for each of the different rocks. How can you find a number given that information for each rock.")
        print("")
        time.sleep(3)
        UndeadCastleRun() 

    elif red == 2 and blue == 3 and green != 7:
        print("")
        print("Looks like you have the correct number of red and blue rocks. But the number of green rocks are incorrect. Try Again.")
        print("Remember, the only information given is that there are 2 different numbers for each of the different rocks. How can you find a number given that information for each rock.")
        print("")
        time.sleep(3)
        UndeadCastleRun() 

    elif red == 2 and blue != 3 and green == 7:
        print("")
        print("Looks like you have the correct number of red and green rocks. But the number of blue rocks are incorrect. Try Again.")
        print("Remember, the only information given is that there are 2 different numbers for each of the different rocks. How can you find a number given that information for each rock.")
        print("")
        time.sleep(3)
        UndeadCastleRun() 

    elif red != 2 and blue == 3 and green == 7:
        print("")
        print("Looks like you have the correct number of blue and green rocks. But the number of red rocks are incorrect. Try Again.")
        print("Remember, the only information given is that there are 2 different numbers for each of the different rocks. How can you find a number given that information for each rock.")
        print("")
        time.sleep(3)
        UndeadCastleRun() 
        
    else:
        print("")
        print("Looks like it did nothing. Try Again.")
        print("Remember, the only information given is that there are 2 different numbers for each of the different rocks. How can you find a number given that information for each rock.")
        print("")
        time.sleep(3)
        UndeadCastleRun() 

######################################################################################################

def SkeletonKingBattle():
    import time
    from random import randint

    print("")
    print("Main Rules in Battles:")
    print("You cannot attack more than 3 times in a row")
    print("If your dodge is unsuccessful, you must dodge again.")
    time.sleep(3)

    retrycounter = 0
    attackcounter = 0
    dodgecounter = 0
    burncounter = 0
    health = 2000
    SkeletonKing = 2000
    weapon = ""
    
    while (health > 0 and SkeletonKing > 0) or retrycounter > 0:
        print("")
        print("-----------------------------------------------------------------------------")
        print("Your Health: {} HP     ||     Skeleton King: {} HP".format(health,SkeletonKing))
        print("")
        if "[The Blade of the Lightning Knight]" in KnightsWheelWeapon:
            weapon = "The Blade of the Lightning Knight"
            print("[The Blade of the Lightning Knight] 200 Damage")
        elif "[Excalibur]" in KnightsWheelWeapon:
            weapon = "Excalibur"
            print("[Excalibur] 450 Damage)")
        print("[Dodge] 60% chance of successful dodge with chance to counter attack. An unsuccessful dodge results in the chance of getting burned.")
        print("")
        print("Type Attack to use {}".format(weapon))
        print("Or type Dodge to try and avoid The Skeleton King's attack")
        print("-----------------------------------------------------------------------------")
        command = input()

        if command == "Retry":
            retrycounter += 1
            attackcounter = 0
            dodgecounter = 0
            burncounter = 0
            SkeletonKingBattle()
            
        if burncounter > 0:
            if burncounter > 3:
                burncounter = 0
            elif burncounter > 0 and burncounter < 4:
                print("You are burning from the flaming arrow. (You lose 50 health)")
                time.sleep(1)
                burncounter += 1
                health -= 50
        
        if command == "Attack" and attackcounter < 3 and dodgecounter == 0:
            attackcounter += 1
            
            if "[The Blade of the Lightning Knight]" in KnightsWheelWeapon:
                print("You swing your Blade with the full force of a lightnight blast. (The Skeleton King loses 200 health)")
                SkeletonKing -= 200
                stun = randint(0,9)
                if stun >= 0 and stun <= 2:
                    print("You stunned The Skeleton King and he does not return an attack.")
                elif stun > 2 and stun <= 9:
                    print("The Skeleton King returns with a powerful strike using his blade dealing massive damage. (You lose 300 health)")
                    health -= 300
                    
            elif "[Excalibur]" in KnightsWheelWeapon:
                critical = randint(0,9)
                if critical >= 0 and critical <= 1:
                    print("You swing Excalibur with a great force dealing major damage. (The Skeleton King loses 450 health)")
                    SkeletonKing -= 450
                elif critical > 1 and critical <= 9:
                    print("Your Excalibur glows, emmiting a green light. You swing with all of your strength dealing massive damage. (The Skeleton King loses 675 health)")
                    SkeletonKing -= 650
                    
                stun = randint(0,9)
                if stun >= 0 and stun <= 2:
                    print("You stunned The Skeleton King and he does not return an attack.")
                elif stun > 2 and stun <= 9:
                    print("The Skeleton King returns with a powerful strike using his blade dealing massive damage. (You lose 300 health)")
                    health -= 300
                
            time.sleep(3)
            
        elif command == "Attack" and attackcounter == 3:
            print("")
            print("You cannot attack more than 3 times in a row. Try dodging.")
            time.sleep(2)
            
        elif command == "Dodge":
            attackcounter = 0
            num = randint(0,4)
            print("The Skeleton King shoots at you with his crossbow.")
            if num >= 0 and num <= 2:
                dodgecounter = 0
                if "[The Blade of the Lightning Knight]" in KnightsWheelWeapon:
                    print("You successfully dodge The Skeleton King's attack and you counter with your blade. (The Skeleton King loses 100 health)")
                    SkeletonKing -= 100

                elif "[Excalibur]" in KnightsWheelWeapon:
                    print("You successfully dodge The Skeleton King's attack and you counter using your Excalibur. (The Skeleton King loses 225 health)")
                    SkeletonKing -= 225
                    
                time.sleep(3)
                
            elif num > 2 and num <= 4:
                dodgecounter += 1
                print("You dodged too late and The Skeleton King shoots you with a flaming arrow. (You lose 50 health)")
                burn = randint (0,9)
                if burn >= 0 and burn <= 3:
                    burncounter = 1
                    print("The flaming arrow is burning you.")
                
                health -= 50
                
                time.sleep(3)
                
        elif command == "Attack" and dodgecounter != 0:
            print("")
            print("You cannot attack after an unsuccessful dodge. Try dodging again.")
            time.sleep(2)
                   
        else:
            print("Invalid Choice. Try Again")
 
    if health <= 0:
        print("")
        print("Game Over.")
        print("The Skeleton King proved too powerful and you lose the fight.")
        print("Press Enter to start from the beginning of the fight.")
        command = input()
        if command != 112358:
            SkeletonKingBattle()
        
    print("")
    print("Congratulations, you defeated the Skeleton King.")
    print("You gained 500 additional health")
    print("New Ability Unlocked: Burn (When counter attacking, there is a 30% chance to burn enemies for three turns)")
    Burn.append("Bow")

    commandcounter = 0
    while commandcounter == 0:
        print("To continue ---> Type Next")
        command = input()
        if command == "Next":
            commandcounter += 1
            boulder()
        else:
            print("Invalid Choice. Try Again")

######################################################################################################

def boulder():
    import time

    print("")
    print("After defeating the Skeleton King, he collapses into a pile of bones.")
    print("Suddenly, the room begins to shake as if it was a 6.0 magnitude earthquake.")
    print("A giant boulder falls out of nowhere right above you.")
    time.sleep(7)
    b = True #declare boolean so that code can be executed only if it is still True
    t1 = time.time()
    answer = input("---------------------------------------\nQuickly type Dodge. You have 3 seconds.\n---------------------------------------\n")
    t2 = time.time()
    t = t2 - t1
    if t > 3:
        print("Game over.")
        print("You reacted too slow and the boulder crushes you.")
        b = False
        commandcounter = 0
        while commandcounter == 0:
            print("To try again ---> Press Enter")
            command = input()
            if command != 112358:
                commandcounter += 1
                boulder()
            else:
                print("Invalid Choice. Try Again")
    if answer != "Dodge":
        print("Invalid Choice. Try Again.")
        time.sleep(2)
        boulder()
    if b == True:
        print("With a fast reaction, you successfully avoid getting crushed by the boulder.")
        sprint()

######################################################################################################
        
def sprint():
    import time
    
    print("")
    print("It appears that the ceiling is crumbling and the entire room will soon be crushed.")
    print("You don't have much time.")
    time.sleep(5)
    b = True #declare boolean so that code can be executed only if it is still True
    t1 = time.time()
    answer = input("----------------------------------------\nQuickly type Sprint. You have 3 seconds.\n----------------------------------------\n")
    t2 = time.time()
    t = t2 - t1
    if t > 3:
        print("Game over.")
        print("You did not run fast enough and giant rocks barricade the exits and you eventually get crushed.")
        b = False
        commandcounter = 0
        while commandcounter == 0:
            print("To try again ---> Press Enter")
            command = input()
            if command != 112358:
                commandcounter += 1
                boulder()
            else:
                print("Invalid Choice. Try Again")
    if answer != "Sprint":
        print("Invalid Choice. Try Again.")
        time.sleep(2)
        boulder()
    if b == True:
        print("You sprint as fast as you possibly can and make it out the room.")
        time.sleep(1)
        duck()

######################################################################################################

def duck():
    import time
    
    print("")
    print("As you exit the room you notice a long hallway when suddenly a flaming arrow is shot heading directly for your face.")
    time.sleep(4)
    b = True #declare boolean so that code can be executed only if it is still True
    t1 = time.time()
    answer = input("--------------------------------------\nQuickly type Duck. You have 3 seconds.\n--------------------------------------\n")
    t2 = time.time()
    t = t2 - t1
    if t > 3:
        print("Game over.")
        print("You did not duck in time and the flaming arrow hits you through the hole of your helmet.")
        b = False
        commandcounter = 0
        while commandcounter == 0:
            print("To try again ---> Press Enter")
            command = input()
            if command != 112358:
                commandcounter += 1
                boulder()
            else:
                print("Invalid Choice. Try Again")
    if answer != "Duck":
        print("Invalid Choice. Try Again.")
        time.sleep(2)
        boulder()
    if b == True:
        print("You ducked in time, avoiding the flaming arrow.")
        time.sleep(1)
        Hallway()
    

######################################################################################################

def Hallway():
    
    print("")
    print("You stand still facing the long hallway and things seem to be calming down.")
    print("There does not seem to be anything suspicious but you notice that the floor has black and white tiles.")
    print("You take time to think strategically before making any decision.")
    print("You decide that it is best if you stay either on the white tiles or either on the black tiles,")
    print("as there is a high chance if the hallway is booby trapped, it will only be associated with one specific coloured tile.")
    print("There is a 50% chance of selecting the correct colour and making it past the hallway.")
    print("")
    print("Type White to only walk on the white tiles.")
    print("OR Type Black to only walk on the black tiles.")
    command = input()
    if command == "White":
        WhiteTiles()
    elif command == "Black":
        BlackTiles()
    else:
        print("Invalid Choice. Try Again")
        Hallway()
    
    

######################################################################################################

def WhiteTiles():
    
    print("")
    print("As you are walking on the white tiles you notice that everything seems to be fine.")
    print("That is until you reach the halfway point where suddenly the exit is closed off and the walls begin to close in, leaving you with no way out.")
    print("Game over.")
    print("Press enter to try again.")
    command = input()
    if command != 112358:
        Hallway()   

######################################################################################################
        
def BlackTiles():
    import time
    
    print("")
    print("As you are walking on the black tiles you notice that everything seems to be fine.")
    print("That is until you reach the halfway point where suddenly the tiles begin to dissapear at a constant speed starting from the first tiles.")
    print("You must hurry.")
    
    time.sleep(5)
    b = True #declare boolean so that code can be executed only if it is still True
    t1 = time.time()
    answer = input("-------------------------------------\nQuickly type Run. You have 3 seconds.\n-------------------------------------\n")
    t2 = time.time()
    t = t2 - t1
    if t > 3:
        print("Game over.")
        print("You did not make it out in time and you fell to your eventual demise.")
        b = False
        commandcounter = 0
        while commandcounter == 0:
            print("To try again ---> Press Enter")
            command = input()
            if command != 112358:
                commandcounter += 1
                Hallway()
            else:
                print("Invalid Choice. Try Again")
    if answer != "Run":
        print("Invalid Choice. Try Again.")
        time.sleep(2)
        Hallway()
    if b == True:
        print("You successfully made it out in time.")
        time.sleep(1)
        ZombieKing()

######################################################################################################
        
def UndeadCastleBattle():
    import time
    
    print("")
    print("You decide to face the army single handedly.")
    print("You notice that the army consist of zombies and skeletons.")
    print("The first wave of monsters charge towards you.")

    time.sleep(5)
    b = True #declare boolean so that code can be executed only if it is still True
    t1 = time.time()
    answer = input("---------------------------------------\nQuickly type Blast. You have 3 seconds.\n---------------------------------------\n")
    t2 = time.time()
    t = t2 - t1
    if t > 3:
        print("Game over.")
        print("You did not blast the monsters in time and they trample you.")
        b = False
        commandcounter = 0
        while commandcounter == 0:
            print("To try again ---> Press Enter")
            command = input()
            if command != 112358:
                commandcounter += 1
                UndeadCastleBattle()
            else:
                print("Invalid Choice. Try Again")
    if answer != "Blast":
        print("Invalid Choice. Try Again.")
        time.sleep(2)
        UndeadCastleBattle()
    if b == True:
        print("You blast the first wave of monsters with a powerful lightning blast.")
        time.sleep(1)
        Shields()

######################################################################################################

def Shields():
    import time
    
    print("")
    print("You decide to blast the entire army with an even larger lightning blast.")
    print("But just in time, the monsters take out their shields and block, uneffected by the blast.")
    print("The army changes formation, leaving a clear opening for the skeletons.")
    print("All of the skeletons aim at you and shoot hundreds of flaming arrows at you.")

    time.sleep(9)
    b = True #declare boolean so that code can be executed only if it is still True
    t1 = time.time()
    answer = input("---------------------------------------\nQuickly type Block. You have 3 seconds.\n---------------------------------------\n")
    t2 = time.time()
    t = t2 - t1
    if t > 3:
        print("Game over.")
        print("You did not block in time and your armour was not strong enough to withstand all of the flaming arrows.")
        b = False
        commandcounter = 0
        while commandcounter == 0:
            print("To try again ---> Press Enter")
            command = input()
            if command != 112358:
                commandcounter += 1
                UndeadCastleBattle()
            else:
                print("Invalid Choice. Try Again")
    if answer != "Block":
        print("Invalid Choice. Try Again.")
        time.sleep(2)
        UndeadCastleBattle()
    if b == True:
        print("You quickly spin your sword with great speed, creating a powerful wind.")
        print("You then strike at all of the incoming arrows with such a powerful blow that destroys most of the arrows,")
        print("and sends the rest towards the monsters, taking out most of the skeletons.")
        time.sleep(5)
        DrumTechnique()

######################################################################################################

def DrumTechnique():
    
    print("")
    print("You continue to spin your sword with great speed while generating lightning and you take out most of the undead warrior groups.")
    print("However, when one final group remains, before you could swing your sword, out of nowhere a skeleton shoots your hand from the side with a flaming arrow.")
    print("This causes you to drop your sword and a zombie charges at you and hits you with a powerful strike knocking you to the ground.")
    print("You manage to kick the zombie back and create distance.")
    print("As the zombie charges towards you, a whisper can be heard in your head.")
    print("|Voice|: \"Use the Drum Technique, remember this power.\"")
    print("Suddenly you unlock a memory that does not belong to you of this powerful Drum Technique.")
    print("Your hands begin to generate a massive amount of heat.")
    print("")
    print("Type Counter to use the Drum Technique against the zombie.")
    command = input()
    if command == "Counter":
        PelletDrum()
    else:
        print("Invalid Choice. Try Again")
        DrumTechnique()

######################################################################################################

def PelletDrum():
    
    print("")
    print("You hear what sounds like pellet drums in the background.")
    print("With a single motion you block the zombie's strike and you hit it with a powerful flaming punch knocking it out instantly.")
    print("")
    print("As the final undead warriors charge at you from all angles, you quickly reach out to your sword.")
    print("You command your sword back to your hand and strike it into the ground creating a massive shockwave taking out all of the warriors in the giant room.")
    print("")
    print("You gained 500 additional health")
    print("New Ability Unlocked: Burn (When counter attacking, there is a 30% chance to burn enemies for three turns)")
    Burn.append("Drum")
    print("")
    print("Type Exit to leave the room.")
    
    command = input()
    if command == "Exit":
        ZombieKing()
    else:
        print("Invalid Choice. Try Again")
        PelletDrum()

######################################################################################################

def ZombieKing():
    
    print("")
    print("You enter through a portal that sends you to the very top of the castle.")
    print("Standing before you is the Zombie King, Ruler of the Undead.")
    print("You suddenly get a wave of knowledge about The Zombie King.")
    print("")
    print("[Zombie King Backstory]")
    print("-----------------------")
    print("The Zombie King was once a human from Earth who was born in 437 CE.")
    print("His name, however, remains unknown.")
    print("He is a master swordsman and was one of King Arthur's greatest enemies.")
    print("During the winter of the year 483 CE, he fought King Arthur in an epic battle during a blizzard.")
    print("The battle was very close, none of them significantly more skilled than the other.")
    print("Suddenly a breach appeared and King Arthur sought an opportunity and used Excalibur to hit him through the breach.")
    print("When he fell through, the breach closed and he never returned to Earth again.")
    print("Waiting for him was a large group of zombies.")
    print("He fought many of them off but there were too many to face.")
    print("He eventually got bitten and soon later became a zombie.")
    print("However, something was different, it was as if he was conscious that he turned into a zombie and still had his memories, skills, and intelligence.")
    print("This gave him power over the other zombies, and he overthrew the leader, officially making him the The Zombie King.")
    print("He conquered The Dark Warlock's Dimension and his army continued to grow rapidly.")
    print("Once he ruled all of the zombies, he then faced and defeated The Skeleton King, and ruled over all of the skeletons.")
    print("He then earned the title, Ruler of the Undead.")
    print("With an army large enough, The Zombie King waged war upon The Dark Warlock.")
    print("At first The Dark Warlock was going to amuse The Zombie King and slay every last one of the undead warriors.")
    print("But The Dark Warlock realized that The Zombie King would be a useful ally.")
    print("At first The Zombie King would not listen, but The Dark Warlock showed The Zombie King two possible futures.")
    print("The first future showed The Zombie King going to war, and his entire army being slaughtered.")
    print("The second showed a future where The Zombie King could rule the dimension alongside The Dark Warlock as allies.")
    print("The Zombie King accepted The Dark Warlock's offer and as a token of their truce, The Zombie King was gifted The Key of the Undead.")
    print("-----------------------")
    print("")
    print("|The Zombie King|: \"So this is the one who has been causing trouble in my castle.\"")
    print("|You|: \"I'm here for The Key of the Undead, and I'm not leaving without it.\"")
    print("|The Zombie King|: \"Looks like you reached a dead end. If you really want my key, you will have to take it from me.\"")
    print("[The Zombie King takes out his Sword]")
    print("")
    print("Type Fight to battle The Zombie King.")
    
    command = input()
    if command == "Fight":
        ZombieKingBattle()
    else:
        print("Invalid Choice. Try Again")
        ZombieKing()
    
######################################################################################################

def ZombieKingBattle():
    
    import time
    from random import randint

    print("")
    print("Main Rules in Battles:")
    print("You cannot attack more than 3 times in a row")
    print("If your dodge is unsuccessful, you must dodge again.")
    time.sleep(3)

    retrycounter = 0
    count = 0
    attackcounter = 0
    dodgecounter = 0
    burncounter = 0
    poisoncounter = 0
    health = 2500
    ZombieKing = 3500
    weapon = ""
    
    while (health > 0 and ZombieKing > 0) or retrycounter > 0:
        print("")
        print("-----------------------------------------------------------------------------")
        print("Your Health: {} HP     ||     Zombie King: {} HP".format(health,ZombieKing))
        print("")
        if "[The Blade of the Lightning Knight]" in KnightsWheelWeapon:
            weapon = "The Blade of the Lightning Knight"
            print("[The Blade of the Lightning Knight] 300 Damage")
        elif "[Excalibur]" in KnightsWheelWeapon:
            weapon = "Excalibur"
            print("[Excalibur] 500 Damage)")
        print("[Dodge] 60% chance of successful dodge with chance to counter attack. An unsuccessful dodge results in the chance of getting poisoned.")
        print("")
        print("Type Attack to use {}".format(weapon))
        print("Type Dodge to try and avoid The Zombie King's attack")
        print("Type Retry to start the fight from the beginning.")
        print("-----------------------------------------------------------------------------")
        command = input()

        if command == "Retry":
            retrycounter += 1
            count = 0
            attackcounter = 0
            dodgecounter = 0
            burncounter = 0
            poisoncounter = 0
            ZombieKingBattle()
            
        if ZombieKing <= 2500 and ZombieKing > 1500 and count == 0 and (command == "Attack" or command == "Dodge") and attackcounter != 3 and dodgecounter == 0:
            print("")
            print("|The Zombie King|: \"Your more powerful than I suspected, but still you are no match for my power.\"")
            print("|You|: \"We shall see about that.\"") 
            print("")
            count += 1
            time.sleep(2)

        elif ZombieKing <= 1500 and ZombieKing > 750 and count == 1 and (command == "Attack" or command == "Dodge") and attackcounter != 3 and dodgecounter == 0:
            print("")
            print("|The Zombie King|: \"You remind me of King Arthur. But even he feared my power.\"")
            print("|You|: \"And you still could never defeat him.\"")
            print("")
            count += 1
            time.sleep(2)

        elif ZombieKing <= 750 and count == 2 and (command == "Attack" or command == "Dodge") and attackcounter != 3 and dodgecounter == 0:
            print("")
            print("|The Zombie King|: \"Impossible. I've only seen this power in The Dark Warlock.\"")
            print("|You|: \"Give up while you still can and give me the key.\"")
            print("|The Zombie King|: \"This fight is not over yet.\"")
            print("")
            count += 1
            time.sleep(2)

        if poisoncounter > 0 and (command == "Attack" or command == "Dodge") and attackcounter != 3:
            if poisoncounter > 3:
                poisoncounter = 0
            elif poisoncounter > 0 and poisoncounter < 4:
                print("You are poisoned. (You lose 75 health)")
                time.sleep(1)
                poisoncounter += 1
                health -= 75
                
        if burncounter > 0 and (command == "Attack" or command == "Dodge") and attackcounter != 3 and dodgecounter == 0:
            if burncounter > 3:
                burncounter = 0
            elif burncounter > 0 and burncounter < 4:
                print("The Zombie King is burned. (The Zombie King loses 50 health)")
                time.sleep(1)
                burncounter += 1
                ZombieKing -= 50
        
        if command == "Attack" and attackcounter < 3 and dodgecounter == 0:
            attackcounter += 1
            
            if "[The Blade of the Lightning Knight]" in KnightsWheelWeapon:
                print("You swing your Blade with the full force of a lightnight blast. (The Zombie King loses 300 health)")
                ZombieKing -= 300
                stun = randint(0,9)
                if stun >= 0 and stun <= 2:
                    print("You stunned The Zombie King and he does not return an attack.")
                elif stun > 2 and stun <= 9:
                    print("The Zombie King returns with multiple powerful strikes using his blade dealing massive damage. (You lose 400 health)")
                    health -= 400
                    
            elif "[Excalibur]" in KnightsWheelWeapon:
                critical = randint(0,9)
                if critical >= 0 and critical <= 1:
                    print("You swing Excalibur with a great force dealing major damage. (The Zombie King loses 500 health)")
                    ZombieKing -= 500
                elif critical > 1 and critical <= 9:
                    print("Your Excalibur glows, emmiting a green light. You swing with all of your strength dealing massive damage. (The Zombie King loses 750 health)")
                    ZombieKing -= 750
                    
                stun = randint(0,9)
                if stun >= 0 and stun <= 2:
                    print("You stunned The Zombie King and he does not return an attack.")
                elif stun > 2 and stun <= 9:
                    print("The Zombie King returns with multiple powerful strikes using his blade dealing massive damage. (You lose 400 health)")
                    health -= 400
                
            time.sleep(3)
            
        elif command == "Attack" and attackcounter == 3:
            print("")
            print("You cannot attack more than 3 times in a row. Try dodging.")
            time.sleep(2)
            
        elif command == "Dodge":
            attackcounter = 0
            num = randint(0,4)
            print("The Zombie King charges at you.")
            if num >= 0 and num <= 2:
                dodgecounter = 0
                if "Bow" in Burn:
                    print("You successfully dodge The Zombie King's attack and you counter with your bow by shooting a flaming arrow. (The Zombie King loses 150 health)")
                    ZombieKing -= 150
                    burned = randint (0,9)
                    if burned >= 0 and burned <= 3:
                        burncounter = 1
                        print("The flaming arrow burned The Zombie King.")
                elif "Drum" in Burn:
                    print("You successfully dodge The Zombie King's attack and you counter using the Drum Technique with a flaming punch. (The Zombie King loses 150 health)")
                    ZombieKing -= 150
                    burned = randint (0,9)
                    if burned >= 0 and burned <= 3:
                        burncounter = 1
                        print("Your powerful flaming punch burned The Zombie King.")
                    
                time.sleep(3)
                
            elif num > 2 and num <= 4:
                dodgecounter += 1
                print("You dodged too late and The Zombie King scratches with his large hand. (You lose 50 health)")
                poison = randint (0,9)
                if poison >= 0 and poison <= 3:
                    poisoncounter = 1
                    print("The scratch poisoned your blood.")
                
                health -= 50
                
                time.sleep(3)
                
        elif command == "Attack" and dodgecounter != 0:
            print("")
            print("You cannot attack after an unsuccessful dodge. Try dodging again.")
            time.sleep(2)
                   
        else:
            print("Invalid Choice. Try Again")
 
    if health <= 0:
        print("")
        print("Game Over.")
        print("The Zombie King proved too powerful and you lose the fight.")
        print("Press Enter to start from the beginning of the fight.")
        command = input()
        if command != 112358:
            ZombieKingBattle()
        
    print("")
    print("-----------------------------------------------------------------------------")
    print("The Zombie King is weak but as you approach him, a horde of zombies surround you.")
    print("They start attacking you and you fall to the ground, struggling to get up.")
    print("You are losing hope when suddenly you hear a whisper.")
    print("|Voice|: \"You were chosen to have this power because you are worthy.\"")
    print("|Voice|: \"Reach within and show them your true power.\"")
    print("You manage to strike the horde of zombies with a single motion, stunning them.")
    print("The Zombie King seeks an opportunity to strike, when unexpectedly your eyes begin to glow purple.")
    print("At a speed far greater than lightning, you channel all of the power in your body into a single punch, dealing collosal damage.")
    print("")
    print("Congratulations, you defeated the Zombie King.")
    print("You gained 500 additional health")
    print("Dodging now has a 70% success rate")
    print("New Ability Unlocked: Infinity Punch (After landing three consecutive stuns, you activate the Infinity Punch, deals 1000 damage.")
    print("")

    commandcounter = 0
    while commandcounter == 0:
        print("To continue ---> Type Next")
        command = input()
        if command == "Next":
            commandcounter += 1
            ZombieKingChest()
        else:
            print("Invalid Choice. Try Again")
    

######################################################################################################

def ZombieKingChest():
    
    print("")
    print("You notice a small chest and you walk past The Zombie King.")
    print("The chest is sealed by a magic spell and requires a specific object to open it.")
    print("You look around and you have an idea of potential objects that would open this chest.")
    print("The Zombie King's Sword, a bright Gold Orb, and a Middlemist Camellia Flower.")
    print("")
    print("What do you choose?")
    print("Type Sword to select The Zombie King's Sword.")
    print("Type Orb to select the bright Gold Orb.")
    print("Type Flower to select the Middlemist Camellia Flower.")

    command = input()
    if command == "Sword":
        ZombieKingSword()
    elif command == "Orb":
        Orb()
    elif command == "Flower":
        Flower()
    else:
        print("Invalid Choice. Try Again")
        ZombieKingChest()

######################################################################################################

def ZombieKingSword():
    
    print("")
    print("You place The Zombie King's Sword on top of the chest.")
    print("The sword begins to glow.")
    print("Magic particles appear in front of you.")
    print("The chest opens and The Key of the Undead is inside.")
    print("Congratulations you found the first key.")
    print("|You|: \"Now where might the second key be located.\"")
    print("As if the key is responding to you, it tells you clue about where the second key is located.")
    print("")
    print("The Amazon warriors never leave.")
    print("Weak to fire or an axe.")
    print("Seek the colour that is green.")
    print("And The Key of Mystic Power will be yours at last.")
    print("")
    print("You keep this in mind, thinking about the answer to the clue.")
    print("You decide to hold on to The Zombie King's Sword, the Gold Orb, and the Middlemist Camellia Flower as they might be helpful in the future.")
    print("")
    print("Type Leave to exit the castle.")

    command = input()
    if command == "Leave":
        LeavingUndeadCastle()
    else:
        print("Invalid Choice. Try Again")
        ZombieKingSword()

######################################################################################################

def Orb():

    import time
    
    print("")
    print("You place the bright Gold Orb on top of the chest.")
    print("Looks like nothing is happening. Try selecting something else.")

    time.sleep(3)

    ZombieKingChest()

######################################################################################################

def Flower():

    import time
    
    print("")
    print("You place the Middlemist Camellia Flower on top of the chest.")
    print("Looks like nothing is happening. Try selecting something else.")

    time.sleep(3)

    ZombieKingChest()

######################################################################################################

def LeavingUndeadCastle():

    import time
    
    print("")
    print("As you are leaving Undead Castle, more zombies and skeletons begin to chase after you.")
    print("You reach a dead end and the zombies and skeletons are running towards you.")
    print("You hold up The Zombie King's Sword and the zombies and skeletons stop in their place.")
    print("All of the zombies and skeletons start kneeling in front of you.")
    print("You are now the Ruler of the Undead.")
    print("You leave the castle.")
    print("")
    print("You realize that The Zombie King's sword can be very useful.")
    print("You hear another whisper in your head.")
    print("|Voice|: \"Use the Gold Orb.\"")
    print("")
    time.sleep(1)

    if "[The Blade of the Lightning Knight]" in KnightsWheelWeapon:
        print("You place the Gold Orb on the ground.")
        print("In one hand you hold The Blade of the Lightning Knight.")
        print("In the other, you hold The Zombie King's Sword.")
        print("The Gold Orb begins to levitate.")
        print("It's pulling the swords towards it so you decide to let go of the swords.")
        print("The swords start orbiting the Gold Orb like Earth around the Sun.")
        print("The swords are orbiting at an accelerated speed.")
        print("A bright gold light is emmited, eating away at all of the darkness in the area.")
        print("The gold orb falls to the ground and you see a single sword hovering in the air.")
        print("You reach out to the sword and it flies straight into your hand.")
        print("Congratualations, you unlocked [The Lightning Blade of the Undead] 500 Damage")
        print("Stun Ability Upgraded: When attacking there is a 40% chance to stun enemies preventing them from attacking back.")
        UndeadWeapon.append("[The Lightning Blade of the Undead]")

    elif "[Excalibur]" in KnightsWheelWeapon:
        print("You place the Gold Orb on the ground.")
        print("In one hand you hold Excalibur.")
        print("In the other, you hold The Zombie King's Sword.")
        print("The Gold Orb begins to levitate.")
        print("It's pulling the swords towards it so you decide to let go of the swords.")
        print("The swords start orbiting the Gold Orb like Earth around the Sun.")
        print("The swords are orbiting at an accelerated speed.")
        print("A bright gold light is emmited, eating away at all of the darkness in the area.")
        print("The gold orb falls to the ground and you see a single sword hovering in the air.")
        print("You reach out to the sword and it flies straight into your hand.")
        print("Congratualations, you unlocked [Excalibur: Ruler of the Undead] 750 Damage")
        print("Stun Ability Upgraded: When attacking there is a 40% chance to stun enemies preventing them from attacking back.")
        UndeadWeapon.append("[Excalibur: Ruler of the Undead]")

    print("")
    print("Type Next to continue on your journey.")

    command = input()
    if command == "Next":
        ActTwo()
    else:
        print("Invalid Choice. Try Again")
        LeavingUndeadCastle()

######################################################################################################

def ActTwo():

    print("")
    print("ACT 2: THE Magic Word")
    print("---------------------")
    print("")
    print("You think about the clue and study the map to see where the Key of Mystic Power may be located.")
    print("You figure it out.")
    print("")
    print("The Amazon warriors never leave.")
    print("Weak to fire or an axe.")
    print("Seek the colour that is green.")
    print("And The Key of Mystic Power will be yours at last.")
    print("")
    print("|You|: \"Amazon, refers to the amazon forest, and leave refers to leaves on a tree.\"")
    print("|You|: \"Trees are weak to fire and an axe can be used to cut down trees.\"")
    print("|You|: \"And typically, trees are green.\"")
    print("After looking at the map and given the name, The Key of Mystic Power, you decide to explore Voodoo Forest.")
    print("")
    print("It is the middle of the night and you reach the forest.")
    print("You notice a sign that says,")
    print("-------------")
    print("| Keep Out! |")
    print("-------------")
    print("")
    print("Type Explore to enter the forest.")

    command = input()
    if command == "Explore":
        VoodooForest()
    else:
        print("Invalid Choice. Try Again")
        ActTwo()

######################################################################################################

def VoodooForest():

    import time
    
    print("")
    print("Immediately the forest is very fitting of its name.")
    print("You notice creepy old dolls hanging on trees, with their eyes missing.")
    print("As you are walking you feel as if you are being watched.")
    print("Suddenly you hear a loud scream at your 1 o'clock.")
    print("You run towards the sound, but smell something weird.")
    print("You start feeling dizzy and you eventually collapse.")
    time.sleep(1)
    print("...")
    time.sleep(1)
    print("...")
    time.sleep(1)
    print("...")
    time.sleep(1)
    print("You wake up.")
    print("You're tied up to a chair in this old and eerie looking hut.") 
    print("It seems as if the rope that is tied around you has some sort of spell making its material unbreakable.")
    print("You hear voices in another room.")
    print("Then you hear their laughs...")
    print("They are witches.")
    print("One witch enters the room you are in.")
    print("|You|: \"Who are you?\"")
    print("|Witch|: \"It doesn't matter who I am, but you seem to have gotten The Dark Warlock's attention.")
    print("|Witch|: \"He never received his Gold Orb, so he sent us to investigate.\"")
    print("|You|: \"Us?\"")
    print("|Witch|: \"We have been keeping an eye on you, strange how one ordinary man, managed to defeat The Zombie King.")
    print("|You|: \"I'm no ordinary man.\"")
    print("|Witch|: \"Yet you still managed to get captured so easily.\"")
    print("|Witch|: \"As much as I want to continue chatting, I have to deliever this orb to The Great Sorcerer.\"")
    print("[The Witch leaves.]")
    print("|You|: \"I need to find a way out of here.\"")
    print("")
    print("In the distance you see your belongings in a bag.")
    print("You try to command your sword to you but it seems as if the rope has dampened your abilities.")
    print("You hear the witches in the other room and figure out they are planning to use your body parts and organs for potions and spells.")
    print("It's now or never, we must do something.")
    print("You hear a whisper again in your head.")
    print("|Voice|: \"You are fluent in every language.\"")
    print("|You|: \"Who are you and why are you always in my head?\"")
    print("Suddenly your brain gets filled with all of the knowledge of every language.")
    print("You know that spells are spoken in Latin.")
    print("The witches are entering the room you are in, there isn't much time.")
    print("There are three potential spells that may work to break the rope's spell.")
    print("")
    print("1. Tollere Alica")
    print("2. Perdere Incantatores")
    print("3. Conteram Incantatores")
    print("")
    print("Type 1 to select spell 1")
    print("Type 2 to select spell 2")
    print("Type 3 to select spell 3")
    command = input()
    if command == "1":
        RemoveTheSpell()
    elif command == "2":
        DestroyTheSpell()
    elif command == "3":
        BreakTheSpell()
    else:
        print("Invalid Choice. Try Again")
        VoodooForest()
    
    

######################################################################################################

def RemoveTheSpell():

    print("")
    print("The witches are walking towards you.")
    print("You say the spell but nothing happens and you can't escape the rope.")
    print("Game Over.")
    print("Helpless and without power, the witches torture you and eventually kill you, using your body for spells and potions.")
    print("Press Enter to try again.")
    command = input()
    if command != 112358:
        VoodooForest()
    

######################################################################################################

def DestroyTheSpell():

    print("")
    print("The witches are walking towards you.")
    print("You say the spell but nothing happens and you can't escape the rope.")
    print("Game Over.")
    print("Helpless and without power, the witches torture you and eventually kill you, using your body for spells and potions.")
    print("Press Enter to try again.")
    command = input()
    if command != 112358:
        VoodooForest()

######################################################################################################

def BreakTheSpell():

    print("")
    print("The witches are walking towards you.")
    print("The spell works and you command your sword to your hand, cutting the rope.")
    print("The witches gasp.")
    print("The witches quickly run to the other room.")
    print("You grab the bag with all of your belongings and you put on your armour.")
    print("You turn around and some sort of pumpkin is thrown at you.")
    print("With fast reflexes you catch the pumpkin, until it explodes, blasting you outside of the hut.")
    print("One of the witches is waiting outside for you and throws some sort of potion on you.")
    
    if "Warrior" in battleclass:
        print("You feel significantly weaker.") #Only for warrior class, deals 15% less damage and takes 15% more damage
        print("Looks like the spell did something to you.")

    print("Time to deal with this witch.")
    print("")
    print("Type Fight to face the witch.")
    command = input()
    if command == "Fight":
        GreenWitchBattle()
    else:
        print("Invalid Choice. Try Again")
        BreakTheSpell()

######################################################################################################

def GreenWitchBattle():

    import time
    from random import randint

    print("")
    print("Main Rules in Battles:")
    print("You cannot attack more than 3 times in a row")
    print("If your dodge is unsuccessful, you must dodge again.")

    time.sleep(3)
    
    if "Warrior" in battleclass:
        print("")
        print("The potion has reduced your defence and attack damage by 15%.") #Only for warrior class, deals 15% less damage and takes 15% more damage
        
    time.sleep(3)

    retrycounter = 0
    stuncounter = 0
    count = 0
    attackcounter = 0
    dodgecounter = 0
    burncounter = 0
    dizzycounter = 0
    dizzyhit = 0
    dcounter = 0
    health = 3000
    GreenWitch = 4000
    weapon = ""
    
    while (health > 0 and GreenWitch > 0) or retrycounter > 0:
        print("")
        print("-----------------------------------------------------------------------------")
        print("Your Health: {} HP     ||     The Green Witch: {} HP".format(health,GreenWitch))
        print("")
        if "[The Lightning Blade of the Undead]" in UndeadWeapon:
            weapon = "The Lightning Blade of the Undead"
            print("[The Lightning Blade of the Undead] 500 Damage - 15%")
        elif "[Excalibur: Ruler of the Undead]" in UndeadWeapon:
            weapon = "Excalibur: Ruler of the Undead"
            print("[Excalibur: Ruler of the Undead] 700 Damage - 15%)")
        print("[Dodge] 70% chance of successful dodge with chance to counter attack. An unsuccessful dodge results in the chance of getting dizzy.")
        print("")
        print("Type Attack to use {}".format(weapon))
        print("Type Dodge to try and avoid The Green Witch's attack")
        print("Type Retry to start the fight from the beginning.")
        print("-----------------------------------------------------------------------------")
        command = input()

        if command == "Retry":
            retrycounter += 1
            stuncounter = 0
            count = 0
            attackcounter = 0
            dodgecounter = 0
            burncounter = 0
            dizzycounter = 0
            dizzyhit = 0
            dcounter = 0
            GreenWitchBattle()

        if dizzycounter > 0 and ((command == "Attack" and dodgecounter == 0) or command == "Dodge") and attackcounter != 3:
            if dizzycounter > 3:
                dizzycounter = 0
                dizzyhit = 0
                dcounter = 0
            elif dizzycounter > 0 and dizzycounter < 4:
                print("You are dizzy.")
                time.sleep(1)
                dizzycounter += 1
                dizzyhit += 1
                
        if burncounter > 0 and (command == "Attack" or command == "Dodge") and attackcounter != 3 and dodgecounter == 0:
            if burncounter > 3:
                burncounter = 0
            elif burncounter > 0 and burncounter < 4:
                print("The Green Witch is burned. (The Green Witch loses 100 health)")
                time.sleep(1)
                burncounter += 1
                GreenWitch -= 100

        if dizzyhit > 0 and (command == "Attack" or command == "Dodge") and attackcounter != 3 and dodgecounter == 0:
            d = randint(0,9)
            if d >= 0 and d <= 2:
                print("You feel too dizzy and you are unable to move.")
                print("The Green Witch hits you with a powerful spell dealing major damage. (You lose 400 health)")
                health -= 400
                dcounter += 1
                time.sleep(1)
            elif d > 2 and d <= 9:
                print("You feel dizzy, but you fight through it.")
                dcounter = 0
        
        if command == "Attack" and attackcounter < 3 and dodgecounter == 0 and dcounter == 0:
            attackcounter += 1
            
            if "[The Lightning Blade of the Undead]" in UndeadWeapon:
                print("You summon a dark grey cloud that strikes The Green Witch with a powerful red strike of lightning. (The Green Witch loses 425 health)")
                GreenWitch -= 425 
                stun = randint(0,9)
                if stun >= 0 and stun <= 3:
                    print("You stunned The Green Witch and she does not return an attack.")
                    stuncounter += 1
                    if stuncounter == 3 and attackcounter == 3:
                        print("You stunned The Green Witch 3 times in a row and you activate The Infinity Punch.")
                        print("The Green Witch is stunned and your eyes glow purple.")
                        print("At a speed far greater than lightning, you channel all of the power in your body into a single punch, dealing collosal damage.")
                        print("(The Green Witch loses 1000 health)")
                        GreenWitch -= 1000
                        stuncounter = 0
                elif stun > 3 and stun <= 9:
                    print("The Green Witch absorbs some of the electricity and returns with a powerful green spell dealing massive damage. (You lose 600 health)")
                    health -= 600
                    stuncounter = 0
                    
            elif "[Excalibur: Ruler of the Undead]" in UndeadWeapon:
                critical = randint(0,9)
                if critical >= 0 and critical <= 1:
                    print("You swing Excalibur with the commanding power of the undead. (The Green Witch loses 595 health)")
                    GreenWitch -= 595
                elif critical > 1 and critical <= 9:
                    print("Your Excalibur glows, emmiting a black cloud. You swing with the full force of the undead dealing massive damage. (The Green Witch loses 892 health)")
                    GreenWitch -= 892
                    
                stun = randint(0,9)
                if stun >= 0 and stun <= 3:
                    print("You stunned The Green Witch and she does not return an attack.")
                    stuncounter += 1
                    if stuncounter == 3 and attackcounter == 3:
                        print("You stunned The Green Witch 3 times in a row and you activate The Infinity Punch.")
                        print("The Green Witch is stunned and your eyes glow purple.")
                        print("At a speed far greater than lightning, you channel all of the power in your body into a single punch, dealing collosal damage.")
                        print("(The Green Witch loses 1000 health)")
                        GreenWitch -= 1000
                        stuncounter = 0
                elif stun > 3 and stun <= 9:
                    print("The Green Witch absorbs some of the undead power and returns with a powerful green spell dealing massive damage. (You lose 700 health)")
                    health -= 700
                    stuncounter = 0
                
            time.sleep(3)
            
        elif command == "Attack" and attackcounter == 3 and dcounter == 0:
            print("")
            print("You cannot attack more than 3 times in a row. Try dodging.")
            time.sleep(2)
            
        elif command == "Dodge" and dcounter == 0:
            stuncounter = 0
            attackcounter = 0
            num = randint(0,4)
            print("The Green Witch creates a powerful wind going in your direction.")
            if num >= 0 and num <= 2:
                dodgecounter = 0
                if "Bow" in Burn:
                    print("You successfully dodge the direction of the wind attack and you counter with your bow by shooting a flaming arrow. (The Green Witch loses 200 health)")
                    GreenWitch -= 200
                    burned = randint (0,9)
                    if burned >= 0 and burned <= 3:
                        burncounter = 1
                        print("The flaming arrow burned The Green Witch.")
                elif "Drum" in Burn:
                    print("You successfully dodge the wind attack and you counter using the Drum Technique with a flaming punch. (The Green Witch loses 200 health)")
                    GreenWitch -= 200
                    burned = randint (0,9)
                    if burned >= 0 and burned <= 3:
                        burncounter = 1
                        print("Your powerful flaming punch burned The Green Witch.")
                    
                time.sleep(3)
                
            elif num > 2 and num <= 4:
                dodgecounter += 1
                print("You dodged too late and the wind grabs and spins you at a great speed. (You lose 50 health)")
                dizzy = randint (0,9)
                if dizzy >= 0 and dizzy <= 3:
                    dizzycounter = 1
                    print("You are now extremly dizzy.")
                
                health -= 50
                
                time.sleep(3)
                
        elif command == "Attack" and dodgecounter != 0 and dcounter == 0:
            print("")
            print("You cannot attack after an unsuccessful dodge. Try dodging again.")
            time.sleep(2)
                   
        elif command != "Attack" and command != "Dodge" and command != "Retry":
            print("Invalid Choice. Try Again")
 
    if health <= 0:
        print("")
        print("Game Over.")
        print("The Green Witch proved too powerful and you lose the fight.")
        print("Press Enter to start from the beginning of the fight.")
        command = input()
        if command != 112358:
            GreenWitchBattle()
        
    print("")
    print("-----------------------------------------------------------------------------")
    print("Congratulations, you defeated The Green Witch.")
    print("The Green Witch is out knocked out cold.")
    print("You hear a witch's cackle inside the Witch Hut.")
    print("You walk inside.")
    print("")

    commandcounter = 0
    while commandcounter == 0:
        print("To continue ---> Type Walk")
        command = input()
        if command == "Walk":
            commandcounter += 1
            WitchHut()
        else:
            print("Invalid Choice. Try Again")
    

######################################################################################################

def WitchHut():

    print("")
    print("As you walk inside, the Red Witch throws another pumpkin bomb.")
    print("You quickly deflect it with your sword sending it through the window.")
    print("The Red Witch shoots you with a powerful red spell, blasting you back outside.")
    print("The Red Witch comes outside.")
    print("|Red Witch|: \"Resisting will only make it more painful.\"")
    print("|Red Witch|: \"Surrender now and your death will be swift and painless.\"")
    print("|You|: \"Never!\"")
    print("Type Fight to face the Red Witch.")
    command = input()
    if command == "Fight":
        RedWitchBattle()
    else:
        print("Invalid Choice. Try Again")
        WitchHut()
    

######################################################################################################

def RedWitchBattle():

    import time
    from random import randint

    print("")
    print("Main Rules in Battles:")
    print("You cannot attack more than 3 times in a row")
    print("If your dodge is unsuccessful, you must dodge again.")

    time.sleep(3)
    
    if "Warrior" in battleclass:
        print("")
        print("The Green Witch's potion is still in effect and has reduced your defence and attack damage by 15%.") #Only for warrior class, deals 15% less damage and takes 15% more damage
        
    time.sleep(3)

    retrycounter = 0
    stuncounter = 0
    count = 0
    attackcounter = 0
    dodgecounter = 0
    burncounter = 0
    pumpkincounter = 0
    pumpkinstun = 0
    health = 3000
    RedWitch = 4000
    weapon = ""
    
    while (health > 0 and RedWitch > 0) or retrycounter > 0:
        print("")
        print("-----------------------------------------------------------------------------")
        print("Your Health: {} HP     ||     The Red Witch: {} HP".format(health,RedWitch))
        print("")
        if "[The Lightning Blade of the Undead]" in UndeadWeapon:
            weapon = "The Lightning Blade of the Undead"
            print("[The Lightning Blade of the Undead] 500 Damage - 15%")
        elif "[Excalibur: Ruler of the Undead]" in UndeadWeapon:
            weapon = "Excalibur: Ruler of the Undead"
            print("[Excalibur: Ruler of the Undead] 700 Damage - 15%)")
        print("[Dodge] 70% chance of successful dodge with chance to counter attack. An unsuccessful dodge results in the chance of getting stunned and burned.")
        print("")
        print("Type Attack to use {}".format(weapon))
        print("Type Dodge to try and avoid The Red Witch's attack")
        print("Type Retry to start the fight from the beginning.")
        print("-----------------------------------------------------------------------------")
        command = input()

        if command == "Retry":
            retrycounter += 1
            stuncounter = 0
            count = 0
            attackcounter = 0
            dodgecounter = 0
            burncounter = 0
            RedWitchBattle()
                
        if burncounter > 0 and ((command == "Attack" and dodgecounter == 0) or command == "Dodge") and attackcounter != 3:
            if burncounter > 3:
                burncounter = 0
            elif burncounter > 0 and burncounter < 4:
                print("The Red Witch is burned. (The Red Witch loses 100 health)")
                burncounter += 1
                RedWitch -= 100
                time.sleep(1)

        if pumpkincounter > 0 and ((command == "Attack" and dodgecounter == 0) or command == "Dodge") and attackcounter != 3:
            if pumpkincounter > 3:
                pumpkincounter = 0
            elif pumpkincounter > 0 and pumpkincounter < 4:
                print("You are burned. (You lose 75 health)")
                pumpkincounter += 1
                health -= 75
                time.sleep(1)

        if pumpkinstun > 1 and command == "Dodge" and attackcounter != 3:
            print("You find the strength to continue fighting.")
            print("You stand up and call your sword to your hand.")
            pumpkinstun = 0
            time.sleep(1)

        if pumpkinstun == 1 and command == "Dodge" and attackcounter != 3:
            print("You are stunned and cannot move.")
            print("The Red Witch blasts you with a powerful red spell. (You lose 400 health)")
            pumpkinstun += 1
            health -= 400
            time.sleep(1)
        
        if command == "Attack" and attackcounter < 3 and dodgecounter == 0 and pumpkinstun != 2:
            attackcounter += 1
            
            if "[The Lightning Blade of the Undead]" in UndeadWeapon:
                print("You summon a dark grey cloud that strikes The Red Witch with a powerful red strike of lightning. (The Red Witch loses 425 health)")
                RedWitch -= 425 
                stun = randint(0,9)
                if stun >= 0 and stun <= 3:
                    print("You stunned The Red Witch and she does not return an attack.")
                    stuncounter += 1
                    if stuncounter == 3 and attackcounter == 3:
                        print("You stunned The Red Witch 3 times in a row and you activate The Infinity Punch.")
                        print("The Red Witch is stunned and your eyes glow purple.")
                        print("At a speed far greater than lightning, you channel all of the power in your body into a single punch, dealing collosal damage.")
                        print("(The Red Witch loses 1000 health)")
                        RedWitch -= 1000
                        stuncounter = 0
                elif stun > 3 and stun <= 9:
                    print("The Red Witch absorbs some of the electricity and returns with a powerful red spell dealing massive damage. (You lose 600 health)")
                    health -= 600
                    stuncounter = 0
                    
            elif "[Excalibur: Ruler of the Undead]" in UndeadWeapon:
                critical = randint(0,9)
                if critical >= 0 and critical <= 1:
                    print("You swing Excalibur with the commanding power of the undead. (The Red Witch loses 595 health)")
                    RedWitch -= 595
                elif critical > 1 and critical <= 9:
                    print("Your Excalibur glows, emmiting a black cloud. You swing with the full force of the undead dealing massive damage. (The Red Witch loses 892 health)")
                    RedWitch -= 892
                    
                stun = randint(0,9)
                if stun >= 0 and stun <= 3:
                    print("You stunned The Red Witch and she does not return an attack.")
                    stuncounter += 1
                    if stuncounter == 3 and attackcounter == 3:
                        print("You stunned The Red Witch 3 times in a row and you activate The Infinity Punch.")
                        print("The Red Witch is stunned and your eyes glow purple.")
                        print("At a speed far greater than lightning, you channel all of the power in your body into a single punch, dealing collosal damage.")
                        print("(The Red Witch loses 1000 health)")
                        RedWitch -= 1000
                        stuncounter = 0
                elif stun > 3 and stun <= 9:
                    print("The Red Witch absorbs some of the undead power and returns with a powerful red spell dealing massive damage. (You lose 700 health)")
                    health -= 700
                    stuncounter = 0
                
            time.sleep(3)
            
        elif command == "Attack" and attackcounter == 3 and pumpkinstun != 2:
            print("")
            print("You cannot attack more than 3 times in a row. Try dodging.")
            time.sleep(2)
            
        elif command == "Dodge" and pumpkinstun != 2:
            stuncounter = 0
            attackcounter = 0
            num = randint(0,4)
            print("The Red Witch throws 3 pumpkin bombs in your direction.")
            if num >= 0 and num <= 2:
                dodgecounter = 0
                if "Bow" in Burn:
                    print("You spin your sword at a great speed and use that momentum to leap over the 3 pumpkin bombs.")
                    print("In midair you counter with your bow by shooting a flaming arrow. (The Red Witch loses 200 health)")
                    RedWitch -= 200
                    burned = randint (0,9)
                    if burned >= 0 and burned <= 3:
                        burncounter = 1
                        print("The flaming arrow burned The Red Witch.")
                elif "Drum" in Burn:
                    print("You spin your sword at a great speed and use that momentum to leap over the 3 pumpkin bombs.")
                    print("As you land, The Red Witch tries to attack, but you counter using the Drum Technique with a flaming punch. (The Red Witch loses 200 health)")
                    RedWitch -= 200
                    burned = randint (0,9)
                    if burned >= 0 and burned <= 3:
                        burncounter = 1
                        print("Your powerful flaming punch burned The Red Witch.")
                    
                time.sleep(3)
                
            elif num > 2 and num <= 4:
                dodgecounter += 1
                print("You dodged too late and all 3 pumpkin bombs explode dealing massive damage. (You lose 300 health)")
                pumpkin = randint (0,9)
                if pumpkin >= 0 and pumpkin <= 3:
                    pumpkincounter = 1
                    pumpkinstun = 1
                    print("You are now stunned and burned.")
                
                health -= 50
                
                time.sleep(3)
                
        elif command == "Attack" and dodgecounter != 0:
            print("")
            print("You cannot attack after an unsuccessful dodge. Try dodging again.")
            time.sleep(2)
                   
        elif command != "Attack" and command != "Dodge" and command != "Retry":
            print("Invalid Choice. Try Again")
 
    if health <= 0:
        print("")
        print("Game Over.")
        print("The Red Witch proved too powerful and you lose the fight.")
        print("Press Enter to start from the beginning of the fight.")
        command = input()
        if command != 112358:
            RedWitchBattle()
        
    print("")
    print("-----------------------------------------------------------------------------")
    print("Congratulations, you defeated The Red Witch.")
    print("You gained 500 more health.")
    print("You go back inside the hut to investigate.")
    print("")

    commandcounter = 0
    while commandcounter == 0:
        print("To continue ---> Type Hut")
        command = input()
        if command == "Hut":
            commandcounter += 1
            Hut()
        else:
            print("Invalid Choice. Try Again")
    

######################################################################################################

def Hut():

    print("")
    print("You explore the hut.")
    print("The hut looks very normal on the main floor, as if a normal person lives here.")
    print("You then find a locked door.")
    print("You use your sword to generate enough lightning to break down the door.")
    print("There is a staircase to the basement.")
    print("|You|: \"This must be where the witches create their potions and spells.\"")
    print("You look around the massive room.")
    print("On the left side of the room is a giant bookshelf, probably full of spell ingredients and diaries.")
    print("On the right side of the room is a giant inventory of all the ingredients a witch could possibly need.")
    print("There is a massive counter in the centre of the room.")
    print("On the counter is a book that is opened, but is not finished.")
    print("|You|: \"It seems as if the witches were trying to make a spell.\"")
    print("After further investigation, you realize the witches were attempting to create a spell capable of stealing your powers!")
    print("You realize that if the spell was complete, you must be careful when confronting The Purple Witch and even The Sorceror.")
    print("Some time goes by after exploring everything in the room.")
    print("You decide that you have time to make 1 of 2 potential potions that will be helpful in future battles.")
    print("All of the ingredients books are locked by a spell, however, there are two ripped pages on the floor.")
    print("The two pages are two different sets of ingredients, but you are unsure what the potential potion will do.")
    print("Choose wisely.")
    print("Potion 1 Ingredients: 3 Hercules Beatle Horns, 1 T-Rex tooth, 5 Litres of Spinach Juice, and 1 Middlemist Camellia Flower.")
    print("Potion 2 Ingredients: 10 Garlic cloves, 2 Dragon Scales, 5 Litres of Holy Water, and 1 Middlemist Camellia Flower.")
    print("Potion 3 Ingredients: 5 Eels, 500 Grams of Cheetah fur, 5 Litres of Chocolate Syrup, and 1 Middlemist Camellia Flower.")
    print("Type 1 to select Potion 1")
    print("Type 2 to select Potion 2")
    print("Type 3 to select Potion 3")
    command = input()
    if command == "1":
        Potion.append("Potion of Hercules")
        PotionTest()
    elif command == "2":
        Potion.append("Potion of Pure Health")
        PotionTest()
    elif command == "3":
        Potion.append("Potion of Godspeed")
        PotionTest()
    else:
        print("Invalid Choice. Try Again")
        Hut()

######################################################################################################

def PotionTest():

    import time
    
    print("")
    print("You test out a sample of the potion you created.")
    print("You perform 3 experiments to determine the effects of the potion.")
    print("Strength Test: Before and after consuming the potion, punch a tree with your hand.")
    print("Health Test: Before consuming the potion, cut your hand with your sword, notice any changes after consuming the potion.")
    print("Speed Test: Before and after consuming the potion, shoot an arrow straight up in the air and run 25 metres away and run back to catch the arrow.")
    print("You begin the tests.")

    if "Potion of Hercules" in Potion:
        print("")
        print("...")
        time.sleep(1)
        print("You completed the Strength Test.")
        print("Before drinking the potion, you punched through half of the tree trunk.")
        print("However, after drinking the potion, you manage to punch through the entire tree with your fists.")
        print("...")
        time.sleep(1)
        print("You completed the Health Test.")
        print("You cut your hand, however, after drinking the potion nothing changed.")
        print("...")
        time.sleep(1)
        print("You completed the Speed Test.")
        print("Both before and after drinking the potion you were unsuccessful with catching the arrow.")
        print("Based on the results, the potion you created is The Potion of Hercules.")
        print("Congratulations you unlocked the Potion of Hercules.")
        print("You can only use the potion once per battle. The potion allows you to deal double damage when attacking for 3 turns.")
        
    elif "Potion of Pure Health" in Potion:
        print("")
        print("...")
        time.sleep(1)
        print("You completed the Strength Test.")
        print("Before drinking the potion, you punched through half of the tree trunk.")
        print("After drinking the potion, there is no change in your punching power.")
        print("...")
        time.sleep(1)
        print("You completed the Health Test.")
        print("You cut your hand and after drinking the potion the wound fully healed within seconds.")
        print("...")
        time.sleep(1)
        print("You completed the Speed Test.")
        print("Both before and after drinking the potion you were unsuccessful with catching the arrow.")
        print("Based on the results, the potion you created is the Potion of Pure Health.")
        print("Congratulations you unlocked the Potion of Pure Health.")
        print("You can only use the potion once per battle. The potion allows you to gain back 40% health.")
    elif "Potion of Godspeed" in Potion:
        print("")
        print("...")
        time.sleep(1)
        print("You completed the Strength Test.")
        print("Before drinking the potion, you punched through half of the tree trunk.")
        print("After drinking the potion, there is no change in your punching power.")
        print("...")
        time.sleep(1)
        print("You completed the Health Test.")
        print("You cut your hand, however, after drinking the potion nothing changed.")
        print("...")
        time.sleep(1)
        print("You completed the Speed Test.")
        print("Before drinking the potion you were unsuccessful with catching the arrow.")
        print("However, after consuming the potion, you were able to catch the air with extreme speed.")
        print("Based on the results, the potion you created is the Potion of Godspeed.")
        print("Congratulations you unlocked the Potion of Godspeed.")
        print("You can only use the potion once per battle. The potion allows you to dodge and stun without fail for consecutive 5 turns.")

    time.sleep(3)
    print("Type Investigate to explore the rest of the hut and find clues about where the purple witch has gone and helpful information about the socerer.")

    command = input()
    if command == "Investigate":
        InvestigateHut()
    else:
        print("Invalid Choice. Try Again")
        PotionTest()


    

######################################################################################################

def InvestigateHut():

    import time
    
    print("")
    print("You enter the hut once again.")
    print("")

    

    
    print("Type .")

    command = input()
    if command == "":
        InvestigateHut()
    else:
        print("Invalid Choice. Try Again")
        PotionTest()


    

######################################################################################################

#main
global KnightsWheelWeapon, health, knight1, knight2
battleclass = []
KnightsWheelWeapon = []
Burn = []
UndeadWeapon = []
Potion = []
StartGame()

