label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    play music "<loop 0.00>..//audio//hillSong.mp3" volume 0.5

    scene bush with Fade(2.0, 0.0, 2.0)
    "The sun beats down on two kids' backs, hiding in a bush."
    show octa Neutral at right
    o "Listen, Tetra. How much are you willing to bet?"
    show tetra Neutral at left
    t "How much are you willing to bet, Octa?"
    o "Bet?"
    show octa Happy at right
    o "I'm willing to bet my entire life's savings!"
    t "And how much is that?"
    o "Five pence!"
    t "Pennies???"
    o "Bet you don't have anything like that!"

    "Tetra places a finger over Octa's mouth."
    show octa Neutral at right
    show tetra Angry at left
    t "Shh!"
    "A man emerges from the shop, tall and stout. His basket filled with steaming bread."
    "Octa's eyes widen."
    show octa Angry at right
    o "That's him! That's the Viper. The vile villain who uh...."
    show tetra Neutral at left
    t "Who uh....?"
    menu:
        "gambles a lot?":
            jump continuing1
        "led the rise of the bread monster in the forest?":
            jump continuing1

label continuing1:
    o "It doesn't matter! We're gonna get him."

    "Octa sneaks up closer to the man."
    show octa Happy at right
    o "Are you bready for this?"
    t "I'm gonna ignore that."
    t "So what's the plan?"
    o "I'm gonna take his hat, and we're hiding it in the bushes."
    o "You'll be the distraction!"
    show tetra Angry at left
    t "Wait, I had no idea about this!"
    o "Trust me. Viper will have no idea what hit him."
    show tetra Neutral at left

    hide octa Happy
    "And there Octa goes, crawling away like a mischievous rat."
    t "..."
    t "Okay, think, Tetra, what can we do with this?"
    hide tetra Neutral
    menu:
        "Squawk like a bird":
            menu:
                "Roll Die":
                    $ rollDie = renpy.random.randint(1, 6)
                "Roll Die with Compassion":
                    $ rollDie = renpy.random.randint(1, 6)
                "ROLL DIE WITH PASSION":
                    $ rollDie = renpy.random.randint(1, 6)
            if(rollDie == 1):
                show roll1 at truecenter
            elif(rollDie == 2):
                show roll2 at truecenter
            elif(rollDie == 3):
                show roll3 at truecenter
            elif(rollDie == 4):
                show roll4 at truecenter 
            elif(rollDie == 5):
                show roll5 at truecenter
            else:
                show roll6 at truecenter
            play sound diceRoll
            if(rollDie >= 3):
                show tetra Happy at left
                "From out of Tetra's throat, the sound of a sparrow comes out."
                "The man turns his head over to the source."
                "From behind the man, Octa pops out from behind."
                "He snatches the hat and runs off."
            else:
                show tetra Neutral at left
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
            if(rollDie == 1):
                show roll1 at truecenter
            elif(rollDie == 2):
                show roll2 at truecenter
            elif(rollDie == 3):
                show roll3 at truecenter
            elif(rollDie == 4):
                show roll4 at truecenter 
            elif(rollDie == 5):
                show roll5 at truecenter
            else:
                show roll6 at truecenter
            play sound diceRoll
            if(rollDie >= 5):
                "He lies down and starts rolling quickly down the path."
                "The man gasps."
                m "What is that?!"
                show tetra Happy at left
                "Then Tetra rolls into the bush with such finesse that he doesn't get caught."
            else:
                "Tetra lies and veers off the path."
                show tetra Sad at left
                "And then he bumps into something."
                "Rather it's a someone."
                "And he bumped into the man with the bread."
                "Please hedoesn'twanttobeturnedintoabreadmonster."
            jump continuing2

label continuing2:
    scene crossroads with Fade(2.0, 0.0, 2.0)
    show octa Happy at right
    o "Go go go! I got it!"
    hide octa Happy
    "Octa zooms by so quickly that Tetra could not get his bearings."
    "The man starts looming over him."
    "Time to book it!"
    "Within seconds, Tetra pushes himself up to run after Octa."
    show tetra Sad at left
    t "Wait up!"
    "Behind them, the man chases after them, bread and all."
    show octa Neutral at right
    o "We gotta lose him somehow. Come on!"

    "Before the two boys, a crossroad stretches out."
    o "Which way do we go?"
    show tetra Angry at left
    t "You're asking me?!"
    o "I don't remember where we came from!"
    o "You choose!"
    menu:
        "Left":
            show octa Neutral at left
            t "Go left!"
            jump leftRoute
        "Right":
            show octa Neutral at left
            t "Go right!"
            jump rightRoute
        "I don't know?":
            show tetra Angry at left
            t "Why should I be the one to choose?"
            show octa Angry at right
            o "We don't have time! Your luck ends up working out anyways!"
            show tetra Happy at left
            t "Okay let me bring out my dice."
            o "Oh my god, Tetra!"
            menu:
                "Roll Die":
                    $ rollDie = renpy.random.randint(1, 6)
                "Roll Die with Fear":
                    $ rollDie = renpy.random.randint(1, 6)
                "ROLL DIE WITH A CRIPPLING SENSE OF EXISTENTIALISM":
                    $ rollDie = renpy.random.randint(1, 6)
            if(rollDie == 1):
                show roll1 at truecenter
            elif(rollDie == 2):
                show roll2 at truecenter
            elif(rollDie == 3):
                show roll3 at truecenter
            elif(rollDie == 4):
                show roll4 at truecenter 
            elif(rollDie == 5):
                show roll5 at truecenter
            else:
                show roll6 at truecenter
            play sound diceRoll
            if(rollDie >= 4):
                t "Go right!"
                jump rightRoute
            else:
                t "Go left!"
                jump leftRoute

label leftRoute:
    scene forest with Fade(2.0, 0.0, 2.0)
    show tetra Neutral at left
    t "To be honest, I don't think we went this way at all!"
    show octa Neutral at right
    o "It's fine! As long as we can get away!"
    "They end up catching their breath near one large tree."
    "Octa looks behind them."
    o "I think we lost him."
    o "But we got it!"

    show octa Happy at right
    "Octa holds the chef's hat victoriously."
    show octa Neutral at right
    o "Okay, but where are we now?"
    t "I told you I don't remember where this leads."
    show octa Sad at right
    "Octa deflates at that thought."
    o "There's no road leading back either..."
    show octa Neutral at right
    o "Why don't we ask the birds?"
    show tetra Angry at left
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
            if(rollDie == 1):
                show roll1 at truecenter
            elif(rollDie == 2):
                show roll2 at truecenter
            elif(rollDie == 3):
                show roll3 at truecenter
            elif(rollDie == 4):
                show roll4 at truecenter 
            elif(rollDie == 5):
                show roll5 at truecenter
            else:
                show roll6 at truecenter
            play sound diceRoll
            if(rollDie >= 4):
                b "Hello, tiny human."
                show tetra Happy at left
                "Tetra jumps back, while Octa laughs."
                show tetra Angry at left
                t "Not funny."
                show octa Happy at right
                o "It's very funny."
                show tetra Neutral at left
                t "Whatever. So little bird, do you know a way back to town?"
                b "Tiny human, your towns are so different from my own."
                b "But there is a place to the east from here."
                o "Thank you, bird friend!"
            else:
                "The bird starts chirping, and Octa seems enraptured by this converation."
                show tetra Angry at left
                t "Tell me you're messing with me."
                show octa Neutral at right
                o "Hm? Sorry, I'm talking with the bird."
                o "So there's something to the east? Gotcha!"
                o "Okay, Tetra, say thank you to the bird."
                show tetra Sad at left
                t "Thank you...?"
        "Do nothing.":
            show tetra Neutral at left
            "Tetra stands there like a stone statue."
            show octa Neutral at right
            o "Hello? Earth to Tetra?"
            menu:
                "Stand there longer.":
                    o "Uhhh... Tetra?"
                    menu:
                        "Turn into a stone statue.":
                            show octa Sad at right
                            o "Now you're just joking with me."
                            hide tetra Neutral
                            "Octa nudges Tetra, and he tilts over, slamming into the ground and breaking into bits of stone."
                            "Life's hard when you turn to stone."
                            return
                "Wave hand.":
                    show octa Neutral at right
                    o "Well, don't scare me like that!"
                    o "Anyways, I talked to the bird, and there's something east from here."
                    t "You talked to a bird?"
                    o "And you almost turned into stone."

    show octa Happy at right
    o "Okay! We got a lead. We head east from here!"
    show tetra Sad at left
    t "Are you sure a bird is a good source?"
    o "I'll take a bird over that bread monster."
    "Octa raises his hand up as he marches over to the right."
    show tetra Neutral at left
    t "Fine."
    "Tetra follows after his friend."
    scene birbHouse with Fade(2.0, 0.0, 2.0)
    "A large expanse of trees fold before them. In fact, it like their own civilization."
    "Bridges and ropes and seeds and waaaay more birds than expected."
    t "What is this?"

    "A red bird flies down to perch on Octa's shoulders."
    show octa Neutral at right
    o "This must be the amazing bird civilizations from the stories!"
    show tetra Neutral at left
    t "Wait, you've heard of this?"
    o "Obviously, who hasn't? Anyways, birdie, do you know where the town is?"
    "The bird chirps and shakes its head."
    t "Well, could you lead us to your ruler?"
    "The bird nods and flaps over to the inside of the tree."
    o "Now, we gotta go."
    show tetra Sad at left
    t "I don't-"
    "Octa grabs Tetra's wrist and goes inside."

    "The bird leads them through a vast expanse of stairs."
    "The boys have no idea when they'll reach the top until they stand before two ornate doors."
    "The doors open inward to reveal a royal blue bird."
    show tetra Happy at left
    t "I've never seen a bird so big..."
    show octa Angry at right
    o "Don't be rude to their ruler!"
    "The large bird tilts its head towards them."
    b "Welcome to our humble abode! My name is Queen Birb."
    b "Might I interest you treats or a tour of this place?"
    show octa Neutral at right
    "Octa looks to Tetra."
    menu:
        "Bow head.":
            show tetra Neutral at left
            b "Truly, there is no need to be so formal."
            o "I'm so, so sorry to inconvenience you, but might you know the way back."
            b "Would you happen to be part of the Bread Town?"
            t "Bread Town?"
            b "Yes, there is a town south of here, known for their freshest bread."
            show octa Happy at right
            o "Yes, yes! We are part of that town. We don't know how to get back."
            show tetra Angry at left
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
    show octa Happy at right
    o "Look, Tetra! We can go home now!"
    show tetra Sad at left
    t "Are you even sure?"
    o "It's better than being lost!"
    "To the side, two large birds appear near the window."
    b "Those two birds shall be your rides. Though you're always welcome to come back."
    o "Thank you so much, Queen Birb."
    show tetra Neutral at left
    t "Yes, uh, thank you."

    "The two boys climb onto the backs of the larger birds."
    t "Huh, why don't these ones speak?"
    show octa Neutral at right
    o "You just can't understand them."
    "The birds squawk and within seconds the two boys ascend into the air."
    show octa Happy at right
    o "I've never seen something like this in my life!"
    menu:
        "Roll Die":
            $ rollDie = renpy.random.randint(1, 6)
        "Roll Die with Vigor":
            $ rollDie = renpy.random.randint(1, 6)
        "ROLL DIE WITH OH GOD WE'RE GONNA PLUMMET TO OUR DEATHS":
            $ rollDie = renpy.random.randint(1, 6)
    if(rollDie == 1):
        show roll1 at truecenter
    elif(rollDie == 2):
        show roll2 at truecenter
    elif(rollDie == 3):
        show roll3 at truecenter
    elif(rollDie == 4):
        show roll4 at truecenter 
    elif(rollDie == 5):
        show roll5 at truecenter
    else:
        show roll6 at truecenter
    play sound diceRoll
    if(rollDie >= 5):
        show tetra Happy at left
        t "Me too! I might want to come back to this place."
        "The entire ride goes without a hitch. The sky is so blue and vast."
        "It's a sight that neither child wants to forget this wild day."
    elif(rollDie >=3):
        show tetra Neutral at left
        t "This whole thing is kind of nervewrecking."
        "Tetra grips at the feathers, causing the bird to screech."
        "This whole ride is turbulent, but the view makes up for it. Somewhat."
    else:
        show tetra Sad at left
        t "Help!"
        "Tetra slips from the back of the bird."
        hide tetra Sad
        show octa Neutral at right
        o "Tetra!"
        show octa Sad at right
        o "Hey, birdie, please?"
        menu:
            "Roll Die":
                $ rollDie = renpy.random.randint(1, 6)
            "Roll Die with Grace":
                $ rollDie = renpy.random.randint(1, 6)
            "ROLL DIE WITH THE POWER OF THE UNYIELDING BIRB KNIGHT":
                $ rollDie = renpy.random.randint(1, 6)
        if(rollDie == 1):
            show roll1 at truecenter
        elif(rollDie == 2):
            show roll2 at truecenter
        elif(rollDie == 3):
            show roll3 at truecenter
        elif(rollDie == 4):
            show roll4 at truecenter 
        elif(rollDie == 5):
            show roll5 at truecenter
        else:
            show roll6 at truecenter
        play sound diceRoll
        if(rollDie >= 4):
            "Two claws latch onto Tetra's shoulders, pulling him out of free fall."
            show octa Happy at right
            o "I've got you!"
            "Tetra squirms in the grip, but stills himself."
            show tetra Sad at left
            t "This is a horrible experience."
            o "Would you rather still be falling?"
            show tetra Angry at left
            t "No."
        else:
            "The claws were unable to catch Tetra and he plummets to the ground."
            o "Oh no!"
            show tetra Sad at left
            t "Please! Save meeeee-!"
            scene bush with Fade(2.0, 0.0, 2.0)
            show tetra Sad at left
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
                    if(rollDie == 1):
                        show roll1 at truecenter
                    elif(rollDie == 2):
                        show roll2 at truecenter
                    elif(rollDie == 3):
                        show roll3 at truecenter
                    elif(rollDie == 4):
                        show roll4 at truecenter 
                    elif(rollDie == 5):
                        show roll5 at truecenter
                    else:
                        show roll6 at truecenter
                    play sound diceRoll
                    if(rollDie > 2):
                        w "Child, you have appear out of the sky all of a sudden."
                        t "You talk."
                        show tetra Happy at left
                        w "That I do. Now come, let us find you new furs."
                        "Tetra slowly became more acquainted to the wolf. Then they were family."
                        "Nowadays, he spends his time in forest hunting and foraging with the wolf."
                        return
                    else:
                        show tetra Neutral at left
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
                    if(rollDie == 1):
                        show roll1 at truecenter
                    elif(rollDie == 2):
                        show roll2 at truecenter
                    elif(rollDie == 3):
                        show roll3 at truecenter
                    elif(rollDie == 4):
                        show roll4 at truecenter 
                    elif(rollDie == 5):
                        show roll5 at truecenter
                    else:
                        show roll6 at truecenter
                    play sound diceRoll
                    if(rollDie > 2):
                        show tetra Neutral at left
                        "Tetra picks up the stick and readies it to attack."
                        "He waves it at the wolf before it starts running away."
                        show tetra Happy at left
                        "This is his territory now, and he'll defend it with his life."
                        return
                    else:
                        show tetra Sad at left
                        "Instead of defending himself with the stick he found, the stick slips out of his hand and into the woods."
                        "He braces himself for impact, but the stick is right in front of him with the wolf."
                        show tetra Happy at left
                        "He throws it again. The wolf chases after it. It turns into a game of fetch."
                        "He's found a friend right here after all."
                        return

    "The birds land without a problem onto the familiar streets the boys know."
    "They wave a thanks and farewell to the birds."
    scene bush with Fade(2.0, 0.0, 2.0)
    show octa Happy at right
    o "Now what do you think about that for an adventure?"
    show tetra Neutral at left
    t "Not what I signed up for. At all."
    o "Come on, now-"
    m "You."
    "Octa scurries to hide behind Tetra."
    hide octa Happy
    show tetra Angry at left
    t "You."
    m "You're friends with the birds now, I take it?"
    o "We are! So you should fear us!"

    "The man lets out a hearty laugh."
    m "I'm actually friends with them too!"
    show tetra Neutral at left
    show octa Neutral at right
    o "Wait.... I thought you made bread monsters!"
    t "Now where did you hear that from?"
    m "But I lost my lucky hat, and my bread hasn't been good since."
    t "It's been a da-"
    o "Don't mind my friend here."
    "Octa procures a white hat out of thin air?"
    "Thought he lost it for a while."
    show octa Happy at right
    o "Would this be yours?"

    "The man takes the hat from Octa's hands."
    m "This is it! Thank you so much!"
    show tetra Angry at left
    "Tetra side-eyes Octa."
    show tetra Happy at left
    o "It's no problem at all."
    t "Octa, there's no way that he's forgotten."
    o "Count your blessings, Tetra. Count them lots."

    m "Now, I have to feed the birds."
    show octa Neutral at right
    o "Can we join?"
    show tetra Angry at left
    t "Octa!"
    show octa Sad at right
    o "What? Nothing wrong with just asking."
    m "You'd like to join me?"
    "The man pulls out extra bread from his basket."
    m "Let us go then!"
    show octa Happy at right
    show tetra Happy at left
    m "I'm not the well-known baker of this place for nothing!"

    "The boys rush after the baker and his bread."
    scene goodend with Fade(2.0, 0.0, 2.0)
    "When they stop on a grassy field, multiple birds land nearby."
    "Though wary at first, the three pass out the bread to all of them."
    "Octa takes turns talking to each of the birds, introducing everyone to each one."
    show tetra Happy at left
    t "So about what we're betting?"
    show octa Neutral at right
    o "Betting? I didn't say anything about that."
    t "Your five pence, or whatever it is."
    show octa Happy at right
    o "Well.... Let's roll then! You have a die for a reason."
    o "If you get the number I'm thinking, you win!"
    "Tetra shakes the die and rolls."
    menu:
        "Roll Die":
            $ rollDie = renpy.random.randint(1, 6)
        "Roll Die with a renewed sense of Vigor and Spirit":
            $ rollDie = renpy.random.randint(1, 6)
        "ROLL DIE WITH YEAH":
            $ rollDie = renpy.random.randint(1, 6)
    play sound diceRoll
    "It lands."
    show octa Sad at right
    o "Dang it!"

    return

label rightRoute:
    # This ends the game.
    show octa Angry at right
    o "TETRA WHERE ARE YOU GOING THIS IS THE LEFT NOT RIGHT."
    show tetra Happy at left
    t "W h a t."
    jump leftRoute
