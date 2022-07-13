label Chapter1A:

scene bg blck
"{cps=25}sampailah Raven di bus stop yang tak jauh dengan rumah Mei"
"{cps=25}Raven turun dari bus, dan pergi ke rumah Mei"
scene bg Mei House with dissolve
play music "BGM/005-Mei House-himatubusi.mp3" fadeout 1
"{cps=25}Sampailah ia di tempat tujuannya"
"{cps=25}dan kini, Raven tepat di depan rumahnya Mei"
"{cps=15}.............{w}...................{w}............"
"{cps=25}hampir 5 menit lebih, Raven berdiri menunggu Mei keluar dari rumahnya"

"{cps=25}tapi Mei tak kunjung keluar"
show Raven Sekolah Diam
rb "{cps=25}um..."
rb "{cps=25}biasanya jam segini, Mei berangkat ke sekolah"
rb "{cps=25}tapi kok...."
rb "{cps=25}hmmmm........"
show Raven Sekolah Berpikir

menu:
        rb "{cps=25}apa yang harus aku lakukan?"
    
        "Menunggu sedikit lagi":
            show Raven Sekolah Diam
            rb "{cps=25}{i}'mungkin aku menunggu sedikit lagi'{/i}"
            jump choice7_tunggu

        "berteriak memanggilnya":
            show Raven Sekolah Terkejut
            rb "{cps=25}MEI!!"
            rb "{cps=25}HALLO MEI!!"
            rb "{cps=25}INI AKU RAVEN!!"
            rb "{cps=25}AYO KE SEKOLAH BARENG!!"
            show Raven Sekolah Murung
            rb "{cps=25}......................."
            jump choice7_nohome
            
        "membunyikan bell rumah":
            "{cps=25}Raven berniat membunyikan bell rumah"
            show Raven Sekolah Diam
            play sound "Sound Effect/002-Bell Rumah Mei.mp3"
            "{cps=25}.........{w}.............."
            show Raven Sekolah Berbicara
            rb "{cps=25}Mei?"
            play sound "Sound Effect/002-Bell Rumah Mei.mp3"
            rb "{cps=25}ini aku, yuk pergi bareng"
            show Raven Sekolah Diam
            play sound "Sound Effect/002-Bell Rumah Mei.mp3"
            "{cps=25}.............."
            show Raven Sekolah Berbicara
            rb "{cps=25}Mei?"        
            jump choice7_nohome

label choice7_tunggu:
$ menu_flag = False
        
"{cps=25}Raven memutuskan untuk menunggunya"
"{cps=25}walaupun waktu sudah menunjukan pukul 7:00"
"{cps=25}tapi, Raven tetap menunggunya"
"{cps=25}10 menit berlalu.."
"{cps=25}ada seorang ibu yang sedang memegang belanjaan, datang menghampiri Raven"
show Tante Rika Bertanya
t "{cps=25}Raven?!"
show Raven Sekolah Diam
rb "{cps=25}......?!"
show Raven Sekolah Berbicara
rb "{cps=25}eh tante, Pagi tante"
"{cps=25}rupanya itu adalah Tante Rikka"
"{cps=25}Ibunya Mei"
show Tante Rika Ramah
r "{cps=25}selamat pagi, jemput Mei?"
show Raven Sekolah Tersenyum
rb "{cps=25}iya tante"
rb "{cps=25}tapi, Mei belum keluar juga dari tadi"
show Tante Rika Berbicara
r "{cps=25}ya memang, karena Mei udah berangkat dari tadi"
r "{cps=25}sebelum tante ke pasar"
show Raven Sekolah Terkejut
rb "{cps=25}eh?!!, dari tadi?"
show Tante Rika Bertanya
r "{cps=25}iya, katanya ada urusan penting di perpus"
show Raven Sekolah Murung
rb "{cps=25}begitu ya.."
show Raven Sekolah Berbicara
rb "{cps=25}terima kasih tante, mari aku bantu bawa barang berlanjaannya"
show Tante Rika Ramah
r "{cps=25}ah tidak apa-apa, ini tidak terlalu banyak kok"
show Tante Rika Berbicara
r "{cps=25}lagipula, bukannya kamu sudah telat?"
show Raven Sekolah Tersenyum
rb "{cps=25}eh iya betul, kalau begitu saya permisi dulu"
show Tante Rika Ramah
r "{cps=25}ya silahkan"
show Tante Rika Bertanya
r "{cps=25}oh iya......"
show Tante Rika Ramah
r "{cps=25}selamat ulang tahun Raven"
show Raven Sekolah Tersenyum
rb "{cps=25}terima kasih tante"
hide Tante Rika Ramah
stop music fadeout 1
scene bg Bus Stop1 with slideright
"{cps=25}Raven menuju ke bus stop, dan menunggu bus sekolah yang lewat"
show Raven Sekolah Murung
rb "{cps=25}{i}'bukannya ini sedikit aneh?'{/i}"
rb "{cps=25}{i}'aku sudah menunggu Mei dari jam setengah 7 loh..'{/i}"
show Raven Sekolah Berpikir
rb "{cps=25}{i}'tapi Mei sudah berangkat dari tadi'{/i}"
rb "{cps=25}{i}'urusan macam apa, sehingga ia berangkat lebih awal?'{/i}"
rb "{cps=25}{i}'lagi pula, ia berangkat dengan apa?'{/i}"
rb "{cps=25}{i}'kalau bus sekolah, seharusnya kita bertemu di bus tadi'{/i}"
show Raven Sekolah Murung
rb "{cps=25}{i}'jangan bilang, aku tidak memperhatikannya'{/i}"
rb "{cps=25}{i}'kalau tadi kita satu bus..'{/i}"
show Raven Sekolah Berpikir
rb "{cps=25}{i}'ah,,, bodohnya aku'{/i}"
show Raven Sekolah Murung
rb "{cps=25}{i}'dan juga, lebih aneh lagi'{/i}"
rb "{cps=25}{i}'dari tadi, bus satupun tidak ada yang lewat'{/i}"
rb "{cps=25}{i}'baru udah telat lagi..'{/i}"
"{cps=25}Raven membuang pandangannya sedikit, ia melihat ada pangkalan ojek disitu"
show Raven Sekolah Diam
rb "{cps=25}{i}'apa aku harus menggunakan tukang ojek aja?'{/i}"
show Raven Sekolah Murung
rb "{cps=25}{i}'tapi, uangku pas-pasan'{/i}"
rb "{cps=25}{i}'tidak cukup nanti untuk jajan, maupun pulang nanti'{/i}"
    
menu:
    "{cps=25}apa yang harus dilakukan?"
    
    "ojek, biar cepat":
        jump choice8_ojek

    "berjalan kaki, biar hemat":
        jump choice8_jalan

label choice8_ojek:
$ menu_flag = False
show Raven Sekolah Berpikir        
rb "{cps=25}hm..."
show Raven Sekolah Diam
rb "{cps=25}dari pada saya terlambat"
"{cps=25}Raven memutuskan untuk menggunakan tukang ojek"
scene bg blck
"{cps=25}tak perlu waktu lama"        
jump sekolah

        
label choice8_jalan:
$ menu_flag = True
show Raven Sekolah Diam
rb "{cps=25}lebih baik, saya jalan kaki aja"
rb "{cps=25}dari pada aku tak bisa pulang"
rb "{cps=25}lagipula, jarak sekolah tidak jauh amat"
scene bg blck with fade
"{cps=25}Raven memutuskan untuk berjalan kaki sampai ke sekolah"
scene bg Sekolah Tutup
"{cps=25}sampailah ia di sekolah"
"{cps=25}tapi, gerbang sekolah sudah tutup"
"{cps=25}tandanya ia sudah terlambat dan tak bisa masuk sekolah lagi"
show Raven Sekolah Berbicara Datar
rb "{cps=25}sial..."
jump choice8_done

label choice8_done:
menu:
    "{cps=25}apa yang harus dilakukan?"
    
    "Pulang saja":
        jump choice9_pulang

    "Memanggil bantuan":
        jump choice9_bantuan

label choice9_pulang:
$ menu_flag = False
show Raven Sekolah Berpikir        
rb "{cps=25}hm..."
show Raven Sekolah Murung
rb "{cps=25}lebih baik aku pulang saja"
scene bg blck
"{cps=25}Raven memutuskan untuk pulang ke rumahnya"
jump pulang
            
label choice9_bantuan:

$ menu_flag = False
        
show Raven Sekolah Diam
rb "{cps=25}hm..."
rb "{cps=25}mungkin aku bisa memanggil bantuan mereka"
    
"{cps=25}Raven mengeluarkan ponselnya, untuk memanggil bantuan temannya"
show Raven Sekolah MainHp
rb "{cps=25}tapi siapa ya?"
menu:
    "{cps=25}siapa yang harus kupanggil?"
    
    "Memanggil Mei":
        "{cps=25}Raven mencari kontak Mei, lalu menelponya"
        "{cps=25}.........{w}........."
        "{cps=25}.........{w}........."
        "{cps=25}namun Mei tidak mengangkatnya"
        rb "{cps=25}um..."
        show Raven Sekolah Murung
        rb "{cps=25}sebaiknya aku pulang saja"
        "{cps=25}Raven memutuskan untuk pulang saja"
        jump pulang

    "Memanggil Aston":
        "{cps=25}Raven mencari kontak Aston, lalu menelponya"
        "{cps=25}............{w}.........."
        "{cps=25}............{w}.........."
        a "{cps=25}hallo...?"
        rb "{cps=25}Aston?"
        a "{cps=25}ya.. kenapa Raven?"
        a "{cps=25}aku sedang dikelas nih"
        rb "{cps=25}aku butuh bantuanmu. aku ter-"
        rb "{cps=25}hallo.... hallo... Aston?"
        show Raven Sekolah Murung
        rb "{cps=25}yah...{w=.5}putus"
        rb "{cps=25}sepertinya, aku memang tak bisa masuk lagi"
        rb "{cps=25}sebaiknya aku pulang saja"
        "{cps=25}Raven memutuskan untuk pulang saja"
        jump pulang
            
    "Memanggil Astrid":
        jump choice10_bantuan

label choice10_bantuan:
$ menu_flag = False
        
"{cps=25}Raven mencari kontak Astrid, lalu menelponya"
"{cps=25}...........{w}............"
"{cps=25}...........{w}............."
As "{cps=25}Hallo..Raven?"
As "{cps=25}ada apa?"
As "{cps=25}kamu gak sekolah?"
rb "{cps=25}Asrid, dengarkan aku.."
rb "{cps=25}aku butuh bantuanmu"
As "{cps=25}heh?..kau kenapa?"
rb "{cps=25}aku terlambat, dan aku terkunci diluar sekolah nih"
rb "{cps=25}bisakah kamu membantuku?"
As "{cps=25}huf... kirain apaan, cuma terlambat doang"
As "{cps=25}kau membuatku cemas saja"
rb "{cps=25}hah?....apa yang membuatmu cemas?"
As "{cps=25}aku pikir kamu-"
As "{cps=25}ah.. sudah, lupakan..!!"
As "{cps=25}kamu ke belakang sekolah sekarang."
As "{cps=25}aku akan membantumu disana"
As "{cps=25}sudah ya.. bye.."
rb "{cps=25}baiklah, terima-"
rb "{cps=25}hallo?.. hallo?"
"{cps=25}Astrid memutuskan panggilannya.."
show Raven Sekolah Berbicara
rb "{cps=25}aku harus ke belakang sekolah sekarang"
"{cps=25}Raven menuju ke belakang sekolah, sesuai intruksi Astrid"


scene bg Belakang Sekolah
play music "BGM/007-With Astrid-haru no kyousitu.mp3" fadeout 1
"{cps=25}sesampainya disana, Raven melihat Astrid yang sedang menunggunya dari atas pagar tembok itu"
show Raven Sekolah Terkejut
rb "{cps=25}bagaimana kamu bisa sampai disitu, bukannya itu lumayan tinggi?"
show Astrid Sekolah Berbicara
As "{cps=25}ah.. sudahlah, buruan lempar tasmu"
show Raven Sekolah Berbicara
rb "{cps=25}baiklah"
"{cps=25}Raven mengoper tasnya ke Astrid"
As "{cps=25}hup..!"
hide Astrid Sekolah Berbicara
"{cps=25}setelah menangkap tasnya Raven, Astrid mengulurkan tangannya"
rb "{cps=25}aku bisa kok"
show Astrid Sekolah Tersenyum
As "{cps=25}baiklah, buruan..."
hide Astrid Sekolah Tersenyum
"{cps=25}Raven mengambil ancang-ancang. kemudian melompat berusaha menggapai tembok yang lumayan tinggi itu"
"{cps=25}setelah ia menggapainya, Raven mengangkat tubuhnya berusaha menaiki tembok itu"
"{cps=25}dengan hati-hati Raven mendarat keseberang tembok"
show Raven Sekolah Tersenyum
rb "{cps=25}fiuh... ternyata aku lumayan atletik"
show Astrid Sekolah Berbicara
As "{cps=25}atletik apaan, cuman naik tembok segitu doang"
rb "{cps=25}biarkan aku memuji diriku sendiri."
show Astrid Sekolah Tersenyum
As "{cps=25}iya..iyadeh"
show Astrid Sekolah Berbicara
As "{cps=25}yuk pergi dari sini, sebelum guru menemukan kita"
rb "{cps=25}ah benar juga..."
hide Astrid Sekolah Berbicara
"{cps=25}Raven dan Astrid beranjak dari tempat itu"
jump tertangkap
          
label tertangkap:
scene bg Lorong Kelas Raven with fade
"{cps=25}saat menuju ke kelasnya, Mereka bertemu Pak Agus yang sedang piket saat itu"
show Pak Agus Marah
pa "{cps=25}nah loh, kalian dari mana?"
hide Pak Agus Marah
show Astrid Sekolah Terkejut
As "{cps=25}anu.. pak"
hide Astrid Sekolah Terkejut
show Pak Agus Menatap
pa "{cps=25}lalu kamu dari mana Raven, sambil bawa tas gitu?"
show Raven Sekolah Berpikir
menu:
    rb "{cps=25}um....."
    
    "Mengaku Terlambat":
        show Raven Sekolah Terkejut
        rb "{cps=25}um... sebenarnya pak"
        rb "{cps=25}aku terlambat, dan terkunci diluar"
        show Pak Agus Menatap
        pa "{cps=25}lalu?"
        show Raven Sekolah Beralasan
        rb "{cps=25}um...{w=.5} aku memaksa masuk dengan naik dari pagar belakang pak"
        hide Pak Agus Menatap
        show Astrid Sekolah Terkejut
        As "{cps=25}oi Raven!"
        hide Astrid Sekolah Terkejut
        show Pak Agus Menatap
        pa "{cps=25}lalu Astrid?"
        hide Pak Agus Menatap
        show Raven Sekolah Murung
        show Astrid Sekolah Terkejut
        As "{cps=25}anu-........."
        hide Astrid Sekolah Terkejut
        rb "{cps=25}aku meminta Astrid untuk membantuku, pak"
        rb "{cps=25}aku tau ini salah, tapi kumohon pak"
        "{cps=25}Raven menundukan kepala, tanda memohon kepada Pak Agus"
        show Raven Sekolah Terkejut
        rb "{cps=25}jangan hukum Astrid, ia hanya terlibat karena aku yang memintanya"
        rb "{cps=25}sebagai gantinya hukum aku 2x lipat, pak"
        rb "{cps=25}kumohon..."
        show Pak Agus Menatap
        pa "{cps=25}heee...?!{w=.5}kenapa kamu sangat melindunginya?"
        show Pak Agus Berbicara
        pa "{cps=25}apa kalian berdua pacaran?"
        hide Pak Agus Berbicara
        show Astrid Sekolah Malu
        As "{cps=25}GAK KOK!"
        rb "{cps=25}bukan kok pak"
        hide Astrid Sekolah Malu
        show Pak Agus Berbicara
        pa "{cps=25}mm...begitu ya"
        pa "{cps=25}kalau begitu,{w} Astrid!"
        hide Pak Agus Berbicara
        show Astrid Sekolah Malu Malu
        As "{cps=25}ya pak?"
        hide Astrid Sekolah Malu Malu
        show Pak Agus Berbicara
        pa "{cps=25}kembali ke kelasmu,{w} dan Raven"
        show Pak Agus Menatap
        pa "{cps=25}ikutlah denganku"
        rb "{cps=25}baik pak"
        hide Pak Agus Menatap
        "{cps=25}Astrid Kembali Ke kelas"        
        "{cps=25}Sedangkan"        
        scene bg Gudang with dissolve
        "{cps=25}Pak Agus membawa Raven ke gudang sekolah"        
        show Pak Agus Berbicara
        pa "{cps=25}inilah hukumanmu"
        show Raven Sekolah Berbicara
        rb "{cps=25}um... maksudnya pak?"
        pa "{cps=25}kamu bersihkan gudang ini, dan juga rapikan benda-benda disini"
        show Raven Sekolah Terkejut
        rb "{cps=25}heh? semuanya?, dengan debu setebal ini?"
        show Pak Agus Menatap
        pa "{cps=25}lah bukannya kamu minta hukumanmu 2x lipat?"
        show Raven Sekolah Berpikir
        rb "{cps=25}{i}'ah benar juga, ah bodohnya aku'{/i}"
        show Raven Sekolah Berbicara
        rb "{cps=25}baiklah pak"
        show Pak Agus Berbicara
        pa "{cps=25}pokoknya bersih ya, saya pergi dulu"
        rb "{cps=25}baik pak"
        hide Pak Agus Berbicara with moveoutleft
        "{cps=25}Pak Agus pergi meninggalkan Raven"
        rb "{cps=25}well... hadiah terbaik yang aku terima dihari ultahku"
        "{cps=25}Raven mulai membersihkan gudang itu, sendirian"
        "{cps=25}10 menit kemudian"
        "{cps=25}Raven yang tengah kewalahan membersihkan gudang itu sendirian"
        show Astrid Sekolah Berbicara
        As "{cps=25}butuh bantuan?"
        hide Astrid Sekolah Berbicara
        "{cps=25}Astrid yang sedang berdiri di pintu, menawarkan bantuan"
        rb "{cps=25}tidak perlu, ini hukumanku"
        show Astrid Sekolah Berbicara
        As "{cps=25}huufft...bagaimanapun juga ini salahku"
        As "{cps=25}dan juga, aku lagi ngangur"
        rb "{cps=25}jangan bilang, kamu lagi dihukum berdiri diluar?"
        show Astrid Sekolah Tersenyum
        As "{cps=25}ya.. begitulah"
        show Raven Sekolah Tersenyum
        rb "{cps=25}kalau begitu, nih"
        "{cps=25}Raven memberikan sapu ke Astrid"
        hide Astrid Sekolah Tersenyum
        "{cps=25}Raven dan Astrid sama-sama membersihkan gudang itu"
        "{cps=25}karena mereka berkerja sama, maka gudang itu dapat bersih dengan cepat"
        show Raven Sekolah Berbicara
        rb "{cps=25}well.. sudah bersih, tinggal merapikannya saja"
        show Astrid Sekolah Terkejut
        As "{cps=25}merapikan?, bukannya hanya bersihkan?"
        rb "{cps=25}kata Pak Agus gitu sih"
        As "{cps=25}semuanya?"
        rb "{cps=25}yup, katanya ini hukumanku yang 2x lipat"
        show Astrid Sekolah Berbicara
        As "{cps=25}muke gile, kamu disuruh kerja sendirian kek gini"
        rb "{cps=25}ya begitulah, tapi kau sudah datang membantuku"
        rb "{cps=25}sehingga jadi agak ringan"
        show Raven Sekolah Tersenyum
        rb "{cps=25}terimakasih ya, sudah mau membantuku"
        show Astrid Sekolah Malu
        As "{cps=25}........."
        As "{cps=25}seharusnya aku yang berterima kasih"
        show Raven Sekolah Terkejut
        rb "{cps=25}heh?"
        As "{cps=25}yaaa..karena kamu, aku bebas hukuman"
        show Raven Sekolah Tersenyum
        rb "{cps=25}hmm.. tapi sama aja sih, soalnya kamu disini sekarang"
        show Astrid Sekolah Berbicara
        As "{cps=25}iya juga ya..."
        show Astrid Sekolah Tertawa
        As "{cps=25}hahahaha"
        show Raven Sekolah Berbicara
        rb "{cps=25}cukup basa-basinya, ayo kita cepat selesaikan ini"
        show Astrid Sekolah Tersenyum
        As "{cps=25}ah benar juga.."
        hide Astrid Sekolah Tersenyum
        jump choice11_done

    "Alibi":
        show Raven Sekolah Berbicara
        rb "{cps=25}um.. pak"
        show Raven Sekolah Beralasan
        rb "{cps=25}kami dari kantin pak"
        show Raven Sekolah Tersenyum
        rb "{cps=25}saya belum sempat sarapan, jadi saya ajak Asrid menemaniku"
        show Pak Agus Berbicara
        pa "{cps=25}heee.. kalian berdua pacaran?"
        hide Pak Agus Berbicara
        show Astrid Sekolah Malu
        As "{cps=25}GAK KOK!"
        show Raven Sekolah Terkejut
        rb "{cps=25}bukan kok"
        hide Astrid Sekolah Malu
        show Pak Agus Berbicara
        pa "{cps=25}hmm..begitu ya"
        pa "{cps=25}tapi, kamu tau gak?"
        show Raven Sekolah Diam
        rb "{cps=25}ya pak?"
        pa "{cps=25}kantin jam begini belum pada buka"
        show Pak Agus Menatap
        pa "{cps=25}kamu mau menipuku ya?"
        show Pak Agus Marah
        pa "{cps=25}kalian berdua ikut saya sekarang"
        show Raven Sekolah Terkejut
        rb "{cps=25}heh?!"
        hide Pak Agus Marah
        scene bg Gudang with dissolve
        "{cps=25}Pak Agus membawa mereka ke gudang sekolah"
        show Pak Agus Berbicara
        pa "{cps=25}inilah hukuman kalian"
        show Raven Sekolah Diam
        rb "{cps=25}um...maksudnya pak?"
        pa "{cps=25}kalian berdua bersihkan tempat ini, dan rapikan barang-barang disini"
        show Raven Sekolah Terkejut
        rb "{cps=25}heh? semuanya?, dengan debu setebal ini?"
        pa "{cps=25}iya, semuanya"
        hide Pak Agus
        show Astrid Sekolah Terkejut
        As "{cps=25}tapi pak-"
        hide Astrid Sekolah Terkejut
        show Pak Agus Menatap
        pa "{cps=25}tidak ada tapi-tapi"
        show Pak Agus Marah
        pa "{cps=25}kerjakan sekarang"
        rb "{cps=25}baiklah pak"
        show Pak Agus Berbicara
        pa "{cps=25}kalau begitu, bapak pergi dulu"
        show Pak Agus Menatap
        pa "{cps=25}walaupun cuma kalian berdua, jangan buat aneh-aneh ya disini"
        hide Pak Agus Menatap
        show Astrid Sekolah Malu
        As "{cps=25}.....!?"
        show Astrid Sekolah Malu Berbicara with dissolve
        As "{cps=25}GAK AKAN PAK!"
        show Raven Sekolah Berbicara Datar 
        rb "{cps=25}{i}'seharusnya pak juga jaga disini, kan'{/i}"
        hide Astrid Sekolah Berbicara
        show Pak Agus Menatap
        pa "{cps=25}pokoknya bersih ya."
        hide Pak Agus Menatap
        show Astrid Sekolah Berbicara
        As "{cps=25}baik pak"
        hide Astrid Sekolah Berbicara
        "{cps=25}Pak Agus pergi meninggalkan mereka"
        rb "{cps=25}well..jadi gimana nih?"
        show Astrid Sekolah Terkejut
        As "{cps=25}bagaimana apanya?"
        show Astrid Sekolah Menatap
        As "{cps=25}mau tidak mau, harus kerja kan"
        As "{cps=25}soalnya ini hukuman kita"
        rb "{cps=25}um..ok"
        hide Astrid Sekolah Menatap
        "{cps=25}Raven dan Astrid mulai membersihkan gudang itu"
        "{cps=25}.......{w}......."
        "{cps=25}15 menit berlalu"
        show Raven Sekolah Berbicara Datar
        rb "{cps=25}fiuh...bersih juga"
        show Astrid Sekolah Berbicara
        As "{cps=25}tinggal merapikannya saja, kan"
        rb "{cps=25}yup, dan juga aku minta maaf ya Astrid"
        show Astrid Sekolah Terkejut
        As "{cps=25}soal?"
        show Raven Sekolah Berbicara Murung
        rb "{cps=25}gara-gara aku, kamupun dihukum"
        As "{cps=25}....."
        show Astrid Sekolah Menatap with dissolve
        As "{cps=25}lain kali, nipunya agak pintar dikit"
        rb "{cps=25}maaf"
        show Astrid Sekolah Terkejut with dissolve
        As "{cps=25}ah...benar juga ya."
        show Astrid Sekolah Berbicara with dissolve
        As "{cps=25}kamu kan, buruk dalam hal berbohong"
        show Raven Sekolah Berbicara Datar
        rb "{cps=25}hah? apa maksudmu?"
        As "{cps=25}ya selama ini, yang kulihat"
        As "{cps=25}kamu selalu mengatakan yang sebenarnya"
        As "{cps=25}tidak peduli siapapun orangnya, apapun resikonya"
        As "{cps=25}bisa dibilang, kamu terlalu jujur"
        As "{cps=25}tapi, baru kali ini aku melihat kamu mencoba berbohong"
        As "{cps=25}ya, tapi bohongmu sangat payah sekali"
        As "{cps=25}dan juga sangat lucu"
        show Astrid Sekolah Tertawa with dissolve
        As "{cps=25}hahahahaha..."
        show Raven Sekolah Diam
        rb "{cps=25}......."
        show Astrid Sekolah Berbicara with dissolve
        As "{cps=25}ah maaf, aku menertawakanmu"
        show Astrid Sekolah Tersenyum with dissolve
        As "{cps=25}yuk kita lanjutkan kerjanya"
        show Raven Sekolah Berbicara
        rb "{cps=25}um Astrid....kamu kembali aja ke kelas"
        rb "{cps=25}biar aku saja merapikan"
        show Astrid Sekolah Terkejut with dissolve
        As "{cps=25}huh? jangan kerja sendiri"
        show Astrid Sekolah Berbicara with dissolve
        As "{cps=25}tidak baik loh"
        As "{cps=25}lagipula aku lagi ngangur kok"
        show Raven Sekolah Berbicara Datar
        rb "{cps=25}jangan bilang, kamu lagi dihukum berdiri diluar?"
        show Astrid Sekolah Tersenyum with dissolve
        As "{cps=25}ya begitu lah"
        rb "{cps=25}kalau begitu, yuk selesaikan ini"
        show Astrid Sekolah Berbicara with dissolve
        As "{cps=25}.........."
        hide Astrid Sekolah Berbicara with dissolve
        jump choice11_done

label choice11_done:
$ menu_flag = False

"{cps=25}sementara Raven dan Astrid sedang merapikan"
"{cps=25}benda-benda di gudang itu"
"{cps=25}Astrid mengajak ngobrol"
show Astrid Sekolah Malu
As "{cps=25}um.. Raven.."
show Raven Sekolah Diam
rb "{cps=25}hm?"
As "{cps=25}um.. soal tadi.."
show Raven Sekolah Berbicara
rb "{cps=25}tadi?"
As "{cps=25}um.."
As "{cps=25}um....."
show Raven Sekolah Diam
rb "{cps=25}......?"
show Astrid Sekolah Malu Malu
As "{cps=25}apa menurutmu.."
As "{cps=25}kita ini terlihat seperti pacaran?"
show Raven Sekolah Berbicara
rb "{cps=25}aahh.. soal kata Pak Agus tadi?"
show Raven Sekolah Tersenyum
rb "{cps=25}Pak Agus memang suka begitu"
rb "{cps=25}kamu ti-"
As "{cps=25}apa menurutmu, kita terlihat seperti itu?!"
show Raven Sekolah Terkejut
rb "{cps=25}heh?.. um..."
show Raven Sekolah Tersenyum
rb "{cps=25}mungkin karena kita terlihat dekat, jadinya seperti itulah"
show Raven Sekolah Berbicara
rb "{cps=25}apa kamu merasa terganggu?"
show Astrid Sekolah Malu
As "{cps=25}buk-"
rb "{cps=25}kalau kamu merasa terganggu, maafkan aku"
show Astrid Sekolah Malu Berbicara
As "{cps=25}BUKANNYA BEGITU!!"
show Astrid Sekolah Malu Malu
As "{cps=25}hanya saja.."
show Raven Sekolah Diam
rb "{cps=25}hanya?"
As "{cps=25}aku takut, kamu merasa terganggu denganku"
As "{cps=25}karena kita sering dikatakan gitu"
show Raven Sekolah Tersenyum
rb "{cps=25}ah, tidak kok"
rb "{cps=25}aku tidak merasa terganggu, sama sekali"
As "{cps=25}begitu ya."
show Raven Sekolah Beralasan
rb "{cps=25}jadi ya, kita bersikap seperti biasa aja"
show Raven Sekolah Tersenyum
rb "{cps=25}tak perlu dipikirkan"
show Astrid Sekolah Malu
As "{cps=25}hmmm...."
show Raven Sekolah Berbicara
rb "{cps=25}lagi pula, mana mungkin kamu menyukaiku"
show Astrid Sekolah Malu Malu
As "{cps=25}aku menyukaimu kok"
show Raven Sekolah Tersenyum
rb "{cps=25}cowok yang tak punya apa-apa kek aku"
stop music fadeout 1
show Raven Sekolah Diam
rb "{cps=25}.............?!"
show Raven Sekolah Terkejut
rb "{cps=25}heh?!"
As "{cps=25}aku menyukaimu kok"
rb "{cps=25}heh?!!"
rb "{cps=25}kau bercanda kan?"
show Astrid Sekolah Malu Berbicara
As "{cps=25}apa aku terlihat bercanda?"
hide Astrid Sekolah Malu Berbicara
"{cps=25}Astrid berdiri langsung berhadapan dengan Raven"
"{cps=25}membuat Raven sangat berkeringat dingin"
show Raven Sekolah Tersenyum
rb "{cps=25}............."
rb "{cps=25}{i}'situasi macam apa ini?'{/i}"
show Astrid Sekolah Malu Berbicara
As "{cps=25}DENGARKAN AKU!"
As "{cps=25}aku menyukaimu"
rb "{cps=25}sebagai teman, kan?"
show Astrid Sekolah Malu Malu
As "{cps=25}bukan sebagai teman"
show Astrid Sekolah Malu Berbicara
As "{cps=25}aku menyukaimu, sebagai lawan jenis!"
play sound "Sound Effect/Heart_Beat01-2L.mp3"
show Raven Sekolah Tersenyum
rb "{cps=25}........."
rb "{cps=25}{i}'tunggu dulu, ini terlalu tiba-tiba'{/i}"
rb "{cps=25}{i}'hatiku belum siap untuk ini'{/i}"
hide Astrid Sekolah Malu Berbicara
play sound "Sound Effect/004-Benda Jatuh.mp3"
"{cps=25}tiba-tiba suara bunyi benda terjatuh membuat mereka tersadar"
show Mei Sekolah Murung
play music "BGM/003-Ending Astrid-Mei-heisarenai.mp3" fadeout 1
"{cps=25}ternyata Mei sedang berdiri di pintu, melihat semuanya"
m "{cps=25}umm..."
show Mei Sekolah Menangis
m "{cps=25}maaf menggangu kalian"
hide Mei Sekolah Menangis
"{cps=25}Mei langsung berlari meninggalkan mereka"
show Raven Sekolah Terkejut
rb "{cps=25}Mei tunggu!!"
scene bg Lorong Sekolah Gudang
"{cps=25}Raven dengan segera ia mengejar Mei"
show Pak Agus Menatap
pa "{cps=25}hey.. mau kemana kamu?!"
"{cps=25}tapi Raven bertemu Pak Agus"
show Raven Sekolah Diam
rb "{cps=25}um..."
pa "{cps=25}jangan kabur kamu!"
pa "{cps=25}emangnya, perkerjaan kamu sudah selesai?"
rb "{cps=25}tinggal merapikan saja pak"
pa "{cps=25}kalau begitu"
show Pak Agus Marah
pa "{cps=25}KEMBALI BEKERJA!!"
show Raven Sekolah Murung
rb "{cps=25}baik pak"
rb "{cps=25}{i}'aku seperti seorang tahanan, yang sedang dipaksa bekerja'{/i}"
hide Pak Agus Marah
scene bg Gudang
"{cps=25}Raven kembali ke gudang"
"{cps=25}ia melihat, Astrid yang sedang merapikan benda-benda kecil"
show Raven Sekolah Murung
rb "{cps=25}um...."
"{cps=25}Raven menjadi canggung, binggung untuk membuka topik pembicaraan"
"{cps=25}setelah kejadian yang sangat mendadak itu"
show Astrid Sekolah Malu Maluin
As "{cps=25}Raven, aku mau pergi dulu"
rb "{cps=25}heh?, kau mau pergi meninggalkanku?"
As "{cps=25}ya begitulah"
As "{cps=25}aku sudah membereskan beberapa benda, tinggal kamu kerjakan yang sisanya"
show Raven Sekolah Murung
rb "{cps=25}.............."
As "{cps=25}dan juga Raven....."
rb "{cps=25}............."
As "{cps=25}lupakan yang aku katakan tadi"
As "{cps=25}anggap saja, aku tak pernah mengucapkannya"
rb "{cps=25}............{w}"
"{i}*Raven hanya bisa mengangguk*{/i}"
As "{cps=25}bye..."
hide Astrid Sekolah Malu Maluin with moveoutleft
rb "{cps=25}..................."
"{cps=25}Astrid meninggalkan Raven"
"{cps=25}Raven tau, bahwa sebenarnya Astrid ingin sendirian"
"{cps=25}setelah mengucapkan hal yang sangat memalukan baginya"
"{cps=25}dan juga, Raven tak mampu mengucapkan satu katapun"
"{cps=25}karena ia telah melakukan sesuatu yang tak bisa dimaafkan"
"{cps=25}antara Mei dan Astrid"
rb "{cps=25}apa yang harus kulakukan?"
"{cps=25}ia melihat beberapa benda yang masih berantakan"
rb "{cps=25}lebih baik kuselesaikan, biar hukuman ini selesai"
"{cps=25}Raven memutuskan untuk selesaikan hukuman yang sekarang ia jalani"
rb "{cps=25}............."
"{cps=25}tetap saja Raven masih memikirkan soal tadi"
show Raven Sekolah Berpikir
rb "{cps=25}aarrgghh....!!"
rb "{cps=25}pikiran ini menggangguku"
"{cps=25}walaupun pikirannya sedang terganggu, tapi Raven akhirnya menyelesaikannya"
show Raven Sekolah Murung
rb "{cps=25}.........."
rb "{cps=25}sebaiknya aku melaporkannya ke Pak Agus"
show Pak Agus Berbicara
pa "{cps=25}bagaimana?{w} udah selesai?"
"{cps=25}tapi, Pak Agus sudah berada disitu untuk mengecek Raven"
rb "{cps=25}um... iya pak, sudah selesai"
pa "{cps=25}baguslah, sekarang kamu kembali ke kelasmu"
rb "{cps=25}terima kasih pak"
hide Pak Agus Berbicara
"{cps=25}Raven-pun bergegas kembali ke kelasnya"
scene bg Lorong Kelas Raven with dissolve
"{cps=25}sampailah ia ke kelasnya"
"{cps=25}tapi, sesampainya disana kelas sudah bubar"
"{cps=25}kelas dipulangkan, karena guru sedang rapat mendadak"
show Raven Sekolah Terkejut
rb "{cps=25}heh? bukannya ini terlalu mendadak?"
show Raven Sekolah Berpikir
rb "{cps=25}ah bodoh amat, sebaiknya aku mencari mereka"
scene bg Kelas Raven1 with dissolve
"{cps=25}Raven mencari Astrid di kelasnya"
show Raven Sekolah Berbicara
rb "{cps=25}apa kalian melihat Astrid?"
"{cps=25}ternyata Astrid sudah pulang duluan"
scene bg Kelas Mei with dissolve
"{cps=25}kemudian, Raven pergi ke kelas Mei"
"{cps=25}tapi disana pun kelasnya sudah kosong"
scene bg Perpus01 with dissolve
"{cps=25}Raven melanjukan mencari di perpus"
"{cps=25}tapi, kemanapun Raven mencari"
"{cps=25}ia tak menemukan mereka lagi"
show Raven Sekolah Murung
rb "{cps=25}aaaa... dimana mereka?"
"{cps=25}Raven mengambil ponselnya"
"{cps=25}dan berusaha menghubungi mereka"
"{cps=25}.............{w}.........."
"{cps=25}..............{w}.........."
"{cps=25}tapi tak ada satu pun dari mereka menganggkat telponnya"
rb "{cps=25}............"
rb "{cps=25}sebaiknya aku pulang saja"
scene bg blck
"{cps=25}Raven menyerah dan iapun memutuskan untuk pulang"
jump ending1
    
    
    
    
label pulang:
scene bg Raven House02 with dissolve    
"{cps=25}sampailah Raven di rumahnya"
show Raven Sekolah Berbicara Murung
rb "{cps=25}aku pulang.."
show Mama Terkejut
i "{cps=25}kok pulang cepat?"
rb "{cps=25}ya begitulah, ada banyak hal yang terjadi"
i "{cps=25}heh?!"
hide Mama Terkejut
"{cps=25}dengan wajah yang cemberut, Raven langsung menuju kamarnya"
scene bg Raven Room After
play sound "Sound Effect/003-Mengkunci Pintu Raven.mp3"
"{cps=25}ia mengunci pintunya, dan langsung berbaring dikasurnya"
show Raven Sekolah Berpikir
rb "{cps=25}........."
rb "{cps=25}apa yang sudah kulakukan.."
show Raven Sekolah Berbicara Datar
rb "{cps=25}ah.......bodohnya diriku ini"
rb "{cps=25}seandainya kalau aku bisa kembali"
show Raven Sekolah Murung
rb "{cps=25}...........??!!"
show Raven Sekolah Terkejut
rb "{cps=25}tunggu dulu..."
"{cps=25}Raven teringat akan sesuatu"
"{cps=25}ia mencari jam silver yang membuat bisa kembali itu"
show Raven Sekolah Diam
rb "{cps=25}dimana aku menyimpannya ya?"
"{cps=25}setelah mencari cukup lama"
"{cps=25}akhirnya, ia menemukan jam silver itu"
rb "{cps=25}......"
"{cps=25}sambil memegang jam itu, Raven merasa sedikit ragu"
show Raven Sekolah Murung
rb "{cps=25}apakah aku harus kembali sekarang?"
show Raven Sekolah Berpikir
menu:
    rb "{cps=25}............"
    
    "ya, sekarang!":
        rb "{cps=25}...."
        show Raven Sekolah Diam
        rb "{cps=25}well, mungkin harus sekarang"
        rb "{cps=25}sebelum nanti menyesal"
        "{cps=25}Raven menekan tombol itu"
        show Raven Sekolah Terkejut
        rb "{cps=25}...!!"
        rb "{cps=25}...!!"
        "{cps=25}Raven merasakan keanehan dalam dirinya"
        play sound "Sound Effect/Heart_Beat01-3L.mp3"
        queue sound "Sound Effect/Heart_Beat01-3L.mp3"
        queue sound "Sound Effect/Heart_Beat01-3L.mp3"
        queue sound "Sound Effect/Heart_Beat01-3L.mp3"
        "{cps=25}jantung yang berdebar tak beraturan"
        "{cps=25}membuat pandangan Raven mulai memudar"
        "{cps=25}Raven kehilangan keseimbangan, sehingga ia terjatuh"
        "{cps=25}kesadaran Raven mulai di ambang batas"
        scene bg Meja Makan with Fade(0.2, 0.0, 0.8, color='#FF0000')
        play sound "Sound Effect/001-Kembali Checkpoint-Accent37-1.mp3"
        $renpy.load('checkpoint')
    
    "nanti saja":
        rb "{cps=25}....."
        show Raven Sekolah Diam
        rb "{cps=25}mungkin, nanti saja"
        "{cps=25}Raven menyimpan kembali jam itu"
        i "{cps=25}Raven!!{p}mari bantu Mama dulu"
        show Raven Sekolah Berbicara
        rb "{cps=25}iya Ma.."
        scene bg Raven House02 with dissolve
        "{cps=25}Raven membantu ibunya untuk mempersiapkan perayaan ultahnya"
        scene bg Raven House03 with dissolve
        scene bg Raven House01 with dissolve
        "{cps=25}Hingga Malam Perayaanpun tiba.."
        "{cps=25}Raven merayakan ultahnya dengan teman dan keluarganya"
        "{cps=25}perayaan berlangsung lancar hingga akhir{p}Mei tidak datang ke acaranya, karena ia belum mengundang Mei"
        "{cps=25}seharusnya itu yang dipikirkan Raven bahwa ia berhasil{p}yaa.. itu seharusnya"
        "{cps=25}namun.....{w}."
        jump MeiDie


label choice7_nohome:
$ menu_flag = True

"{cps=25}namun tak ada jawaban"
show Raven Sekolah Diam
rb "{cps=25}um...."
rb "{cps=25}apakah ia sudah pergi?"
show Raven Sekolah Berbicara Murung
rb "{cps=25}tapi bagaimana mungkin"
rb "{cps=25}aku sudah menunggunya dari tadi"
show Raven Sekolah Berpikir
rb "{cps=25}hmm..{w}ah sudahlah"
show Raven Sekolah Diam
rb "{cps=25}lebih baik aku pergi saja"
"{cps=25}Raven memutuskan pergi tanpa Mei"
stop music fadeout 1
scene bg Bus Stop2
"{cps=25}Raven sekarang di bus stop yang tak jauh dari rumah Mei"
"{cps=25}tak perlu menunggu lama, bus sekolah melintas dan Raven naik ke bus itu"
jump sekolah

label sekolah:
scene bg Sekolah01 with fade
"{cps=25}sampailah Raven di sekolah"
"{cps=25}karena sudah jam belajar mengajar, pagar sekolah ingin di tutup"
"{cps=25}dengan sekuat tenaga, Raven berlari agar tidak terkunci diluar"
show Raven Sekolah Terkejut
rb "{cps=25}sedikit lagi......"
scene bg Sekolah Tutup with dissolve
"{cps=25}walaupun pagar sekolah ditutup, tapi Raven berhasil masuk"
show Raven Sekolah Berbicara Datar
rb "{cps=25}fiuh.....syukurlah, masih sempat"
"{cps=25}Raven menarik nafas lega"
show Pak Agus Berbicara
pa "{cps=25}Raven?!"
pa "{cps=25}tumben, kamu terlambat"
"{cps=25}Pak Agus menyapa Raven"
"{cps=25}Pak Agus Adalah Guru Piket pada saat itu"
show Raven Sekolah Berbicara Murung
rb "{cps=25}maaf pak, ada hal yang harus kulakukan"
rb "{cps=25}tapi, saya tidak terlambat, kan?"
pa "{cps=25}sebenarnya termasuk terlambat sih"
pa "{cps=25}tapi, kamu masuk pas pagar belum tertutup"
pa "{cps=25}termasuk amanlah"
show Pak Agus Menatap with dissolve
pa "{cps=25}Tapi, bukan berarti kamu bebas hukuman"
pa "{cps=25}squat jump 5x . baru kamu boleh pergi"
hide Pak Agus Menatap with dissolve
show Raven Sekolah Murung
rb "{cps=25}baiklah pak"
"{cps=25}Raven mematuhi hukuman yang diberikan oleh Pak Agus"
"{cps=25}setelah itu, ia langsung bergegas ke kelasnya"
scene bg Kelas Raven1
"{cps=25}sesampainya di Kelas, Raven langsung duduk di bangkunya"
"{cps=25}Karena, Gurunya sudah hadir"
"{cps=25}5 Menit Kemudian"
jump kumpul_PR

return