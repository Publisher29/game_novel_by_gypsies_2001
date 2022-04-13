label day1:
    
    scene cg black
    ah "Новый день новые подвиги."
    ah "Встаем."

    play music lenin loop
    scene gostinnay_day with dissolve
    show danik at center 
    with dissolve



    d "Блин голова так раскалывается."
    d "О 7:53 пора на работу."
    ah "Так я иду мыться а он жрать пусть готовит."
    d "Все в 10:10 идти на работу."
    d "Надо все по быстрее сделать."
    d "И надо все спомнить что-я хотел."
    d "ГХМ..."
    ah "Ну все я тут."
    $working = False
    menu:
        d "Что мне сейчас сделать?"

        "Пойти умыться.":
            $working = True
            d "Ладно теперь идти мыться."
            ah "Нечего предъява!"
            ah "Партия будет тобой гордиться!"

            d "Сейчас будет Рашен сафари!"

            scene tualet
            show danik at p4_4
            play sound tapwater
            noname ""
            d "Сегодня хорошее утро!"
            d "Теперь вымыться!"
            
            ah "АЕЕЕЕЕЕЕМ..."
            ah "ДЕТКИ ЗАКРЫВАЕМ ГЛАЗКИ."
            
            scene cg black
            noname ""
            ah "Прошло 12 минут."

            scene gostinaya
            show danik at center
            d "Теперь идти кушать."
            hide danik rage2
            with dissolve
        "Пойти по-есть.":
           $working = True
           d "Хорошо,пойду приготовлю."
           
           scene cg black
           ah "Прошло 7 минут."
    
    scene cg black    
    d "Ну все."
    d "Теперь идти."
    d "Пойду прогуляюсь,время ище есть"

    scene podesda_day
    show danik at center
    d "..."
    hide danik rage2
    with moveoutleft

    scene cg black with dissolve
    scene larca_day
    show danik at center
    d "Ау!?"
    d "Хм пока там не кого-нет."
    d "А может пока-что я где-то прогуляюсь?"
    ah "Ну ладно,пусть гуляет."
    ah "А я в Америку пойду"
    
    $ renpy.music.stop(channel='music', fadeout = 2.0)
    scene cg black with dissolve
    d "А?"
    play music white loop
    scene magasa
    show bab at center
    show danik at p6_1
    bab "Вот он"
    bab "Довайте его закопаем на@хуй"
    bab "ДА!"
    
    d "Ой ой."
    hide danik rage2 
    with moveoutleft
    
    bab "ЛОВИМ!"
    hide bab rage2 
    with moveoutleft
    
    ah "Каждый день такое xDDDDDD"

    scene gostinaya 
    show danik at center
    d "Да ну!"
    d "Они щас будут как д@ры возле двери стаять."
    ad "А НУ ВОН ПОШЛИ!!!"
    bab "АЙ!"
    d "А?"
    
    
    d "{i}(Кто это их так?){i}"
    d "{i}(Нука){i}"
    
    scene podesda_day
    show danik at p6_1
    d "Ау?"
    d "Хм не кого-нет."
    
    show bab at right
    with dissolve
    bab "АГА ВОТ ОН!"
    bab "ЛОВИМ!"
    d "Да капец."
    d "{i}(Они меня затр@хали >:(( ){i}"
    
    ah "Ого! какие он слова знает"
    hide danik at rage2
    with dissolve
    
    bab "ПАШЛИТЕ ЗАНИМ!"
    hide bab at rage2
    with dissolve
    
    scene gostinnay_day
    show danik at center
    d "Да мне скора на работу надо."
    d "А там орда бабок замной гоняется."
    d "Беспредел."
    d "..."
    
    play sound doorknockloud
    d "Кто-то дверь хочет сломать?"
    bab "Оооткрыыыывааааааай..."
    sh "Д-ДА ПАШЛИ ВОН."
    play sound footsteps1
    play sound barrelcrash
    bab "Получай..."
    sh "ДА ВЫ МНЕ ДВЕРЬ СЛОМАЛИ БАБЫ!"
    sh "ДВЕРЬ МНЕ ЗАПИЛИЛИ БЫСТРО Б@ЯТЬ!"
    ah "Весело"
    ah "ХЫХЫХВХЫХЫАХАХАХАХАХАХАХАХАХХААХАХАХАХАХАХАХАХААХАХХАХААХАХАХАХХХХХАХАХАХАХАХАХА."
    ah "ПОЛТОРА ЧАСА БУДУ РЖАТЬ ХЫХЫХЫХЫ."
    d "Вот ужас."
    d "Какие не одыкваты."
    sh "ДА ПАШЛИ ВОН УЖЕ..."
    bab "АЙ!"
    bab "БАБЫ ЗАБЕРАЙТЕ ЕГО."
    shit "МЫ ВАМ ЩАС ДАДИМ ЗАБЕРАЙТЕ ЕГО."
    shit "ПОЛОЖИЛИ ЕГО НА МЕСТО!БЫСТРО!"
    shit "ВОН ИЗ ПОДЪЕЗДА!"
    bab "ДА ИДИ-ТЕ ВЫ НА Х..."
    shit "ЧТ-ЧТОООО?"
    sh "ВАМ СКАЗАЛИ РУССКИМИ СЛОВАМИ ВОН!"
    shit "НУ ВСЕ ВЫ-ДА ПРОСИЛИСЬ..."
    
    play sound fallingbody
    shit "ПЕРВАЯ ГОТОВА!"
    
    play sound fallingbody
    shit "ВТОРАЯ ГОТОВА!"
    
    play sound fallingbody
    shit "ТРЕТЬЯ ГОТОВА!"
    
    play sound doorclose
    shit "ТОКА ПОПРОБУЙТЕ ВОЙТИ!"
    
    bab "*Плохо слышно иза двери!*"
    
    d "Слишком весело!"
    d "Подожду 20 минут и пойду на работу."
    
    $ renpy.music.stop(channel='music', fadeout = 2.0)
    scene cg black
    ah "Прошло 20 минут."
    
    play music camp_buddy loop
    scene garderob
    show danik at center
    with dissolve
    
    d "Ну все."
    d "Пойду."
    
    play music gameover loop
    scene podesde
    show bab at right
    with dissolve
    bab "Наверна щас выйдет..."
    bab "*Ржут*"
    
    
    show danik at p2_1
    with dissolve
    d "ДА СУ.."
    
    play sound fallingbody
    hide danik
    with moveoutbottom
        
    bab "ПОЛУЧАЙ"
    bab "ХАХАХАХАХАХА"
    
    shit "АХ ВЫ..."
    shit "НУ ВСЕ ВЫ ДА ПРОСИЛИСЬ"
    
    bab "Бежим!"
    hide bab at rage2
    with dissolve 
    
    ah "Ну вот."
    
    $ renpy.music.stop(channel='music', fadeout = 2.0)
    play music dark loop
    show medik at right
    with dissolve
    ad "Ого."
    ad "Ну ладно."
    $working = False
    menu:
        ad "Что мне с ним сейчас сделать?"

        "Вылечить.":
            $working = True
            d "Ок."
            
            jump hospital

        "Не лечить,оставить его в квартире.":
           $working = True
           ad "(А эммм)"
           ad "Ок."

    scene cg black with dissolve
    scene cg black
    d "А?"
    d "Я щас опаздаю..."
    
    scene gostinnay_day 
    show dansex at center
    d "Быстро идти."
    
    $ renpy.music.stop(channel='music', fadeout = 2.0)
    play music camp_buddy loop
    scene cg black with dissolve
    scene auvtobus_day
    show danik at center
    d "Ну все пойду."
    
    ah "Ну вот и все."
    ah "Сказочки теперь конец."
    
    scene cg black with dissolve
    scene auvtobus
    show danik at center
    
    d "Ну все по-работали и хватит,{i}(на сегодня){i} "
    ah "Капец за две минуты уже устал."
    
    hide danik at rage2
    with dissolve
    ah "Кто-то рядом."
    
    $ renpy.music.stop(channel='music', fadeout = 2.0)
    play music white loop
    show bab at p2_1
    with dissolve
    
    bab "Смотрите бабы!"
    bab "Довайте его закапаем!"
    bab "ДА!"
    bab "Идем!"
    ah "ДАНЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯ"
    ah "По быстрей домой иди!"
    
    hide bab at rage2
    with dissolve

    scene podesda
    show danik at center
    with dissolve
    d "..."
    
    hide danik at rage2
    with dissolve

    show bab at center
    with dissolve
    
    bab "Вот тут он!"

    hide bab at rage2
    with dissolve
    
    $ renpy.music.stop(channel='music', fadeout = 2.0)
    play music kino loop
    scene gostinaya
    show danik at center
    d "Ну все я дома!"
    ah "Ну это-славно!"

    play sound doorbell
    d "..."
    play sound doorknockloud
    d "(ДА КТО ЭТО.)"
    
    ad "*Тихо говорят* Ща выйдет"
    d "Наверна опять эти бабы >:( "
    d "Я щас пойду и вызову милицию!"
    ah "Да!"
    ah "Сразу милицию!"
    ah "А-то иш"
    ah "Аккаянные!"

    d "Дурдом какой-та."
    d "Дежавю?"

    ah "Агхм"
    ah "Иза много-слов у меня горло заболело."

    d "Лучше подожду 7 минут."
    d "Если не уйдут тогда вызову милицию."

    $ renpy.music.stop(channel='music', fadeout = 2.0)
    play music dark loop
    scene cg black
    ah "А?"
    ah "Уже ночь?"
    ah "Неверю!"
    ah "Так,надо проверить где у нас Даня"

    scene spalnia_strah
    $ renpy.music.stop(channel='music', fadeout = 2.0)
    play music strah2 loop 
    ah "Понятно..."
    ah "Пустая комната."
    ah "Это проблемная комната."
    ah "Тут-живут теперь страшные духи."
    ah "Ладно,не об этом."
    
    #Пашел нахуй он к хуям
    $ renpy.music.stop(channel='music', fadeout = 2.0)
    play music ost loop

    scene kuhnia
    ah "Сиди тут,пока что."
    ah "Пойду пока-что прогуляюсь по квартире,может и даник встанет."
    
    ah "Не уже все"
    ah "Новый день короче :)))) "

    $ renpy.music.stop(channel='music', fadeout = 2.0)
    play sound sleeping_time
    $time_transition_night_to_day()


    jump day2

