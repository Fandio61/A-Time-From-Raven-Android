label MeiDie:
$ menu_flag = True
scene bg Raven House02 with fade
"{cps=25}esok paginya..{w}."
"{cps=25}Raven terbangun dari tidurnya yang nyenyak"
"{cps=25}ia melakukan aktivitas paginya seperti biasa"
"{cps=25}sarapan dan lain sebagainya untuk bersiap ke sekolah"
"{cps=25}saat ia membuka tv untuk menemaninya saat sarapan"
scene bg blck
"{cps=25}nafsu makannya tiba-tiba terhenti{p}karena ia melihat suatu berita di tv yang sangat mengejutkan"
show image "images/Scene/Mei_Rumahan_Scene 01.png" with dissolve
"{cps=25}seorang mayat ditemukan meninggal dengan keadaan sangat mengenaskan"
"{cps=25}dan mayat itu adalah.."
"{cps=25}Mei"
hide image "images/Scene/Mei_Rumahan_Scene 01.png" with dissolve
scene bg Raven Room After
"{cps=25}Raven segera beranjak disitu dan menuju kekamarnya{p}ia mencari jam itu untuk bisa kembali"
"{cps=25}setelah ia menemukan jam itu{p}ia menatapnya dengan serius"
show Raven Sekolah Berbicara Datar
rb "{cps=25}seharusnya aku menyelamatkannya"
rb "{cps=25}tapi aku gagal"
show Raven Sekolah Serius
rb "{cps=25}tunggu aku Mei{p}aku akan menyelamatkanmu"
"{cps=25}Raven menekan tombol itu"
"{cps=25}Raven merasakan keanehan dalam dirinya"
"{cps=25}jantung yang berdebar tak beraturan"
"{cps=25}membuat pandangan Raven mulai memudar"
"{cps=25}Raven kehilangan keseimbangan, sehingga ia terjatuh"
"{cps=25}kesadaran Raven mulai di ambang batas"
play sound "Sound Effect/001-Kembali Checkpoint-Accent37-1.mp3"
scene bg Meja Makan with Fade(0.2, 0.0, 0.8, color='#FF0000')
$renpy.load('checkpoint')

label RavenDie:
$ menu_flag = True
scene Dark with fade
play music "BGM/006-Meet Unknow Either-The Dark Eternal Night.mp3" fadeout 1
show Raven Rumahan Murung
rb "{cps=25}aku..."
rb "{cps=25}mengapa aku bisa disini?"
show Unknown02 with dissolve
t "{cps=25}hadeeeh...."
t "{cps=25}well..{p}setidaknya kamu sudah berusaha"
t "{cps=25}lain kali, hati-hati dalam pilihanmu"
rb "{cps=25}........"
stop music fadeout 1
menu:
    
    "kembali ke checkpoint":
        play sound "Sound Effect/001-Kembali Checkpoint-Accent37-1.mp3"
        scene bg Meja Makan with Fade(0.2, 0.0, 0.8, color='#FF0000')
        $renpy.load('checkpoint')
        
    "keluar menu utama":
        $MainMenu(confirm=False)()

label melanggar1:

scene Dark with fade
play music "BGM/006-Meet Unknow Either-The Dark Eternal Night.mp3" fadeout 1
show Raven Sekolah Berpikir
rb "{cps=25}mengapa aku bisa disini?"
rb "{cps=25}aku..."
show Unknown02 with dissolve
t "{cps=25}hadeeeh...."
t "{cps=25}walaupun kamu berusaha menulisnya"
t "{cps=25}kamu tetap melanggar peraturan yang sudah kita sepakati"
t "{cps=25}kamu pikir, aku tidak mengetahuinya"
rb "{cps=25}peraturan?"
t "{cps=25}kau ini kenapa sih"
t "{cps=25}apa kamu lupa sama perjanjiannya?"
rb "{cps=25}perjanjian?"
rb "{cps=25}apa maksudmu?"
rb "{cps=25}hey! {w=0.5}jawab aku!"
rb "{cps=25}hey!!"
stop music fadeout 1
play sound "Sound Effect/001-Kembali Checkpoint-Accent37-1.mp3"
scene bg Meja Makan with Fade(0.2, 0.0, 0.8, color='#FF0000')
$renpy.load('checkpoint')

label melanggar2:
    
scene Dark with fade
play music "BGM/006-Meet Unknow Either-The Dark Eternal Night.mp3" fadeout 1
show Raven Sekolah Berpikir
rb "{cps=25}aku..."
rb "{cps=25}mengapa aku bisa disini?"
show Unknown02 with dissolve
t "{cps=25}kamu melanggar peraturan yang sudah kita sepakati"
rb "{cps=25}peraturan?"
t "{cps=25}jangan bilang"
t "{cps=25}apa kamu lupa sama perjanjiannya?"
rb "{cps=25}perjanjian?"
rb "{cps=25}apa maksudmu?"
rb "{cps=25}hey! {w=0.5}jawab aku!"
hide Unknown02 with dissolve
rb "{cps=25}hey!!"
stop music fadeout 1
play sound "Sound Effect/001-Kembali Checkpoint-Accent37-1.mp3"
scene bg Meja Makan with Fade(0.2, 0.0, 0.8, color='#FF0000')
$renpy.load('checkpoint')


return