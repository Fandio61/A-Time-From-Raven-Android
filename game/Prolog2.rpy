label prolog2:

scene Dark with fade
show chapter 0 at center with dissolve
play sound "Sound Effect/000-Chapter Intro-kidouontekina2.mp3"
"{cps=25}Unexpected Gift"
$ renpy.pause(4, hard=True)
hide chapter 0 with dissolve

play music "BGM/001-Meet Nita-Tsumetai_Kehai-2(Fast).mp3" fadeout 1
rb "{cps=25}{i}'apa yang terjadi padaku?'{/i}"
rb "{cps=25}{i}'dimana aku?'{/i}"
rb "{cps=25}{i}'tubuhku terasa sangat ringan'{/i}"
rb "{cps=25}{i}'seolah-olah aku melayang di ruang gelap ini'{/i}"
rb "{cps=25}{i}'aku tak tau ini dimana, {w=.5}dan bagaimana aku bisa disini'{/i}"
rb "{cps=25}{i}'tapi...'{/i}"
rb "{cps=25}{i}'kepalaku... {w=.5}rasanya sakit sekali'{/i}"
show screen skip_aja
rb "{cps=25}{i}'aku juga mulai merasakan, ada yang menepuk pipiku'{/i}"
rb "{cps=25}{i}'indra perabaku, merasakan tangan yang hangat ini'{/i}"
rb "{cps=25}{i}'yang terus menepuk pipiku dengan lembut'{/i}"
t "{cps=25}bangun...."
rb "{cps=25}{i}'indra pendengaranku, mulai mendengar suara itu'{/i}"
t "{cps=25}bangun..."
hide screen skip_aja
show Raven Rumahan Murung
rb "{cps=25}{i}'lama-kelamaan....{w=.5}pipiku mulai terasa sakit'{/i}"
rb "{cps=25}{i}'rasa sakit ini sangat menggangguku'{/i}"
rb "{cps=25}............."

scene bg Raven-Start with Fade(0.2, 0.0, 0.8, color='#fff')
show Raven Rumahan Terkejut
rb "{cps=25}!!!!!"
show Nita Casual Khawatir
t "{cps=25}ah...{w=.5}akhirnya kau sadar"
hide Nita Casual Khawatir
show Nita Casual Khawatir1
t "{cps=25}sumpah..{w=.5}kau membuatku panik"
show Raven Before Diam
    
menu:
    
    rb "{cps=10}um......."
    "apa yang terjadi padaku?":
        jump choice3_apa

    "siapa kamu?":
        jump choice3_siapa

label choice3_apa:
    
    $ menu_flag = False
    
    show Raven Before Bicara
    rb "{cps=25}apa yang terjadi padaku?"
    show Nita Casual Khawatir
    t "{cps=25}jangan bilang..{w=.5}kamu hilang ingatan?"
    show Raven Before Diam
    rb "{cps=25}........"
    show Nita Casual Berbicara
    t "{cps=25}tadi..{w=.5}aku melihat kamu jatuh dari lantai 3"
    show Nita Casual Bertanya
    t "{cps=25}tapi {w=.5} kamu tidak apa-apa, kan?"
    show Raven Before Bicara
    rb "{cps=25}begitu ya.."
    show Raven Before Males
    rb "{cps=25}lagi-lagi aku gagal, ya"
    rb "{cps=25}kenapa aku sangat sulit untuk mati, ya Tuhan.."
    t "{cps=25}hah? apa maksudmu?"
    show Raven Before Bicara
    rb "{cps=25}aku-"
    show Nita Casual Khawatir1
    t "{cps=25}jangan bilang, kamu bunuh diri?"
    show Raven Before Males
    rb "{cps=25}ya begitulah"
    show Raven Before Diam
    rb "{cps=25}{i}'kepalaku sepertinya memar'{/i}"
        
    "untuk memastikan, Raven meraba belakang kepalanya"
        
    show Raven Rumahan Murung
    rb "{cps=25}aww........."
    rb "{cps=25}{i}'memang memar..'{/i}"
    t "{cps=25}kau tidak apa-apa, kan?"
    show Raven Before Bicara
    rb "{cps=25}lalu... {w=.5}kamu siapa?"
    show Nita Casual Berbicara
    t "{cps=25}aku...{b}Nita{/b}"
    show Nita Casual Bertanya
    N "{cps=25}kau benar-benar tidak apa-apa, kan?"

    jump choice3_done

label choice3_siapa:

    $ menu_flag = False
    show Raven Before Bicara
    rb "{cps=25}um....{w=.5}kamu siapa?"
    hide Nita Casual Khawatir
    show Nita Casual Berbicara
    t "{cps=25}aku {b}Nita{/b}"
    rb "{cps=25}{i}'namanya Nita, ya.......'{/i}"
    hide Nita Casual Berbicara
    show Nita Casual Khawatir
    N "{cps=25}aku melihat kamu terjatuh dari lantai 3"
    hide Nita Casual Khawatir
    show Nita Casual Bertanya
    N "{cps=25}kau tidak apa-apa, kan?"
    rb "{cps=25}begitu ya.."
    rb "{cps=25}lagi-lagi aku gagal, ya"
    rb "{cps=25}kenapa aku sangat sulit untuk mati, ya Tuhan.."
    hide Nita Casual Bertanya
    show Nita Casual Khawatir
    N "{cps=25}hah? apa maksudmu?"
    rb "{cps=25}aku-"
    show Nita Casual Khawatir1
    N "{cps=25}jangan bilang.....{w} kamu bunuh diri?"
    rb "{cps=25}ya begitulah"
    show Raven Before Diam
    rb "{cps=25}{i}'kepalaku sepertinya memar'{/i}"
        
    "untuk memastikan, Raven meraba belakang kepalanya"
        
    rb "{cps=25}aww...!"
    rb "{cps=25}{i}'memang memar..'{/i}"
    show Nita Casual Khawatir
    t "{cps=25}kau tidak apa-apa, kan?"
        
    jump choice3_done

label choice3_done:
    show Raven Before Bicara
    rb "{cps=25}maaf membuatmu khawatir"
    rb "{cps=25}tapi, aku baik-baik saja"
    rb "{cps=25}terimakasih ya, Nita"
    "{cps=25}setelah mengucapkan terima kasih, Raven beranjak dari situ meninggalkan Nita"
    show Nita Casual Bertanya
    N "{cps=25}heh?"
    show Nita Casual Khawatir
    N "{cps=25}hey...tunggu dulu"
    hide Nita Casual Khawatir
    "{cps=25}Raven mengabaikan Nita dengan terus berjalan menjauhinya"
    scene bg Jalan Malam with fade
    rb "{cps=25}lompat dari gedung pun tidak bisa, ya"
    rb "{cps=25}aw..."
    rb "{cps=25}walaupun aku lompat dari lantai 3"
    show Raven Before Bicara
    rb "{cps=25}aku tak apa-apa, hanya kepala saja yang memar"
    rb "{cps=25}tapi, tetap saja kepalaku masih sakit"
    "{cps=25}sementara Raven berjalan sambil merenung"
    "{cps=25}ia menyadari, ada yang membuntutinya"
    rb "{cps=25}siapa disana?"
    "{cps=25}orang itu menunjukkan dirinya"
    show Nita Casual Beralasan with dissolve
    pause (2)
    N "{cps=25}um....."
    rb "{cps=25}kenapa kamu mengikutiku?"
    N "{cps=25}eh..{w=.5}um..."
    N "{cps=25}aku hanya khawatir padamu"
    show Nita Casual Berbicara
    N "{cps=25}mungkin saja kamu pingsan atau semacamnya"
    rb "{cps=25}aku baik-baik saja, jadi kamu tak perlu mengikutiku"
    show Nita Casual Khawatir1
    N "{cps=25}tapi-"
    rb "{cps=25}tapi apa?"
    rb "{cps=25}sudah kubilang, aku baik-baik aja"
    N "{cps=25}tapi{w=.5}, mungkin saja kamu masih mencoba bunuh diri"
    rb "{cps=25}hadeh...{w=.5}jadi gitu, ya"
    rb "{cps=25}aku janji gak buat lagi"
    rb "{cps=25}PUAS?"
    rb "{cps=25}aku mau pulang ke rumahku, jadi kau tak perlu mengikutiku lagi"
    rb "{cps=25}bye....."
    hide Nita Casual Khawatir1
    "{cps=25}Raven mempercepat langkahnya agar menjauh darinya"
    "{cps=25}tapi{w}, Nita tetap mengikutinya"
    "{cps=25}semakin cepat langkah Raven berusaha menjauhinya"
    "{cps=25}Nita pun semakin mempercepat langkahnya mengikuti Raven"
    "{cps=25}tentu saja, Raven sangat terganggu dengannya"
    show Raven Before Diam
    
    menu:
        rb "{cps=10}..........."
        "mengancamnya":
            
            jump choice4_ancam

        "mengabaikannya":
            jump choice4_abaikan

    label choice4_ancam:
    
        $ menu_flag = False
        
        show Raven Before Bicara
        rb "{cps=25}lebih baik kamu berhenti sekarang"
        "{cps=25}Raven mengeluarkan hpnya dari kantong"
        show Raven Rumahan Menelpon
        rb "{cps=25}atau aku nanti telpon polisi"
        show Nita Casual Khawatir
        N "{cps=25}atas dasar tuduhan?"
        rb "{cps=25}menguntit"
        show Nita Casual Ejek
        N "{cps=25}haha.. coba saja kalau berani"
        rb "{cps=25}{i}'nih orang nantang?'{/i}"
        show Nita Casual Mengejek
        N "{cps=25}lagi pula, aku juga akan beritahu ke polisi"
        N "{cps=25}bahwa kamu sedang mencoba bunuh diri"
        N "{cps=25}dan kau pun terpidana, hahahaha..."
        rb "{cps=25}{i}'cih{w}, nih orang cerdik juga'{/i}"
        rb "{cps=25}{i}'tapi, senyumannya bikin kesel'{/i}"
        "{cps=25}Raven urungkan niatnya, ia menyimpan kembali hp ke kantongnya"
        show Raven Before Bicara
        rb "{cps=25}terserah kau, dah"
        hide Nita Casual Mengejek
        "{cps=25}Raven pun melanjutkan perjalan ke rumahnya bersama Nita"
        
        jump choice4_done

    label choice4_abaikan:

        $ menu_flag = False
        show Raven Before Males
        rb "{cps=25}{i}'abaikan aja, nanti dia capek sendiri'{/i}"
        "{cps=25}Raven mengabaikannya, berharap Nita nanti tidak mengikutinya lagi"
        
        jump choice4_done

    label choice4_done:
    
    show Nita Casual Berbicara
    N "{cps=25}hey...{w=.5}dimana rumahmu?"
    show Raven Before Bicara
    rb "sedikit lagi sampai"
    hide Nita Casual Berbicara
    "tak perlu langkah banyak, sampailah mereka di rumah Raven"
    
    scene bg R_Home03 with dissolve
    rb "{cps=25}inilah rumahku"
    show Nita Casual Bertanya
    N "wow.."
    hide Nita Casual Bertanya
    "{cps=25}Raven hendak membuka pintu dan ingin masuk rumah"
    rb "{cps=25}aku sudah sampai dengan selamat"
    show Nita Casual Berbicara
    rb "{cps=25}jadi, kau boleh pulang sekarang"
    show Nita Casual Beralasan
    N "{cps=25}aku{w}, tak punya rumah"
    rb "{cps=25}hah?"
    N "{cps=25}boleh, aku menginap di rumahmu?"
    show Raven Before Diam
    rb "{cps=25}........"
    show Nita Casual Berbicara
    N "{cps=25}........."
    show Raven Before Bicara
    rb "{cps=25}gak!"
    "{cps=25}Raven langsung menutup pintu rumahnya"
    hide Nita Casual Berbicara
    "{cps=25}tapi ditahan Nita, sehingga pintunya setengah tertutup"
    show Nita Casual Khawatir1
    N "{cps=25}kumohon padamu"
    rb "{cps=25}gak!"
    N "{cps=25}kumohon..."
    show Raven Before Males
    rb "{cps=25}GAK!"
    N "{cps=25}hanya 1 malam saja"
    show Raven Before Bicara
    rb "{cps=25}apaan sih, aku bilang gak, ya gak"
    show Nita Casual Beralasan
    N "{cps=25}aku baru saja tiba disini"
    N "{cps=25}aku tak tau harus tidur dimana"
    
    "{cps=25}Raven yang bersikeras, akhirnya tergerak hatinya"
    hide Nita Casual Beralasan
    show Raven Before Diam
    rb "{cps=25}........"
    "{cps=25}Raven membuka pintu dan membiarkan Nita masuk"
    show Raven Before Males
    rb "{cps=25}maaf rumahku agak berantakan"
    show Nita Casual Berbicara
    N "{cps=25}....."
    "{cps=25}Nita hanya membalas dengan senyuman"
    show Raven Before Bicara
    rb "{cps=25}aku tak punya kamar kosong"
    rb "{cps=25}jadi, kamu hanya bisa tidur di ruang tamu"
    N "{cps=25}hmm, terima kasih"
    N "{cps=25}itu saja sudah cukup"
    play sound "Sound Effect/001-Nita Lapar.mp3"
    "{cps=25}bunyi perut keroncongannya Nita terdengar"
    show Nita Casual Beralasan
    N "{cps=25}........"
    show Raven Before Diam
    rb "{cps=25}......."
    show Raven Before Bicara
    rb "{cps=25}um...{w=.5}aku hanya punya mie cup instan"
    rb "{cps=25}tunggu, aku buatkan"
    show Nita Casual Berbicara
    N "{cps=25}hmmm...{w=.5}terima kasih"
    show Raven Before Diam
    rb "{cps=25}....."
    hide Nita Casual Berbicara
    "{cps=25}Raven pergi ke dapur, kemudian membuat mie cup instan"
    "{cps=25}semenara menunggu mie matang, Raven merenung sejenak"
    show Raven Rumahan Berpikir
    rb "{cps=25}{i}'tunggu dulu...'{/i}"
    rb "{cps=25}{i}'bukanya agak aneh, kalau membiarkan orang asing menginap ke dalam rumah'{/i}"
    rb "{cps=25}{i}'walaupun hanya 1 malam, tapi tetap aneh kan?'{/i}"
    rb "{cps=25}{i}'apa lagi dia cewek'{/i}"
    rb "{cps=25}{i}'apa kata tetangga nanti'{/i}"
    rb "{cps=25}{i}'tapi kan, dia tidak punya rumah'{/i}"
    show Raven Before Diam
    rb "{cps=25}{i}'lagi pula kita juga agak berisik tadi{w=.5}, hanya gara-gara rebutan pintu doang'{/i}"
    show Raven Rumahan Murung
    rb "{cps=25}{i}'kalau kita masih ribut, bakal lebih runyam lagi'{/i}"
    rb "{cps=25}.................."
    show Raven Before Diam
    rb "{cps=25}{i}'sekarang pertanyaannya adalah'{/i}"
    rb "{cps=25}{i}'apakah orang ini bisa dipercaya?'{/i}"
    rb "{cps=25}{i}'ah... bodoh amat'{/i}"
    rb "{cps=25}{i}'tidak ada barang berharga dirumah ini'{/i}"
    "{cps=25}{i}{b}'beep beep'{/b}{/i}"
    "{cps=25}bunyi timer, menandakan sudah 3 menit berlalu dan mienya sudah matang"
    show Raven Before Bicara
    rb "{cps=25}baiklah, sudah matang"
    "{cps=25}Raven membawa mie cup tersebut ke ruang tamu"
    "{cps=25}ia melihat Nita sedang duduk manis, layaknya tamu sedang menunggu sajian dari tuan rumah"
    "{cps=25}saat Raven sedang membawa mie cupnya, mata Nita sangat besinar"
    "{cps=25}seolah-olah ia sedang melihat malaikat pembawa makanan"
    show Raven Before Diam
    rb "{cps=25}......"
    "{cps=25}tapi, tatapan Nita membuat Raven merasa agak risih"
    show Raven Before Bicara
    rb "{cps=25}um....{w}kau mau rasa soto, atau rasa kari?"
    "{cps=25}Raven menawarkan rasa dari 2 mie cup di pegangnya"
    show Nita Casual Berbicara
    N "{cps=25}kalau begitu rasa kari."
    "{cps=25}Raven memberikan mie cup rasa kari dari tanggan kirinya"
    rb "{cps=25}maaf, tangan kiri"
    N "{cps=25}mm..{w=.5}terima kasih"
    hide Nita Casual Berbicara
    "{cps=25}mereka akhirnya menikmati mie cup bersama"
    "{cps=25}walaupun hanya menyantap mie instan, tapi Raven merasakan sesuatu"
    "{cps=25}suatu yang membuat dia sangat bernostalgia"
    "{cps=25}yaitu{w}, makan bersama"
    "{cps=25}tanpa sadar, air mata Raven mengalir di pipinya"
    show Nita Casual Bertanya
    N "{cps=25}kamu nanggis?"
    "{cps=25}rupanya Nita menyadarinya"
    show Raven Before Males
    rb "{cps=25}gak kok, cuma kelilipan uap panas"
    "{cps=25}Raven mengusap air mata"
    N "{cps=25}ngomong-ngomong orang tuamu dimana?"
    rb "{cps=25}telah tiada, aku sendiri saja disini"
    hide Nita Casual Bertanya
    N "{cps=25}......"
    show Nita Casual Berbicara
    N "{cps=25}kamu tadi nangis, karena rindu mereka ya"
    rb "{cps=25}sudah kubilang kan, tadi hanya kelilipan uap panas"
    show Nita Casual Khawatir
    N "{cps=25}jangan bohong kamu, aku tahu air mata seperti itu-"
    N "{cps=25}air mata kerinduan terhadap sesuatu"
    show Raven Before Diam
    rb "{cps=25}.........."
    show Nita Casual Berbicara
    N "{cps=25}kamu rindu mereka, ya"
    show Raven Before Bicara
    rb "{cps=25}sudah lama aku tidak pernah makan bersama, selama ini hanya sendirian"
    rb "{cps=25}ah.. tentu saja aku juga merindukan mereka"
    hide Nita Casual Berbicara
    "{cps=25}Raven mempercepat proses makannya, hingga habis duluan"
    show Nita Casual Berbicara
    N "{cps=25}begitu ya"
    N "{cps=25}selama ini kamu sendirian ya"
    show Raven Before Diam
    rb "{cps=25}......."
    show Raven Before Bicara
    rb "{cps=25}apa maksudmu kalau aku sendirian?"
    show Nita Casual Khawatir
    N "{cps=25}ah.. aku tidak maksud aneh-aneh kok"
    "{cps=25}Nita menyelesaikan makanannya."
    show Nita Casual Berbicara
    N "{cps=25}ah... leganya, soalnya aku belum makan seharian"
    rb "{cps=25}um...{w}perlu kubuatkan mie lagi?"
    N "{cps=25}ah tidak perlu, satu aja cukup kok"
    N "{cps=25}terima kasih ya"
    "{cps=25}dengan tersenyum, Nita memberikan cup kosong untuk dibuang Raven"
    rb "{cps=25}kamu bisa tidur di sofa kan?"
    N "{cps=25}ah aman, intinya aku bisa tidur"
    show Nita Casual Khawatir
    N "{cps=25}oh iya, ulurkan tanganmu"
    rb "{cps=25}hah?"
    "{cps=25}Raven mengulurkan tangan, lalu Nita memberikan sebuah benda"
    "{cps=25}sebuah jam berwarna silver"
    rb "{cps=25}apa ini?"
    show Nita Casual Berbicara
    N "{cps=25}ungkapan terima kasih dariku"
    rb "{cps=25}gak perlu"
    N "{cps=25}udah, ambil saja"
    show Nita Casual Mengejek
    N "{cps=25}mungkin saja ini bisa membantumu"
    rb "{cps=25}um..{w=.5} baiklah, terima kasih"
    hide Nita Casual Mengejek
    "{cps=25}Raven menyimpan jam itu di kantongnya"
    "{cps=25}setelah Raven membuang sampah, ia ke kamarnya"
    scene bg Raven Room Before
    "{cps=25}ia berbaring di kasurnya, berusaha tidur"
    show Raven Rumahan Berpikir
    rb "{cps=25}........"
    "{cps=25}tapi ia tak bisa tidur, karena masih penasaran benda pemberian Nita"
    "{cps=25}ia beranjak dari kasurnya, mengambil benda itu"
    show Raven Before Bicara
    rb "{cps=25}sebenarnya ini jam mahal atau apa?"
    rb "{cps=25}apa maksudnya bisa membantu?"
    "{cps=25}sementara memegang benda itu, Raven melihat ada suatu tombol"
    "{cps=25}ia pun menekan tombol itu"
    show Raven Rumahan Murung
    rb "{cps=25}aw..."
    "{cps=25}rupanya tombol itu ada jarum, sehingga membuat jempolnya tertusuk dan berdarah"
    show Raven Before Bicara
    rb "{cps=25}benda apa ini?"
    rb "{cps=25}jangan-jangan.."
    "{cps=25}karena rasa curiga yang berlebihan, Raven keluar dari kamarnya"
    "{cps=25}dan hendak mencari Nita"
    scene bg Raven House01
    rb "{cps=25}Nita....{w=.5}Nita"
    "{cps=25}tapi, Nita sudah tidak ada di ruang tamu"
    rb "{cps=25}benda apa yang kau berikan padaku?"
    
    rb "{cps=25}dimana dia?"
    "{cps=25}pandangan Raven mulai memudar"
    "{cps=25}Raven kehilangan keseimbangan, sehingga ia terjatuh"
    play sound "Sound Effect/009-Raven Terjatuh.mp3"
    "{cps=25}kesadaran Raven mulai diambang batas"
    show Raven Rumahan Terdiam
    rb "{cps=25}{i}'ah.. mungkin aku mati?'{/i}"
    N "{cps=25}maaf Raven"
    rb "{cps=25}{i}'tapi, kenapa ini?'{/i}"
    rb "{cps=25}{i}'perasaan apa ini?'{/i}"
    rb "{cps=25}{i}'apa aku takut mati?'{/i}"
    rb "{cps=25}{i}'ya benar, aku takut mati'{/i}"
    rb "{cps=25}aku tidak mau mati"
    rb "{cps=25}aku takut"
    rb "{cps=25}aku-......."
    "{cps=25}............."
    stop music fadeout 1
    call screen ask_chapter0_done
    screen ask_chapter0_done:
        fixed:
            text "Chapter Prolog Selesai" xalign 0.5 yalign 0.3
            ##textbutton "Save" xalign 0.33 yalign 0.5 action QuickSave()
            textbutton "Save" xalign 0.33 yalign 0.5 action ShowMenu("save")
            textbutton "Lanjutkan Chapter 1" xalign 0.66 yalign 0.5 action Return(True)
            textbutton "Keluar Main Menu" xalign 0.5 yalign 0.65 action MainMenu()
return