# Kamu dapat taruh script game mu di file ini.


#renpy.can_rollback(false)

#label splashscreen:

 #   $ renpy.movie_cutscene('movie.ogv')
  #  with Pause(1)
    
   # return

# Game dimulai disini.
label start:
    stop music fadeout 1
    scene bg blck with dissolve
    init python:
        config.has_autosave = False
        config.has_quicksave = True
        config.autosave_on_quit = False
        config.autosave_on_choice = False
        
    "{cps=25}hallo dan selamat datang"
    "{cps=25}namaku Challista"
    scene Underwater with fade
    play music "BGM/001-Prolog Chalista-tikakenkyuuzyo.mp3" fadeout 1
    show Unknown03
    ch "{cps=25}aku yang akan mengamati kamu"
    ch "{cps=25}selama kamu bermain game ini"
    ch "{cps=25}game ini masih dalam perkembangan"
    ch "{cps=25}aku harap game ini dapat menghibur kalian"
    
    play sound "Sound Effect/000-Chapter Intro-kidouontekina2.mp3"
    show prolog 01 at center with dissolve
    "{cps=25}Sebuah Permintaan"
    $ renpy.pause(2, hard=True)
    hide prolog 01 with dissolve
    
    ch "{cps=1}..."
    ch "{cps=25}baiklah.. cukup untuk basa-basinya"
    ch "{cps=25}aku punya satu permintaan"
    ch "{cps=25}dan aku rasa ini permintaan mungkin sulit untukmu"
    ch "{cps=25}aku ingin kamu untuk untuk menolong 'Raven'"
    
    menu:

        "um... Baiklah":
            jump choice1_baiklah

        "Sebentar, Siapa Raven?":
            jump choice1_tunggu

    label choice1_baiklah:

        $ menu_flag = False
        
        "{cps=25}umm.. baiklah"
        ch "{cps=25}Terima kasih. walaupun kamu tak mengenalinya"
        ch "{cps=25}tapi kamu mau menolongnya"
        "{cps=25}jadi, apa yang aku harus lakukan?"
        ch "{cps=25}well....."

        jump choice1_done

    label choice1_tunggu:

        $ menu_flag = True
        "{cps=25}kalau boleh tau, dia itu {b}siapa{/b}?"
        ch "{cps=25}oh benar juga ya... kamu tak mengenalinya"
        ch "{cps=25}baiklah aku akan beritahukan padamu"
        ch "{cps=1}........."
        ch "{cps=25}tapi, lebih bagusnya kalau aku"
        ch "{cps=25}membagi ingatan Raven padamu"
        ch "{cps=25}setelah ini kamu akan melihat ingatan Raven"
        ch "{cps=25}aku harap kamu dapat membantunya"
        
        call prolog1 from _call_prolog1
        
        scene Underwater with fade
        play music "BGM/001-Prolog Chalista-tikakenkyuuzyo.mp3" fadeout 1
        show Unknown03
        ch "{cps=25}baiklah.."
        ch "{cps=25}aku rasa cukup sampai disini"
        jump choice1_done

    label choice1_done:

        # ... the game continues here.
 
    ch "{cps=25}setelah ini "
    ch "{cps=25}kamu akan mengendalikan karakter Raven"
    ch "{cps=25}kamu harus menuntun Raven dalam membuat keputusannya"
    ch "{cps=25}tapi.......{w}ingat ini...."
    ch "{cps=25}setiap pilihan{w=.5}, setiap keputusan"
    ch "{cps=25}punya konsekuensinya masing-masing"
    ch "{cps=25}jadi....{w=.5}kumohon, buatlah keputusan yang tepat"
    "{cps=25}akan kuusahakan.."
    ch "{cps=25}Goodluck"
    stop music fadeout 1
    
    call prolog2 from _call_prolog2
    call chapter1 from _call_chapter1
    if ending1:
        jump chapter2a
    else:
        jump chapter2b
        
    

    return
