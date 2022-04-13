label mr_mix_start_game:
    show screen level_info
    play music level loop
    mr "Cucumber"
    
    pause 0.1
    show fx_mr_mix at fx_pos
    pause 0.1
    hide fx_mr_mix rage2
    menu:
        mr "The reddest is the most delicious"
        
        "Tomato":
            pause 3
            mr "Yes!"
            
        "Apple":
            pause 3
            scene gm_mr_mix_no
            mr "```````$o$`````````````o88888888888So````````````````````$`o8```````````````"
            
            pause 3
            $ renpy.music.stop(channel='music', fadeout = 2.0)
            play sound krik
            pause 0.1
            show fx_mr_mix2 at fx_pos
            pause 0.1
            hide fx_mr_mix2 rage2
            
            scene gm_mr_mix_nous
            mr "$o$_o88888888888So_$`o8"
            pause 3
            
            return
    mr "I'll cook you like a shawarma"
    menu:
        mr "Green and included in the salad"
        
        "avocado!":
            pause 3
            scene gm_mr_mix_no
            mr "```````$o$`````````````o88888888888So````````````````````$`o8```````````````"
            
            pause 3
            $ renpy.music.stop(channel='music', fadeout = 2.0)
            play sound krik
            pause 0.1
            show fx_mr_mix2 at fx_pos
            pause 0.1
            hide fx_mr_mix2 rage2
            
            scene gm_mr_mix_nous
            mr "$o$_o88888888888So_$`o8"
            pause 3
            
            return
        "Cucumber":
            pause 3
            mr "Yes!"
        "Apple":
            pause 3
            scene gm_mr_mix_no
            mr "```````$o$`````````````o88888888888So````````````````````$`o8```````````````"
            
            pause 3
            $ renpy.music.stop(channel='music', fadeout = 2.0)
            play sound krik
            pause 0.1
            show fx_mr_mix3 at fx_pos
            pause 0.1
            hide fx_mr_mix3 rage2
            
            scene gm_mr_mix_nous
            mr "$o$_o88888888888So_$`o8"
            pause 3
            
            return
    mr "Well done"
    
    $ renpy.music.stop(channel='music', fadeout = 2.0)
    hide screen level_info with dissolve
    show screen level_info2 with dissolve
    mr "Level 2"
    mr "baby"
    mr "How do you do that!?"
    menu:
        mr "is yellow good for eyesight?"
        
        "baby":
            pause 3
            scene gm_mr_mix_no
            mr "```````$o$`````````````o88888888888So````````````````````$`o8```````````````"
            
            pause 3
            $ renpy.music.stop(channel='music', fadeout = 2.0)
            play sound krik
            pause 0.1
            show fx_mr_mix2 at fx_pos
            pause 0.1
            hide fx_mr_mix2 rage2
            
            scene gm_mr_mix_nous
            mr "$o$_o88888888888So_$`o8"
            pause 3
            
            return
        "Carrot":
            pause 3
            mr "Yes!"
        "Dry apple":
            pause 3
            scene gm_mr_mix_no
            mr "```````$o$`````````````o88888888888So````````````````````$`o8```````````````"
            
            pause 3
            $ renpy.music.stop(channel='music', fadeout = 2.0)
            play sound krik
            pause 0.1
            show fx_mr_mix2 at fx_pos
            pause 0.1
            hide fx_mr_mix2 rage2
            
            scene gm_mr_mix_nous
            mr "$o$_o88888888888So_$`o8"
            pause 3
            
            return
    mr "Brilliant"
    
    play music level loop
    scene gm_mr_mix_level6
    mr "And now the main number"
    mr "Now we're playing fair"
    menu:
        mr "What is the name of growth when a child is born?"
        
        "baby":
            pause 3
            mr "Yes!"
            pause 0.1
            show fx_mr_mix2 at fx_pos
            pause 0.1
            hide fx_mr_mix2 rage2
        
        "baby":
            pause 3
            mr "Yes!"
            pause 0.1
            show fx_mr_mix2 at fx_pos
            pause 0.1
            hide fx_mr_mix2 rage2
        
        "baby":
            pause 3
            mr "Yes!"
            pause 0.1
            show fx_mr_mix2 at fx_pos
            pause 0.1
            hide fx_mr_mix2 rage2
        
        "baby":
            pause 3
            mr "Yes!"
            pause 0.1
            show fx_mr_mix2 at fx_pos
            pause 0.1
            hide fx_mr_mix2 rage2
    mr "$o$_o88888888888So_$`o8"
    
    pause 1
    show gm_mr_mix_nous at center
    pause 3
    hide gm_mr_mix_nous rage2
    
    pause 1
    mr "baby"
    pause 0.1
    show fx_mr_mix at fx_pos
    pause 0.1
    hide fx_mr_mix rage2
    pause 0.1
    show fx_mr_mix_2 at fx_pos
    pause 0.1
    hide fx_mr_mix_2 rage2
    
    pause 1
    show gm_mr_mix_nous at center
    pause 3
    hide gm_mr_mix_nous rage2
    pause 1
    mr "baby"
    pause 1
    
    pause 0.1
    show fx_mr_mix at fx_pos
    pause 0.1
    hide fx_mr_mix rage2
    pause 0.1
    show fx_mr_mix_2 at fx_pos
    pause 0.1
    hide fx_mr_mix_2 rage2
    
    pause 1
    show gm_mr_mix_nous at center
    pause 3
    hide gm_mr_mix_nous rage2
    pause 1
    mr "baby"
    
    pause 0.1
    show fx_mr_mix at fx_pos
    pause 0.1
    hide fx_mr_mix rage2
    pause 0.1
    show fx_mr_mix_2 at fx_pos
    pause 0.1
    hide fx_mr_mix_2 rage2
    
    pause 1
    show gm_mr_mix_nous at center
    pause 3
    hide gm_mr_mix_nous rage2
    pause 1
    mr "baby"
    
    pause 0.1
    show fx_mr_mix at fx_pos
    pause 0.1
    hide fx_mr_mix rage2
    pause 0.1
    show fx_mr_mix_2 at fx_pos
    pause 0.1
    hide fx_mr_mix_2 rage2
    
    pause 1
    show gm_mr_mix_nous at center
    pause 3
    hide gm_mr_mix_nous rage2
    pause 1
    mr "baby"
    
    pause 6
    scene gm_mr_mix_l
    play music sound loop
    pause 99999999999999
    
    $ renpy.music.stop(channel='music', fadeout = 2.0)
    scene diviner_fon
    show diviner_exe at center
    di "Wow, you're winning!"
    di "Let's play some more!"
    hide diviner_exe
    scene diviner_fon1
    di "Let's play"
    scene gm_mr_mix
    $working = False
    menu:
         mr "Continue?"
         
         "Let's go":
            mr "We start cooking for our kids"
            
         "No":
            return
    mr "Chamomile"
    
    hide screen level_info2 with dissolve
    show screen level_info7 with dissolve
    mr "level7"
    
    scene gm_mr_mix_level6
    play music level loop
    pause 0.1
    show fx_mr_mix at fx_pos
    pause 0.1
    hide fx_mr_mix rage2
    pause 0.1
    show fx_mr_mix_2 at fx_pos
    pause 0.1
    hide fx_mr_mix_2 rage2
    
    pause 1
    show gm_mr_mix_nous at center
    pause 3
    hide gm_mr_mix_nous rage2
    pause 1
    pause 0.1
    show fx_mr_mix at fx_pos
    pause 0.1
    hide fx_mr_mix rage2
    pause 0.1
    show fx_mr_mix_2 at fx_pos
    pause 0.1
    hide fx_mr_mix_2 rage2
    
    pause 1
    show gm_mr_mix_nous at center
    pause 3
    hide gm_mr_mix_nous rage2
    pause 1
    pause 0.1
    show fx_mr_mix at fx_pos
    pause 0.1
    hide fx_mr_mix rage2
    pause 0.1
    show fx_mr_mix_2 at fx_pos
    pause 0.1
    hide fx_mr_mix_2 rage2
    
    pause 1
    show gm_mr_mix_nous at center
    pause 3
    hide gm_mr_mix_nous rage2
    pause 1
    menu:
        mr "What is the name of growth when a child is born?"
        
        "baby":
            pause 3
            mr "Yes!"
            pause 0.1
            show fx_mr_mix2 at fx_pos
            pause 0.1
            hide fx_mr_mix2 rage2
        
        "baby":
            pause 3
            mr "Yes!"
            pause 0.1
            show fx_mr_mix2 at fx_pos
            pause 0.1
            hide fx_mr_mix2 rage2
        
        "baby":
            pause 3
            mr "Yes!"
            pause 0.1
            show fx_mr_mix2 at fx_pos
            pause 0.1
            hide fx_mr_mix2 rage2
        
        "baby":
            pause 3
            mr "Yes!"
            pause 0.1
            show fx_mr_mix2 at fx_pos
            pause 0.1
            hide fx_mr_mix2 rage2
    mr "$o$_o88888888888So_$`o8"
    menu:
        mr "What is the name of growth when a child is born?"
        
        "baby":
            pause 3
            mr "Yes!"
            pause 0.1
            show fx_mr_mix2 at fx_pos
            pause 0.1
            hide fx_mr_mix2 rage2
        
        "baby":
            pause 3
            mr "Yes!"
            pause 0.1
            show fx_mr_mix2 at fx_pos
            pause 0.1
            hide fx_mr_mix2 rage2
        
        "baby":
            pause 3
            mr "Yes!"
            pause 0.1
            show fx_mr_mix2 at fx_pos
            pause 0.1
            hide fx_mr_mix2 rage2
        
        "baby":
            pause 3
            mr "Yes!"
            pause 0.1
            show fx_mr_mix2 at fx_pos
            pause 0.1
            hide fx_mr_mix2 rage2
    mr "$o$_o88888888888So_$`o8"
    menu:
        mr "What is the name of growth when a child is born?"
        
        "baby":
            pause 3
            mr "Yes!"
            pause 0.1
            show fx_mr_mix2 at fx_pos
            pause 0.1
            hide fx_mr_mix2 rage2
        
        "baby":
            pause 3
            mr "Yes!"
            pause 0.1
            show fx_mr_mix2 at fx_pos
            pause 0.1
            hide fx_mr_mix2 rage2
        
        "baby":
            pause 3
            mr "Yes!"
            pause 0.1
            show fx_mr_mix2 at fx_pos
            pause 0.1
            hide fx_mr_mix2 rage2
        
        "baby":
            pause 3
            mr "Yes!"
            pause 0.1
            show fx_mr_mix2 at fx_pos
            pause 0.1
            hide fx_mr_mix2 rage2
    mr "$o$_o88888888888So_$`o8"
    menu:
        mr "The reddest is the most delicious"
        
        "Tomato":
            pause 3
            mr "Yes!"
            
        "Apple":
            pause 3
            scene gm_mr_mix_level6_2
            mr "```````$o$`````````````o88888888888So````````````````````$`o8```````````````"
            
            pause 3
            $ renpy.music.stop(channel='music', fadeout = 2.0)
            play sound krik
            pause 0.1
            show fx_mr_mix2 at fx_pos
            pause 0.1
            hide fx_mr_mix2 rage2
            
            scene gm_mr_mix_nous
            mr "$o$_o88888888888So_$`o8"
            pause 3
            
            return
    scene gm_mr_mix_level6_2
    mr "Well$o$`````````````o88888888888So``You````````````````````$`o8```````````````"
    
    hide screen level_info7 with dissolve
    show screen level_info8 with dissolve
    mr "level8"
    $ renpy.music.stop(channel='music', fadeout = 2.0)
    hide screen level_info8 with dissolve
    play music sound loop
    pause 0.1
    show fx_mr_mix at fx_pos
    pause 0.1
    hide fx_mr_mix rage2
    pause 0.1
    show fx_mr_mix_2 at fx_pos
    pause 0.1
    hide fx_mr_mix_2 rage2
    pause 0.1
    show fx_mr_mix_3 at fx_pos
    pause 0.1
    hide fx_mr_mix_3 rage2
    pause 0.1
    show gm_mr_mix_nous at center
    pause 0.1
    hide gm_mr_mix_nous rage2
    pause 0.1
    show fx_mr_mix at fx_pos
    pause 0.1
    hide fx_mr_mix rage2
    pause 0.1
    show fx_mr_mix_2 at fx_pos
    pause 0.1
    hide fx_mr_mix_2 rage2
    pause 0.1
    show fx_mr_mix_3 at fx_pos
    pause 0.1
    hide fx_mr_mix_3 rage2
    pause 0.1
    show gm_mr_mix_nous at center
    pause 0.1
    hide gm_mr_mix_nous rage2
    pause 0.1
    show fx_mr_mix at fx_pos
    pause 0.1
    hide fx_mr_mix rage2
    pause 0.1
    show fx_mr_mix_2 at fx_pos
    pause 0.1
    hide fx_mr_mix_2 rage2
    pause 0.1
    show fx_mr_mix_3 at fx_pos
    pause 0.1
    hide fx_mr_mix_3 rage2
    pause 0.1
    show gm_mr_mix_nous at center
    pause 0.1
    hide gm_mr_mix_nous rage2
    pause 0.1
    show fx_mr_mix at fx_pos
    pause 0.1
    hide fx_mr_mix rage2
    pause 0.1
    show fx_mr_mix_2 at fx_pos
    pause 0.1
    hide fx_mr_mix_2 rage2
    pause 0.1
    show fx_mr_mix_3 at fx_pos
    pause 0.1
    hide fx_mr_mix_3 rage2
    pause 0.1
    show gm_mr_mix_nous at center
    pause 0.1
    hide gm_mr_mix_nous rage2
    pause 0.1
    show fx_mr_mix at fx_pos
    pause 0.1
    hide fx_mr_mix rage2
    pause 0.1
    show fx_mr_mix_2 at fx_pos
    pause 0.1
    hide fx_mr_mix_2 rage2
    pause 0.1
    show fx_mr_mix_3 at fx_pos
    pause 0.1
    hide fx_mr_mix_3 rage2
    pause 0.1
    show gm_mr_mix_nous at center
    pause 0.1
    hide gm_mr_mix_nous rage2
    pause 0.1
    show fx_mr_mix at fx_pos
    pause 0.1
    hide fx_mr_mix rage2
    pause 0.1
    show fx_mr_mix_2 at fx_pos
    pause 0.1
    hide fx_mr_mix_2 rage2
    pause 0.1
    show fx_mr_mix_3 at fx_pos
    pause 0.1
    hide fx_mr_mix_3 rage2
    pause 0.1
    show gm_mr_mix_nous at center
    pause 0.1
    hide gm_mr_mix_nous rage2
    pause 0.1
    show fx_mr_mix at fx_pos
    pause 0.1
    hide fx_mr_mix rage2
    pause 0.1
    show fx_mr_mix_2 at fx_pos
    pause 0.1
    hide fx_mr_mix_2 rage2
    pause 0.1
    show fx_mr_mix_3 at fx_pos
    pause 0.1
    hide fx_mr_mix_3 rage2
    pause 0.1
    show gm_mr_mix_nous at center
    pause 0.1
    hide gm_mr_mix_nous rage2
    pause 0.1
    show fx_mr_mix at fx_pos
    pause 0.1
    hide fx_mr_mix rage2
    pause 0.1
    show fx_mr_mix_2 at fx_pos
    pause 0.1
    hide fx_mr_mix_2 rage2
    pause 0.1
    show fx_mr_mix_3 at fx_pos
    pause 0.1
    hide fx_mr_mix_3 rage2
    pause 0.1
    show gm_mr_mix_nous at center
    pause 0.1
    hide gm_mr_mix_nous rage2
    pause 0.1
    show fx_mr_mix at fx_pos
    pause 0.1
    hide fx_mr_mix rage2
    pause 0.1
    show fx_mr_mix_2 at fx_pos
    pause 0.1
    hide fx_mr_mix_2 rage2
    pause 0.1
    show fx_mr_mix_3 at fx_pos
    pause 0.1
    hide fx_mr_mix_3 rage2
    pause 0.1
    show gm_mr_mix_nous at center
    pause 0.1
    hide gm_mr_mix_nous rage2
    pause 0.1
    show fx_mr_mix at fx_pos
    pause 0.1
    hide fx_mr_mix rage2
    pause 0.1
    show fx_mr_mix_2 at fx_pos
    pause 0.1
    hide fx_mr_mix_2 rage2
    pause 0.1
    show fx_mr_mix_3 at fx_pos
    pause 0.1
    hide fx_mr_mix_3 rage2
    pause 0.1
    show gm_mr_mix_nous at center
    pause 0.1
    hide gm_mr_mix_nous rage2
    pause 0.1
    show fx_mr_mix at fx_pos
    pause 0.1
    hide fx_mr_mix rage2
    pause 0.1
    show fx_mr_mix_2 at fx_pos
    pause 0.1
    hide fx_mr_mix_2 rage2
    pause 0.1
    show fx_mr_mix_3 at fx_pos
    pause 0.1
    hide fx_mr_mix_3 rage2
    pause 0.1
    show gm_mr_mix_nous at center
    pause 0.1
    hide gm_mr_mix_nous rage2
    pause 0.1
    show fx_mr_mix at fx_pos
    pause 0.1
    hide fx_mr_mix rage2
    pause 0.1
    show fx_mr_mix_2 at fx_pos
    pause 0.1
    hide fx_mr_mix_2 rage2
    pause 0.1
    show fx_mr_mix_3 at fx_pos
    pause 0.1
    hide fx_mr_mix_3 rage2
    pause 0.1
    show gm_mr_mix_nous at center
    pause 0.1
    hide gm_mr_mix_nous rage2
    pause 0.1
    show fx_mr_mix at fx_pos
    pause 0.1
    hide fx_mr_mix rage2
    pause 0.1
    show fx_mr_mix_2 at fx_pos
    pause 0.1
    hide fx_mr_mix_2 rage2
    pause 0.1
    show fx_mr_mix_3 at fx_pos
    pause 0.1
    hide fx_mr_mix_3 rage2
    pause 0.1
    show gm_mr_mix_nous at center
    pause 0.1
    hide gm_mr_mix_nous rage2
    pause 0.1
    show fx_mr_mix at fx_pos
    pause 0.1
    hide fx_mr_mix rage2
    pause 0.1
    show fx_mr_mix_2 at fx_pos
    pause 0.1
    hide fx_mr_mix_2 rage2
    pause 0.1
    show fx_mr_mix_3 at fx_pos
    pause 0.1
    hide fx_mr_mix_3 rage2
    pause 0.1
    show gm_mr_mix_nous at center
    pause 0.1
    hide gm_mr_mix_nous rage2
    pause 0.1
    show fx_mr_mix at fx_pos
    pause 0.1
    hide fx_mr_mix rage2
    pause 0.1
    show fx_mr_mix_2 at fx_pos
    pause 0.1
    hide fx_mr_mix_2 rage2
    pause 0.1
    show fx_mr_mix_3 at fx_pos
    pause 0.1
    hide fx_mr_mix_3 rage2
    pause 0.1
    show gm_mr_mix_nous at center
    pause 0.1
    hide gm_mr_mix_nous rage2
    pause 0.1
    show fx_mr_mix at fx_pos
    pause 0.1
    hide fx_mr_mix rage2
    pause 0.1
    show fx_mr_mix_2 at fx_pos
    pause 0.1
    hide fx_mr_mix_2 rage2
    pause 0.1
    show fx_mr_mix_3 at fx_pos
    pause 0.1
    hide fx_mr_mix_3 rage2
    pause 0.1
    show gm_mr_mix_nous at center
    pause 0.1
    hide gm_mr_mix_nous rage2
    pause 0.1
    show fx_mr_mix at fx_pos
    pause 0.1
    hide fx_mr_mix rage2
    pause 0.1
    show fx_mr_mix_2 at fx_pos
    pause 0.1
    hide fx_mr_mix_2 rage2
    pause 0.1
    show fx_mr_mix_3 at fx_pos
    pause 0.1
    hide fx_mr_mix_3 rage2
    pause 0.1
    show gm_mr_mix_nous at center
    pause 0.1
    hide gm_mr_mix_nous rage2
    pause 0.1
    show fx_mr_mix at fx_pos
    pause 0.1
    hide fx_mr_mix rage2
    pause 0.1
    show fx_mr_mix_2 at fx_pos
    pause 0.1
    hide fx_mr_mix_2 rage2
    pause 0.1
    show fx_mr_mix_3 at fx_pos
    pause 0.1
    hide fx_mr_mix_3 rage2
    pause 0.1
    show gm_mr_mix_nous at center
    pause 0.1
    hide gm_mr_mix_nous rage2
    pause 0.1
    show fx_mr_mix at fx_pos
    pause 0.1
    hide fx_mr_mix rage2
    pause 0.1
    show fx_mr_mix_2 at fx_pos
    pause 0.1
    hide fx_mr_mix_2 rage2
    pause 0.1
    show fx_mr_mix_3 at fx_pos
    pause 0.1
    hide fx_mr_mix_3 rage2
    pause 0.1
    show gm_mr_mix_nous at center
    pause 0.1
    hide gm_mr_mix_nous rage2
    pause 0.1
    show fx_mr_mix at fx_pos
    pause 0.1
    hide fx_mr_mix rage2
    pause 0.1
    show fx_mr_mix_2 at fx_pos
    pause 0.1
    hide fx_mr_mix_2 rage2
    pause 0.1
    show fx_mr_mix_3 at fx_pos
    pause 0.1
    hide fx_mr_mix_3 rage2
    pause 0.1
    show gm_mr_mix_nous at center
    pause 0.1
    hide gm_mr_mix_nous rage2
    pause 0.1
    show fx_mr_mix at fx_pos
    pause 0.1
    hide fx_mr_mix rage2
    pause 0.1
    show fx_mr_mix_2 at fx_pos
    pause 0.1
    hide fx_mr_mix_2 rage2
    pause 0.1
    show fx_mr_mix_3 at fx_pos
    pause 0.1
    hide fx_mr_mix_3 rage2
    pause 0.1
    show gm_mr_mix_nous at center
    pause 0.1
    hide gm_mr_mix_nous rage2
    pause 0.1
    show fx_mr_mix at fx_pos
    pause 0.1
    hide fx_mr_mix rage2
    pause 0.1
    show fx_mr_mix_2 at fx_pos
    pause 0.1
    hide fx_mr_mix_2 rage2
    pause 0.1
    show fx_mr_mix_3 at fx_pos
    pause 0.1
    hide fx_mr_mix_3 rage2
    pause 0.1
    show gm_mr_mix_nous at center
    pause 0.1
    hide gm_mr_mix_nous rage2
    pause 0.1
    show fx_mr_mix at fx_pos
    pause 0.1
    hide fx_mr_mix rage2
    pause 0.1
    show fx_mr_mix_2 at fx_pos
    pause 0.1
    hide fx_mr_mix_2 rage2
    pause 0.1
    show fx_mr_mix_3 at fx_pos
    pause 0.1
    hide fx_mr_mix_3 rage2
    pause 0.1
    show gm_mr_mix_nous at center
    pause 0.1
    hide gm_mr_mix_nous rage2
    pause 0.1
    show fx_mr_mix at fx_pos
    pause 0.1
    hide fx_mr_mix rage2
    pause 0.1
    show fx_mr_mix_2 at fx_pos
    pause 0.1
    hide fx_mr_mix_2 rage2
    pause 0.1
    show fx_mr_mix_3 at fx_pos
    pause 0.1
    hide fx_mr_mix_3 rage2
    pause 0.1
    show gm_mr_mix_nous at center
    pause 0.1
    hide gm_mr_mix_nous rage2
    pause 0.1
    show fx_mr_mix at fx_pos
    pause 0.1
    hide fx_mr_mix rage2
    pause 0.1
    show fx_mr_mix_2 at fx_pos
    pause 0.1
    hide fx_mr_mix_2 rage2
    pause 0.1
    show fx_mr_mix_3 at fx_pos
    pause 0.1
    hide fx_mr_mix_3 rage2
    pause 0.1
    show gm_mr_mix_nous at center
    pause 0.1
    hide gm_mr_mix_nous rage2
    pause 0.1
    show fx_mr_mix at fx_pos
    pause 0.1
    hide fx_mr_mix rage2
    pause 0.1
    show fx_mr_mix_2 at fx_pos
    pause 0.1
    hide fx_mr_mix_2 rage2
    pause 0.1
    show fx_mr_mix_3 at fx_pos
    pause 0.1
    hide fx_mr_mix_3 rage2
    pause 0.1
    show gm_mr_mix_nous at center
    pause 0.1
    hide gm_mr_mix_nous rage2
    pause 0.1
    show fx_mr_mix at fx_pos
    pause 0.1
    hide fx_mr_mix rage2
    pause 0.1
    show fx_mr_mix_2 at fx_pos
    pause 0.1
    hide fx_mr_mix_2 rage2
    pause 0.1
    show fx_mr_mix_3 at fx_pos
    pause 0.1
    hide fx_mr_mix_3 rage2
    pause 0.1
    show gm_mr_mix_nous at center
    pause 0.1
    hide gm_mr_mix_nous rage2
    pause 0.1
    show fx_mr_mix at fx_pos
    pause 0.1
    hide fx_mr_mix rage2
    pause 0.1
    show fx_mr_mix_2 at fx_pos
    pause 0.1
    hide fx_mr_mix_2 rage2
    pause 0.1
    show fx_mr_mix_3 at fx_pos
    pause 0.1
    hide fx_mr_mix_3 rage2
    pause 0.1
    show gm_mr_mix_nous at center
    pause 0.1
    hide gm_mr_mix_nous rage2
    pause 0.1
    show fx_mr_mix at fx_pos
    pause 0.1
    hide fx_mr_mix rage2
    pause 0.1
    show fx_mr_mix_2 at fx_pos
    pause 0.1
    hide fx_mr_mix_2 rage2
    pause 0.1
    show fx_mr_mix_3 at fx_pos
    pause 0.1
    hide fx_mr_mix_3 rage2
    pause 0.1
    show gm_mr_mix_nous at center
    pause 0.1
    hide gm_mr_mix_nous rage2
    pause 0.1
    show fx_mr_mix at fx_pos
    pause 0.1
    hide fx_mr_mix rage2
    pause 0.1
    show fx_mr_mix_2 at fx_pos
    pause 0.1
    hide fx_mr_mix_2 rage2
    pause 0.1
    show fx_mr_mix_3 at fx_pos
    pause 0.1
    hide fx_mr_mix_3 rage2
    pause 0.1
    show gm_mr_mix_nous at center
    pause 0.1
    hide gm_mr_mix_nous rage2
    pause 0.1
    show fx_mr_mix at fx_pos
    pause 0.1
    hide fx_mr_mix rage2
    pause 0.1
    show fx_mr_mix_2 at fx_pos
    pause 0.1
    hide fx_mr_mix_2 rage2
    pause 0.1
    show fx_mr_mix_3 at fx_pos
    pause 0.1
    hide fx_mr_mix_3 rage2
    pause 0.1
    show gm_mr_mix_nous at center
    pause 0.1
    hide gm_mr_mix_nous rage2
    pause 0.1
    show fx_mr_mix at fx_pos
    pause 0.1
    hide fx_mr_mix rage2
    pause 0.1
    show fx_mr_mix_2 at fx_pos
    pause 0.1
    hide fx_mr_mix_2 rage2
    pause 0.1
    show fx_mr_mix_3 at fx_pos
    pause 0.1
    hide fx_mr_mix_3 rage2
    pause 0.1
    show gm_mr_mix_nous at center
    pause 0.1
    hide gm_mr_mix_nous rage2
    pause 0.1
    show fx_mr_mix at fx_pos
    pause 0.1
    hide fx_mr_mix rage2
    pause 0.1
    show fx_mr_mix_2 at fx_pos
    pause 0.1
    hide fx_mr_mix_2 rage2
    pause 0.1
    show fx_mr_mix_3 at fx_pos
    pause 0.1
    hide fx_mr_mix_3 rage2
    pause 0.1
    show gm_mr_mix_nous at center
    pause 0.1
    hide gm_mr_mix_nous rage2
    pause 0.1
    show fx_mr_mix at fx_pos
    pause 0.1
    hide fx_mr_mix rage2
    pause 0.1
    show fx_mr_mix_2 at fx_pos
    pause 0.1
    hide fx_mr_mix_2 rage2
    pause 0.1
    show fx_mr_mix_3 at fx_pos
    pause 0.1
    hide fx_mr_mix_3 rage2
    pause 0.1
    show gm_mr_mix_nous at center
    pause 0.1
    hide gm_mr_mix_nous rage2
    pause 0.1
    show fx_mr_mix at fx_pos
    pause 0.1
    hide fx_mr_mix rage2
    pause 0.1
    show fx_mr_mix_2 at fx_pos
    pause 0.1
    hide fx_mr_mix_2 rage2
    pause 0.1
    show fx_mr_mix_3 at fx_pos
    pause 0.1
    hide fx_mr_mix_3 rage2
    pause 0.1
    show gm_mr_mix_nous at center
    pause 0.1
    hide gm_mr_mix_nous rage2
    pause 0.1
    show fx_mr_mix at fx_pos
    pause 0.1
    hide fx_mr_mix rage2
    pause 0.1
    show fx_mr_mix_2 at fx_pos
    pause 0.1
    hide fx_mr_mix_2 rage2
    pause 0.1
    show fx_mr_mix_3 at fx_pos
    pause 0.1
    hide fx_mr_mix_3 rage2
    pause 0.1
    show gm_mr_mix_nous at center
    pause 0.1
    hide gm_mr_mix_nous rage2
    pause 0.1
    show fx_mr_mix at fx_pos
    pause 0.1
    hide fx_mr_mix rage2
    pause 0.1
    show fx_mr_mix_2 at fx_pos
    pause 0.1
    hide fx_mr_mix_2 rage2
    pause 0.1
    show fx_mr_mix_3 at fx_pos
    pause 0.1
    hide fx_mr_mix_3 rage2
    pause 0.1
    show gm_mr_mix_nous at center
    pause 0.1
    hide gm_mr_mix_nous rage2
    pause 0.1
    show fx_mr_mix at fx_pos
    pause 0.1
    hide fx_mr_mix rage2
    pause 0.1
    show fx_mr_mix_2 at fx_pos
    pause 0.1
    hide fx_mr_mix_2 rage2
    pause 0.1
    show fx_mr_mix_3 at fx_pos
    pause 0.1
    hide fx_mr_mix_3 rage2
    pause 0.1
    show gm_mr_mix_nous at center
    pause 0.1
    hide gm_mr_mix_nous rage2
    pause 0.1
    show fx_mr_mix at fx_pos
    pause 0.1
    hide fx_mr_mix rage2
    pause 0.1
    show fx_mr_mix_2 at fx_pos
    pause 0.1
    hide fx_mr_mix_2 rage2
    pause 0.1
    show fx_mr_mix_3 at fx_pos
    pause 0.1
    hide fx_mr_mix_3 rage2
    pause 0.1
    show gm_mr_mix_nous at center
    pause 0.1
    hide gm_mr_mix_nous rage2
    pause 0.1
    show fx_mr_mix at fx_pos
    pause 0.1
    hide fx_mr_mix rage2
    pause 0.1
    show fx_mr_mix_2 at fx_pos
    pause 0.1
    hide fx_mr_mix_2 rage2
    pause 0.1
    show fx_mr_mix_3 at fx_pos
    pause 0.1
    hide fx_mr_mix_3 rage2
    pause 0.1
    show gm_mr_mix_nous at center
    pause 0.1
    hide gm_mr_mix_nous rage2
    pause 0.1
    show fx_mr_mix at fx_pos
    pause 0.1
    hide fx_mr_mix rage2
    pause 0.1
    show fx_mr_mix_2 at fx_pos
    pause 0.1
    hide fx_mr_mix_2 rage2
    pause 0.1
    show fx_mr_mix_3 at fx_pos
    pause 0.1
    hide fx_mr_mix_3 rage2
    pause 0.1
    show gm_mr_mix_nous at center
    pause 0.1
    hide gm_mr_mix_nous rage2
    pause 0.1
    show fx_mr_mix at fx_pos
    pause 0.1
    hide fx_mr_mix rage2
    pause 0.1
    show fx_mr_mix_2 at fx_pos
    pause 0.1
    hide fx_mr_mix_2 rage2
    pause 0.1
    show fx_mr_mix_3 at fx_pos
    pause 0.1
    hide fx_mr_mix_3 rage2
    pause 0.1
    show gm_mr_mix_nous at center
    pause 0.1
    hide gm_mr_mix_nous rage2
    pause 0.1
    show fx_mr_mix at fx_pos
    pause 0.1
    hide fx_mr_mix rage2
    pause 0.1
    show fx_mr_mix_2 at fx_pos
    pause 0.1
    hide fx_mr_mix_2 rage2
    pause 0.1
    show fx_mr_mix_3 at fx_pos
    pause 0.1
    hide fx_mr_mix_3 rage2
    pause 0.1
    show gm_mr_mix_nous at center
    pause 0.1
    hide gm_mr_mix_nous rage2
    pause 0.1
    show fx_mr_mix at fx_pos
    pause 0.1
    hide fx_mr_mix rage2
    pause 0.1
    show fx_mr_mix_2 at fx_pos
    pause 0.1
    hide fx_mr_mix_2 rage2
    pause 0.1
    show fx_mr_mix_3 at fx_pos
    pause 0.1
    hide fx_mr_mix_3 rage2
    pause 0.1
    show gm_mr_mix_nous at center
    pause 0.1
    hide gm_mr_mix_nous rage2
    pause 0.1
    show fx_mr_mix at fx_pos
    pause 0.1
    hide fx_mr_mix rage2
    pause 0.1
    show fx_mr_mix_2 at fx_pos
    pause 0.1
    hide fx_mr_mix_2 rage2
    pause 0.1
    show fx_mr_mix_3 at fx_pos
    pause 0.1
    hide fx_mr_mix_3 rage2
    pause 0.1
    show gm_mr_mix_nous at center
    pause 0.1
    hide gm_mr_mix_nous rage2
    pause 0.1
    show fx_mr_mix at fx_pos
    pause 0.1
    hide fx_mr_mix rage2
    pause 0.1
    show fx_mr_mix_2 at fx_pos
    pause 0.1
    hide fx_mr_mix_2 rage2
    pause 0.1
    show fx_mr_mix_3 at fx_pos
    pause 0.1
    hide fx_mr_mix_3 rage2
    pause 0.1
    show gm_mr_mix_nous at center
    pause 0.1
    hide gm_mr_mix_nous rage2
    pause 0.1
    show fx_mr_mix at fx_pos
    pause 0.1
    hide fx_mr_mix rage2
    pause 0.1
    show fx_mr_mix_2 at fx_pos
    pause 0.1
    hide fx_mr_mix_2 rage2
    pause 0.1
    show fx_mr_mix_3 at fx_pos
    pause 0.1
    hide fx_mr_mix_3 rage2
    pause 0.1
    show gm_mr_mix_nous at center
    pause 0.1
    hide gm_mr_mix_nous rage2
    pause 0.1
    show fx_mr_mix at fx_pos
    pause 0.1
    hide fx_mr_mix rage2
    pause 0.1
    show fx_mr_mix_2 at fx_pos
    pause 0.1
    hide fx_mr_mix_2 rage2
    pause 0.1
    show fx_mr_mix_3 at fx_pos
    pause 0.1
    hide fx_mr_mix_3 rage2
    pause 0.1
    show gm_mr_mix_nous at center
    pause 0.1
    hide gm_mr_mix_nous rage2
    pause 0.1
    show fx_mr_mix at fx_pos
    pause 0.1
    hide fx_mr_mix rage2
    pause 0.1
    show fx_mr_mix_2 at fx_pos
    pause 0.1
    hide fx_mr_mix_2 rage2
    pause 0.1
    show fx_mr_mix_3 at fx_pos
    pause 0.1
    hide fx_mr_mix_3 rage2
    pause 0.1
    show gm_mr_mix_nous at center
    pause 0.1
    hide gm_mr_mix_nous rage2
    pause 0.1
    show fx_mr_mix at fx_pos
    pause 0.1
    hide fx_mr_mix rage2
    pause 0.1
    show fx_mr_mix_2 at fx_pos
    pause 0.1
    hide fx_mr_mix_2 rage2
    pause 0.1
    show fx_mr_mix_3 at fx_pos
    pause 0.1
    hide fx_mr_mix_3 rage2
    pause 0.1
    show gm_mr_mix_nous at center
    pause 0.1
    hide gm_mr_mix_nous rage2
    pause 0.1
    show fx_mr_mix at fx_pos
    pause 0.1
    hide fx_mr_mix rage2
    pause 0.1
    show fx_mr_mix_2 at fx_pos
    pause 0.1
    hide fx_mr_mix_2 rage2
    pause 0.1
    show fx_mr_mix_3 at fx_pos
    pause 0.1
    hide fx_mr_mix_3 rage2
    pause 0.1
    show gm_mr_mix_nous at center
    pause 0.1
    hide gm_mr_mix_nous rage2
    pause 0.1
    show fx_mr_mix at fx_pos
    pause 0.1
    hide fx_mr_mix rage2
    pause 0.1
    show fx_mr_mix_2 at fx_pos
    pause 0.1
    hide fx_mr_mix_2 rage2
    pause 0.1
    show fx_mr_mix_3 at fx_pos
    pause 0.1
    hide fx_mr_mix_3 rage2
    pause 0.1
    show gm_mr_mix_nous at center
    pause 0.1
    hide gm_mr_mix_nous rage2
    pause 0.1
    show fx_mr_mix at fx_pos
    pause 0.1
    hide fx_mr_mix rage2
    pause 0.1
    show fx_mr_mix_2 at fx_pos
    pause 0.1
    hide fx_mr_mix_2 rage2
    pause 0.1
    show fx_mr_mix_3 at fx_pos
    pause 0.1
    hide fx_mr_mix_3 rage2
    pause 0.1
    show gm_mr_mix_nous at center
    pause 0.1
    hide gm_mr_mix_nous rage2
    pause 0.1
    show fx_mr_mix at fx_pos
    pause 0.1
    hide fx_mr_mix rage2
    pause 0.1
    show fx_mr_mix_2 at fx_pos
    pause 0.1
    hide fx_mr_mix_2 rage2
    pause 0.1
    show fx_mr_mix_3 at fx_pos
    pause 0.1
    hide fx_mr_mix_3 rage2
    pause 0.1
    show gm_mr_mix_nous at center
    pause 0.1
    hide gm_mr_mix_nous rage2
    pause 0.1
    show fx_mr_mix at fx_pos
    pause 0.1
    hide fx_mr_mix rage2
    pause 0.1
    show fx_mr_mix_2 at fx_pos
    pause 0.1
    hide fx_mr_mix_2 rage2
    pause 0.1
    show fx_mr_mix_3 at fx_pos
    pause 0.1
    hide fx_mr_mix_3 rage2
    pause 0.1
    show gm_mr_mix_nous at center
    pause 0.1
    hide gm_mr_mix_nous rage2
    pause 0.1
    show fx_mr_mix at fx_pos
    pause 0.1
    hide fx_mr_mix rage2
    pause 0.1
    show fx_mr_mix_2 at fx_pos
    pause 0.1
    hide fx_mr_mix_2 rage2
    pause 0.1
    show fx_mr_mix_3 at fx_pos
    pause 0.1
    hide fx_mr_mix_3 rage2
    pause 0.1
    show gm_mr_mix_nous at center
    pause 0.1
    hide gm_mr_mix_nous rage2
    pause 0.1
    show fx_mr_mix at fx_pos
    pause 0.1
    hide fx_mr_mix rage2
    pause 0.1
    show fx_mr_mix_2 at fx_pos
    pause 0.1
    hide fx_mr_mix_2 rage2
    pause 0.1
    show fx_mr_mix_3 at fx_pos
    pause 0.1
    hide fx_mr_mix_3 rage2
    pause 0.1
    show gm_mr_mix_nous at center
    pause 0.1
    hide gm_mr_mix_nous rage2
    pause 0.1
    show fx_mr_mix at fx_pos
    pause 0.1
    hide fx_mr_mix rage2
    pause 0.1
    show fx_mr_mix_2 at fx_pos
    pause 0.1
    hide fx_mr_mix_2 rage2
    pause 0.1
    show fx_mr_mix_3 at fx_pos
    pause 0.1
    hide fx_mr_mix_3 rage2
    pause 0.1
    show gm_mr_mix_nous at center
    pause 0.1
    hide gm_mr_mix_nous rage2
    pause 0.1
    show fx_mr_mix at fx_pos
    pause 0.1
    hide fx_mr_mix rage2
    pause 0.1
    show fx_mr_mix_2 at fx_pos
    pause 0.1
    hide fx_mr_mix_2 rage2
    pause 0.1
    show fx_mr_mix_3 at fx_pos
    pause 0.1
    hide fx_mr_mix_3 rage2
    pause 0.1
    show gm_mr_mix_nous at center
    pause 0.1
    hide gm_mr_mix_nous rage2
    pause 0.1
    show fx_mr_mix at fx_pos
    pause 0.1
    hide fx_mr_mix rage2
    pause 0.1
    show fx_mr_mix_2 at fx_pos
    pause 0.1
    hide fx_mr_mix_2 rage2
    pause 0.1
    show fx_mr_mix_3 at fx_pos
    pause 0.1
    hide fx_mr_mix_3 rage2
    pause 0.1
    show gm_mr_mix_nous at center
    pause 0.1
    hide gm_mr_mix_nous rage2
    pause 0.1
    show fx_mr_mix at fx_pos
    pause 0.1
    hide fx_mr_mix rage2
    pause 0.1
    show fx_mr_mix_2 at fx_pos
    pause 0.1
    hide fx_mr_mix_2 rage2
    pause 0.1
    show fx_mr_mix_3 at fx_pos
    pause 0.1
    hide fx_mr_mix_3 rage2
    pause 0.1
    show gm_mr_mix_nous at center
    pause 0.1
    hide gm_mr_mix_nous rage2
    pause 0.1
    show fx_mr_mix at fx_pos
    pause 0.1
    hide fx_mr_mix rage2
    pause 0.1
    show fx_mr_mix_2 at fx_pos
    pause 0.1
    hide fx_mr_mix_2 rage2
    pause 0.1
    show fx_mr_mix_3 at fx_pos
    pause 0.1
    hide fx_mr_mix_3 rage2
    pause 0.1
    show gm_mr_mix_nous at center
    pause 0.1
    hide gm_mr_mix_nous rage2
    pause 0.1
    show fx_mr_mix at fx_pos
    pause 0.1
    hide fx_mr_mix rage2
    pause 0.1
    show fx_mr_mix_2 at fx_pos
    pause 0.1
    hide fx_mr_mix_2 rage2
    pause 0.1
    show fx_mr_mix_3 at fx_pos
    pause 0.1
    hide fx_mr_mix_3 rage2
    pause 0.1
    show gm_mr_mix_nous at center
    pause 0.1
    hide gm_mr_mix_nous rage2
    pause 0.1
    show fx_mr_mix at fx_pos
    pause 0.1
    hide fx_mr_mix rage2
    pause 0.1
    show fx_mr_mix_2 at fx_pos
    pause 0.1
    hide fx_mr_mix_2 rage2
    pause 0.1
    show fx_mr_mix_3 at fx_pos
    pause 0.1
    hide fx_mr_mix_3 rage2
    pause 0.1
    show gm_mr_mix_nous at center
    pause 0.1
    hide gm_mr_mix_nous rage2
    pause 0.1
    show fx_mr_mix at fx_pos
    pause 0.1
    hide fx_mr_mix rage2
    pause 0.1
    show fx_mr_mix_2 at fx_pos
    pause 0.1
    hide fx_mr_mix_2 rage2
    pause 0.1
    show fx_mr_mix_3 at fx_pos
    pause 0.1
    hide fx_mr_mix_3 rage2
    pause 0.1
    show gm_mr_mix_nous at center
    pause 0.1
    hide gm_mr_mix_nous rage2
    pause 0.1
    show fx_mr_mix at fx_pos
    pause 0.1
    hide fx_mr_mix rage2
    pause 0.1
    show fx_mr_mix_2 at fx_pos
    pause 0.1
    hide fx_mr_mix_2 rage2
    pause 0.1
    show fx_mr_mix_3 at fx_pos
    pause 0.1
    hide fx_mr_mix_3 rage2
    pause 0.1
    show gm_mr_mix_nous at center
    pause 0.1
    hide gm_mr_mix_nous rage2
    pause 0.1
    show fx_mr_mix at fx_pos
    pause 0.1
    hide fx_mr_mix rage2
    pause 0.1
    show fx_mr_mix_2 at fx_pos
    pause 0.1
    hide fx_mr_mix_2 rage2
    pause 0.1
    show fx_mr_mix_3 at fx_pos
    pause 0.1
    hide fx_mr_mix_3 rage2
    pause 0.1
    show gm_mr_mix_nous at center
    pause 0.1
    hide gm_mr_mix_nous rage2
    pause 0.1
    show fx_mr_mix at fx_pos
    pause 0.1
    hide fx_mr_mix rage2
    pause 0.1
    show fx_mr_mix_2 at fx_pos
    pause 0.1
    hide fx_mr_mix_2 rage2
    pause 0.1
    show fx_mr_mix_3 at fx_pos
    pause 0.1
    hide fx_mr_mix_3 rage2
    pause 0.1
    show gm_mr_mix_nous at center
    pause 0.1
    hide gm_mr_mix_nous rage2
    pause 0.1
    show fx_mr_mix at fx_pos
    pause 0.1
    hide fx_mr_mix rage2
    pause 0.1
    show fx_mr_mix_2 at fx_pos
    pause 0.1
    hide fx_mr_mix_2 rage2
    pause 0.1
    show fx_mr_mix_3 at fx_pos
    pause 0.1
    hide fx_mr_mix_3 rage2
    pause 0.1
    show gm_mr_mix_nous at center
    pause 0.1
    hide gm_mr_mix_nous rage2
    pause 0.1
    show fx_mr_mix at fx_pos
    pause 0.1
    hide fx_mr_mix rage2
    pause 0.1
    show fx_mr_mix_2 at fx_pos
    pause 0.1
    hide fx_mr_mix_2 rage2
    pause 0.1
    show fx_mr_mix_3 at fx_pos
    pause 0.1
    hide fx_mr_mix_3 rage2
    pause 0.1
    show gm_mr_mix_nous at center
    pause 0.1
    hide gm_mr_mix_nous rage2
    
    scene diviner_fon2
    di "LOL"
    scene gm_mr_mix
    mr "Thank you for helping!"
    
    pause 0.1
    show fx_mr_mix at fx_pos
    pause 0.1
    hide fx_mr_mix rage2
    pause 0.1
    show fx_mr_mix_2 at fx_pos
    pause 0.1
    hide fx_mr_mix_2 rage2
    pause 0.1
    show fx_mr_mix_3 at fx_pos
    pause 0.1
    hide fx_mr_mix_3 rage2
    pause 0.1
    show gm_mr_mix_nous at center
    pause 0.1
    hide gm_mr_mix_nous rage2
    pause 0.1
    show fx_mr_mix at fx_pos
    pause 0.1
    hide fx_mr_mix rage2
    pause 0.1
    show fx_mr_mix_2 at fx_pos
    pause 0.1
    hide fx_mr_mix_2 rage2
    pause 0.1
    show fx_mr_mix_3 at fx_pos
    pause 0.1
    hide fx_mr_mix_3 rage2
    pause 0.1
    show gm_mr_mix_nous at center
    pause 0.1
    hide gm_mr_mix_nous rage2
    pause 0.1
    show fx_mr_mix at fx_pos
    pause 0.1
    hide fx_mr_mix rage2
    pause 0.1
    show fx_mr_mix_2 at fx_pos
    pause 0.1
    hide fx_mr_mix_2 rage2
    pause 0.1
    show fx_mr_mix_3 at fx_pos
    pause 0.1
    hide fx_mr_mix_3 rage2
    pause 0.1
    show gm_mr_mix_nous at center
    pause 0.1
    hide gm_mr_mix_nous rage2
    pause 0.1
    show fx_mr_mix at fx_pos
    pause 0.1
    hide fx_mr_mix rage2
    pause 0.1
    show fx_mr_mix_2 at fx_pos
    pause 0.1
    hide fx_mr_mix_2 rage2
    pause 0.1
    show fx_mr_mix_3 at fx_pos
    pause 0.1
    hide fx_mr_mix_3 rage2
    pause 0.1
    show gm_mr_mix_nous at center
    pause 0.1
    hide gm_mr_mix_nous rage2
    pause 0.1
    show fx_mr_mix at fx_pos
    pause 0.1
    hide fx_mr_mix rage2
    pause 0.1
    show fx_mr_mix_2 at fx_pos
    pause 0.1
    hide fx_mr_mix_2 rage2
    pause 0.1
    show fx_mr_mix_3 at fx_pos
    pause 0.1
    hide fx_mr_mix_3 rage2
    pause 0.1
    show gm_mr_mix_nous at center
    pause 0.1
    hide gm_mr_mix_nous rage2
    pause 0.1
    show fx_mr_mix at fx_pos
    pause 0.1
    hide fx_mr_mix rage2
    pause 0.1
    show fx_mr_mix_2 at fx_pos
    pause 0.1
    hide fx_mr_mix_2 rage2
    pause 0.1
    show fx_mr_mix_3 at fx_pos
    pause 0.1
    hide fx_mr_mix_3 rage2
    pause 0.1
    show gm_mr_mix_nous at center
    pause 0.1
    hide gm_mr_mix_nous rage2
    pause 0.1
    show fx_mr_mix at fx_pos
    pause 0.1
    hide fx_mr_mix rage2
    pause 0.1
    show fx_mr_mix_2 at fx_pos
    pause 0.1
    hide fx_mr_mix_2 rage2
    pause 0.1
    show fx_mr_mix_3 at fx_pos
    pause 0.1
    hide fx_mr_mix_3 rage2
    pause 0.1
    show gm_mr_mix_nous at center
    pause 0.1
    hide gm_mr_mix_nous rage2
    pause 0.1
    show fx_mr_mix at fx_pos
    pause 0.1
    hide fx_mr_mix rage2
    pause 0.1
    show fx_mr_mix_2 at fx_pos
    pause 0.1
    hide fx_mr_mix_2 rage2
    pause 0.1
    show fx_mr_mix_3 at fx_pos
    pause 0.1
    hide fx_mr_mix_3 rage2
    pause 0.1
    show gm_mr_mix_nous at center
    pause 0.1
    hide gm_mr_mix_nous rage2
    pause 0.1
    show fx_mr_mix at fx_pos
    pause 0.1
    hide fx_mr_mix rage2
    pause 0.1
    show fx_mr_mix_2 at fx_pos
    pause 0.1
    hide fx_mr_mix_2 rage2
    pause 0.1
    show fx_mr_mix_3 at fx_pos
    pause 0.1
    hide fx_mr_mix_3 rage2
    pause 0.1
    show gm_mr_mix_nous at center
    pause 0.1
    hide gm_mr_mix_nous rage2
    pause 0.1
    show fx_mr_mix at fx_pos
    pause 0.1
    hide fx_mr_mix rage2
    pause 0.1
    show fx_mr_mix_2 at fx_pos
    pause 0.1
    hide fx_mr_mix_2 rage2
    pause 0.1
    show fx_mr_mix_3 at fx_pos
    pause 0.1
    hide fx_mr_mix_3 rage2
    pause 0.1
    show gm_mr_mix_nous at center
    pause 0.1
    hide gm_mr_mix_nous rage2
    pause 0.1
    show fx_mr_mix at fx_pos
    pause 0.1
    hide fx_mr_mix rage2
    pause 0.1
    show fx_mr_mix_2 at fx_pos
    pause 0.1
    hide fx_mr_mix_2 rage2
    pause 0.1
    show fx_mr_mix_3 at fx_pos
    pause 0.1
    hide fx_mr_mix_3 rage2
    pause 0.1
    show gm_mr_mix_nous at center
    pause 0.1
    hide gm_mr_mix_nous rage2
    pause 0.1
    show fx_mr_mix at fx_pos
    pause 0.1
    hide fx_mr_mix rage2
    pause 0.1
    show fx_mr_mix_2 at fx_pos
    pause 0.1
    hide fx_mr_mix_2 rage2
    pause 0.1
    show fx_mr_mix_3 at fx_pos
    pause 0.1
    hide fx_mr_mix_3 rage2
    pause 0.1
    show gm_mr_mix_nous at center
    pause 0.1
    hide gm_mr_mix_nous rage2
    pause 0.1
    show fx_mr_mix at fx_pos
    pause 0.1
    hide fx_mr_mix rage2
    pause 0.1
    show fx_mr_mix_2 at fx_pos
    pause 0.1
    hide fx_mr_mix_2 rage2
    pause 0.1
    show fx_mr_mix_3 at fx_pos
    pause 0.1
    hide fx_mr_mix_3 rage2
    pause 0.1
    show gm_mr_mix_nous at center
    pause 0.1
    hide gm_mr_mix_nous rage2
    pause 0.1
    show fx_mr_mix at fx_pos
    pause 0.1
    hide fx_mr_mix rage2
    pause 0.1
    show fx_mr_mix_2 at fx_pos
    pause 0.1
    hide fx_mr_mix_2 rage2
    pause 0.1
    show fx_mr_mix_3 at fx_pos
    pause 0.1
    hide fx_mr_mix_3 rage2
    pause 0.1
    show gm_mr_mix_nous at center
    pause 0.1
    hide gm_mr_mix_nous rage2
    pause 0.1
    show fx_mr_mix at fx_pos
    pause 0.1
    hide fx_mr_mix rage2
    pause 0.1
    show fx_mr_mix_2 at fx_pos
    pause 0.1
    hide fx_mr_mix_2 rage2
    pause 0.1
    show fx_mr_mix_3 at fx_pos
    pause 0.1
    hide fx_mr_mix_3 rage2
    pause 0.1
    show gm_mr_mix_nous at center
    pause 0.1
    hide gm_mr_mix_nous rage2
    pause 0.1
    show fx_mr_mix at fx_pos
    pause 0.1
    hide fx_mr_mix rage2
    pause 0.1
    show fx_mr_mix_2 at fx_pos
    pause 0.1
    hide fx_mr_mix_2 rage2
    pause 0.1
    show fx_mr_mix_3 at fx_pos
    pause 0.1
    hide fx_mr_mix_3 rage2
    pause 0.1
    show gm_mr_mix_nous at center
    pause 0.1
    hide gm_mr_mix_nous rage2
    pause 0.1
    show fx_mr_mix at fx_pos
    pause 0.1
    hide fx_mr_mix rage2
    pause 0.1
    show fx_mr_mix_2 at fx_pos
    pause 0.1
    hide fx_mr_mix_2 rage2
    pause 0.1
    show fx_mr_mix_3 at fx_pos
    pause 0.1
    hide fx_mr_mix_3 rage2
    pause 0.1
    show gm_mr_mix_nous at center
    pause 0.1
    hide gm_mr_mix_nous rage2
    pause 0.1
    show fx_mr_mix at fx_pos
    pause 0.1
    hide fx_mr_mix rage2
    pause 0.1
    show fx_mr_mix_2 at fx_pos
    pause 0.1
    hide fx_mr_mix_2 rage2
    pause 0.1
    show fx_mr_mix_3 at fx_pos
    pause 0.1
    hide fx_mr_mix_3 rage2
    pause 0.1
    show gm_mr_mix_nous at center
    pause 0.1
    hide gm_mr_mix_nous rage2
    pause 0.1
    show fx_mr_mix at fx_pos
    pause 0.1
    hide fx_mr_mix rage2
    pause 0.1
    show fx_mr_mix_2 at fx_pos
    pause 0.1
    hide fx_mr_mix_2 rage2
    pause 0.1
    show fx_mr_mix_3 at fx_pos
    pause 0.1
    hide fx_mr_mix_3 rage2
    pause 0.1
    show gm_mr_mix_nous at center
    pause 0.1
    hide gm_mr_mix_nous rage2
    pause 0.1
    show fx_mr_mix at fx_pos
    pause 0.1
    hide fx_mr_mix rage2
    pause 0.1
    show fx_mr_mix_2 at fx_pos
    pause 0.1
    hide fx_mr_mix_2 rage2
    pause 0.1
    show fx_mr_mix_3 at fx_pos
    pause 0.1
    hide fx_mr_mix_3 rage2
    pause 0.1
    show gm_mr_mix_nous at center
    pause 0.1
    hide gm_mr_mix_nous rage2
    pause 0.1
    show fx_mr_mix at fx_pos
    pause 0.1
    hide fx_mr_mix rage2
    pause 0.1
    show fx_mr_mix_2 at fx_pos
    pause 0.1
    hide fx_mr_mix_2 rage2
    pause 0.1
    show fx_mr_mix_3 at fx_pos
    pause 0.1
    hide fx_mr_mix_3 rage2
    pause 0.1
    show gm_mr_mix_nous at center
    pause 0.1
    hide gm_mr_mix_nous rage2
    pause 0.1
    show fx_mr_mix at fx_pos
    pause 0.1
    hide fx_mr_mix rage2
    pause 0.1
    show fx_mr_mix_2 at fx_pos
    pause 0.1
    hide fx_mr_mix_2 rage2
    pause 0.1
    show fx_mr_mix_3 at fx_pos
    pause 0.1
    hide fx_mr_mix_3 rage2
    pause 0.1
    show gm_mr_mix_nous at center
    pause 0.1
    hide gm_mr_mix_nous rage2
    pause 0.1
    show fx_mr_mix at fx_pos
    pause 0.1
    hide fx_mr_mix rage2
    pause 0.1
    show fx_mr_mix_2 at fx_pos
    pause 0.1
    hide fx_mr_mix_2 rage2
    pause 0.1
    show fx_mr_mix_3 at fx_pos
    pause 0.1
    hide fx_mr_mix_3 rage2
    pause 0.1
    show gm_mr_mix_nous at center
    pause 0.1
    hide gm_mr_mix_nous rage2
    pause 0.1
    show fx_mr_mix at fx_pos
    pause 0.1
    hide fx_mr_mix rage2
    pause 0.1
    show fx_mr_mix_2 at fx_pos
    pause 0.1
    hide fx_mr_mix_2 rage2
    pause 0.1
    show fx_mr_mix_3 at fx_pos
    pause 0.1
    hide fx_mr_mix_3 rage2
    pause 0.1
    show gm_mr_mix_nous at center
    pause 0.1
    hide gm_mr_mix_nous rage2
    pause 0.1
    show fx_mr_mix at fx_pos
    pause 0.1
    hide fx_mr_mix rage2
    pause 0.1
    show fx_mr_mix_2 at fx_pos
    pause 0.1
    hide fx_mr_mix_2 rage2
    pause 0.1
    show fx_mr_mix_3 at fx_pos
    pause 0.1
    hide fx_mr_mix_3 rage2
    pause 0.1
    show gm_mr_mix_nous at center
    pause 0.1
    hide gm_mr_mix_nous rage2
    pause 0.1
    show fx_mr_mix at fx_pos
    pause 0.1
    hide fx_mr_mix rage2
    pause 0.1
    show fx_mr_mix_2 at fx_pos
    pause 0.1
    hide fx_mr_mix_2 rage2
    pause 0.1
    show fx_mr_mix_3 at fx_pos
    pause 0.1
    hide fx_mr_mix_3 rage2
    pause 0.1
    show gm_mr_mix_nous at center
    pause 0.1
    hide gm_mr_mix_nous rage2
    pause 0.1
    show fx_mr_mix at fx_pos
    pause 0.1
    hide fx_mr_mix rage2
    pause 0.1
    show fx_mr_mix_2 at fx_pos
    pause 0.1
    hide fx_mr_mix_2 rage2
    pause 0.1
    show fx_mr_mix_3 at fx_pos
    pause 0.1
    hide fx_mr_mix_3 rage2
    pause 0.1
    show gm_mr_mix_nous at center
    pause 0.1
    hide gm_mr_mix_nous rage2
    pause 0.1
    show fx_mr_mix at fx_pos
    pause 0.1
    hide fx_mr_mix rage2
    pause 0.1
    show fx_mr_mix_2 at fx_pos
    pause 0.1
    hide fx_mr_mix_2 rage2
    pause 0.1
    show fx_mr_mix_3 at fx_pos
    pause 0.1
    hide fx_mr_mix_3 rage2
    pause 0.1
    show gm_mr_mix_nous at center
    pause 0.1
    hide gm_mr_mix_nous rage2
    pause 0.1
    show fx_mr_mix at fx_pos
    pause 0.1
    hide fx_mr_mix rage2
    pause 0.1
    show fx_mr_mix_2 at fx_pos
    pause 0.1
    hide fx_mr_mix_2 rage2
    pause 0.1
    show fx_mr_mix_3 at fx_pos
    pause 0.1
    hide fx_mr_mix_3 rage2
    pause 0.1
    show gm_mr_mix_nous at center
    pause 0.1
    hide gm_mr_mix_nous rage2
    pause 0.1
    show fx_mr_mix at fx_pos
    pause 0.1
    hide fx_mr_mix rage2
    pause 0.1
    show fx_mr_mix_2 at fx_pos
    pause 0.1
    hide fx_mr_mix_2 rage2
    pause 0.1
    show fx_mr_mix_3 at fx_pos
    pause 0.1
    hide fx_mr_mix_3 rage2
    pause 0.1
    show gm_mr_mix_nous at center
    pause 0.1
    hide gm_mr_mix_nous rage2
    pause 0.1
    show fx_mr_mix at fx_pos
    pause 0.1
    hide fx_mr_mix rage2
    pause 0.1
    show fx_mr_mix_2 at fx_pos
    pause 0.1
    hide fx_mr_mix_2 rage2
    pause 0.1
    show fx_mr_mix_3 at fx_pos
    pause 0.1
    hide fx_mr_mix_3 rage2
    pause 0.1
    show gm_mr_mix_nous at center
    pause 0.1
    hide gm_mr_mix_nous rage2
    pause 0.1
    show fx_mr_mix at fx_pos
    pause 0.1
    hide fx_mr_mix rage2
    pause 0.1
    show fx_mr_mix_2 at fx_pos
    pause 0.1
    hide fx_mr_mix_2 rage2
    pause 0.1
    show fx_mr_mix_3 at fx_pos
    pause 0.1
    hide fx_mr_mix_3 rage2
    pause 0.1
    show gm_mr_mix_nous at center
    pause 0.1
    hide gm_mr_mix_nous rage2
    pause 0.1
    show fx_mr_mix at fx_pos
    pause 0.1
    hide fx_mr_mix rage2
    pause 0.1
    show fx_mr_mix_2 at fx_pos
    pause 0.1
    hide fx_mr_mix_2 rage2
    pause 0.1
    show fx_mr_mix_3 at fx_pos
    pause 0.1
    hide fx_mr_mix_3 rage2
    pause 0.1
    show gm_mr_mix_nous at center
    pause 0.1
    hide gm_mr_mix_nous rage2
    pause 0.1
    show fx_mr_mix at fx_pos
    pause 0.1
    hide fx_mr_mix rage2
    pause 0.1
    show fx_mr_mix_2 at fx_pos
    pause 0.1
    hide fx_mr_mix_2 rage2
    pause 0.1
    show fx_mr_mix_3 at fx_pos
    pause 0.1
    hide fx_mr_mix_3 rage2
    pause 0.1
    show gm_mr_mix_nous at center
    pause 0.1
    hide gm_mr_mix_nous rage2
    pause 0.1
    show fx_mr_mix at fx_pos
    pause 0.1
    hide fx_mr_mix rage2
    pause 0.1
    show fx_mr_mix_2 at fx_pos
    pause 0.1
    hide fx_mr_mix_2 rage2
    pause 0.1
    show fx_mr_mix_3 at fx_pos
    pause 0.1
    hide fx_mr_mix_3 rage2
    pause 0.1
    show gm_mr_mix_nous at center
    pause 0.1
    hide gm_mr_mix_nous rage2
    pause 0.1
    show fx_mr_mix at fx_pos
    pause 0.1
    hide fx_mr_mix rage2
    pause 0.1
    show fx_mr_mix_2 at fx_pos
    pause 0.1
    hide fx_mr_mix_2 rage2
    pause 0.1
    show fx_mr_mix_3 at fx_pos
    pause 0.1
    hide fx_mr_mix_3 rage2
    pause 0.1
    show gm_mr_mix_nous at center
    pause 0.1
    hide gm_mr_mix_nous rage2
    pause 0.1
    show fx_mr_mix at fx_pos
    pause 0.1
    hide fx_mr_mix rage2
    pause 0.1
    show fx_mr_mix_2 at fx_pos
    pause 0.1
    hide fx_mr_mix_2 rage2
    pause 0.1
    show fx_mr_mix_3 at fx_pos
    pause 0.1
    hide fx_mr_mix_3 rage2
    pause 0.1
    show gm_mr_mix_nous at center
    pause 0.1
    hide gm_mr_mix_nous rage2
    pause 0.1
    show fx_mr_mix at fx_pos
    pause 0.1
    hide fx_mr_mix rage2
    pause 0.1
    show fx_mr_mix_2 at fx_pos
    pause 0.1
    hide fx_mr_mix_2 rage2
    pause 0.1
    show fx_mr_mix_3 at fx_pos
    pause 0.1
    hide fx_mr_mix_3 rage2
    pause 0.1
    show gm_mr_mix_nous at center
    pause 0.1
    hide gm_mr_mix_nous rage2
    pause 0.1
    show fx_mr_mix at fx_pos
    pause 0.1
    hide fx_mr_mix rage2
    pause 0.1
    show fx_mr_mix_2 at fx_pos
    pause 0.1
    hide fx_mr_mix_2 rage2
    pause 0.1
    show fx_mr_mix_3 at fx_pos
    pause 0.1
    hide fx_mr_mix_3 rage2
    pause 0.1
    show gm_mr_mix_nous at center
    pause 0.1
    hide gm_mr_mix_nous rage2
    pause 0.1
    show fx_mr_mix at fx_pos
    pause 0.1
    hide fx_mr_mix rage2
    pause 0.1
    show fx_mr_mix_2 at fx_pos
    pause 0.1
    hide fx_mr_mix_2 rage2
    pause 0.1
    show fx_mr_mix_3 at fx_pos
    pause 0.1
    hide fx_mr_mix_3 rage2
    pause 0.1
    show gm_mr_mix_nous at center
    pause 0.1
    hide gm_mr_mix_nous rage2
    pause 0.1
    show fx_mr_mix at fx_pos
    pause 0.1
    hide fx_mr_mix rage2
    pause 0.1
    show fx_mr_mix_2 at fx_pos
    pause 0.1
    hide fx_mr_mix_2 rage2
    pause 0.1
    show fx_mr_mix_3 at fx_pos
    pause 0.1
    hide fx_mr_mix_3 rage2
    pause 0.1
    show gm_mr_mix_nous at center
    pause 0.1
    hide gm_mr_mix_nous rage2
    pause 0.1
    show fx_mr_mix at fx_pos
    pause 0.1
    hide fx_mr_mix rage2
    pause 0.1
    show fx_mr_mix_2 at fx_pos
    pause 0.1
    hide fx_mr_mix_2 rage2
    pause 0.1
    show fx_mr_mix_3 at fx_pos
    pause 0.1
    hide fx_mr_mix_3 rage2
    pause 0.1
    show gm_mr_mix_nous at center
    pause 0.1
    hide gm_mr_mix_nous rage2
    pause 0.1
    show fx_mr_mix at fx_pos
    pause 0.1
    hide fx_mr_mix rage2
    pause 0.1
    show fx_mr_mix_2 at fx_pos
    pause 0.1
    hide fx_mr_mix_2 rage2
    pause 0.1
    show fx_mr_mix_3 at fx_pos
    pause 0.1
    hide fx_mr_mix_3 rage2
    pause 0.1
    show gm_mr_mix_nous at center
    pause 0.1
    hide gm_mr_mix_nous rage2
    pause 0.1
    show fx_mr_mix at fx_pos
    pause 0.1
    hide fx_mr_mix rage2
    pause 0.1
    show fx_mr_mix_2 at fx_pos
    pause 0.1
    hide fx_mr_mix_2 rage2
    pause 0.1
    show fx_mr_mix_3 at fx_pos
    pause 0.1
    hide fx_mr_mix_3 rage2
    pause 0.1
    show gm_mr_mix_nous at center
    pause 0.1
    hide gm_mr_mix_nous rage2
    pause 0.1
    show fx_mr_mix at fx_pos
    pause 0.1
    hide fx_mr_mix rage2
    pause 0.1
    show fx_mr_mix_2 at fx_pos
    pause 0.1
    hide fx_mr_mix_2 rage2
    pause 0.1
    show fx_mr_mix_3 at fx_pos
    pause 0.1
    hide fx_mr_mix_3 rage2
    pause 0.1
    show gm_mr_mix_nous at center
    pause 0.1
    hide gm_mr_mix_nous rage2
    pause 0.1
    show fx_mr_mix at fx_pos
    pause 0.1
    hide fx_mr_mix rage2
    pause 0.1
    show fx_mr_mix_2 at fx_pos
    pause 0.1
    hide fx_mr_mix_2 rage2
    pause 0.1
    show fx_mr_mix_3 at fx_pos
    pause 0.1
    hide fx_mr_mix_3 rage2
    pause 0.1
    show gm_mr_mix_nous at center
    pause 0.1
    hide gm_mr_mix_nous rage2
    pause 0.1
    show fx_mr_mix at fx_pos
    pause 0.1
    hide fx_mr_mix rage2
    pause 0.1
    show fx_mr_mix_2 at fx_pos
    pause 0.1
    hide fx_mr_mix_2 rage2
    pause 0.1
    show fx_mr_mix_3 at fx_pos
    pause 0.1
    hide fx_mr_mix_3 rage2
    pause 0.1
    show gm_mr_mix_nous at center
    pause 0.1
    hide gm_mr_mix_nous rage2
    pause 0.1
    show fx_mr_mix at fx_pos
    pause 0.1
    hide fx_mr_mix rage2
    pause 0.1
    show fx_mr_mix_2 at fx_pos
    pause 0.1
    hide fx_mr_mix_2 rage2
    pause 0.1
    show fx_mr_mix_3 at fx_pos
    pause 0.1
    hide fx_mr_mix_3 rage2
    pause 0.1
    show gm_mr_mix_nous at center
    pause 0.1
    hide gm_mr_mix_nous rage2
    pause 0.1
    show fx_mr_mix at fx_pos
    pause 0.1
    hide fx_mr_mix rage2
    pause 0.1
    show fx_mr_mix_2 at fx_pos
    pause 0.1
    hide fx_mr_mix_2 rage2
    pause 0.1
    show fx_mr_mix_3 at fx_pos
    pause 0.1
    hide fx_mr_mix_3 rage2
    pause 0.1
    show gm_mr_mix_nous at center
    pause 0.1
    hide gm_mr_mix_nous rage2
    pause 0.1
    show fx_mr_mix at fx_pos
    pause 0.1
    hide fx_mr_mix rage2
    pause 0.1
    show fx_mr_mix_2 at fx_pos
    pause 0.1
    hide fx_mr_mix_2 rage2
    pause 0.1
    show fx_mr_mix_3 at fx_pos
    pause 0.1
    hide fx_mr_mix_3 rage2
    pause 0.1
    show gm_mr_mix_nous at center
    pause 0.1
    hide gm_mr_mix_nous rage2
    pause 0.1
    show fx_mr_mix at fx_pos
    pause 0.1
    hide fx_mr_mix rage2
    pause 0.1
    show fx_mr_mix_2 at fx_pos
    pause 0.1
    hide fx_mr_mix_2 rage2
    pause 0.1
    show fx_mr_mix_3 at fx_pos
    pause 0.1
    hide fx_mr_mix_3 rage2
    pause 0.1
    show gm_mr_mix_nous at center
    pause 0.1
    hide gm_mr_mix_nous rage2
    pause 0.1
    show fx_mr_mix at fx_pos
    pause 0.1
    hide fx_mr_mix rage2
    pause 0.1
    show fx_mr_mix_2 at fx_pos
    pause 0.1
    hide fx_mr_mix_2 rage2
    pause 0.1
    show fx_mr_mix_3 at fx_pos
    pause 0.1
    hide fx_mr_mix_3 rage2
    pause 0.1
    show gm_mr_mix_nous at center
    pause 0.1
    hide gm_mr_mix_nous rage2
    pause 0.1
    show fx_mr_mix at fx_pos
    pause 0.1
    hide fx_mr_mix rage2
    pause 0.1
    show fx_mr_mix_2 at fx_pos
    pause 0.1
    hide fx_mr_mix_2 rage2
    pause 0.1
    show fx_mr_mix_3 at fx_pos
    pause 0.1
    hide fx_mr_mix_3 rage2
    pause 0.1
    show gm_mr_mix_nous at center
    pause 0.1
    hide gm_mr_mix_nous rage2
    pause 0.1
    show fx_mr_mix at fx_pos
    pause 0.1
    hide fx_mr_mix rage2
    pause 0.1
    show fx_mr_mix_2 at fx_pos
    pause 0.1
    hide fx_mr_mix_2 rage2
    pause 0.1
    show fx_mr_mix_3 at fx_pos
    pause 0.1
    hide fx_mr_mix_3 rage2
    pause 0.1
    show gm_mr_mix_nous at center
    pause 0.1
    hide gm_mr_mix_nous rage2
    pause 0.1
    show fx_mr_mix at fx_pos
    pause 0.1
    hide fx_mr_mix rage2
    pause 0.1
    show fx_mr_mix_2 at fx_pos
    pause 0.1
    hide fx_mr_mix_2 rage2
    pause 0.1
    show fx_mr_mix_3 at fx_pos
    pause 0.1
    hide fx_mr_mix_3 rage2
    pause 0.1
    show gm_mr_mix_nous at center
    pause 0.1
    hide gm_mr_mix_nous rage2
    pause 0.1
    show fx_mr_mix at fx_pos
    pause 0.1
    hide fx_mr_mix rage2
    pause 0.1
    show fx_mr_mix_2 at fx_pos
    pause 0.1
    hide fx_mr_mix_2 rage2
    pause 0.1
    show fx_mr_mix_3 at fx_pos
    pause 0.1
    hide fx_mr_mix_3 rage2
    pause 0.1
    show gm_mr_mix_nous at center
    pause 0.1
    hide gm_mr_mix_nous rage2
    pause 0.1
    show fx_mr_mix at fx_pos
    pause 0.1
    hide fx_mr_mix rage2
    pause 0.1
    show fx_mr_mix_2 at fx_pos
    pause 0.1
    hide fx_mr_mix_2 rage2
    pause 0.1
    show fx_mr_mix_3 at fx_pos
    pause 0.1
    hide fx_mr_mix_3 rage2
    pause 0.1
    show gm_mr_mix_nous at center
    pause 0.1
    hide gm_mr_mix_nous rage2
    pause 0.1
    show fx_mr_mix at fx_pos
    pause 0.1
    hide fx_mr_mix rage2
    pause 0.1
    show fx_mr_mix_2 at fx_pos
    pause 0.1
    hide fx_mr_mix_2 rage2
    pause 0.1
    show fx_mr_mix_3 at fx_pos
    pause 0.1
    hide fx_mr_mix_3 rage2
    pause 0.1
    show gm_mr_mix_nous at center
    pause 0.1
    hide gm_mr_mix_nous rage2
    pause 0.1
    show fx_mr_mix at fx_pos
    pause 0.1
    hide fx_mr_mix rage2
    pause 0.1
    show fx_mr_mix_2 at fx_pos
    pause 0.1
    hide fx_mr_mix_2 rage2
    pause 0.1
    show fx_mr_mix_3 at fx_pos
    pause 0.1
    hide fx_mr_mix_3 rage2
    pause 0.1
    show gm_mr_mix_nous at center
    pause 0.1
    hide gm_mr_mix_nous rage2
    pause 0.1
    show fx_mr_mix at fx_pos
    pause 0.1
    hide fx_mr_mix rage2
    pause 0.1
    show fx_mr_mix_2 at fx_pos
    pause 0.1
    hide fx_mr_mix_2 rage2
    pause 0.1
    show fx_mr_mix_3 at fx_pos
    pause 0.1
    hide fx_mr_mix_3 rage2
    pause 0.1
    show gm_mr_mix_nous at center
    pause 0.1
    hide gm_mr_mix_nous rage2
    pause 0.1
    show fx_mr_mix at fx_pos
    pause 0.1
    hide fx_mr_mix rage2
    pause 0.1
    show fx_mr_mix_2 at fx_pos
    pause 0.1
    hide fx_mr_mix_2 rage2
    pause 0.1
    show fx_mr_mix_3 at fx_pos
    pause 0.1
    hide fx_mr_mix_3 rage2
    pause 0.1
    show gm_mr_mix_nous at center
    pause 0.1
    hide gm_mr_mix_nous rage2
    pause 0.1
    show fx_mr_mix at fx_pos
    pause 0.1
    hide fx_mr_mix rage2
    pause 0.1
    show fx_mr_mix_2 at fx_pos
    pause 0.1
    hide fx_mr_mix_2 rage2
    pause 0.1
    show fx_mr_mix_3 at fx_pos
    pause 0.1
    hide fx_mr_mix_3 rage2
    pause 0.1
    show gm_mr_mix_nous at center
    pause 0.1
    hide gm_mr_mix_nous rage2
    pause 0.1
    show fx_mr_mix at fx_pos
    pause 0.1
    hide fx_mr_mix rage2
    pause 0.1
    show fx_mr_mix_2 at fx_pos
    pause 0.1
    hide fx_mr_mix_2 rage2
    pause 0.1
    show fx_mr_mix_3 at fx_pos
    pause 0.1
    hide fx_mr_mix_3 rage2
    pause 0.1
    show gm_mr_mix_nous at center
    pause 0.1
    hide gm_mr_mix_nous rage2
    pause 0.1
    show fx_mr_mix at fx_pos
    pause 0.1
    hide fx_mr_mix rage2
    pause 0.1
    show fx_mr_mix_2 at fx_pos
    pause 0.1
    hide fx_mr_mix_2 rage2
    pause 0.1
    show fx_mr_mix_3 at fx_pos
    pause 0.1
    hide fx_mr_mix_3 rage2
    pause 0.1
    show gm_mr_mix_nous at center
    pause 0.1
    hide gm_mr_mix_nous rage2
    pause 0.1
    show fx_mr_mix at fx_pos
    pause 0.1
    hide fx_mr_mix rage2
    pause 0.1
    show fx_mr_mix_2 at fx_pos
    pause 0.1
    hide fx_mr_mix_2 rage2
    pause 0.1
    show fx_mr_mix_3 at fx_pos
    pause 0.1
    hide fx_mr_mix_3 rage2
    pause 0.1
    show gm_mr_mix_nous at center
    pause 0.1
    hide gm_mr_mix_nous rage2
    pause 0.1
    show fx_mr_mix at fx_pos
    pause 0.1
    hide fx_mr_mix rage2
    pause 0.1
    show fx_mr_mix_2 at fx_pos
    pause 0.1
    hide fx_mr_mix_2 rage2
    pause 0.1
    show fx_mr_mix_3 at fx_pos
    pause 0.1
    hide fx_mr_mix_3 rage2
    pause 0.1
    show gm_mr_mix_nous at center
    pause 0.1
    hide gm_mr_mix_nous rage2
    pause 0.1
    show fx_mr_mix at fx_pos
    pause 0.1
    hide fx_mr_mix rage2
    pause 0.1
    show fx_mr_mix_2 at fx_pos
    pause 0.1
    hide fx_mr_mix_2 rage2
    pause 0.1
    show fx_mr_mix_3 at fx_pos
    pause 0.1
    hide fx_mr_mix_3 rage2
    pause 0.1
    show gm_mr_mix_nous at center
    pause 0.1
    hide gm_mr_mix_nous rage2
    pause 0.1
    show fx_mr_mix at fx_pos
    pause 0.1
    hide fx_mr_mix rage2
    pause 0.1
    show fx_mr_mix_2 at fx_pos
    pause 0.1
    hide fx_mr_mix_2 rage2
    pause 0.1
    show fx_mr_mix_3 at fx_pos
    pause 0.1
    hide fx_mr_mix_3 rage2
    pause 0.1
    show gm_mr_mix_nous at center
    pause 0.1
    hide gm_mr_mix_nous rage2
    pause 0.1
    show fx_mr_mix at fx_pos
    pause 0.1
    hide fx_mr_mix rage2
    pause 0.1
    show fx_mr_mix_2 at fx_pos
    pause 0.1
    hide fx_mr_mix_2 rage2
    pause 0.1
    show fx_mr_mix_3 at fx_pos
    pause 0.1
    hide fx_mr_mix_3 rage2
    pause 0.1
    show gm_mr_mix_nous at center
    pause 0.1
    hide gm_mr_mix_nous rage2
    pause 0.1
    show fx_mr_mix at fx_pos
    pause 0.1
    hide fx_mr_mix rage2
    pause 0.1
    show fx_mr_mix_2 at fx_pos
    pause 0.1
    hide fx_mr_mix_2 rage2
    pause 0.1
    show fx_mr_mix_3 at fx_pos
    pause 0.1
    hide fx_mr_mix_3 rage2
    pause 0.1
    show gm_mr_mix_nous at center
    pause 0.1
    hide gm_mr_mix_nous rage2
    
    pause 6
    scene gm_mr_mix_l
    play music sound loop
    pause 99999999999999