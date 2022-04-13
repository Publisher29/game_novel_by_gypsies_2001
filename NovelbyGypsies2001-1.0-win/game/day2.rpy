label day2:

    scene cg black with dissolve
    scene gostinnay_day
    show danik at center
    play music outdoors loop
    d "АААААААА"
    ah "Ну допустим,чо ты орешь как еб*нутый?"
    ah "Я для тебя повестку в институт брал."
    ah "А ты орешь с утра по раньше >:( "
    
    $ renpy.music.stop(channel='music', fadeout = 2.0)
    hide danik at rage2 with dissolve
    scene cg black with dissolve    
    scene podesde
    play music gay loop

    show cg_fade at truecenter
    show fx1_povestka at fx_pos
    d "Это что такое?"
    d "В нутри моего ящика."
    d "Допустим."
    ah "Доброе утро солнышко :) "
    
    hide cg_fade at rage2 with dissolve
    hide fx1_povestka at rage2 with dissolve
    d "Ну ок."
    $ renpy.music.stop(channel='music', fadeout = 2.0)
    d "Пойду подготовлюсь."

    play sound sleeping_time
    $time_transition_sunset_to_night()
    
    scene garderob
    d "Хм."
    
    scene cg black with dissolve
    scene cg black
    play music winter_wolf loop 
    ah "Ситуация полная попа."
    ah "Думаю он соберется."
    ah "мужская сексуальная дружба."
    ah "говно дружба жвачка"
    ah "Ну т.к"
    
    $ renpy.music.stop(channel='music', fadeout = 2.0)
    play sound sleeping_time
    $time_transition_night_to_day()

    scene cg black
    ah "Новый день новые подвиги!"

    play music igor loop
    scene auvtobus_day
    show danik at center
    d "Ну что..."
    d "Поехали."

    scene cg black with dissolve
    scene cg black
    ah "Ура."
    ah "Дурдом."
    ah "Все-гда хотел увидеть это."
    
    scene shool
    $ renpy.music.stop(channel='music', fadeout = 2.0)
    play music greatest_memories_title loop
    ah "Капец,почему я не подумал какой взять саратник!?"
    ah "Ну ладно,по учится и хватит."


    jump pdns