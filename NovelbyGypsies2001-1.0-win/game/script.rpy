# Вы можете расположить сценарий своей игры в этом файле.

init: #Лист игры,база данных

    #${первое букво или несколько букв для диалога} = Character("{имя персонажа}", window_background="{папка для указаной новой папки в случий это interface}/{папка служит файлами картинками для диалога в случий это scene}/text_{имя персонажа}.png {служит несколько форматов}", window_top_padding=60)

    $d = Character("Danik", window_background="interface/scene/text_danik.png", window_top_padding=60)
    $con = Character("Кондуктор", window_background="interface/scene/text_conductor.png", window_top_padding=60)
    $ad = Character("???", window_background="interface/scene/text_addanik.png", window_top_padding=60)
    $av = Character("Avan", window_background="interface/scene/text_avan.png", window_top_padding=60)
    $sh = Character("Сосед", window_background="interface/scene/text_shit.png", window_top_padding=60)
    $shit = Character("Соседи", window_background="interface/scene/text_ordashit.png", window_top_padding=60)
    $shitka = Character("Соседка", window_background="interface/scene/text_shitka.png", window_top_padding=60)
    $ah = Character("Автор", window_background="interface/scene/text_author.png", window_top_padding=60)
    $noname = Character(" ! ", window_background="interface/scene/text_empty.png", window_top_padding=60) #Я ебался с этой хуйней долго часа по типу ноунейм,ты должен сказать мне спасибо
    $bab = Character("Орда бабок", window_background="interface/scene/text_orda_bab.png", window_top_padding=60)
    $di = Character("Diviner.exe", window_background="interface/scene/text_diviner.png", window_top_padding=60)
    $mr = Character("MR.MIX.EXE", window_background="interface/scene/text_mix.png", window_top_padding=60)

    $ flash = Fade(.25, 0, .75, color="#fff")

    python:
        #шрифты игры
        style.default.font = "Fonts/TT2020StyleE-Regular.ttf"
        style.say_label.font = "Fonts/TT2020StyleE-Regular.ttf"
        style.say_dialogue.font = "Fonts/TT2020StyleE-Regular.ttf"

        import math

        class Shaker(object):

            anchors = {
                'top' : 0.0,
                'center' : 0.5,
                'bottom' : 1.0,
                'left' : 0.0,
                'right' : 1.0,
                }

            def __init__(self, start, child, dist):
                if start is None:
                    start = child.get_placement()
                #
                self.start = [ self.anchors.get(i, i) for i in start ]  
                self.dist = dist    
                self.child = child

            def __call__(self, t, sizes):
                
                
                def fti(x, r):
                    if x is None:
                        x = 0
                    if isinstance(x, float):
                        return int(x * r)
                    else:
                        return x

                xpos, ypos, xanchor, yanchor = [ fti(a, b) for a, b in zip(self.start, sizes) ]

                xpos = xpos - xanchor
                ypos = ypos - yanchor

                nx = xpos + (1.0-t) * self.dist * (renpy.random.random()*2-1)
                ny = ypos + (1.0-t) * self.dist * (renpy.random.random()*2-1)

                return (int(nx), int(ny), 0, 0)

        def _Shake(start, time, child=None, dist=100.0, **properties):

            move = Shaker(start, child, dist=dist)

            return renpy.display.layout.Motion(move,
                          time,
                          child,
                          add_sizes=True,
                          **properties)

        Shake = renpy.curry(_Shake)
    #

#
    #image {название} = "{папка для указаной новой папки в случий это BGs}/{имя файла}.{формат .jpg или png другое}"
    #Картинки:
    image gameover = "BGs/gameover.jpg"
    image auvtobus = "BGs/auvtobus.jpg"
    image garasi = "BGs/garasi.jpg"
    image gostinaya = "BGs/gostinaya.jpg"
    image kuhnia = "BGs/kuhnia.jpg"
    image magas = "BGs/magas.jpg"
    image ocno = "BGs/ocno.jpg"
    image podval = "BGs/podval.jpg"
    image room1 = "BGs/room1.jpg"
    image room2 = "BGs/room2.jpg"
    image tualet = "BGs/tualet.jpg"
    image u_computera = "BGs/u computera.jpg"
    image u_computeraall = "BGs/u computera2.jpg"
    image micorki = "BGs/u micorki.jpg"
    image ocna = "BGs/u ocna.jpg"
    image ostanovkio = "BGs/u ostanovkio.jpg"
    image plosadki = "BGs/u plosadki.jpg"
    image podesda = "BGs/u podesda.jpg"
    image u_room1 = "BGs/u room1.jpg"
    image garase = "BGs/v garase.jpg"
    image auvtobus_day = "BGs/auvtobus_day.jpg"
    image musorki_day = "BGs/u musorki_day.jpg"
    image gostinnay_day = "BGs/gostinnay_day.jpg"
    image room_day = "BGs/u room_day.jpg"
    image ostanovkio_day = "BGs/u ostanovkio_day.jpg"
    image ostanovkio_day2 = "BGs/u ostanovkio_day2.jpg"
    image magasa = "BGs/u magasa.jpg"
    image podesde = "BGs/v podesde.jpg"
    image podesda_day = "BGs/u podesda_day.jpg"
    image garderob = "BGs/garderob.jpg"
    image spalnia_strah = "BGs/spalnia_strah.jpg"
    image spalnia = "BGs/spalnia.jpg"
    image larca_day = "BGs/u larca_day.jpg"
    image hospital = "BGs/hospital.jpg"
    image hospital2 = "BGs/hospital2.jpg"
    image hospital3 = "BGs/hospital3.jpg"
    image dva = "BGs/dva.jpg"
    image day7 = "BGs/day7.jpg"
    image shool = "BGs/shool.jpg"
    image cop_shool = "BGs/cor_shool.jpg"
    image cop_shool2 = "BGs/cor_shool2.jpg"
    image klass = "BGs/klass.jpg"
    image klass2 = "BGs/klass2.jpg"
    image day_danik = "BGs/klass2.jpg"
    image night_danik = "BGs/klass2.jpg"
    image diviner = "BGs/diviner_fon.jpg"
    
    #minigame
    image gm_mr_mix = "minigame/gm_mr_mix.jpg"
    image gm_mr_mix_no = "minigame/gm_mr_mix_no.jpg"
    image gm_mr_mix_nous = "minigame/gm_mr_mix_nous.jpg"
    image gm_mr_mix_level6 = "minigame/gm_mr_mix_level6.jpg"
    image gm_mr_mix_l = "minigame/gm_mr_mix.png"
    image gm_mr_mix_level6_2 = "minigame/gm_mr_mix_level6_2.jpg"
    image diviner_fon1 = "minigame/diviner_fon.jpg"
    image diviner_fon2 = "minigame/diviner_fon2.jpg"
    
    #image {название} = "    #image {название} = "{папка для указаной новой папки в случий это fx}/{папка с картинками}/{имя файла}.{формат .jpg или png другое}"
    #FX
    image fxy1_keitaro = "images/fx/fx1-keitaro.jpg"
    image fxy2_hunter = "images/fx/fx2-hunter.jpg"
    image fx1_povestka = "images/fx/fx1-povestka.jpg"
    image fx_mr_mix = "images/fx/fx_mr_mix.png"
    image fx_mr_mix2 = "images/fx/fx_mr_mix_2.png"
    image fx_mr_mix3 = "images/fx/fx_mr_mix_3.png"
    #CG
    image cg black = "#000000"
    image cg white = "#ffffff"
    image cg_fade = "CGs/cg_fade.png"
    image cg_blur = "BGs/blur.png"
    
    image logo = "interface/logo.png"
    image disclaimer2 = "interface/disclaimer2.jpg"
    image disclaimer3 = "interface/Demo Disclaimer 3.jpg"

    #define audio.{название} = "{папка для указаной новой папки}/{папка с мьзиклами записями}/{имя файла}.{формат .mp3 или другое}"
    #песенки
    define audio.exploration = "audio/BGM/Exploration.mp3"
    define audio.greatest_memories_title = "audio/BGM/Greatest Memories (Title Screen).mp3"
    define audio.greatest_memories = "audio/BGM/Greatest Memories.mp3"
    define audio.opposites_attract = "audio/BGM/Opposites Attract.mp3"
    define audio.outdoors = "audio/BGM/Outdoors.mp3"
    define audio.winter_wolf_slow = "audio/BGM/Winter Wolf (Slow).mp3"
    define audio.winter_wolf = "audio/BGM/Winter Wolf.mp3"
    define audio.camp_buddy = "audio/BGM/dr.mp3"
    define audio.net = "audio/BGM/kino.mp3"
    define audio.test = "audio/BGM/test_ost_Novel_by_Gypsies.mp3"
    define audio.strah = "audio/BGM/Institute_Buddy_ost.mp3"
    define audio.ost = "audio/BGM/ost.mp3"
    define audio.strah_2 = "audio/BGM/strah.mp3"
    define audio.strah2 = "audio/BGM/strah2.mp3"
    define audio.lenin = "audio/BGM/lenin.mp3" 
    define audio.gameover = "audio/BGM/gameover.mp3"
    define audio.white = "audio/BGM/white.mp3"
    define audio.dark = "audio/BGM/dark.mp3"
    define audio.igor = "audio/BGM/igor.mp3"
    define audio.gay = "audio/BGM/gay.mp3"
    define audio.level = "audio/BGM/level6.mp3"
    define audio.trap = "audio/BGM/tpar.mp3"
    define audio.sound = "audio/BGM/sound.mp3"

    #define audio.{название} = "{папка для указаной новой папки}/{папка с аудио записями}/{имя файла}.{формат .mp3 или другое}"
    #SFX
    define audio.sleeping_time = "audio/BGM/016 - Sleeping time.mp3"
    define audio.alarmclock = "audio/SFX/sfx_alarmclock.mp3"
    define audio.barrelcrash = "audio/SFX/sfx_barrelcrash.mp3"
    define audio.busdoor = "audio/SFX/sfx_busdoor.wav"
    define audio.busengine = "audio/SFX/sfx_busengine.mp3"
    define audio.camerashot = "audio/SFX/sfx_camerashot.mp3"
    define audio.clotheschanging = "audio/SFX/sfx_clotheschanging.mp3"
    define audio.crowdcheer = "audio/SFX/sfx_crowdcheer.wav"
    define audio.deskpunch = "audio/SFX/sfx_deskpunch.mp3"
    define audio.dinnerbell = "audio/SFX/sfx_dinnerbell.mp3"
    define audio.dishes = "audio/SFX/sfx_dishes.mp3"
    define audio.dogwhistle = "audio/SFX/sfx_dogwhistle.mp3"
    define audio.doorclose = "audio/SFX/sfx_doorclose.mp3"
    define audio.doorknock = "audio/SFX/sfx_doorknock.wav"
    define audio.doorknockloud = "audio/SFX/sfx_doorknockloud.wav"
    define audio.doublewhistle = "audio/SFX/sfx_doublewhistle.mp3"
    define audio.fallingbody = "audio/SFX/sfx_fallingbody.mp3"
    define audio.flame = "audio/SFX/sfx_flame.mp3"
    define audio.footsteps1 = "audio/SFX/sfx_footsteps1.mp3"
    define audio.footsteps2 = "audio/SFX/sfx_foosteps2.mp3"
    define audio.grassrustle = "audio/SFX/sfx_grassrustle.mp3"
    define audio.longwhistle = "audio/SFX/sfx_longwhistle.mp3"
    define audio.phone = "audio/SFX/sfx_phone.wav"
    define audio.phonebutton = "audio/SFX/sfx_phonebutton.mp3"
    define audio.powerdown = "audio/SFX/sfx_powerdown.mp3"
    define audio.pebbles = "audio/SFX/sfx_pebbles.mp3"
    define audio.scream = "audio/SFX/sfx_scream.mp3"
    define audio.snore = "audio/SFX/sfx_snore.wav"
    define audio.stomachgrowl = "audio/SFX/sfx_stomachgrowl.mp3"
    define audio.sweep = "audio/SFX/sfx_sweep.mp3"
    define audio.tapwater = "audio/SFX/sfx_tapwater.mp3"
    define audio.thunder1 = "audio/SFX/sfx_thunder1.mp3"
    define audio.thunder2 = "audio/SFX/sfx_thunder2.mp3"
    define audio.whistle = "audio/SFX/sfx_whistle.mp3"
    define audio.bagdrop = "audio/SFX/sfx_bagdrop.mp3"
    define audio.headbonk = "audio/SFX/sfx_headbonk.mp3"
    define audio.splash = "audio/SFX/sfx_splash.mp3"
    define audio.swimming1 = "audio/SFX/sfx_swimming1.mp3"
    define audio.trashcankick = "audio/SFX/sfx_trashcankick.mp3"
    define audio.stickrub = "audio/SFX/sfx_stickrub.mp3"
    define audio.spillsoup = "audio/SFX/sfx_spillsoup.mp3"
    define audio.slamdoor2 = "audio/SFX/sfx_slamdoor2.mp3"
    define audio.simmer = "audio/SFX/sfx_simmer.mp3"
    define audio.scrub = "audio/SFX/sfx_scrub.mp3"
    define audio.scribble = "audio/SFX/sfx_scribble.mp3"
    define audio.reeling = "audio/SFX/sfx_reeling.mp3"
    define audio.printer2 = "audio/SFX/sfx_printer2.mp3"
    define audio.pillowpunch = "audio/SFX/sfx_pillowpunch.mp3"
    define audio.icingsplat2 = "audio/SFX/sfx_icingsplat2.mp3"
    define audio.frying = "audio/SFX/sfx_frying.mp3"
    define audio.fireworks = "audio/SFX/sfx_fireworks.mp3"
    define audio.fire = "audio/SFX/sfx_fire.mp3"
    define audio.filecabinet = "audio/SFX/sfx_filecabinet.mp3"
    define audio.lockeddoor1 = "audio/SFX/sfx_lockeddoor1.mp3"
    define audio.doortackle = "audio/SFX/sfx_doortackle.mp3"
    define audio.doorkey = "audio/SFX/sfx_doorkey.mp3"
    define audio.crumple = "audio/SFX/sfx_crumple.mp3"
    define audio.clinking = "audio/SFX/sfx_clinking.mp3"
    define audio.choppingfast = "audio/SFX/sfx_choppingfast.mp3"
    define audio.chopping = "audio/SFX/sfx_chopping.mp3"
    define audio.cardriveaway = "audio/SFX/sfx_cardriveaway.mp3"
    define audio.wavesday = "audio/SFX/sfx_wavesday.mp3"
    define audio.sfxloop_forest1 = "audio/SFX/sfxloop_forest1.mp3"
    define audio.sfxloop_shower = "audio/SFX/sfxloop_shower.mp3"
    define audio.bonecrack = "audio/SFX/sfx_bonecrack.mp3"
    define audio.applause = "audio/SFX/sfx_applause.mp3"
    define audio.bookdrop = "audio/SFX/sfx_bookdrop.mp3"
    define audio.tablesmash = "audio/SFX/sfx_tablesmash.mp3"
    define audio.sfxloop_wavesnight = "audio/SFX/sfxloop_wavesnight.mp3"
    define audio.sfxloop_wavesday = "audio/SFX/sfxloop_wavesday.mp3"
    define audio.blender = "audio/SFX/sfx_blender.mp3"
    define audio.busbeep = "audio/SFX/sfx_busbeep.mp3"
    define audio.lockeddoor = "audio/SFX/sfx_lockeddoor.mp3"
    define audio.slamdoor = "audio/SFX/sfx_slamdoor.mp3"
    define audio.boxontable = "audio/SFX/sfx_boxontable.mp3"
    define audio.phonepickup = "audio/SFX/sfx_phonepickup.mp3"
    define audio.dialing = "audio/SFX/sfx_dialing.mp3"
    define audio.doorbell = "audio/SFX/sfx_doorbell.mp3"
    define audio.cleaningroom = "audio/SFX/sfx_cleaningroom.mp3"
    define audio.boxesdrop = "audio/SFX/sfx_boxesdrop.mp3"
    define audio.cameraclick = "audio/SFX/sfx_cameraclick.mp3"
    define audio.sfxloop_bathroom = "audio/SFX/sfxloop_bathroom.mp3"
    define audio.carbeep = "audio/SFX/sfx_carbeep.mp3"
    define audio.sfxloop_dream = "audio/SFX/sfxloop_dream.mp3"
    define audio.sfxloop_cardriving = "audio/SFX/sfxloop_cardriving.mp3"
    define audio.icingsplat = "audio/SFX/sfx_icingsplat.mp3"
    define audio.pageflip = "audio/SFX/sfx_pageflip.mp3"
    define audio.toiletflush = "audio/SFX/sfx_toiletflush.mp3"
    define audio.fire1 = "audio/SFX/sfx_fire1.mp3"
    define audio.sink = "audio/SFX/sfx_sink.mp3"
    define audio.fancyalarm = "audio/SFX/sfx_fancyalarm.mp3"
    define audio.trekking = "audio/SFX/sfx_trekking.mp3"
    define audio.message =  "audio/SFX/sfx_message.mp3"
    define audio.flash =  "audio/SFX/sfx_flash.mp3"
    define audio.applause =  "audio/SFX/sfx_applause.mp3"
    define audio.waterspray2 =  "audio/SFX/sfx_waterspray2.mp3"
    define audio.waterspray1 =  "audio/SFX/sfx_waterspray1.mp3"
    define audio.shower =  "audio/SFX/Shower - SOUND EFFECTS - Dusche SOUND.mp3"
    define audio.punch =  "audio/SFX/sfx_punch.mp3"
    define audio.wrestling =  "audio/SFX/sfx_wrestling.mp3"
    define audio.dogwhimper =  "audio/SFX/sfx_dogwhimper.mp3"
    define audio.gulp =  "audio/SFX/sfx_gulp.wav"
    define audio.wagon =  "audio/SFX/sfx_wagon.mp3"
    define audio.bagrustle =  "audio/SFX/sfx_bagrustle.mp3"
    define audio.sweep =  "audio/SFX/sfx_sweep.mp3"
    define audio.carpark =  "audio/SFX/sfx_carpark.mp3"
    define audio.dingding =  "audio/SFX/sfx_dingding.mp3"
    define audio.puppycry =  "audio/SFX/sfx_puppycry.mp3"
    define audio.boxmove =  "audio/SFX/sfx_boxmove.mp3"
    define audio.chainyank =  "audio/SFX/sfx_chainyank.mp3"
    define audio.chain =  "audio/SFX/sfx_chain.mp3"
    define audio.busstop =  "audio/SFX/sfx_busstop.mp3"
    define audio.sand =  "audio/SFX/sfx_sand.mp3"
    define audio.crash =  "audio/SFX/sfx_crash.mp3"
    define audio.paperfalling =  "audio/SFX/sfx_paperfalling.mp3"
    define audio.howlweak =  "audio/SFX/sfx_howlweak.wav"
    define audio.forestrunning =  "audio/SFX/sfx_forestrunning.mp3"
    define audio.calldrop =  "audio/SFX/sfx_calldrop.mp3"
    define audio.utensil =  "audio/SFX/sfx_utensil.mp3"
    define audio.whistling =  "audio/SFX/whistling.wav"
    define audio.sfxloop_wavesindoor =  "audio/SFX/sfxloop_wavesindoor.mp3"
    define audio.sfxloop_lake =  "audio/SFX/sfxloop_lake.mp3"
    define audio.whistleweak =  "audio/SFX/sfx_whistleweak.mp3"
    define audio.treepunch =  "audio/SFX/sfx_treepunch.mp3"
    define audio.thermometer =  "audio/SFX/sfx_thermometer.mp3"
    define audio.stallopen =  "audio/SFX/sfx_stallopen.mp3"
    define audio.soapsound =  "audio/SFX/sfx_soapsound.mp3"
    define audio.reeling =  "audio/SFX/sfx_reeling.mp3"
    define audio.printer1 =  "audio/SFX/sfx_printer1.mp3"
    define audio.poolclean =  "audio/SFX/sfx_poolclean.mp3"
    define audio.pitfall =  "audio/SFX/sfx_pitfall.mp3"
    define audio.ovending =  "audio/SFX/sfx_ovending.mp3"
    define audio.fancyalarm =  "audio/SFX/sfx_fancyalarm.mp3"
    define audio.fallingrocks =  "audio/SFX/sfx_fallingrocks.mp3"
    define audio.enginestart =  "audio/SFX/sfx_enginestart.mp3"
    define audio.eggdrop =  "audio/SFX/sfx_eggdrop.mp3"
    define audio.drumroll =  "audio/SFX/sfx_drumroll.mp3"
    define audio.closebook =  "audio/SFX/sfx_closebook.mp3"
    define audio.boxesdrop2 =  "audio/SFX/sfx_boxesdrop2.mp3"
    define audio.toiletflush =  "audio/SFX/sfx_toiletflush.mp3"
    define audio.sfxloop_shower =  "audio/SFX/sfxloop_shower.mp3"
    define audio.sfxloop_rainindoor =  "audio/SFX/sfxloop_rainindoor.mp3"
    define audio.sfxloop_forest2 =  "audio/SFX/sfxloop_forest2.mp3"
    define audio.sfxloop_bathroom =  "audio/SFX/sfxloop_bathroom.mp3"
    define audio.valve =  "audio/SFX/sfx_valve.mp3"
    define audio.unzip =  "audio/SFX/sfx_unzip.mp3"
    define audio.trekking =  "audio/SFX/sfx_trekking.mp3"
    define audio.stickrub =  "audio/SFX/sfx_stickrub.mp3"
    define audio.spillsoup =  "audio/SFX/sfx_spillsoup.mp3"
    define audio.slamdoor =  "audio/SFX/sfx_slamdoor.mp3"
    define audio.simmer =  "audio/SFX/sfx_simmer.mp3"
    define audio.scrub =  "audio/SFX/sfx_scrub.mp3"
    define audio.scribble =  "audio/SFX/sfx_scribble.mp3"
    define audio.printer2 =  "audio/SFX/sfx_printer2.mp3"
    define audio.pillowpunch =  "audio/SFX/sfx_pillowpunch.mp3"
    define audio.icingsplat =  "audio/SFX/sfx_icingsplat.mp3"
    define audio.frying =  "audio/SFX/sfx_frying.mp3"
    define audio.fireworks =  "audio/SFX/sfx_fireworks.mp3"
    define audio.fire =  "audio/SFX/sfx_fire.mp3"
    define audio.filecabinet =  "audio/SFX/sfx_filecabinet.mp3"
    define audio.lockeddoor =  "audio/SFX/sfx_lockeddoor.mp3"
    define audio.doortackle =  "audio/SFX/sfx_doortackle.mp3"
    define audio.doorkey =  "audio/SFX/sfx_doorkey.mp3"
    define audio.crumple =  "audio/SFX/sfx_crumple.mp3"
    define audio.clinking =  "audio/SFX/sfx_clinking.mp3"
    define audio.choppingfast =  "audio/SFX/sfx_choppingfast.mp3"
    define audio.chopping =  "audio/SFX/sfx_chopping.mp3"
    define audio.cardriveaway =  "audio/SFX/sfx_cardriveaway.mp3"
    define audio.wavesday =  "audio/SFX/sfx_wavesday.mp3"
    define audio.sfxloop_forest1 =  "audio/SFX/sfxloop_forest1.mp3"
    define audio.bonecrack =  "audio/SFX/sfx_bonecrack.mp3"
    define audio.bookdrop =  "audio/SFX/sfx_bookdrop.mp3"
    define audio.tablesmash =  "audio/SFX/sfx_tablesmash.mp3"
    define audio.sfxloop_wavesnight =  "audio/SFX/sfxloop_wavesnight.mp3"
    define audio.sfxloop_wavesday =  "audio/SFX/sfxloop_wavesday.mp3"
    define audio.blender =  "audio/SFX/sfx_blender.mp3"
    define audio.busbeep =  "audio/SFX/sfx_busbeep.mp3"
    define audio.slamdoor1 =  "audio/SFX/sfx_slamdoor1.mp3"
    define audio.boxontable =  "audio/SFX/sfx_boxontable.mp3"
    define audio.phonepickup =  "audio/SFX/sfx_phonepickup.mp3"
    define audio.dialing =  "audio/SFX/sfx_dialing.mp3"
    define audio.doorbell =  "audio/SFX/sfx_doorbell.mp3"
    define audio.cleaningroom =  "audio/SFX/sfx_cleaningroom.mp3"
    define audio.static2 =  "audio/SFX/sfx_static2.mp3"
    define audio.cameraclick =  "audio/SFX/sfx_cameraclick.mp3"
    define audio.carbeep =  "audio/SFX/sfx_carbeep.mp3"
    define audio.sfxloop_dream =  "audio/SFX/sfxloop_dream.mp3"
    define audio.sfxloop_cardriving =  "audio/SFX/sfxloop_cardriving.mp3"
    define audio.pageflip =  "audio/SFX/sfx_pageflip.mp3"
    define audio.sink =  "audio/SFX/sfx_sink.mp3"
    define audio.slap =  "audio/SFX/sfx_slap.mp3"
    define audio.whipcrack =  "audio/SFX/sfx_whipcrack.mp3"
    define audio.sfxloop_forest =  "audio/SFX/sfxloop_forest.mp3"
    define audio.shit = "audio/SFX/sfx_shit.mp3"
    define audio.microsoft =  "audio/SFX/microsoft_sound_95.mp3"
    define audio.krik =  "audio/SFX/sfx_krik.mp3"
    
    #Looped SFX {лучше не трогать! если вы удалите файлы то можно}
    define audio.birds = "audio/SFX/Looped SFX/sfxloop_birds.mp3"
    define audio.bonfire = "audio/SFX/Looped SFX/sfxloop_bonfire.mp3"
    define audio.cavedrip = "audio/SFX/Looped SFX/sfxloop_cavedrip.mp3"
    define audio.crowd = "audio/SFX/Looped SFX/sfxloop_crowd.mp3"
    define audio.crowdcheer = "audio/SFX/Looped SFX/sfxloop_crowdcheer.mp3"
    define audio.drizzle = "audio/SFX/Looped SFX/sfxloop_drizzle.mp3"
    define audio.horror = "audio/SFX/Looped SFX/sfxloop_horror.mp3"
    define audio.messhall = "audio/SFX/Looped SFX/sfxloop_messhall.mp3"
    define audio.night = "audio/SFX/Looped SFX/sfxloop_night.mp3"
    define audio.rain = "audio/SFX/Looped SFX/sfxloop_rain.mp3"
    define audio.thunder = "audio/SFX/Looped SFX/sfxloop_thunder.mp3"
    define audio.windy = "audio/SFX/Looped SFX/sfxloop_windy.mp3"
    define audio.fishreel = "audio/SFX/Looped SFX/sfxloop_fishreel.mp3"

    #define audio.{название} =  "{папка для указаной новой папки в случий это audio}/{папка с аудио войсами записями для разговора}/{папка с чем-то лучше это фореплей}/{имя персонажа по название папки}/{имя файла}.{формат .mp3 или другое}"
    #Voices
    define audio.help_danik =  "audio/Voice/foreplay/author/help_danik.mp3"

    #image {название} = "{папка для указаной новой папки в случий это CGs}/{имя файла}.{формат .jpg или png другое}" {показывает отдельное окно или может таже служить базовой фигней}
    #DAY 1 
    image cg orna_1_1 = "CGs/cg_ocno_1_1.jpg"
    image cg orna2_1 = "CGs/cg_ocno_2_1.jpg"
    image cg ocno_1_2 = "CGs/cg_ocno1_2.jpg"

    #image {название} =  "{папка для указаной новой папки в случий это Sprites}/{папка служит файлами персонажами(картинками) в случий это Body}/{имя файла}.{формат .jpg или png другое}"
    #Sprites
    image medik =  "Sprites/Body/Medik.png"
    image avan = "Sprites/Body/avan1_b_casual.png"
    image danik =  "Sprites/Body/Danik.gif"
    image goodboy = "Sprites/Body/Goodboy.png"
    image bab = "Sprites/Body/orda.png"
    image dansex = "Sprites/Body/DanikSex.gif"
    image diviner = "Sprites/Bidy/diviner_exe.png"


    # позиция (лучше не трогать! но наваше усмотрение)
    #$ {название позиции} = Position(xpos={позиция:например 0.9 или 0.70}, xanchor='{тут должен стаять сентер или center}')

    $ right = Position(xpos=0.75, xanchor='center')
    $ left = Position(xpos=0.25, xanchor='center')

    $ right1 = Position(xpos=0.70, xanchor='center')
    $ left1 = Position(xpos=0.30, xanchor='center')

    $ right2 = Position(xpos=0.65, xanchor='center')
    $ left2 = Position(xpos=0.35, xanchor='center')

    $ right3 = Position(xpos=0.57, xanchor='center')
    $ left3 = Position(xpos=0.43, xanchor='center')

    $ right4 = Position(xpos=0.55, xanchor='center')
    $ left4 = Position(xpos=0.45, xanchor='center')

    $ p4_1 = Position(xpos=0.20, xanchor='center')
    $ p4_2 = Position(xpos=0.40, xanchor='center')
    $ p4_3 = Position(xpos=0.60, xanchor='center')
    $ p4_4 = Position(xpos=0.80, xanchor='center')

    $ p5_1 = Position(xpos=0.20, xanchor='center')
    $ p5_2 = Position(xpos=0.35, xanchor='center')
    $ p5_3 = Position(xpos=0.50, xanchor='center')
    $ p5_4 = Position(xpos=0.65, xanchor='center')
    $ p5_5 = Position(xpos=0.80, xanchor='center')

    $sniff  = Position(xpos=0.55, xanchor='center')
    $ p4_1a = Position(xpos=0.21, xanchor='center')
    $ p4_2a = Position(xpos=0.39, xanchor='center')
    $ p4_1b = Position(xpos=0.22, xanchor='center')
    $ p4_2b = Position(xpos=0.38, xanchor='center')
    $ p4_1c = Position(xpos=0.24, xanchor='center')
    $ p4_2c = Position(xpos=0.36, xanchor='center')

    $ p2_1 = Position(xpos=0.3333333333333333, xanchor='center')
    $ p2_2 = Position(xpos=0.6666666666666666, xanchor='center')

    $ p6_1 = Position(xpos=0.1428571428571429, xanchor='center')
    $ p6_2 = Position(xpos=0.2857142857142858, xanchor='center')
    $ p6_3 = Position(xpos=0.4285714285714287, xanchor='center')
    $ p6_4 = Position(xpos=0.5714285714285716, xanchor='center')
    $ p6_5 = Position(xpos=0.7142857142857145, xanchor='center')
    $ p6_6 = Position(xpos=0.8571428571428574, xanchor='center')

    $ p7_1 = Position(xpos=0.11, xanchor='center')
    $ p7_2 = Position(xpos=0.25, xanchor='center')
    $ p7_3 = Position(xpos=0.38, xanchor='center')
    $ p7_4 = Position(xpos=0.44, xanchor='center')
    $ p7_5 = Position(xpos=0.62, xanchor='center')
    $ p7_6 = Position(xpos=0.76, xanchor='center')
    $ p7_7 = Position(xpos=0.90, xanchor='center')

   
    $ p7_1a = Position(xpos=0.11, xanchor='center')
    $ p7_2a = Position(xpos=0.21, xanchor='center')
    $ p7_3a = Position(xpos=0.32, xanchor='center')
    $ p7_4a = Position(xpos=0.43, xanchor='center')
    $ p7_5a = Position(xpos=0.54, xanchor='center')
    $ p7_6a = Position(xpos=0.75, xanchor='center')
    $ p7_7a = Position(xpos=0.88, xanchor='center')

    
    $ p7_1b = Position(xpos=0.10, xanchor='center')
    $ p7_2b = Position(xpos=0.22, xanchor='center')
    $ p7_3b = Position(xpos=0.34, xanchor='center')
    $ p7_4b = Position(xpos=0.46, xanchor='center')
    $ p7_5b = Position(xpos=0.58, xanchor='center')
    $ p7_6b = Position(xpos=0.70, xanchor='center')
    $ p7_7b = Position(xpos=0.90, xanchor='center')

    
    $ p7_1c = Position(xpos=0.14, xanchor='center')
    $ p7_2c = Position(xpos=0.27, xanchor='center')
    $ p7_3c = Position(xpos=0.46, xanchor='center')
    $ p7_4c = Position(xpos=0.57, xanchor='center')
    $ p7_5c = Position(xpos=0.68, xanchor='center')
    $ p7_6c = Position(xpos=0.79, xanchor='center')
    $ p7_7c = Position(xpos=0.89, xanchor='center')

   
    $ p7_1d = Position(xpos=0.14, xanchor='center')
    $ p7_2d = Position(xpos=0.26, xanchor='center')
    $ p7_3d = Position(xpos=0.38, xanchor='center')
    $ p7_4d = Position(xpos=0.50, xanchor='center')
    $ p7_5d = Position(xpos=0.62, xanchor='center')
    $ p7_6d = Position(xpos=0.74, xanchor='center')
    $ p7_7d = Position(xpos=0.86, xanchor='center')

    
    $ p8_1 = Position(xpos=0.12, xanchor='center')
    $ p8_2 = Position(xpos=0.21, xanchor='center')
    $ p8_3 = Position(xpos=0.30, xanchor='center')
    $ p8_4 = Position(xpos=0.39, xanchor='center')
    $ p8_5 = Position(xpos=0.48, xanchor='center')
    $ p8_6 = Position(xpos=0.70, xanchor='center')
    $ p8_7 = Position(xpos=0.80, xanchor='center')
    $ p8_8 = Position(xpos=0.89, xanchor='center')

    
    $ p8_1a = Position(xpos=0.08, xanchor='center')
    $ p8_2a = Position(xpos=0.20, xanchor='center')
    $ p8_3a = Position(xpos=0.32, xanchor='center')
    $ p8_4a = Position(xpos=0.44, xanchor='center')
    $ p8_5a = Position(xpos=0.56, xanchor='center')
    $ p8_6a = Position(xpos=0.68, xanchor='center')
    $ p8_7a = Position(xpos=0.80, xanchor='center')
    $ p8_8a = Position(xpos=0.92, xanchor='center')

    
    $ p9_1 = Position(xpos=0.03, xanchor='center')
    $ p9_2 = Position(xpos=0.15, xanchor='center')
    $ p9_3 = Position(xpos=0.27, xanchor='center')
    $ p9_4 = Position(xpos=0.39, xanchor='center')
    $ p9_5 = Position(xpos=0.50, xanchor='center')
    $ p9_6 = Position(xpos=0.62, xanchor='center')
    $ p9_7 = Position(xpos=0.74, xanchor='center')
    $ p9_8 = Position(xpos=0.86, xanchor='center')
    $ p9_9 = Position(xpos=0.98, xanchor='center')

    
    $ p10_1 = Position(xpos=0.08, xanchor='center')
    $ p10_2 = Position(xpos=0.17, xanchor='center')
    $ p10_3 = Position(xpos=0.25, xanchor='center')
    $ p10_4 = Position(xpos=0.33, xanchor='center')
    $ p10_5 = Position(xpos=0.41, xanchor='center')
    $ p10_6 = Position(xpos=0.61, xanchor='center')
    $ p10_7 = Position(xpos=0.69, xanchor='center')
    $ p10_8 = Position(xpos=0.77, xanchor='center')
    $ p10_9 = Position(xpos=0.85, xanchor='center')
    $ p10_10 = Position(xpos=0.93, xanchor='center')

     
    $ p10_1a = Position(xpos=0.05, xanchor='center')
    $ p10_2a = Position(xpos=0.15, xanchor='center')
    $ p10_3a = Position(xpos=0.25, xanchor='center')
    $ p10_4a = Position(xpos=0.35, xanchor='center')
    $ p10_5a = Position(xpos=0.45, xanchor='center')
    $ p10_6a = Position(xpos=0.55, xanchor='center')
    $ p10_7a = Position(xpos=0.65, xanchor='center')
    $ p10_8a = Position(xpos=0.75, xanchor='center')
    $ p10_9a = Position(xpos=0.85, xanchor='center')
    $ p10_10a = Position(xpos=0.95, xanchor='center')

    $ p12_1 = Position(xpos=0.06, xanchor='center')
    $ p12_2 = Position(xpos=0.14, xanchor='center')
    $ p12_3 = Position(xpos=0.22, xanchor='center')
    $ p12_4 = Position(xpos=0.30, xanchor='center')
    $ p12_5 = Position(xpos=0.38, xanchor='center')
    $ p12_6 = Position(xpos=0.46, xanchor='center')
    $ p12_7 = Position(xpos=0.54, xanchor='center')
    $ p12_8 = Position(xpos=0.62, xanchor='center')
    $ p12_9 = Position(xpos=0.70, xanchor='center')
    $ p12_10 = Position(xpos=0.78, xanchor='center')
    $ p12_11 = Position(xpos=0.86, xanchor='center')
    $ p12_12 = Position(xpos=0.94, xanchor='center')

    $ fx_pos = Position(xpos=0.5, xanchor='center', ypos=0.065, yanchor='top')
    $ right2_foreplay = Position(xpos=0.6, xanchor='center', ypos=0.49, yanchor='center')
    $ left2_foreplay = Position(xpos=0.4, xanchor='center', ypos=0.49, yanchor='center')

    $chatbox_pos = Position(xpos=1600, ypos=1075)

    #Курсор
    define config.mouse = { 'default' : [ ('images/interface/cursor.png', 0, 0)] }






label splashscreen:

    scene cg white with dissolve
    show logo at truecenter
    $renpy.pause(2.0)

    scene disclaimer2 with dissolve
    $renpy.pause()

    return

label start:
    $_game_menu_screen = None

    $ renpy.music.stop(channel='music', fadeout = 0.0)
    $ foreplay = True

    default persistent.gamebeat = False

    # день
    default persistent.currency = 0
    default persistent.sx_unlocked = []
    default persistent.sx_purchased = []

    jump startday #стартинг {jump это стартинг модуля}

    return