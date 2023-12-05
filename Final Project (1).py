# Code made by Topher, Taisa, Sevi, and Sumi

import random


def inp_correct(word):
    word = word.strip()
    word = word.capitalize()
    return word


def response_intake3(a, b, c):
    option_a = a
    option_b = b
    option_c = c
    print(option_a, option_b, option_c)
    intake = input("(Type an option): ")
    intake = inp_correct(intake)
    if (intake == option_a) or (intake == option_b) or (intake == option_c):
        return intake
    else:
        print("Invalid Input")
        return response_intake3(option_a, option_b, option_c)


def response_intake2(a, b):
    option_a = a
    option_b = b
    print(option_a, option_b)
    intake = input("(Type an option): ")
    intake = inp_correct(intake)
    if (intake == option_a) or (intake == option_b):
        return intake
    else:
        print("Invalid Input")
        return response_intake2(option_a, option_b)


def error_exit():
    print("An Error has occurred. Quitting Game")
    quit()


class Player():
    def __init__(self, pname):
        self.name = pname
        self.victory_points = 0
        self.tool = ""

    def add_tool(self, in_tool):
        self.tool = in_tool.tname
        self.victory_points = self.victory_points + in_tool.vp_worth

    def remove_tool(self, in_tool):
        self.tool = ""
        self.victory_points = self.victory_points - in_tool.vp_worth

    def update_vp(self, up_vp):
        if up_vp > 0:
            print(self.name, 'gained', up_vp, "victory points.")
        elif up_vp < 0:
            print(self.name, 'loss', up_vp, "victory points.")
        self.victory_points = self.victory_points + up_vp

    def display_status(self):
        print("*****")
        print(self.name, "currently has", self.victory_points, "victory points.")
        if self.tool == "":
            print("No Tool Eqiupped")
        else:
            print(self.name, "currently has the", self.tool, "equipped.")
        print("*****")

    def end_screen(self):
        print("*****")
        print("You found an End.")
        print(self.name, "gained", self.victory_points, "total victory points")
        quit()


class Tool():
    def __init__(self, tname, vp):
        self.tname = tname
        self.vp_worth = vp


if __name__ == '__main__':
    name = input("What is your name?: ")
    name = inp_correct(name)
    chara = Player(name)

    print("The rain pours on outside of your bedroom window. You are currently tuned in to your computer science lecture.")
    print("The lecture is a demonstration about coding attributes.")
    print(".")
    print(".")
    print(".")
    print("You check the clock to your left-- it is 9:03 AM.")

    # Sevi - I just made this as a small scenario to get the user adjusted to the game. No VP adding/subtracting is needed for this one.
    key = False
    while not key:
        print("Your eyelids are getting heavy. Take a quick rest?")
        print("Yes, I'll catch up later.")
        print("No, I need to stay awake.")
        nap = response_intake2("Yes", "No")

        if nap == 'No':
            print("You chose to stay awake. However, nothing in the lecture stuck.")
            print("You went on to fail your final exam.")
            print("BAD END")
            print("Tip: Maybe you should have taken the nap.")
        elif nap == 'Yes':
            print("You slowly close your eyes...")
            key = True
        else:
            error_exit()

    print(".")
    print(".")
    print(".")
    print("The desk isn't a very comfortable spot to nap. You should probably move to the bed.")
    print("You go to move to your bed...wait...where are you?")
    print("This place appears to be the Life Sciences building on UofL's campus...")
    print("It seems to be the dead of night-- but it's darker than usual.")
    print("You notice that all of the street lights surrounding you are completely turned off.")
    print("You check your phone.")
    print(".")
    print(".")
    print(".")
    print("No signal. Strangely, the time is 00:00 AM.")
    print("With not much else around aside from the buzzing of flies, you enter the building.")
    print(".")
    print(".")
    print(".")
    print("After aimlessly walking around the empty halls, you see an open classroom door.")

    key = False
    while not key:
        print("You see a table with five items scattered across it.")
        print("After moving closer, you see a small sign. 'TAKE ONLY ONE' it says in scribbled text.")
        print("1 = A Hatchet")
        print("2 = A Small Piece of Rope")
        print("3 = A Flashlight")
        print("4 = A Cinnamon Hard Candy")
        print("5 = A Pocket Knife")
        print("6 = Take Two Instead")
        toolchoice = input("What do you take? ")  

        if toolchoice == '1':
            print("You obtained the hatchet.")
            sel_tool = Tool("Hatchet", 1)
            chara.add_tool(sel_tool)
            key = True
        elif toolchoice == '2':
            print("You obtained the rope.")
            sel_tool = Tool("Rope", 2)
            chara.add_tool(sel_tool)
            key = True
        elif toolchoice == '3':
            print("You obtained the flashlight.")
            sel_tool = Tool("Flashlight", 3)
            chara.add_tool(sel_tool)
            key = True
        elif toolchoice == '4':
            print("You obtained the cinnamon candy.")
            sel_tool = Tool("Cinnamon Candy", 1)
            chara.add_tool(sel_tool)
            key = True
        elif toolchoice == '5':
            print("You obtained the pocketknife.")
            sel_tool = Tool("Pocketknife", 3)
            chara.add_tool(sel_tool)
            key = True
        elif toolchoice == '6':
            print("'What power does a stupid sign have over me?' You think to yourself cheekily.")
            print("You pop the cinnamon candy into your mouth and shift to grab one of the other tools- ")
            print("You've been grabbed from behind with a rope around your neck.")
            print("1 to Struggle")
            struggle = input("What do you do? ")
            if struggle != '':
                print("You kick and attempt to scream-- but you don't have enough oxygen in your lungs left.")
                print("Enter anything to Struggle")
                struggle2 = input("What do you do? ")
            if struggle2 != '':
                print("You start to cry. You think of home.")
                print("Enter anything to Struggle")
                struggle3 = input("What do you do? ")
            if struggle3 != '':
                print("CRACK")
                print("You felt something break.")
                print("Your vision fades.")
                print("BAD END")
                print("Tip - Listen to the strange signs")
        else:
            print("Incorrect input. Please enter the number next to item you would like.")

    chara.display_status()

    print(".")
    print(".")
    print(".")
    print("Since there isn't much else for you to do in the Life Sciences building, you leave.")
    print("After exiting through the double doors, you hear a clicking sound behind you.")
    print("Someone (or something) locked the door.")
    print("You begin walking.")
    walking1 = response_intake3("Left", "Right", "Forward")

    if walking1 == 'Left':
        print(".")
        print(".")
        print(".")
        print("After walking for a short time, you reach what seems to be Strickler Hall.")
        print("You enter through the front entrance.")
        print("It's disappointingly quiet. The only sound you can hear is your own breathing.")
        print("You feel like you're being watched.")
        print("As expected, all of the classroom doors on the first floor are locked or bolted shut.")
        print("Your next idea is to search the second floor.")
        print("Just like last time, there is one singular door open that leads to a classroom.")
        print("You peek into the room.")
        print("In the classroom, there is a singular desk and chair, a piece of paper, and a pencil.")
        print("There is also a chalkboard with scribbled text that says, 'QUIZ TIME'")
        print('I will give you two numbers and you will provide me the product. If you answer correctly, I will give you victory points, if not, you get...... NOTHING!')
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        answer = num1 * num2
        print("What is ", num1, "*", num2, "=")
        comp_answer = int(input("answer: "))

        if comp_answer == answer:
            chara.update_vp(2)
        else:
            print("Incorrect Answer")

    if walking1 == 'Right':
        print(".")
        print(".")
        print(".")
        print("After walking for a short time, you reach what seems to be Davidson Hall.")
        print("You enter through the front entrance.")
        print("It feels almost unfamiliar-- without the smell of fresh Subway bread and chattering voices.")
        print("As expected, all of the classroom doors on the first floor are locked or bolted shut.")
        print("Your next idea is to search the second floor.")
        print("DIIIING")
        print("You turn to see that the elevator is functioning")
        print("Which one are you going to take? ")
        goingup = response_intake2("Elevator", "Stairs")
        if goingup == 'Elevator':
            print(".")
            print(".")
            print(".")
            print("You press the button for the second floor-- it lights up as confirmation.")
            print("The elevator roars to life as it shifts upwards.")
            print("DIIIING")
            print("You made it to the second floor.")
        if goingup == 'Stairs':
            print(".")
            print(".")
            print(".")
            print("You walk past the elevator and open the door to the stairwell.")
            print("It's dark. You can barely see the floor.")
            print("You step carefully up the stairs.")
            print("You make it halfway up, but you slip and fall on your hands.")
            print("...blood?")
            print("Ignore it and keep moving.")
            print("Check your hands.")
            check = response_intake2("Ignore", "Check")
            # Sevi - Have the player lose a small amount of VP
            if check == 'Ignore':
                print(".")
                print(".")
                print(".")
                print("You made it to the second floor.")
                chara.update_vp(-1)
            # Sevi - Have the player lose a larger amount of VP
            if check == 'Check':
                print(".")
                print(".")
                print(".")
                print("You stop and check your hands.")
                print("Your left hand has a small bruise, but the blood isn't yours.")
                print("The blood is from a corpse in front of you.")
                print("The overwhelming smell of blood and decomposition causes you to gag.")
                print("You don't have time to spare. You HAVE to get out of here.")
                print("You scramble to your feet and continue upwards.")
                print("You made it to the second floor.")
                chara.update_vp(-3)

        print("Once again, there is one singular door open that leads to a classroom.")
        print("You peek into the room.")
        print("In the classroom, there is a singular desk and chair, a piece of paper, and a pencil.", '\n')

        print('Let’s play a Madlib!')
        num = input('Enter a number: ')
        # adj = input('Enter an adjective: ')
        verb = input('Enter a past tense verb: ')
        ani = input('Enter an animal: ')
        noun = input('Enter a noun: ')
        noun2 = input('Enter another noun: ')
        onoma = input('Enter an onomatopoeia: ')
        print("")
        print("Wow I am so glad that I was only " + num, "minutes late to class today.")
        print("The entire highway was covered in " + noun, "so everyone had to exit!")
        print("Then, once I arrived to the parking lot I could not find a space so I " + verb,
              "until I was able to find one.")
        print("Crazy thing is, I was greeted by " + chara.name, "the Cardinal " + ani, "on my way in.")
        print("He gave me a " + noun2, "and said good luck on the quiz today.")
        print(onoma + ", THERE IS A QUIZ?!", "\n")

        print("The paper goes blank, and the writes out 'Thanks for playing! Good Luck!'")
        chara.update_vp(2)

    if walking1 == 'Forward':
        print(".")
        print(".")
        print(".")
        print("After walking forward for a short time, you somehow find yourself at the Chemistry Building.")
        print("Going inside, you are overwhelmed by chemical fumes.")
        chara.update_vp(-1)
        print("There's an open classroom that you can Enter, or you can leave the building.")
        chempath = response_intake2("Enter", "Leave")
        if chempath == "Enter":
            print(".")
            print(".")
            print(".")
            print("Welcome to Science Class! Today we are going to play a riddle game.")
            print("In order for this to go smoothly here are the rules. I ask a question, and you state your answer")
            print("If you answer correctly, you get HP. If not, of course, you get nothing.")
            print("Write 'Hint 1' , or 'Hint 2' for a clue. If you know the answer, you may enter it.")
            print('You get four attempts. Good luck')
            i = 0
            while i <= 3:
                i = i + 1
                confirm = False
                answer = input("What has a mouth but can't chew: ")
                answer = inp_correct(answer)
                if answer == "River":
                    i = 5
                    confirm = True
                elif answer == "Hint 1":
                    print("Mississippi is one of my first names")
                elif answer == "Hint 2":
                    print("I stay hydrated")
                else:
                    print("Incorrect Answer")
            if confirm == True:
                print("Congratulations!")
                chara.update_vp(3)
            else:
                print("YOU LOSE")

        elif chempath == "Leave":
            print("You feel better leaving the building, but it's shame you couldn't find anything useful")



    print("You're exhausted from all of this. You yearn for your soft bed back at home.")
    print("You don't find anything much else of interest, so you begin to head towards the exit.")
    print("*CRUUUNCH*")
    print("The floor beneath you suddenly crumbles away to reveal a void-like cavern and you're falling-- fast")
    print("*THUMP*")
    print("Your shoulder hits the peak of a hill, but your adrenalin rush keeps you from feeling anything.")
    print("Before you can even think of catching yourself, your entire body begins to tumble down the steep slope--")
    print("You notice a dried vine to your right. You should be able to grab it-- but it's risky. ")
    print("What's your choice?")
    print("Grab the Vine or Continue on the Slope? ")
    vine = response_intake2("Vine", "Slope")

    if vine == 'Vine':
        print("You take a chance and quickly extend your arms forwards to grab the vine")
        print("You managed to grab it! You steady yourself.")
        print("Searching the area, you can't see much in front of you since it's so dark.")
        print("However, you do see a lot of rubble. Different objects like old tires, soda cans, papers, and the like are scattered all around.")
        print("You're not sure how long you've been hiking up the rocky slope, but your chest hurts.")
        print("Huh..That's interesting")
        print("You didn't notice it before since you were falling very quickly, but the hill actually forks off into three paths.")
        print("The middle path is the one that you fell from-- so you don't think there would be much luck going that way.")
        print("Do you want to travel left or right?")
        rockypathway = response_intake2("Left", "Right")
        if rockypathway == 'Left':
            print("Let's try going left.")
            print("After a short ascent, you reach a rusty ladder.")
            print("You muster up the last little bit of energy you have left to climb the ladder.")
            print("At the top, your greeted by a steel trapdoor. Luckily, it swings open with ease.")
            print("You rub your eyes to adjust to the sudden shift in lighting.")
            print("You seem to be in what looks like the Bingham Humanities building--")
            print("There aren't any actual lights, but there seem to be hundreds of floating candles all through the hall...")
            print("When you try to reach for one, it floats just out of your reach.")
            print(".")
            print(".")
            print(".")
            print("You know the drill at this point. You turn around the first floor corridor and notice an open door to another classroom.")
            print("You peek inside and see a small, perched gargoyle on top of a stone pillar.")
            print("You hear a distinct sound of scraping concrete as it moves its hand to point at you.")
            print("It speaks slowly, 'Come, sit down...There isn't any reason...to be afraid.'")
            print("'I have the next lesson...ready for you. It's...a...riddle.'")
            print("If you win...I can give you some useful information...")
            print("You have a bad feeling about this.")
            gargoyle = response_intake2("Sit", "Run")
            if gargoyle == "Sit":
                print("You sit down in front of the statue.")
                print("'Here is my riddle...'")

                print("'If you have me...you will want to share me...If you share me...you will no longer have me...")
                riddle1 = input("What am I?:")

                if (riddle1 == 'secret') or (riddle1 == 'a secret') or (riddle1 == 'Secret') or (riddle1 == 'A Secret'):
                    print("'That is...correct'")
                    print("'Congratulations'")
                    print("'Here is your...reward. There is only one...way out of this place.'")
                    print("'A thousand wheels...but move I do not...'")
                    print("'You will find the exit there...in the lot...")
                    print("The gargoyle rests. You feel a sense of relief that it was friendly.")
                    chara.update_vp(3)
                    print("You continue onwards to the exit.")
                else:
                    print("'That is...incorrect'")
                    print("The gargoyle rests. It almost looks a little sad.")
                    chara.update_vp(-1)
                    print("You continue onwards to the exit.")

            elif (gargoyle == "Run") and (chara.tool == "Hatchet"):
                print("You remember that you have a hatchet that you got earlier...")
                print("Looking at the porcelain gargoyle and then at your hatchet in hand, you raise your hatchet high above your head.")
                print("*CRASH*")
                print(".")
                print(".")
                print(".")
                print("Peering down to look at the shards, you begin to-")
                print("You can hear someone.")
                print("With one swift movement, the figure behind you takes a hatchet of their own.")
                print("*WHACK*")
                print("*THUMP*")
                print("Your last memory in life was your head splitting away from your body.")
                print("BAD END")
                print("Tip: Karma is a Pain...Eye for an Eye...You know how it is.")
                chara.end_screen()

            elif (gargoyle == "Run") and (chara.tool == "Rope"):
                print("You remember that you have some rope that you got earlier...")
                print("But you can't think of anything to do with it.")
                print("You choose to run away instead.")
                chara.update_vp(-1)
                print("You continue onwards to the exit.")

            elif (gargoyle == "Run") and (chara.tool == "Flashlight"):
                print("You remember that you have a flashlight that you got earlier...")
                print("But you can't think of anything to do with it.")
                print("You choose to run away instead.")
                chara.update_vp(-1)
                print("You continue onwards to the exit.")

            elif (gargoyle == "Run") and (chara.tool == "Cinnamon Candy"):
                print("You remember that you have a cinnamon hard candy that you got earlier...")
                print("But you can't think of anything to do with it.")
                print("You choose to run away instead.")
                chara.update_vp(-2)
                print("You continue onwards to the exit.")

            elif (gargoyle == "Run") and (chara.tool == "Pocketknife"):
                print("You remember that you have a pocket knife that you got earlier...")
                print("You are really interested in that information...Is it about how you can escape from here?")
                print("You think of making the gargoyle a trade offer--it seems reasonable enough.")
                print("You offer your pocket knife to the gargoyle.")
                # - Sevi: Have the pocket knife leave the inventory
                chara.remove_tool(sel_tool)
                print("'An offering...?' It asks. 'I haven't had one...in hundreds of years.")
                print("'I accept...your offering.")
                print("'In return...There is only one...way out of this place.'")
                print("'A thousand wheels...but move I do not...'")
                print("'You will find the exit there...in the lot...")
                print("The gargoyle rests with the knife by its side. You feel a sense of relief that it was friendly.")
                chara.update_vp(10)
                print("You continue onwards to the exit.")

            else:
                error_exit()

        if rockypathway == 'Right':
            print("Let's try going right.")
            print("After a short ascent, you reach a rusty ladder.")
            print("You muster up the last little bit of energy you have left to climb the ladder.")
            print("At the top, your greeted by a steel trapdoor. Luckily, it swings open with ease.")
            print("You rub your eyes to adjust to the sudden shift in lighting.")
            print("You seem to be in what looks like the Belknap Academic building--")
            print("The massive glass windows reflect the light of the moon just enough to where you can see. It's beautiful.")
            print("This time, it's a little different.")
            print("Rather than an open classroom and some strange task meant to freak you out, there's a singular table with a PC and a chair")
            print("You go over to investigate but you're suddenly grabbed!")
            print("Computer cables wrap themselves tightly around your wrists and you're trapped in front of the keyboard.")
            print("In your panic, a robotic voice from the computer speaks,")
            print("'HEY YOU! LET'ZZZ PLAY A QUIZZZ GAME!'")
            print("'IF YOU GET THEM RIGHT, I'LL GIVE YOU A HINT'")
            print("'IF NOT...IT'ZZZ OKAY!'")
            print("IT'ZZZ JUZZZT A GAME!'")
            print("'BUT BE CAREFUL!'")
            print("i f  y o u  l o o k  a w a y, y o u ' r e  d e a d")
            print("...'QUEZZZTION 1")
            print("'WHAT IZZZ THE YELLOW PART OF AN EGG CALLED? ")
            print("[1] - A White")
            print("[2] - Jelly")
            print("[3] - A Yolk")
            print("[4] - A Bee")
            quiz1 = input("Answer:")
            if quiz1 == '3':
                print("'THAT'ZZZ CORRECT! YOU'RE ZZZO ZZZMART'")
                chara.update_vp(1)
            else:
                print("'THAT'ZZZ INCORRECT! IT'ZZZ OKAY!'")

            print("*drip*")
            print("*drip*")
            print("*drip*")
            print("What's dripping down your neck? It almost feels like someone cracked an egg on top of your head.")
            print("...Do you check?")
            egg = response_intake2("Yes", "No")
            if (egg == 'Yes') and (chara.tool == "Pocketknife"):
                print(".")
                print(".")
                print(".")
                print("'WHY DID YOU LOOK AWAY FROM ME?'")
                print("'ARE YOU NOT ENJOYING YOURZZZELF?'")
                print("'t h e n  d i e'")
                print("You quickly take your pocket knife and slice through the wires on your wrists.")
                print("You kick the computer to the ground and run through the doors at the entrance.")
                print("You feel a sense of confidence.")
                chara.update_vp(4)
            elif egg == 'Yes':
                print(".")
                print(".")
                print(".")
                print("'WHY DID YOU LOOK AWAY FROM ME?'")
                print("'ARE YOU NOT ENJOYING YOURZZZELF?'")
                print("'t h e n  d i e'")
                print("You're exposed to horrors you can't even imagine")
                print("BAD END")
                print("Tip: I mean...it said not to turn around")
                chara.end_screen()
            else:
                print("You decide against it.")
                print("...'QUEZZZTION 2")
                print("'THE PLANET MARZZZ IZZZ ALZZZO KNOWN AZZZ THE _____ PLANET'")
                print("[1] - Red")
                print("[2] - Steamy")
                print("[3] - Orange")
                print("[4] - Spinning")
                quiz2 = input("Answer:")

                if quiz2 == '1':
                    print("'THAT'ZZZ CORRECT! YOU'RE ZZZO ZZZMART'")
                    chara.update_vp(1)
                else:
                    print("'THAT'ZZZ INCORRECT! IT'ZZZ OKAY!'")

                print("It's so hot. You feel a heat that you've never felt before coming from behind you...")
                print("...Do you check?")
                mars = response_intake2("Yes", "No")
                if (mars == 'Yes') and (chara.tool == "Pocketknife"):
                    print(".")
                    print(".")
                    print(".")
                    print("'WHY DID YOU LOOK AWAY FROM ME?'")
                    print("'ARE YOU NOT ENJOYING YOURZZZELF?'")
                    print("'t h e n  d i e'")
                    print("You quickly take your pocket knife and slice through the wires on your wrists.")
                    print("You kick the computer to the ground and run through the doors at the entrance.")
                    print("You feel a sense of confidence.")
                    chara.update_vp(4)
                elif (mars == 'Yes'):
                    print(".")
                    print(".")
                    print(".")
                    print("'WHY DID YOU LOOK AWAY FROM ME?'")
                    print("'ARE YOU NOT ENJOYING YOURZZZELF?'")
                    print("'t h e n  d i e'")
                    print("You're exposed to horrors you can't even imagine")
                    print("BAD END")
                    print("Tip: I mean...it said not to turn around")
                    chara.end_screen()
                else:
                    print("You decide against it.")
                    print("...'QUEZZZTION 3")
                    print("'MY MOTHER'ZZZ MOTHER IZZZ MY WHAT?'")
                    print("[1] - Aunt")
                    print("[2] - Step-Mother")
                    print("[3] - Niece")
                    print("[4] - Grandmother")
                    quiz3 = input("Answer:")

                    if quiz3 == '4':
                        print("'THAT'ZZZ CORRECT! YOU'RE ZZZO ZZZMART'")
                        chara.victory_points = chara.victory_points + 1
                    else:
                        print("'THAT'ZZZ INCORRECT! IT'ZZZ OKAY!'")

                    if quiz1 == '3' and quiz2 == '1' and quiz3 == '4':
                        print("'CONGRATULATIONZZZ! YOU GOT THEM ALL RIGHT!'")
                        print("'HERE IZZZ MY HINT:'")
                        print("'THE WAY OUT OF THIZZZ PLACE IS THROUGH THE PARKING LOT'")
                        print("'THANK YOU FOR PLAYING!'")
                        print("The strange computer shuts off and your wrists are freed.")
                        print("You notice that the front doors of the building are now open.")
                        chara.update_vp(1)

                    else:
                        print("'YOU SEEMED TO HAVE MISSED ONE. YOU DIDN'T GET THEM ALL RIGHT'")
                        print("'I DON'T HAVE A HINT FOR YOU'")
                        print("'THANK YOU FOR PLAYING!'")
                        print("The strange computer shuts off and your wrists are freed.")
                        print("You notice that the front doors of the building are now open.")
            print("The night air on your skin feels amazing.")

    if vine == 'Slope':
        print("It's too risky to reach for the vine. You're falling way too fast.")
        print(".")
        print(".")
        print(".")
        print("*THUMP*")
        print("You've finally hit the bottom.")
        print("The temperature change is noticeably much colder.")
        print("The also notice that the floor beneath you has changed from a rocky soil to solid ice.")
        print("You also notice a brilliant red rose tucked away behind a layer of ice- but are unsure of how to get it out.")

        if chara.tool == "Hatchet":
            print("You remember that you have the hatchet from that one room.")
            print("*THUMP* *THUMP* *CRACK* *CRACK*")
            print("It didn't take much effort to free the flower. You hold it in your hand")
            print("Somehow, it still being alive reminds you of your resiliency.")
            chara.update_vp(3)
            print("From what you can see, you have two different directions you can go")
            print("There is a a grouping of large rocks that might have once been the site of a waterfall judging from the shimmering ice.")
            print("You could probably climb the rocks and go through the tunnel near the cavern's roof.")
            print("Or you could go attempt to go through the large stone door ahead of you.")
            print("So, do you want to take the upper path or the lower path?")

        else:
            print("From what you can see, you have two different directions you can go")
            print("There is a a grouping of large rocks that might have once been the site of a waterfall judging from the shimmering ice.")
            print("You could probably climb the rocks and go through the tunnel near the cavern's roof.")
            print("Or you could go attempt to go through the large stone door ahead of you.")
            print("So, do you want to take the upper path or the lower path?")

        icepathway = response_intake2("Upper", "Lower")

        if icepathway == 'Upper':
            print("Let's try taking the upper pathway.")
            print("You carefully check your footing with each step as you scale the large rocks.")
            print(".")
            print(".")
            print(".")
            print("After reaching the top, you were hoping for something more-- but you were greeted by another long hallway.")
            print("As you move forward, however, you begin to see pieces of artwork on the walls.")
            print("There's a large painting of three ladies, all dressed in one of the primary colors, having tea.")
            print("There's a small series of paintings centered around French desserts.")
            print("You also see a large, detailed drawing of a greenhouse filled with plants.")
            print("You find yourself in an art gallery. This must be the Hite Art Institute.")
            print("The wooden floor creaks as you step through the gallery.")
            print("You see that the double doors connecting the lobby to the gallery are open.")

            if chara.tool == "Flashlight":
                print("You remember that you have the flashlight, so you flick it on with your thumb.")
                print("Shakily, you turn the flashlight back towards the gallery for a final check;")
                print("*THUNK*")
                print("You notice that a painting fell off of the wall...")
                print("What's this?...There was a vault hidden on the wall behind the frame.")
                print("Are you going to try the vault or continue on?")

                artgallery = response_intake2("Vault", "Continue")
                if artgallery == 'Vault':
                    print("You clench your hands tightly around the handle and turn it hard")
                    print(".")
                    print(".")
                    print(".")
                    print("You find a Strawberry Soda, a Bag of Gummy Bears and a sticky note that reads,'Sevi's Secret Snack Stash..Don't Touch!'")
                    print("You take a short break and have a snack. You feel a lot better.")
                    chara.update_vp(3)
                    print("You leave the vault.")
                elif artgallery == 'Continue':
                    print("You continue on.")

            print("You find a small note on the ground tucked in a crevice:")
            print("It says, 'I'm a puzzle! Solve me!")
            puzzle = response_intake2("Yes", "No")
            if puzzle == 'Yes':
                print("Q1: What were the colors of the three painted ladies?")
                print("[1] - Red, Green, Blue")
                print("[2] - Orange, Green, Purple")
                print("[3] - Red, Yellow, Blue")
                print("[4] - Yellow, Blue, Green")
                puzzle1 = input("Answer: ")

                print(".")
                print(".")
                print(".")
                print("You write that down.")

                print("Q2: Which one of these is NOT a French dessert?")
                print("[1] - Canoli")
                print("[2] - Petit Fours")
                print("[3] - Eclairs")
                print("[4] - Macarons")
                puzzle2 = input("Answer: ")

                print(".")
                print(".")
                print(".")
                print("You write that down.")

                print("Q3: If a red house is made of red bricks, and a yellow house is made of yellow bricks, what is a greenhouse made of?")
                print("[1] - Red Bricks")
                print("[2] - Green Bricks")
                print("[3] - Yellow Bricks")
                print("[4] - Glass")
                puzzle3 = input("Answer:")

                print(".")
                print(".")
                print(".")
                print("You write that down.")

                if puzzle1 == '3' and puzzle2 == '1' and puzzle3 == '4':
                    print("You matched up the answers to the puzzle on the bottom of the page")
                    print("It reads, 'You're almost to the parking lot! Good Luck!'")
                    print("You feel a sense of pride.")
                    chara.update_vp(3)

                else:
                    print("You matched up the answers to the puzzle on the bottom of the page")
                    print("It reads, 'Yor'ue amsolt ot the kinparg otl! oodG ucLk!'")
                    print("Huh...It doesn't seem right. You feel like you wasted your time.")
                    chara.update_vp(-1)
            elif puzzle == 'No':
                print("You really don't feel like it...")
                print("You notice that the front entrance to the building are open as well.")
                print("You exit the building.")

        if icepathway == 'Lower':
            print("Let's try taking the lower pathway.")
            print("You carefully check your footing and shove the stone door as hard as you can.")
            print("...You realize that it's actually a pull door. It opens pretty easy afterwards.")
            print(".")
            print(".")
            print(".")
            print("After opening the door, you were hoping for something more-- but you were greeted with another long hallway.")
            print("You begin to hear the playing of a piano-- but it's just one key.")
            print("As you walk, the music expands to a simple melody.")
            print("Percussion.")
            print("Strings.")
            print("Woodwind.")
            print("And with a couple of more steps, you began hearing the opening of an opera performance.")
            print("You realize that you seem to be in Thrust Theatre.")
            print("The first thing you notice is a mannequin posed on stage, its head has been replaced with a cardinal mask")
            print("It sings to you, 'Would someone, hear my song? My one wish?'")
            print("Well, do you?")
            song = response_intake2("Yes", "No")
            if song == 'Yes':
                print("You sit down in the seats in front of the mannequin.")
                print("She sings a story to you-- about love, loss, and triumph.")
                print("If you weren't trapped here against your will, you might have shed a tear or two.")
                print("'If only, if only...I had a gift for my child. Something sweet, something to eat...'")
                if chara.tool == "Cinnamon Candy":
                    print("You remember that you have a piece of cinnamon candy in your pocket...")
                    print("You toss it gently on stage.")
                    print("The cardinal looks at it and then at you, while not breaking a tune.")
                    print("She erupts into a major finale-- all of the instruments playing furiously")
                    print("And afterwards,")
                    print("'Thank you, your kindness won't be forgotten...'")
                    chara.update_vp(6)

                print("After the performance of her life, the cardinal falls asleep")
                print("You leave the theatre through the front entrance")
                chara.update_vp(2)
            elif song == 'No':
                print("You really don't feel like this.")
                print("You leave the theatre through the front entrance")

    print("The night air on your skin feels amazing.")

    print("After everything, you finally reach the parking lot.")
    print(".")
    print(".")
    print(".")
    print("You feel your world start to spin")
    print("Your vision becomes blurry with spots appearing before it eventually fades.")
    print("You fall to the ground into a deep sleep.")

    low = 6
    high = 12

    if chara.victory_points <= low:
        # Sevi - This is the bad end that is triggered by having only a small amount of VP
        print(".")
        print(".")
        print(".")
        print("You rub your sore eyes...You blink a few times before looking around the room")
        print("You realize that you're still at the Life Sciences building...")
        print("You throw your head back in frustration, 'I WAS OUT!' You thought to yourself.")
        print("Your legs and arms are tattered in cuts, scrapes and bruises.")
        print("You have no energy left.")
        print("You lay on the sidewalk, staring at the starless sky as the darkness creeps in.")
        print("BAD END")
        print("Tip: Play the game again and try and get more victory points!")
        chara.end_screen()
    elif (chara.victory_points > low) and (chara.victory_points < high):
        # Sevi - This is the neutral end that is triggered by having a medium amount of VP
        print(".")
        print(".")
        print(".")
        print("You rub your sore eyes...You blink a few times before looking around the room")
        print("You realize that you're in your bed at home...")
        print("You throw your head back in happiness, 'Was this all just a dream' You thought to yourself.")
        print("The cuts, scrapes and bruises layered all across your body tell you otherwise. ")
        print(".")
        print(".")
        print(".")
        print("You try going to the university after that,")
        print("It brings back too many bad memories. You're unable to sit through a class without fearing for your life.")
        print("You ask some of your old friends about it, but no one believes you.")
        print("You live the rest of your life in fear of what you've experienced-- scared of one day being transported back to that place.")
        print("NEUTRAL END")
        print("Thanks for playing!")
        print("Tip: Play the game again and try and get more victory points!")
        chara.end_screen()
    elif chara.victory_points >= high:
        # Sevi - This is the good end that is triggered by having a higher amount of VP
        print(".")
        print(".")
        print(".")
        print("You rub your eyes...You blink a few times before looking around the room")
        print("You realize that you're in your bed at home...")
        print("It's soft, warm and comfortable just like you remembered it being")
        print("You throw your head back in happiness, 'Was this all just a dream' You thought to yourself.")
        print("You have some scratches that prove otherwise, but nothing that won't fade with time")
        print(".")
        print(".")
        print(".")
        print("You take some time off to go to therapy.")
        print("You start to go to university again after a couple of weeks,")
        print(
            "You ask some of your friends about it, some were skeptical but others said they experienced something similar.")
        print("'A mass hallucination?, or something else?' You wonder.")
        print("You graduate that spring and make it your life's work trying to find out what happened that strange night.")
        print("BEST END")
        print("Thanks for playing!")
        chara.end_screen()
