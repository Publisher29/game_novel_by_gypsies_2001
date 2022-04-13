label day0:
    
    scene cg black #with dissolve
    $working = True

    play sound busengine
    ad "Ну что."
    ad "Как теперь сохранить воспоминание?"
    ad "Ну ладно,слава богу что я еду с работы."
    ad "*Думает*."

    play sound busdoor
    con "ПОСЛЕДНЯЯ ОСТАНОВКА - \"СЕРОЕ\"!"
    scene ostanovkio
    play music camp_buddy loop

    show danik at center
    ad "Ну все,я приехал."
    ad "Теперь только до дома добраться."
   
    hide screen location
    hide screen timeline
    hide screen quick_menu
    scene cg black with fade
    $ renpy.pause (1.0, hard=True)

    #--------Сцена 2-----------------#
    scene podesda
    show danik at right2
    ad "*Идет.*"
    ad "Фух,как устал."
    ad "Улица Бытовая."
    ad "Хм,подъезд всегда открытый,думаю когда его починят."

    scene cg black with dissolve
    scene podesde
    show danik at p4_1a
    d "А эх."
    
    play sound doorknock
    noname ""

    d "(Свою дверь стучу,дожил блин я.)"
    d "(Лучше я войду,и не буду шуметь в подъезде.)"

    scene cg black with dissolve
    scene kuhnia
    $ renpy.music.stop(channel='music', fadeout = 2.0)
    
    play music kino loop
    ah "Ну вот,Даня пришел домой и это к лучшему."
    ah "думаю лучше его не беспокоить в это время."
    
    show danik at center 
    d "Лучше радио включу."
    d "по веселей было."
    noname ""
    d "Лучше приготовлю покушать."
    d "передам по словам пожрать."
    d "Все соседи спят..."
    d "А может и нет."
    d "да какая разница."

    ah "Ну вот даник начал готовить еду"
    ah "А давайка пойдем в гостиную"

    scene cg black with dissolve
    scene gostinaya
    $ renpy.music.stop(channel='music', fadeout = 2.0)

    ah "Вот гостиная Даника!"
    ah "Может быть и твоя!"
    ah "Пошли в спальную комнату Даника!тоже покажу :)"

    scene cg black with dissolve
    scene spalnia

    ah "Вот это спальня Даника,лучше о нем нечего не говорить."
    ah "У него всегда окно открыто,я тоже спал иногда открытым окном."
    
    play sound dishes
    play music winter_wolf_slow loop
    ah "..."     
      
    d "Гребанные банки."
    d "Как я их не навижу."
    d "Пойду мусор выкину."

    ah "Вот это шум."
    ah "А..."
    ah "А мне пуфик."
    ah "Главное что он жив и цел."
    
    play sound doorclose

    noname ""
    ah "Да он щас всех соседей разбудит..."
    ah "Ну ладно,пашли к нему."
    $ renpy.music.stop(channel='music', fadeout = 2.0)

    scene cg black with dissolve
    scene micorki
    play sound shit
    show danik at center 

    d "Ну все."
    d "Теперь домой."
    d "(А стоп,может в магазин,он щас открыт.)"
    d "(А зачем мне?)"
    d "А черт у меня еда дома,надо поесть и по играть в компьютер,а лучше все в двое."
    
    ah "Ну вот Данек щас профукает еду свою."
    ah "Остынет..."
    ah "Скажи ему."

    scene cg black with dissolve
    scene kuhnia
    play music kino loop
    d "Слава Богу что еда осталось."
    d "Как весело мне живется."

    scene cg black with dissolve
    scene u_computera
    d "Ну все."
    with flash
    play sound microsoft
    scene u_computeraall

    d "*Кушает*"
    
    scene cg black with dissolve
    scene cg black
    ah "Прошло уже 20 минут."
    ah "И он покушал."
    ah "Ну теперь наверна спать пойдет."
    ah "А ты?"
    ah "Ай да ладно)"

    scene cg black with dissolve
    scene u_computera
    
    d "(Очень вкусно было.)"
    d "(Какой я ох**ный человек.)"
    d "(Блин зовидую самого себя.)"
    d "(Ладно спать пойду.)"

    hide screen quick_menu
    scene cg white with dissolve
    show cg orna_1_1 with dissolve
    show screen quick_menu
    play music strah loop
    d "ЧТО ЭТО М*ТЬ ВАШУ?!"
    d "ЭТО ЧО ЗА УЖАС?"
    d "ААААААААААА."
    d "ЫА"
    d "(КАПЕЦ ЩАС СОСЕДЕЙ РАЗБУЖУ)"
    d "(ЛУЧШЕ БУДУ МОЛИТСЯ)"
    d "(НАДО БЫСТРО ЗАКРЫТЬ ОКНО И ВЫКЛЮЧИТЬ СВЕТ ИЛИ БЕЖАТЬ В ХОРОШОЕ УБЕЖИЩЕ)"

    ah "А ой..."
    ah "А вот тут ужас какой-та."
    ah "Думай кто ты там за компом."
    ah "Ладно... Сам сделаю."
    
    scene cg black with dissolve
    scene cg black 
    $ renpy.music.stop(channel='music', fadeout = 2.0)
    ah "Ну вот теперь он переехал на одну ночь в другую комнату."
    ah "Но этот ужас должен кто-то видеть!?"
    ah "Ладно."
    ah "На следующее утро."

    play sound alarmclock
    play music outdoors loop
    scene gostinnay_day
    show danik at center 
    d "..."
    d "(Ну вот.)"
    d "(Пока-что все нормально.)"
    d "(Но может мне в ту ночь показалось?)"
    d "(Но хорошо что-нового года нет.)"
    d "(То было ужас на улице.)"
    d "Эх..."
    d "Пойду умоюсь."

    scene cg black with dissolve
    scene tualet
    play sound tapwater
    show danik at right2
    noname ""
    d "..."
    d "Ну все."
    d "Теперь идти-кушать и потом прогулятся."

    ah "Ну ладно пусть он идет-кушать."

    $ renpy.music.stop(channel='music', fadeout = 2.0)
    scene cg black with dissolve
    scene podesda_day
    show danik at center
    d "..."
    ah "..."
    shit "УИХГ ДА..."
    d "А?"
    ah "Вот это да."
    ah "У кого-то вечеринка."
    d "Нука пройдусь."
    ah "СТАПЕ БЛИН!!!!!!!!!!!!!!!"

    play music exploration loop
    d "А?"
    d "Кто это."
    d "Надо по ближе посмотреть."

    show avan at right
    with dissolve

    av "Гхм."
    d "Аэм..."
    d "Привет."

    av "А?"
    av "Привет."
    
    d "Меня зовут Данек."
    d "(АААААААААААААААА.)"
    d "(Главное что бы шутку не придумал по типу = Данек на ссал на пенек.)"
    d "(...)"

    av "Приятно познакомиться."
    av "Меня зовут Аван Гейсерфорд"
    av "Может тебе что-то надо?"
    av "Могу помочь."
    
    d "Спасибо не надо :)"
    av "Рад тебя знать."
    ah "ОГО...."
    ah "Нашь дорогой друг приобрел себе друга."
    ah "Похвально."

    av "Ладно..."
    
    $ renpy.music.stop(channel='music', fadeout = 2.0)
    play music ost loop
    d "(АГХА?)"
    ah "Ало даня..."
    ah "Давай на твоем языке скажу."
    ah "ДЫФХАФЫАДФЫХЪАДФЫХЪВДФЫХВДФЫХАДХФЫДАФЗЫ; ; ; УГАБУГАУГАБУГА"
    ah "АДФАЫФШ!УЛ!)К8мсч08м8ч0м80ЯЧ__АЧА__ЧА_ЧАФЫ?А?? !№?!"
    ah "Андерстуд?"
    
    ah "Ну ладно."
    ah "Наверно он не понял."

    av "Ну тогда я пойду."
    d "АГХ..."
    d "Хорошо..."

    scene cg black with dissolve
    scene ostanovkio_day
    show danik at center
    d "Эх..."
    d "ООООО"
    d "Пойду с друзьями погуляю."
    d "А то сидеть дома с ужасами."
    d "Ужасы пришли из России"
    hide danik rage2 
    with moveoutleft

    ah "Ну вот."
    ah "Каждый день такое." 
    ah "Оставил меня одного с тобой."
    ah "Ладно,ночью приедет."
    
    $ renpy.music.stop(channel='music', fadeout = 2.0)
    play music camp_buddy loop
    scene cg black with dissolve
    scene cg black
    ah "Где то сейчас времени 20:35 и его щас нет."
    
    scene auvtobus
    show danik at center
    with dissolve
    d "Ну все,по путешествовал."
    d "Ну хватит."

    scene cg black with dissolve
    scene podesda
    show danik at p5_1
    with dissolve

    d "Обычная ночь."
    d "(ДА ЛАДНО...)"
    d "(А ЕСЛИ ОПЯТЬ УЖАС БУДЕТ?)"
    d "(КАПЕЦ)"
    d "(Ну ладно)"
    
    $ renpy.music.stop(channel='music', fadeout = 2.0)
    scene cg black with dissolve
    scene garderob
    show danik at center
    with dissolve
    play sound doorclose
    ah "Ну что."
    ah "Как ты там?"
    
    d "По-есть приготовить надо."
    d "Пойду в магазин."
    
    hide danik
    with dissolve
    
    play sound doorclose

    scene cg black with dissolve
    scene gostinaya
    ah "Вот мы стобой дома."
    ah "Какие были путешествие."
    ah "Ну ладно."

    scene cg black with dissolve
    ah "Прошло 7 минут."
    
    scene spalnia
    play sound doorclose
    ah "О."
    ah "Он вернулся."
    d "Ну все я дома."
    d "Ого уже 21:05"
    d "Надо пойти поесть и ложится спать."
    
   
    show danik at center
    d "ЧТО?"
    
    hide danik
    hide screen quick_menu
    scene cg white with dissolve
    show cg ocno_1_2 with dissolve
    show screen quick_menu
    play music strah_2 loop

    ah "Я скоро от этих-ужасов я рожу..."
    d "О нет"
    d "(МОЖЕТ КТО ТО ЭТО ВИДЕТ????!?!?!?!?!?!?!?!!??!!?!?!?!?!)"
    sh "*Крапит*"
    d "(НЕЧЕГО СЕБЕ.)"
    d "(ДА СКОЛЬКО ЭТИХ С@КИ ТЬМЫ?)"
    
    play sound snore
    sh " *Звуки храпение* "
    
    scene cg black with dissolve
    ah "Даня побежал прятатся."
    ah "В другую комнату."

    $ renpy.music.stop(channel='music', fadeout = 2.0)
    ah "А вы как-бы поступили?"

    scene spalnia_strah 
    play sound sfxloop_forest2
    ah "Даня спал а ужас все ище продолжался"
    ah "Ну все ище тихо..."
    ah "Что?"

    show goodboy at right2
    ah "ВОТ ЭТО ДА!"
    play music strah2 loop
    ah "Нужен тут теперь священник."
    ah "Сегодня я спать не буду."
    show goodboy at right4
    ah "Вот теперь точно не буду."
    show goodboy at p5_5
    noname ""
    ah "..."
    
    $ renpy.music.stop(channel='music', fadeout = 2.0)
    play sound dishes
    
    d "ЭТО ЧТО ЗА СМЕРТНИК В МОЕМ КОМНАТЕ?"
    ah "Похоже даник идет в комнату"
    play music winter_wolf loop
    hide goodboy rage2 
    with moveoutleft
    
    $ renpy.music.stop(channel='music', fadeout = 2.0)
    play music strah loop 
    scene spalnia
    with dissolve
    show danik at p5_5
    with dissolve
    d "КТО ЗДЕСЬ?"
    d "ЧТО ЗА УЖАС БЛ@ТЬ."
    ah "Ого у даника была дома бита."
    ah "Какие мы стобой современные xD"
    d "КУДА УБЕЖАЛ С@КА."
    
    play sound headbonk
    d "ВОЗВРАЩАЙТЕСЬ В АД СУКИ ТЬМЫ."
    hide danik rage2 
    with moveoutleft
    

    play sound headbonk
    d "ДЕТИ САТАНЫЫЫЫ."
    d "УБЕРАЙТЕСЬ."
    ah "Вот это да"
    
    ah "Пойду им дверь открою."
    
    scene garderob with dissolve
    show goodboy at center
    d "КУДА!!?!?!"
    play sound doorknock
    d "КАПЕЦ КТО ТО СТУЧИТ!"
    play sound doorknockloud
    d "ВХОДИ БЛ@ТЬ"
    show avan at right
    with dissolve
    av "Это что за чучело..."
    d "ДА У МЕНЯ ТУТ ВЕСЕЛУМБА!!!!!"
    d "БЕЙ ЕГО."
    d "ПУСТЬ ГОРИТ В АДУ."
    hide goodboy rage2 
    with moveoutleft
    av "..."
    hide avan rage2 
    with moveoutleft

    scene kuhnia 
    with dissolve
    show goodboy at center 
    d "ОН НА КУХНЕ!"
    av "Книгу просветлений надо..."
    show avan at p4_1a
    with dissolve

    av "Я просто в шоке..."
    av "Почему только я и ты вышли на бой"
    
    play sound headbonk
    av "КУДА."
    play sound headbonk
    scene podesda
    with dissolve

    show goodboy at p4_1a
    show danik at center
    show avan at p4_4
    d "КУДА ВЕРНИСЬ!"

    d "СТОЯТЬ!"
    hide goodboy rage2 
    with moveoutleft

    d "В ДОМ БЫСТРО ЗАКРЫТЬ ВСЕ ДВЕРИ И ОКНА НАПРОЧЬ!!!!!"
    
    $ renpy.music.stop(channel='music', fadeout = 2.0)
    play music opposites_attract loop
    scene gostinaya
    with dissolve
    show danik at center
    show avan at p4_4
    
    d "Капец..."
    av "Сам ты как попался в чучело?"
    d "Я спал и произошло звук!"
    d "Слишком громкий."
    d "Я всегда смотрю в окно,но судьба сделала плохой день."
    d "В окне было три псины,тока какая-та из них залезла под коврик (дом)"

    av "Понятно."
    av "Ужасы в нашем доме."
    av "Ладно пойду я пока!"
    d "Пока..."
    hide avan rage2
    with dissolve
    
    d "Капец..."
    d "Надо переехать в другую квартиру."

    $ renpy.music.stop(channel='music', fadeout = 2.0)
    play sound sleeping_time
    $time_transition_night_to_day()


    jump day1

