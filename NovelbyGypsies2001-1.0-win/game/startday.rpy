label startday:
    play music exploration loop
    scene black with dissolve
    pause 3
    show text "Blume Corporation" with dissolve
    pause 3
    show text "Umeni zulu | Umeni Security Все права под охраной!" with dissolve
    pause 3
    show text "ctOS Вас Приветствует в игре!" with dissolve
    pause 3 
    show text "Приятной игры!" with dissolve
    pause 1
    scene black with dissolve
    $ renpy.music.stop(channel='music', fadeout = 2.0)
    pause 1
    
    jump day0
