label mr_mix:
    scene gm_mr_mix
    play music tpar loop
    $working = False
    menu:
         mr "Are you ready?"
         
         "Let's go":
            $ renpy.music.stop(channel='music', fadeout = 2.0)
            jump mr_mix_start_game
            
         "No":
            return