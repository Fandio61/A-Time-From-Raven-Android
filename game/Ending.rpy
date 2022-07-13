label ending1:
default ending1 = False
scene bg R_Home01 with fade
"{cps=25}Raven pulang ke rumahnya"
"{cps=25}perasaan Raven sangat galau saat itu{p}ia benar-benar merasa bersalah pada mereka"
show Mama Terkejut
i "{cps=25}kamu kenapa nak?{p}ada sesuatu di sekolah?"
show Raven Sekolah Murung
rb "{cps=25}ya begitulah..."
hide Mama Terkejut
"{cps=25}Raven melihat ibunya yang sedang sibuk berurusan di dapur"
"{cps=25}ia juga memantu ibunya untuk persiapan perayaan ultahnya"
scene bg R_Home02 with dissolve
scene bg R_Home03 with dissolve
"{cps=25}malampun tiba"
"{cps=25}Raven merayakan ultahnya dengan teman dan keluarganya"
"{cps=25}perayaan berlangsung lancar hingga akhir{p}tapi, Mei dan Astrid tidak datang ke acaranya, karena kejadian tadi"
"{cps=25}setelah beres-beres rumah{p}Raven berbaring di kasur kamarnya"
stop music fadeout 1
scene bg blck
show Raven Rumahan Berpikir
rb "{cps=25}sebaiknya aku tidur.{p}aku sangat lelah hari ini"
rb "{cps=25}banyak yang sudah kulalui hari ini"
rb "{cps=25}apakah Mei baik-baik saja?"
rb "{cps=25}semoga, Mei baik-baik saja{p}besok, aku akan mengeceknya"
rb "....{w}.....{w}......"

scene Dark with fade
play music "BGM/006-Meet Unknow Either-The Dark Eternal Night.mp3" fadeout 1
rb "{cps=25}tempat ini lagi?"
show Unknown02
t "{cps=25}well well, Raven..{p}kamu melakukan yang tebaik"
t "{cps=25}aku sangat terkesan padamu"
rb "{cps=25}sebenarnya siapa kamu?"
t "{cps=25}tidak penting siapa aku{p}tapi, yang penting sekarang"
t "{cps=25}kamu sudah melakukan sesuatu yang bertentangan dengan takdir{p}dan kau harus bertanggung jawab akan hal itu"
t "{cps=25}RAVEN...."
stop music fadeout 1

scene bg Raven Room After with Fade(0.2, 0.0, 0.8, color='#fff')
show Raven Before Terkejut
rb "{cps=25}ha.........!"
"{cps=25}suara weker membuat Raven kaget dan terbangun dari tidurnya"
rb "{cps=25}.........."
show Raven Rumahan Terdiam
rb "{cps=25}Mei!"
scene bg R_Home01 with dissolve
"{cps=25}Raven segera beranjak dari kasurnya{p}kemudian bersiap secepat kilat untuk berangkat ke sekolah"
show Mama Berbicara
i "{cps=25}buru-buru banget"
show Raven Sekolah Berbicara
rb "{cps=25}ada sesuatu yang penting{p}{cps=25}aku berangkat dulu ma."
i "{cps=25}hati-hati nak"
hide Mama Berbicara
scene bg Bus Stop2 with dissolve
"{cps=25}seperti biasanya, Raven berangkat ke sekolah menggunakan bus"
scene bg Sekolah01 with dissolve
"{cps=25}sampailah ia di sekolah"
scene bg Dalam Sekolah with fade
"{cps=25}sementara ia sebagai siswa harus berbaris mengukuti apel pagi"
"{cps=25}Raven membuang pandangan sedikit untuk mencari Mei"
show Raven Sekolah Berbicara Datar
rb "{cps=25}{i}'kumohon Tuhan, semoga Mei ada'{/i}"
rb "{cps=25}{i}'semoga Mei ada'{/i}"
rb "{cps=25}{i}'Mei'{/i}"
show Raven Sekolah Diam
rb "{cps=25}....................."
$ending1 = True
"{cps=25}ia akhirnya melihat Mei sedang ikut juga berbaris mengikuti apel pagi"
rb "{cps=25}{i}'syukurlah, ia tidak apa-apa'{/i}"
show Raven Sekolah Murung
rb "{cps=25}{i}'tapi, hubunganku sama mereka kurang baik'{/i}"
rb "{cps=25}{i}'apakah ini baik-baik saja?'{/i}"
scene bg blck with fade
"{cps=25}Bersambung............."

call screen ask_chapter1a_done
screen ask_chapter1a_done:
    fixed:
        text "Chapter 1 Selesai" xalign 0.5 yalign 0.3
        ##textbutton "Save" xalign 0.33 yalign 0.5 action QuickSave()
        textbutton "Save" xalign 0.33 yalign 0.5 action ShowMenu("save")
        textbutton "Lanjutkan Chapter 2" xalign 0.66 yalign 0.5 action Return(True)
        textbutton "Keluar Main Menu" xalign 0.5 yalign 0.65 action MainMenu()
return

label ending2:
scene bg R Tamu Raven1
"{cps=25}Raven pergi ke ruang tamu{p}lalu berbaring di sofa"
show Raven Rumahan Diam
rb "{cps=25}{i}'aku berhasil kan?'{/i}"
rb "{cps=25}{i}'ya.. bagaimanapun juga inilah yang terbaik menurutku'{/i}"
rb "{cps=25}sebaiknya aku tidur juga.{p}aku sangat lelah hari ini"
show Raven Rumahan Berpikir
rb "{cps=25}banyak yang sudah kulalui hari ini"
rb "....{w}.....{w}......"

scene Dark with fade
play music "BGM/006-Meet Unknow Either-The Dark Eternal Night.mp3" fadeout 1
rb "{cps=25}tempat ini lagi?"
show Unknown02
t "{cps=25}well well, Raven..{p}kamu melakukan yang tebaik"
t "{cps=25}aku sangat terkesan padamu"
show Raven Rumahan Berpikir
rb "{cps=25}sebenarnya siapa kamu?"
t "{cps=25}tidak penting siapa aku{p}tapi, yang penting sekarang"
t "{cps=25}kamu sudah melakukan sesuatu yang bertentangan dengan takdir{p}dan kau harus bertanggung jawab akan hal itu"
t "{cps=25}RAVEN...."
stop music fadeout 1

"{cps=25}bangun...{p}Raven bangun..."
scene bg R Tamu Raven2 with Fade(0.2, 0.0, 0.8, color='#FFFFFF')
show Raven Rumahan Terkejut
rb "{cps=25}haa...!!?"
show Mei Rumahan Berbicara
m "{cps=25}bangun... {p}tukang tidur.."
show Raven Rumahan Diam
rb "{cps=25}ya yaya..{p}aku sudah bangun kok..."
hide Mei Rumahan Berbicara
scene bg blck
"{cps=25}Raven bersiap diri Mengantar Mei ke Rumahnya{p}Karena, masih ada waktu sebelum berangkat sekolah"
scene bg R_Home01
show Raven Rumahan Berbicara
rb "{cps=25}ma.. aku pergi antar Mei dulu"
show Mei Rumahan Berbicara
m "{cps=25}bu.. aku pergi dulu, terima kasih sudah izinkan aku menginap"
hide Mei Rumahan Berbicara
show Mama Berbicara
i "{cps=25}iya.... hati-hati ya"
hide Mama Berbicara
"{cps=25}Raven dan Mei bersamaan keluar dari rumahnya"
"{cps=25}loh.. Raven?"
"{cps=25}ternyata mereka bertemu Astrid tepat didepan rumah Raven"
play sound "Sound Effect/010-Ending Astrid bertemu Raven-tooi sora1.mp3"
show Astrid Rumahan Khawatir
As "{cps=25}Raven dan kak Mei{p}kalian tinggal serumah?"
show Raven Rumahan Sedih
rb "{cps=25}um... Astrid, aku bisa jelaskan"
hide Astrid Rumahan Khawatir
scene bg blck
"{cps=25}Bersambung.............."

call screen ask_chapter1b_done
screen ask_chapter1b_done:
    fixed:
        text "Chapter 1 Selesai" xalign 0.5 yalign 0.3
        textbutton "Save" xalign 0.33 yalign 0.5 action QuickSave()
        textbutton "Lanjutkan Chapter 2" xalign 0.66 yalign 0.5 action Return(True)
        textbutton "Keluar Main Menu" xalign 0.5 yalign 0.65 action MainMenu()
return