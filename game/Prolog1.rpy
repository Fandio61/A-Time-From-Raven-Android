label prolog1:
stop music fadeout 1
scene Raven-BG with dissolve

"{cps=25}Raven.. Itulah namaku.. "

"{cps=25}nama Raven memang terdengar keren,"
"{cps=25}seperti karakter protagonis dalam sebuah cerita."

"{cps=25}tapi, kusadari..."
play sound "Sound Effect/000-Chapter Intro-kidouontekina2.mp3"
show prolog 02 at center with dissolve
"{cps=25}Masa lalu Raven"
$ renpy.pause(2, hard=True)
hide prolog 02 with dissolve
play music "BGM/001-Prolog Raven-Ayamachi No Daisho-1(Slow).mp3" fadeout 1

"{cps=25}Raven dalam bahasa inggris yang artinya {i}gagak{/i}"
 
"{cps=25}Mengapa orang tuaku memberi namaku seperti itu? "
"{cps=25}Apakah Ayahku suka gagak?"
"{cps=25}Atau ibuku yang suka gagak?"
"{cps=25}Ataukah mungkin waktu aku lahir burung gagak lagi treen? "
"{cps=25}Sehingga namaku jadinya begitu"

"{cps=25}Entahlah... "

"{cps=25}Aku bahkan belum pernah bertanya pada orang tuaku"

"{cps=25}Waktu {w}demi {w=.5}waktu.. "

"{cps=25}Aku perlahan mulai melupakan pertanyaan itu"

"{cps=25}Hingga aku berumur {i}17 tahun{/i}, dan akhirnya aku mengerti sendiri.. "
"{cps=25}Mengapa aku di beri nama yang artinya gagak. "

"{cps=25}Itu karena..{w}{cps=10}.. "

"{cps=25}{b}Aku {w=.5}pembawa pesan kematian{/b} .. "

screen skip_aja():
    frame:
        xalign 0.5 ypos 50
        text _("Tekan tombol back untuk SKIP")
 
show screen skip_aja
"{cps=25}Yap..itulah diriku... "

"{cps=25}{b}13 April 2009{/b}{w}{cps=5}...." with Pause(2)
 
"{cps=25}Aku mulai merasakan keganjilan dalam diriku, "

"{cps=25}waktu perayaan ulang tahunku yang ke 17 tahun.. "

"{cps=25}Tentu saja, aku sangat bahagia saat itu, "

hide screen skip_aja
"{cps=25}karena semua keluarga dan temanku hadir di acara itu.. "

"{cps=25}Setelah aku meniup lilin angka 17 di kue ultah buatan ibuku." 

"{cps=25}Semua mengucapkan selamat kepadaku dengan sangat meriah.. "

"{cps=25}aku mulai merasakan keanehan ini.{w}.."

"{cps=25}hawa yang aneh"

"{cps=25}menyelimuti semua orang disekelilingku"
show Dark Flame with Fade(0.2, 0.0, 0.8, color='#fff')
play sound "Sound Effect/Heart_Beat01-2L.mp3"
queue sound "Sound Effect/Heart_Beat01-2L.mp3"
queue sound "Sound Effect/Heart_Beat01-2L.mp3"
queue sound "Sound Effect/Heart_Beat01-2L.mp3"
pause (2)

"{cps=25}ya, Api Hitam Seperti ini"

"{cps=25}{i}'apa ini?'{/i} {w}itu yang ada dipikiranku saat itu"

"{cps=25}dan paling mengganggu ialah.{w}."

"{cps=25}hawa paling mencengkam yang kurasakan saat didekat dia.."

"{cps=25}teman masa kecilku sekaligus orang yang kusukai..{w}{b}Mei{/b}.."

"{cps=25}aku yang seharusnya menyatakan perasaan padanya saat selesai ultahku..."

"{cps=25}tertunda karena hawa yang mengganggu ini"

"{cps=25}aku tidak tau apa itu"

hide Dark Flame with fade
"{cps=25}keesokan harinya...{w}Mei ditemukan meninggal.."

"{cps=25}sedih {w=.5}dan terpukul, yang kurasakan saat itu "

"{cps=25}aku cukup depresi saat itu"

"{cps=25}tidak sampai disitu saja...{w}."

"{cps=25}keluarga{w=.5}, teman{w=.5}, bahkan kenalan"

"{cps=25}satu... {w=.5}per satu {w=.5}mereka meninggal{w=.5}, dengan kematian yang berbeda-beda"

"{cps=25}aku yang awalnya tidak tau hawa apa yang kurasakan saat itu"

"{cps=25}dan akupun sadar, bahwa itu adalah..."

"{cps=25}{b}PETUNJUK KEMATIAN{/b}"
"{cps=25}saat aku merasakan hawa itu pada seseorang"
"{cps=25}pasti mereka sedang dalam bahaya"
"{cps=25}tapi, aku gagal menyelamatkan mereka"
"{cps=25}semuanya sudah terlambat"
"{cps=25}orang terpenting dalam hidupku sudah tiada"
"{cps=25}aku terlalu terlambat untuk menyadarinya"
"{cps=25}lalu, untuk apa aku punya kemampuan ini?"
"{cps=25}kalau aku tidak bisa berbuat apa-apa"
"{cps=25}aku mulai takut dan membenci diriku sendiri"
"{cps=25}aku sudah muak dengan semua ini"
"{cps=25}aku ingin hilang saja dari Dunia ini"
stop music fadeout 1

return