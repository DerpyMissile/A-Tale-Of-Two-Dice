label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    "The sun beats down on two kids' backs, hiding in a bush."
    o "Listen, Tetra. How much are you willing to bet?"
    t "How much are you willing to bet, Octa?"
    o "Bet?"
    o "I'm willing to bet my entire life's savings!"
    t "And how much is that?"
    o "Five pence!"
    t "Pennies???"
    o "Bet you don't have anything like that!"

    "Tetra places a finger over Octa's mouth."
    t "Shh!"
    "A man emerges from the shop, tall and stout. His basket filled with steaming bread."
    "Octa's eyes widen."
    o "That's him! That's the Viper. The vile villain who uh...."
    t "Who uh....?"
    menu:
        "gambles a lot?":
            jump continuing1
        "led the rise of the bread monster in the forest?":
            jump continuing1

label continuing1:
    o "It doesn't matter! We're gonna get him."

    "Octa sneaks up closer to the man."
    o "Are you bready for this?"
    t "I'm gonna ignore that."
    t "So what's the plan?"
    o "I'm gonna take his hat, and we're hiding it in the bushes."
    o "You'll be the distraction!"
    t "Wait, I had no idea about this!"
    o "Trust me. Viper will have no idea what hit him."

    "And there Octa goes, crawling away like a mischievous rat."
    t "..."
    t "Okay, think, Tetra, what can we do with this?"
    menu:
        "Squawk like a bird":
            menu:
                "Roll Die":
                    $ rollDie = renpy.random.randint(1, 6)
                "Roll Die with Compassion":
                    $ rollDie = renpy.random.randint(1, 6)
                "ROLL DIE WITH PASSION":
                    $ rollDie = renpy.random.randint(1, 6)
            if(rollDie >= 3):
                "From out of Tetra's throat, the sound of a sparrow comes out."
                "The man turns his head over to the source."
                "From behind the man, Octa pops out from behind."
                "He snatches the hat and runs off."
            else:
                "Tetra starts coughing and out of his mouth comes a sparrow."
                "What?"
                "Well, it got the man to turn his head anyways, so that worked."
                "Then the sparrow flies away."
                "...And the man is coming over."
                "Octa suddenly appears behind the man and snatches the hat."
            jump continuing2
        "Roll down the road":
            "This seems to be a horrible idea, but nothing seems to be better."
            "Tetra preps himself to side of the road."
            menu:
                "Roll Die":
                    $ rollDie = renpy.random.randint(1, 6)
                "Roll Die with Compassion":
                    $ rollDie = renpy.random.randint(1, 6)
                "ROLL DIE WITH PAIN":
                    $ rollDie = renpy.random.randint(1, 6)
            if(rollDie >= 5):
                "He lies down and starts rolling quickly down the path."
                "The man gasps."
                m "What is that?!"
                "Then Tetra rolls into the bush with such finesse that he doesn't get caught."
            else:
                "Tetra lies and veers off the path."
                "And then he bumps into something."
                "Rather it's a someone."
                "And he bumped into the man with the bread."
                "Please hedoesn'twanttobeturnedintoabreadmonster."
            jump continuing2

label continuing2:
    o "Go go go! I got it!"
    "Octa zooms by so quickly that Tetra could not get his bearings."
    "The man starts looming over him."
    "Time to book it!"
    "Within seconds, Tetra pushes himself up to run after Octa."
    t "Wait up!"
    "Behind them, the man chases after them, bread and all."
    o "We gotta lose him somehow. Come on!"

    "Before the two boys, a crossroad stretches out."
    o "Which way do we go?"
    t "You're asking me?!"
    o "I don't remember where we came from!"
    o "You choose!"
    menu:
        "Left":
            t "Go left!"
            jump leftRoute
        "Right":
            t "Go right!"
            jump rightRoute
        "I don't know?":
            t "Why should I be the one to choose?"
            o "We don't have time! Your luck ends up working out anyways!"
            t "Okay let me bring out my dice."
            o "Oh my god, Tetra!"
            menu:
                "Roll Die":
                    $ rollDie = renpy.random.randint(1, 6)
                "Roll Die with Fear":
                    $ rollDie = renpy.random.randint(1, 6)
                "ROLL DIE WITH A CRIPPLING SENSE OF EXISTENTIALISM":
                    $ rollDie = renpy.random.randint(1, 6)
            if(rollDie >= 4):
                t "Go right!"
                jump rightRoute
            else:
                t "Go left!"
                jump leftRoute

label leftRoute:
    t "To be honest, I don't think we went this way at all!"
    o "It's fine! As long as we can get away!"
    "They end up catching their breath near one large tree."
    "Octa looks behind them."
    o "I think we lost him."
    o "But we got it!"

    "Octa holds the chef's hat victoriously."
    o "Okay, but where are we now?"
    t "I told you I don't remember where this leads."
    "Octa deflates at that thought."
    o "There's no road leading back either..."
    o "Why don't we ask the birds?"
    t "That's not gonna work."

    o "You never asked how the birds were doing, now come on."
    "Octa pulls Tetra along to one of the birds on the rock."
    o "It never hurt to at least say hi to the bird."
    menu:
        "Say hi.":
            t "Hello, little bird?"
            menu:
                "Roll Die":
                    $ rollDie = renpy.random.randint(1, 6)
                "Roll Die with Curiosity":
                    $ rollDie = renpy.random.randint(1, 6)
                "ROLL DIE WITH THE SOUL OF CHARLES DARWIN":
                    $ rollDie = renpy.random.randint(1, 6)
            if(rollDie >= 4):
                b "Hello, tiny human."
                "Tetra jumps back, while Octa laughs."
                t "Not funny."
                o "It's very funny."
                t "Whatever. So little bird, do you know a way back to town?"
                b "Tiny human, your towns are so different from my own."
                b "But there is a place to the east from here."
                o "Thank you, bird friend!"
            else:
                "The bird starts chirping, and Octa seems enraptured by this converation."
                t "Tell me you're messing with me."
                o "Hm? Sorry, I'm talking with the bird."
                o "So there's something to the east? Gotcha!"
                o "Okay, Tetra, say thank you to the bird."
                t "Thank you...?"
        "Do nothing.":
            "Tetra stands there like a stone statue."
            o "Hello? Earth to Tetra?"
            menu:
                "Stand there longer.":
                    o "Uhhh... Tetra?"
                    menu:
                        "Turn into a stone statue.":
                            o "Now you're just joking with me."
                            "Octa nudges Tetra, and he tilts over, slamming into the ground and breaking into bits of stone."
                            "Life's hard when you turn to stone."
                            return
                "Wave hand.":
                    o "Well, don't scare me like that!"
                    o "Anyways, I talked to the bird, and there's something east from here."
                    t "You talked to a bird?"
                    o "And you almost turned into stone."

    o "Okay! We got a lead. We head east from here!"
    t "Are you sure a bird is a good source?"
    o "I'll take a bird over that bread monster."
    "Octa raises his hand up as he marches over to the right."
    t "Fine."
    "Tetra follows after his friend."
    "A large expanse of trees fold before them. In fact, it like their own civilization."
    "Bridges and ropes and seeds and waaaay more birds than expected."
    t "What is this?"

    "A red bird flies down to perch on Octa's shoulders."
    o "This must be the amazing bird civilizations from the stories!"
    t "Wait, you've heard of this?"
    o "Obviously, who hasn't? Anyways, birdie, do you know where the town is?"
    "The bird chirps and shakes its head."
    t "Well, could you lead us to your ruler?"
    "The bird nods and flaps over to the inside of the tree."
    o "Now, we gotta go."
    t "I don't-"
    "Octa grabs Tetra's wrist and goes inside."

    "The bird leads them through a vast expanse of stairs."
    "The boys have no idea when they'll reach the top until they stand before two ornate doors."
    "The doors open inward to reveal a royal blue bird."
    t "I've never seen a bird so big..."
    o "Don't be rude to their ruler!"
    "The large bird tilts its head towards them."
    b "Welcome to our humble abode! My name is Queen Birb."
    b "Might I interest you treats or a tour of this place?"
    "Octa looks to Tetra."
    menu:
        "Bow head.":
            b "Truly, there is no need to be so formal."
            o "I'm so, so sorry to inconvenience you, but might you know the way back."
            b "Would you happen to be part of the Bread Town?"
            t "Bread Town?"
            b "Yes, there is a town south of here, known for their freshest bread."
            o "Yes, yes! We are part of that town. We don't know how to get back."
            "Tetra shoots a glare at Octa."
        "Swear fealty to the queen.":
            b "Oh ho ho, you're a rather bold one, aren't you?"
            b "Do you wish to relinquish your life as a human to become a bird?"
            t "I do."
            b "So be it! You will be my newest knight."
            "From then on, Tetra begins his transformation into a bird knight."
            return
    
    b "I've heard of children getting lost in our forest."
    b "We still don't know why that is the case, but we can take you home."
    b "We prefer to not war with the rest of the humans again."
    o "Look, Tetra! We can go home now!"
    t "Are you even sure?"
    o "It's better than being lost!"
    "To the side, two large birds appear near the window."
    b "Those two birds shall be your rides. Though you're always welcome to come back."
    o "Thank you so much, Queen Birb."
    t "Yes, uh, thank you."

    "The two boys climb onto the backs of the larger birds."
    t "Huh, why don't these ones speak?"
    o "You just can't understand them."
    "The birds squawk and within seconds the two boys ascend into the air."
    o "I've never seen something like this in my life!"
    menu:
        "Roll Die":
            $ rollDie = renpy.random.randint(1, 6)
        "Roll Die with Vigor":
            $ rollDie = renpy.random.randint(1, 6)
        "ROLL DIE WITH OH GOD WE'RE GONNA PLUMMET TO OUR DEATHS":
            $ rollDie = renpy.random.randint(1, 6)
    if(rollDie >= 5):
        t "Me too! I might want to come back to this place."
        "The entire ride goes without a hitch. The sky is so blue and vast."
        "It's a sight that neither child wants to forget this wild day."
    elif(rollDie >=3):
        t "This whole thing is kind of nervewrecking."
        "Tetra grips at the feathers, causing the bird to screech."
        "This whole ride is turbulent, but the view makes up for it. Somewhat."
    else:
        t "Help!"
        "Tetra slips from the back of the bird."
        o "Tetra!"
        o "Hey, birdie, please?"
        menu:
            "Roll Die":
                $ rollDie = renpy.random.randint(1, 6)
            "Roll Die with Grace":
                $ rollDie = renpy.random.randint(1, 6)
            "ROLL DIE WITH THE POWER OF THE UNYIELDING BIRB KNIGHT":
                $ rollDie = renpy.random.randint(1, 6)
        if(rollDie >= 4):
            "Two claws latch onto Tetra's shoulders, pulling him out of free fall."
            o "I've got you!"
            "Tetra squirms in the grip, but stills himself."
            t "This is a horrible experience."
            o "Would you rather still be falling?"
            t "No."
        else:
            "The claws were unable to catch Tetra and he plummets to the ground."
            o "Oh no!"
            t "Please! Save meeeee-!"
            "..."
            "Tetra's not sure how long he falls for until he lands into a lake."
            "He pulls himself up to the land, where wolves are there to greet him."
            menu:
                "Talk to the wolves":
                    menu:
                        "Roll Die":
                            $ rollDie = renpy.random.randint(1, 6)
                        "Roll Die with Courage":
                            $ rollDie = renpy.random.randint(1, 6)
                        "ROLL DIE WITH A PIECE OF LEATHER":
                            $ rollDie = renpy.random.randint(1, 6)
                    if(rollDie > 2):
                        w "Child, you have appear out of the sky all of a sudden."
                        t "You talk."
                        w "That I do. Now come, let us find you new furs."
                        "Tetra slowly became more acquainted to the wolf. Then they were family."
                        "Nowadays, he spends his time in forest hunting and foraging with the wolf."
                        return
                    else:
                        "The Wolf howls at Tetra, and he shrugs."
                        "There's not much he could do now, then wait."
                        return
                "Defend yourself":
                    menu:
                        "Roll Die":
                            $ rollDie = renpy.random.randint(1, 6)
                        "Roll Die with Courage":
                            $ rollDie = renpy.random.randint(1, 6)
                        "ROLL DIE WITH A PIECE OF LEATHER":
                            $ rollDie = renpy.random.randint(1, 6)
                    if(rollDie > 2):
                        "Tetra picks up the stick and readies it to attack."
                        "He waves it at the wolf before it starts running away."
                        "This is his territory now, and he'll defend it with his life."
                        return
                    else:
                        "Instead of defending himself with the stick he found, the stick slips out of his hand and into the woods."
                        "He braces himself for impact, but the stick is right in front of him with the wolf."
                        "He throws it again. The wolf chases after it. It turns into a game of fetch."
                        "He's found a friend right here after all."
                        return

    "The birds land without a problem onto the familiar streets the boys know."
    "They wave a thanks and farewell to the birds."
    o "Now what do you think about that for an adventure?"
    t "Not what I signed up for. At all."
    o "Come on, now-"
    m "You."
    "Octa scurries to hide behind Tetra."
    t "You."
    m "You're friends with the birds now, I take it?"
    o "We are! So you should fear us!"

    "The man lets out a hearty laugh."

    return

label rightRoute:
    # This ends the game.

    return
