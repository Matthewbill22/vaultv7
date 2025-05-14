# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("...")
define y = Character("You")

define m = Character("Mushroom Guy")
define t = Character("TV Guy")
define r = Character("Rainy Girl")

# The game starts here.

label start:

    
    scene black
    

    e "You wake from a deep sleep to find yourself in a strange world."
    scene bg forest with Dissolve(2.0)
    e "The colors seem off, distorted, unreal. You don't recognize the world around you."

    "You look up to see a strange figure before you."

    show mushroom_1 with moveinright:
        xalign 1.0
        yalign 0.5
        


    m "Oh! A visitor! Good, I was getting spored out of my mind!"

    m "I hope you're having a pleasent trip. We could use more visitors like you. To stay here, you'll need to pass a little test. Don't worry, it won't be too punishing!"

    m "What role do mushrooms typically play in an ecosystem?"


    menu:
        
        "Decomposers":
            jump choice1_correct

        "Producers":
            jump choice_incorrect

        "Predators":
            jump choice_incorrect

    label choice1_correct:
        $ menu_flag = True
        m "You know quite a bit about fun guys like me it seems. I'd simply break down if you didn't get that one..."
        jump choice1_done

    label choice_incorrect:
        $ menu_flag = False
        scene wake up bad
        show eileen
        "You open your eyes to see your own bedroom. The dream, which moments ago seemed so viscerally real quickly fades from your memory."
        return

    label choice1_done:
    

    m "Here's where shiitake gets real: what part of a mushroom is responsible for releasing spores?"


    menu:
        "Cap":
            jump choice_incorrect
        "Gills":
            jump choice2_correct
        "Stem":
            jump choice_incorrect

    label choice2_correct:
        $ menu_flag = True
        m "Yes, yes! It seems a bit fishy, but it's true!"
        jump choice2_done

    label choice2_done:

    m "Don't trip up now! This is the most crucial question of them all: what type of mushroom am I?"

    menu:
        "Fly agaric":
            jump choice3_correct
        "Panther cap":
            jump choice_incorrect
        "Blusher":
            jump choice_incorrect

    label choice3_correct:
        $ menu_flag = True
        m "Oh, marvelous! Certainly a morel victory! Time to cap off this visit."

        hide mushroom_1 

        show mushroomspores:
            xalign 0.5
            yalign 0.5
            zoom 2.0


        e "He holds up his hand and blows toward you emitting a dense cloud of spores."
        scene black with Dissolve(1.5)
        e "For a moment, you can't see anything."
        
        jump choice3_done

    label choice3_done:

    
    e "As the cloud disperses, blinking lights emerge all around you. It looks like flashbulbs at a sporting event, but as the room resolves itself around you... "
    scene bg arcade with Dissolve(1.5)
    
    e "...you see that you are in the middle of an old arcade."

    e "In front of you stands another strange figure..."

    show TVmanconfused with moveinright:
        xalign 1.0




    t "WELCOME! To the GREATEST SHOW YOU EVER IMAGINED!"

    label Cloud:
    scene Cloudgirl hallway

    show Cloud girl

    c "You would enter one of the brightest rooms where smell of blooming flowers and shining sun would meet you. You would feel some sort of comfort
until you stumble upon crying Cloud Girl."


    #label choice31:
    menu:
        "Oh not another weirdo again...":
            $ menu_flag = False
            jump reply31_incorrect

        "Are you alright?":
            $ menu_flag = True
            jump reply31_correct

    label reply31_incorrect:
    
        "She would cry even louder."


        y "Okay okay... Sorry! Just don't cry!"
        jump choice1_incorrect

    label reply31_correct:


        c "Yeah... I am just feeling under the weather."

        y "Awh... You poor thing!"
        jump choice31_done
    
    label choice31_done:
  
        "Cloud Girl would keep crying."


    #label choice32:
    menu:
        "Hey! It's gonna be alright!":
            jump choice32_done
        
        "Come on! Crying doesn't fit you!":
            jump choice32_done

    
    label choice32_done:

        "Cloud Girl would keep crying."
    
    #label choice33:
    menu:#incorrect or correct?
        "This place wasn't so colorful before!":
            jump reply33_1 

        "Hey, you made flowers bloom again!":
            jump reply33_2 

    label reply33_1:
        c "Really...?"

        y "When I was passing through here, flowers were wilt!"
        jump choice33_done
       

    label reply33_2:
        c "Did I...?"

        y "Yeah! Seems like your tears brought them back to life!"
        jump choice33_done
   
        
    label choice33_done:

        c "Heh... Thanks..."

        "Cloud Girl would stop crying and turn into a cloud."
    
    #label choice34:
    menu:
        "How do you feel?":
            jump choice34_done

        "You alright?":
            jump choice34_done
    
    label choice34_done:

        c "I am alright! My mind is just clouded right now."
    
    #label choice35:
    menu:
        "Hey! I know how to cheer you up!":
            jump reply35_1
    
        "Hey! How about I tell you a joke":
            jump reply35_2
        
    label reply35_1:
        "How...?"
        jump choice36

    label reply35_2:
        "A joke...?"
        jump choice36
    
    label choice36:
    
    menu:
        "Why is the sun so popular at parties?":
            jump reply36_1
            
        "How does moon cut its hair?":
            jump reply36_2

        "What do clouds wear?":
            jump reply36_3
    

    label reply36_1:
        c "..."

        y "Because he is the sunniest!"
        jump choice36_done

    label reply36_2:
        c "..."

        y "Eclipse it."
        jump choice36_done
    
    label reply36_3:
        c "..."

        y "Thunderwear!"
        jump choice36_done
    
    label choice36_done:
        c "Heh..."

        c "Hahahaha!"

        "Cloud Girl would show fer Sun!"

        c "You are hiliarious!"

        c "Thank you very much for brightening my mood!"

    


    #label choice31_correct:
        $ menu_flag = True
        r "You know quite a bit about fun guys like me it seems."
        jump Ending

    label Ending:
    scene Ending

    show finish

    "(Ending messages here)"

    scene wake up good


    "You open your eyes to see your own bedroom. Your "






    # This ends the game.


    return



