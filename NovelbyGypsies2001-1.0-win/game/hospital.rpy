label hospital:
    
    scene cg black with dissolve
    scene hospital2
    ah "А,ой"
    ah "Вот это случий,"
    ah "Вот что это за бабки"
    ah "Вот теперь грустно мне стало."

    scene dva with dissolve
    scene dva
    noname ""
    scene hospital3
    $ renpy.music.stop(channel='music', fadeout = 2.0)
    play sound sfxloop_forest2
    d "А?"
    d "С утра по раньше"
    ah "А шо за вопли с утра пораньше? Мама дорогая! Сзади лай овчарок и дружки на нарах, с зоны возвращался юный фраерок..."
    d "Птички с утра по раньше поют."
    d "Зато настроение есть!"
    d "Ну...."
    d "Пока что голова по баливает."
    ad "ХААХХАХАХАХААХАХАХАХХАХААХАХАХАХАХАХАХАХХХХХХХХХХХХХХХАХАХААХАХАХ"
    ad "ПОЛУЧАЙ!"
    d "Батюшки..."
    d "Поскорей выйти."

    scene day7 with dissolve
    scene day7
    ah "Капец как быстро :) "
    ah "Ну его выписали с больницы."

    scene ostanovkio_day
    show danik at center

    play music ost loop
    ah "Посейдон ты мой."
    ah "Великолепный."
    ah "Просто мужик."
    ah "Одна мечта Ёб*ная"
    ah "Иди домой!"

    hide danik rage2 with dissolve
    scene cg black with dissolve
    play music outdoors loop
    scene gostinnay_day
    show danik at center 
    d "..."
    ah "Это-че за рация?"
    ah "Ужасы..."
    d "Пройдусь(ка) я пока-что."


    ah "А мы пусть стобой вспомнил какие времена были!"
    hide danik rage2 with dissolve
    show cg_fade at truecenter
    show fxy1_keitaro at fx_pos
    ah "Да!...."
    hide fxy1_keitaro rage2 with dissolve
    show fxy2_hunter at fx_pos
    noname""
    hide fxy2_hunter rage2 with dissolve
    hide cg_fade at rage2
    ah "Ну короче да."
    ah "Ну да."
    ah "Хватит тебе"
    ah "Аазазазазазазазазазазаазаз"
    
    $ renpy.music.stop(channel='music', fadeout = 2.0)
    play sound sleeping_time
    $time_transition_day_to_sunset()
    jump day2