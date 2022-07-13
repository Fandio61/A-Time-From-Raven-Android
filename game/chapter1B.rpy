label Chapter1B:

default kerja = False
scene bg Sekolah01 with fade
"{cps=25}sampailah ia ke sekolah"
scene bg Dalam Sekolah with dissolve
"{cps=25}Raven masuk ke lingkungan sekolah dan masuk kebarisan siswa"
"{cps=25}untuk mengikuti kegiatan apel pagi, seperti biasanya"
"{cps=25}10 menit berlalu..{w}."
"{cps=25}apel pagi telah berakhir"
show Raven Sekolah Berbicara Datar
rb "{cps=25}akhirnya berakhir juga"
scene bg Kelas Raven1 with dissolve
"{cps=25}Raven pergi ke kelasnya"
show Raven Sekolah Berbicara Datar
rb "{cps=25}hmmm{w} masih ada waktu sebelum jam pelajaran mulai"
rb "{cps=25}mungkin sebaiknya aku ke Mei dulu"
show Raven Sekolah Serius
rb "{cps=25}tapi, tunggu dulu.."
show Raven Sekolah Berbicara Datar
rb "{cps=25}bukannya pelajaran pertama nanti"
rb "{cps=25}pelajaran sejarah."
rb "{cps=25}dan juga aku belum mengerjakan pr-nya"
rb "{cps=25}ah.. sial"
show Raven Sekolah Berpikir

menu:
        rb "{cps=25}apa yang aku harus lakukan?"
    
        "kerjakan pr":
            $kerja = True
            show Raven Sekolah Berbicara Datar
            rb "{cps=25}ah, lebih baik aku kerjakan pr saja deh"
            rb "{cps=25}dari pada aku dihukum"
            "{cps=25}Raven pergi kebangkunya"
            "{cps=25}dan mengerjakan pr"
            "{cps=25}....{w}........."
            "{cps=25}sementara Raven sedang mengerjakan pr"
            "{cps=25}tiba-tiba bel sekolah berbunyi"
            "{cps=25}menandakan telah mulai proses belajar mengajar"
            show Raven Sekolah Serius
            rb "{cps=25}ah.. sial"
            rb "{cps=25}aku belum selesai lagi.."
            "{cps=25}Raven mempercepat menulisnya"
            "{cps=25}tapi.."
            "{cps=25}Pak Rudi, guru sejarah itu. sudah masuk ke kelas"
            "{cps=25}seperti biasanya, para murid dikelas memberi salam kepada gurunya"
            "{cps=25}dengan aba-aba dari ketua kelas"
            show Pak Rudi Berbicara
            pr "{cps=25}selamat pagi anak-anak"
            pr "{cps=25}silahkan duduk"
            jump kumpul_PR

        "mencari Mei":
            show Raven Sekolah Berbicara Datar
            rb "{cps=25}ah, lebih baik aku cari saja deh"
            rb "{cps=25}karena waktu di apel pagi tadi"
            rb "{cps=25}aku tidak melihatnya sama sekali"
            show Raven Sekolah Murung
            rb "{cps=25}aku hanya perlu memastikan dia"
            rb "{cps=25}apakah dia baik-baik saja"
            show Raven Sekolah Berpikir
            rb "{cps=25}tapi, harus cari kemana?"
            
            menu:
                "{cps=25}kemana harus mencarinya?"
                
                "Kantin":
                    show Raven Sekolah Diam
                    rb "{cps=25}hmm..{w} coba saja ke kantin"
                    scene bg Kantin with dissolve
                    "{cps=25}Raven mencari Mei di kantin"
                    "{cps=25}tapi, kantin di sekolah sangat luas dan berpetak"
                    "{cps=25}sehingga Raven sangat kesulitan mencarinya"
                    "{cps=25}karena kelamaan mencari"
                    "{cps=25}bel sekolah berbunyi"
                    "{cps=25}tandanya jam belajar mengajar sudah dimulai"
                    show Raven Sekolah Terkejut
                    rb "{cps=25}wah gawat, aku harus kekelas sekarang"
                    "{cps=25}Raven bergegas pergi kekelasnya"
                    scene bg Kelas Raven1 with dissolve
                    "{cps=25}sesampainya ia di kelas"
                    "{cps=25}rupanya Pak Rudi, guru sejarah itu"
                    "{cps=25}sudah berada di depan kelasnya"
                    "{cps=25}Raven segera masuk kelas dan duduk di bangkunya"
                    show Raven Sekolah Berbicara Datar
                    rb "{cps=25}fiiuh, hampir aja"
                    jump kumpul_PR
                
                "Perpustakaan":
                    show Raven Sekolah Diam
                    rb "{cps=25}hmmmm...{w} coba saja ke perpus"
                    scene bg blck with fade
                    "{cps=25}Raven pergi mencari Mei di perpustakaan"
                    "{cps=25}untungnya jarak kelas Raven dan perpustakaan lumayan dekat"
                    scene bg Perpus01 with fade
                    "{cps=25}tak lama kemudian sampailah ia di perpustakaan"
                    jump perpus
                    
                    
                "Kelasnya":
                    show Raven Sekolah Diam
                    rb "{cps=25}hmm..{w}mungkin saja di kelasnya"
                    scene bg blck with fade
                    "{cps=25}Raven mencari Mei di kelasnya"
                    "{cps=25}jarak kelas Mei dan Raven tidak terlalu jauh"
                    "{cps=25}tak lama kemudian, sampailah ia di kelas Mei"
                    scene bg Kelas Mei with fade
                    "{cps=25}Raven mengintip sedikit di kelasnya"
                    show Raven Sekolah Berbicara
                    rb "{cps=25}permisi...{w}Mei ada?"
                    show Aston Sekolah Bertanya with dissolve
                    a "{cps=25}oh kamu, Raven.."
                    show Aston Sekolah Berbicara with dissolve
                    a "{cps=25}cari Mei?"
                    a "{cps=25}dia tidak ada disini"
                    a "{cps=25}mungkin dia ada di perpus"
                    rb "{cps=25}begitu ya, thanks ya"
                    rb "{cps=25}kalau begitu, saya permisi dulu"
                    a "{cps=25}iyo.."
                    hide Aston Sekolah Berbicara with dissolve
                    scene bg blck with fade
                    "{cps=25}rupanya Mei tidak ada di kelasnya"
                    "{cps=25}Raven berniat pergi ke perpus"
                    "{cps=25}untuk melanjutkan pencariannya"
                    "{cps=25}tapi{w}, saat ia ditengah perjalan"
                    "{cps=25}ia bertemu dengan Pak Agus, guru piket saat itu"
                    "{cps=25}Pak Agus mencurigai Raven bolos"
                    "{cps=25}dan menyuruhnya untuk kembali kekelasnya"
                    scene bg Lorong Kelas Raven with fade
                    "{cps=25}Ravenpun pergi kekelasnya"
                    "{cps=25}sesampainya ia di kelas"
                    "{cps=25}rupanya Pak Rudi, guru sejarah itu"
                    "{cps=25}sudah berada di depan kelasnya"
                    scene bg Kelas Raven1 with dissolve
                    "{cps=25}Raven segera masuk kelas dan duduk di bangkunya"
                    show Raven Sekolah Berbicara Datar
                    rb "{cps=25}fiiuh, hampir aja"
                    jump kumpul_PR
label perpus:
"{cps=25}dengan tenang ia masuk kedalam perpustakaan"
"{cps=25}kemudian dia mencari Mei"
"{cps=25}ia melihat Mei yang sedang menyimpan buku di rak buku"
show Raven Sekolah Berbicara
rb "{cps=25}Mei"
show Mei Sekolah Ramah
m "{cps=25}??"
rb "{cps=25}syukurlah kau ada disini"
show Mei Sekolah Berbicara
m "{cps=25}Raven?"
m "{cps=25}kau mencariku?"
rb "{cps=25}ya, begitulah."
m "{cps=25}ada apa emangnya?"
show Raven Sekolah Beralasan
rb "{cps=25}ummm......."
show Raven Sekolah Berbicara Datar with dissolve
menu:
    rb "{cps=25}sebenarnya......"
    
    "ada yang ingin kuberitahu":
        show Raven Sekolah Berbicara Datar
        rb "{cps=25}Mei!"
        m "{cps=25}ya?"
        show Raven Sekolah Berbicara Murung with dissolve
        rb "{cps=25}ada yang ingin kuberitahu"
        rb "{cps=25}jadi dengarlah baik-baik"
        show Mei Sekolah Ramah with dissolve
        m "{cps=25}..?"
        hide Mei Sekolah Ramah
        show Raven Sekolah Murung with dissolve
        rb "{cps=25}{i}'sebenarnya ada banyak hal yang ingin kusampaikan padanya'{/i}"
        rb "{cps=25}{i}'tapi, selama ini aku tak punya kesempatan untuk mengatakannya'{/i}"
        rb "{cps=25}{i}'kesempatan ini tak akan kubuang sia-sia'{/i}"
        show Raven Sekolah Serius with dissolve
        rb "{cps=25}{i}'jadi, hal penting yang ingin kusampaikan padanya'{/i}"
        show Raven Sekolah Serius
        menu:
            rb "{cps=25}{i}'ialah......'{/i}"
            
            "kumohon jangan datang ke acaraku":
                show Mei Sekolah Ramah with dissolve
                show Raven Sekolah Berbicara Datar
                rb "{cps=25}kumohon padamu Mei"
                rb "{cps=25}jangan datang ke acaraku"
                show Mei Sekolah Terkejut with dissolve
                m "{cps=25}heh!? kenapa?"
                show Mei Sekolah Berbicara with dissolve
                show Raven Sekolah Serius with dissolve
                rb "{cps=25}pokoknya jangan!"
                rb "{cps=25}kumohon! jangan!"
                show Mei Sekolah Murung with dissolve
                m "{cps=25}kau kenapa Raven?"
                m "{cps=25}mukamu pucat sekali"
                m "{cps=25}kau baik-baik saja, kan?"
                rb "{cps=25}aku baik-baik saja"
                rb "{cps=25}keselamatan kamu yang lebih penting"
                m "{cps=25}heh? apa maksudmu?"
                show Raven Sekolah Murung
                
                rb "{cps=25}{i}'ah.. percuma bagaimapun aku menjelaskannya'{/i}"
                show Raven Sekolah Serius with dissolve
                rb "{cps=25}dengar aku baik-baik, Mei"
                rb "{cps=25}sebenarnya aku datang dari masa depang"
                rb "{cps=25}aku datang untuk menghentikan kematianmu-"
                show Raven Sekolah Terkejut with dissolve
                rb "{cps=25}urrgh!"
                hide Mei Sekolah
                "{cps=25}tiba-tiba"
                "{cps=25}Raven dadanya terasa sesak"
                play sound "Sound Effect/Heart_Beat01-3L.mp3"
                queue sound "Sound Effect/Heart_Beat01-3L.mp3"
                "{cps=25}jantungnya berdetak tak beraturan"
                scene bg blck with fade
                "{cps=25}dan Raven hilang kesadaran, sehingga ia terjatuh"
                jump melanggar2
                
            "sudah lama aku menyukaimu":
                show Raven Sekolah Berbicara Datar
                rb "{cps=25}um.. gini Mei!"
                show Mei Sekolah Tersenyum
                m "{cps=25}..?"
                show Raven Sekolah Diam
                rb "{cps=25}......."
                hide Mei Sekolah Tersenyum with dissolve
                scene bg blck with dissolve
                show Raven Sekolah Berpikir
                rb "{cps=25}......."
                rb "{cps=25}{i}'memang aku memendam rasa ini sudah lama'{/i}"
                rb "{cps=25}{i}'dan membuat ku terus menyesal karena tidak mennggungkapkannya'{/i}"
                scene bg Perpus01 with fade
                show Mei Sekolah Ramah
                "{cps=25}Mei Menatap Raven dengan serius menatap Raven"
                "{cps=25}tanpa sadar wajah Mei sangat dekat dengan Raven"
                show Raven Sekolah Diam
                rb "{cps=25}{i}'tapi, apa aku harus menggungkapkan sekarang?'{/i}"
                show Mei Sekolah Tersenyum with dissolve
                m "{cps=25}kamu mau ngomong apa?"
                show Raven Sekolah Berpikir
                rb "{cps=25}......."
                show Raven Sekolah Diam
                rb "{cps=25}{i}'ah, bodoh amat dah'{/i}"
                show Raven Sekolah Berbicara Datar
                rb "{cps=25}Mei.."
                rb "{cps=25}sudah lama, aku menyukaimu"
                show Mei Sekolah Terkejut
                m "{cps=25}......!!?"
                scene bg blck with dissolve
                show Raven Sekolah Berpikir
                rb "{cps=25}{i}'ah.. apa yang sudah kulakukan'{/i}"
                scene bg Perpus01
                show Raven Sekolah Berbicara Datar
                rb "{cps=25}aku tau, ini sangat tidak tepat"
                rb "{cps=25}tapi, hati kecilku terus berteriak"
                rb "{cps=25}dan aku tak bisa menahannya lagi perasaan ini...."
                scene bg blck with dissolve
                show Raven Sekolah Berpikir
                rb "{cps=25}{i}'ini sangat memalukan'{/i}"
                rb "{cps=25}{i}'aku tak sanggup melihat wajahnya'{/i}"
                rb "{cps=25}{i}'aku tak tau harus-'{/i}"
                scene bg Perpus01
                show Mei Sekolah Berbicara
                m "{cps=25}Raven!"
                show Mei Sekolah Menepuk with dissolve
                "{cps=25}Mei menepuk kepala Raven"
                show Raven Sekolah Terkejut
                rb "{cps=25}hah.....?"
                
                "Raven sangat bingung atas apa yang dilakukan Mei saat itu"
                m "{cps=25}aku senang, kamu punya perasaan seperti itu"
                m "{cps=25}tapi, aku sudah anggap kamu sebagai adikku"
                "{cps=25}Mei mengelus kepala Raven dengan lembut"
                m "{cps=25}adikku yang sangat manis"
                show Raven Sekolah Murung
                rb "{cps=25}........"
                "{cps=25}Raven hanya bisa terdiam"
                "{cps=25}ia tak bisa berkata apapun{p}atau ekspresi apapun"
                "{cps=25}sebab"
                "{cps=25}di satu sisi, ia sakit hati karena penolakan Mei"
                "{cps=25}di satu sisi juga, ia merasa lega karena sudah menggungkapkannya"
                show Raven Sekolah Berbicara Datar
                rb "{cps=25}{i}'ah.. sudahlah'{/i}"
                hide Mei Sekolah
                "{cps=25}Mei berhenti mengelus kepala Raven"
                jump ucapan
            "aku minta maaf":
                show Raven Sekolah Berbicara Datar
                rb "{cps=25}um. Mei"
                show Mei Sekolah Ramah
                m "{cps=25}...?"
                show Raven Sekolah Murung
                rb "{cps=25}......."
                show Raven Sekolah Berbicara Murung with dissolve
                rb "{cps=25}aku.."
                rb "{cps=25}minta maaf"
                show Mei Sekolah Terkejut
                m "{cps=25}heee?"
                rb "{cps=25}soal kejadian kemarin"
                show Mei Sekolah Berbicara with dissolve
                m "{cps=25}ah soal itu"
                show Mei Sekolah Tersenyum with dissolve
                m "{cps=25}sudahlah, aku tidak terlalu memikirkannya"
                show Mei Sekolah Berbicara with dissolve
                m "{cps=25}lagipula kamu tidak sengaja, kan"
                show Raven Sekolah Berbicara Datar
                rb "{cps=25}tapi, kan-"
                show Mei Sekolah Menepuk with dissolve
                "{cps=25}Tiba-tiba Mei menepuk kepala Raven dengan lembut"
                m "{cps=25}buku itu, bisa aku cari lagi nanti"
                m "{cps=25}intinya kamu tidak apa-apa"
                m "{cps=25}itu sudah cukup bagiku"
                show Raven Sekolah Diam
                rb "{cps=25}....."
                hide Mei Sekolah Menepuk with dissolve
                "{cps=25}Mei berhenti menepuk kepala Raven"
                jump ucapan

    "ku ingin menulis sesuatu":
        show Raven Sekolah Berbicara Datar
        rb "{cps=25}Mei"
        show Mei Sekolah Ramah
        m "{cps=25}iya?"
        rb "{cps=25}boleh ku pinjam sesuatu untuk menulis?"
        show Mei Sekolah Terkejut with dissolve
        m "{cps=25}heh?! untuk apa?!"
        rb "{cps=25}ada hal penting yang ingin kuberitahu"
        m "{cps=25}penting bagaimana?"
        show Mei Sekolah Berbicara with dissolve
        m "{cps=25}ngomong aja kenapa?"
        show Raven Sekolah Serius
        rb "{cps=25}hal ini sangat penting"
        rb "{cps=25}dan aku tak bisa ngomong sekarang"
        rb "{cps=25}aku merasa, ada yang mengawasiku"
        show Mei Sekolah Terkejut with dissolve
        m "{cps=25}heh?!{w} siapa? dimana?"
        m "{cps=25}apa kau baik-baik saja kan, Raven?"
        m "{cps=25}perlu ku-"
        show Raven Sekolah Serius
        rb "{cps=25}ah sudahlah. aku baik-baik saja"
        rb "{cps=25}ini demi hidup kamu"
        rb "{cps=25}kumohon, berikan saja padaku"
        rb "{cps=25}sesuatu yang bisa kutulis, sekarang"
        show Mei Sekolah Murung with dissolve
        m "{cps=25}Raven{w} kau menakutkan"
        hide Mei Sekolah Murung with dissolve
        "{cps=25}Mei memberikan suatu buku notes kecil dan alat tulisnya"
        "{cps=25}Ravenpun menulis..."
        mem "{cps=25}kumohon mei{p=0.5}jangan datang ke acaraku{p=0.5}karena bahaya sedang mengintaimu{p=0.5}percaya atau tidak, aku datang dari masa depan untuk-{p=0.5}----------"
        "{cps=25}sementara Raven menulis"
        "{cps=25}tiba-tiba"
        play sound "Sound Effect/Heart_Beat01-3L.mp3"
        queue sound "Sound Effect/Heart_Beat01-3L.mp3"
        "{cps=25}jantungnya berdetak tak beraturan"
        "{cps=25}dan Raven hilang kesadaran, sehingga ia terjatuh"
        jump melanggar1

label ucapan:
show Mei Sekolah Berbicara
m "{cps=25}oh iya..{p}kamu ulang tahun, kan?"
show Mei Sekolah Tersenyum
m "{cps=25}selamat ulang tahun Raven"
show Mei Sekolah Berbicara
m "{cps=25}umur ke 17, kan{p}kurangi ceroboh kamu ya"
m "{cps=25}sepertinya aku juga harus berhenti menganggapmu{p}adik yang manis lagi kan"
show Mei Sekolah Ramah
m "{cps=25}ah.. aku sedikit kesepian"
show Raven Sekolah Tersenyum
rb "{cps=25}justru itu yang kumau selama ini"
show Mei Sekolah Berbicara
m "{cps=25}hmm.. gitu ya"
m "{cps=25}oh iya {p}sebentar, ada perayaan gitu?"
m "{cps=25}sweet seventeen loh"
scene bg blck with dissolve
show Raven Sekolah Berpikir
rb "{cps=25}{i}'ah betul juga, aku hampir lupa..'{/i}"
rb "{cps=25}{i}'aku harus mencegahnya agar ia tak datang ke acaraku'{/i}"
rb "{cps=25}{i}'tapi, aku tak mau berbohong padanya'{/i}"
rb "{cps=25}{i}'lebih tepatnya aku harus membuatnya tetap hidup'{/i}"
scene bg Perpus01
show Mei Sekolah Berbicara
m "{cps=25}Raven..{p}ada atau tidak?"
show Raven Sekolah Berbicara Datar
menu:
    rb "{cps=25}um..."
    
    "ada":
        show Raven Sekolah Diam
        rb "{cps=25}{i}'aku tak mau berbohong padanya'{/i}"
        show Raven Sekolah Berbicara
        rb "{cps=25}ada kok"
        show Mei Sekolah Berbicara
        m "{cps=25}hmmm gitu ya{p}nanti aku datang deh"
        show Raven Sekolah Serius
        rb "{cps=25}jangan..!"
        show Mei Sekolah Terkejut with dissolve
        m "{cps=25}heh??!.. kenapa?"
        hide Mei Sekolah Terkejut
        "{cps=25}bel sekolah berbunyi tandanya jam belajar mengajar telah dimulai"
        show Mei Sekolah Berbicara
        m "{cps=25}ah.. bel sudah bunyi tuh"
        show Raven Sekolah Serius
        rb "{cps=25}Mei.!{p}jangan pergi kerumahku sendririan"
        rb "{cps=25}tunggu aku{p}aku akan menjemputmu dari rumahmu"
        show Mei Sekolah Tersenyum
        m "{cps=25}hmmm..{p}iya deh"
        rb "{cps=25}janji ya.."
        rb "{cps=25}pokoknya tunggu aku{p}jangan pergi sendirian"
        show Mei Sekolah Ramah
        m "{cps=25}iya iya"
        hide Mei Sekolah Ramah
        "{cps=25}Raven dan Mei berpisah dari perpustakaan{p}lalu menuju ke kelas mereka masing-masing"
        scene bg Lorong Kelas Raven with fade
        "{cps=25}sesampainya Raven tiba di kelasnya.{p}rupanya Pak Rudi sudah masuk dikelasnya"
        "{cps=25}dan Astrid sedang berdiri di depan kelas{p}Raven menghampirinya"
        show Raven Sekolah Berbicara
        rb "{cps=25}disetrap?"
        show Astrid Sekolah Menatap
        As "{cps=25}ya.. begitulah"
        show Raven Sekolah Diam
        rb "{cps=25}hmm..."
        hide Astrid Sekolah Menatap
        "{cps=25}Raven tau, apa yang harus ia lakukan{p}ia ikut berdiri sama-sama dengan Astrid"
        show Astrid Sekolah Terkejut
        As "{cps=25}heh?!"
        show Raven Sekolah Berbicara Datar
        rb "{cps=25}kamu tak perlu kaget gitu{p}aku juga belum kerja tugasnya dia"
        rb "{cps=25}ya.. sekaligus temani kamu, gitu"
        show Astrid Sekolah Malu
        As "{cps=25}hmmm.."
        hide Astrid Sekolah Malu
        "{cps=25}Raven dan Astrid sama-sama disetrap berdiri di luar kelas{p}mereka mengobrol menghabiskan waktu hingga waktu hukuman mereka berakhir"
        scene bg Kelas Raven1 with dissolve
        "{cps=25}waktu hukuman mereka telah berakhir{p}dan mereka duduk di bangkunya masing-masing"
        scene bg Kelas Raven2 with dissolve
        "{cps=25}Raven mengikuti semua mata pelajaran, hingga jam sekolah berakhir"
        scene bg Raven House03 with fade
        "{cps=25}Raven pulang ke rumahnya{p}dan ia memantu ibunya untuk persiapan perayaan ultahnya"
        scene bg Raven House01 with dissolve
        "{cps=25}malampun tiba"
        scene bg blck
        "{cps=25}Sebelum memulai acaranya{p}Raven keluar dari rumah"
        scene bg Jalan Malam with dissolve
        "{cps=25}dan pergi ke rumah Mei{p}berniat untuk menjemputnya"
        show Raven Rumahan Diam
        rb "{cps=25}semoga Mei tetap menungguku"
        show Raven Rumahan Terdiam
        rb "{cps=25}...!!!"
        show Raven Before Terkejut
        rb "{cps=25}....!!"
        "{cps=25}tiba-tiba di tengah perjalanan"
        "{cps=25}Raven ditusuk dari belakang"
        "{cps=25}Raven hilang keseimbangan{p}membuat Raven jatuh tersungkur"
        "{cps=25}darah yang begitu banyak keluar{p}membuat Raven tak sanggup lagi menjaga kesadarannya"
        jump RavenDie
        
    "tidak ada":
        show Raven Sekolah Murung
        rb "{cps=25}{i}'maafkan aku Mei{p}tapi ini demi kebaikanmu'{/i}"
        show Raven Sekolah Berbicara Murung
        rb "{cps=25}tidak ada, Mei"
        show Mei Sekolah Terkejut
        m "{cps=25}kenapa?{p}sweet seventeen loh"
        show Raven Sekolah Beralasan
        rb "{cps=25}ya bagaimanapun juga{p}aku bukan anak kecil lagi"
        rb "{cps=25}ulang tahunnya tidak harus dirayakan"
        show Mei Sekolah Ramah with dissolve
        m "{cps=25}hmmm begitu ya"
        hide Mei Sekolah Ramah with dissolve
        "{cps=25}bel sekolah berbunyi tandanya jam belajar mengajar telah dimulai"
        show Mei Sekolah Berbicara with dissolve
        m "{cps=25}ah.. bel sudah bunyi tuh"
        m "{cps=25}kamu capek-capek datang kesini{p}cuma mau bilang itu saja?"
        show Raven Sekolah Berbicara
        rb "{cps=25}iya{p}itu saja, aku harus kembali ke kelas"
        rb "{cps=25}bye.."
        show Mei Sekolah Tersenyum with dissolve
        m "{cps=25}iya iya.."
        hide Mei Sekolah Tersenyum with dissolve
        "{cps=25}Raven dan Mei berpisah dari perpustakaan{p}lalu menuju ke kelas mereka masing-masing"
        scene bg Lorong Kelas Raven with fade
        "{cps=25}sesampainya Raven tiba di kelasnya.{p}rupanya Pak Rudi sudah masuk dikelasnya"
        "{cps=25}dan Astrid sedang berdiri di depan kelas{p}Raven menghampirinya"
        show Raven Sekolah Berbicara Datar
        rb "{cps=25}disetrap?"
        show Astrid Sekolah Menatap
        As "{cps=25}ya.. begitulah"
        show Raven Sekolah Diam
        rb "{cps=25}hmm..."
        "{cps=25}Raven tau, apa yang harus ia lakukan{p}ia ikut berdiri sama-sama dengan Astrid"
        show Astrid Sekolah Terkejut
        As "{cps=25}heh?!"
        show Raven Sekolah Berbicara Datar
        rb "{cps=25}kamu tak perlu kaget gitu{p}aku juga belum kerja tugasnya dia"
        rb "{cps=25}ya.. sekaligus temani kamu, gitu"
        show Astrid Sekolah Malu
        As "{cps=25}............."
        hide Astrid Sekolah Malu
        "{cps=25}Raven dan Astrid sama-sama disetrap berdiri di luar kelas{p}mereka mengobrol menghabiskan waktu hingga waktu hukuman mereka berakhir"
        scene bg Kelas Raven1 with fade
        "{cps=25}waktu hukuman mereka telah berakhir{p}dan mereka duduk di bangkunya masing-masing"
        scene bg Kelas Raven2 with dissolve
        "{cps=25}Raven mengikuti semua mata pelajaran, hingga jam sekolah berakhir"
        scene bg Raven House03 with fade
        "{cps=25}Raven pulang ke rumahnya{p}dan ia memantu ibunya untuk persiapan perayaan ultahnya"
        scene bg Raven House01 with dissolve
        "{cps=25}malampun tiba"
        "{cps=25}Raven merayakan ultahnya dengan teman dan keluarganya"
        "{cps=25}perayaan berlangsung lancar hingga akhir{p}Mei tidak datang ke acaranya, karena ia telah berbohong pada Mei"
        "{cps=25}seharusnya itu yang dipikirkan Raven bahwa ia berhasil{p}yaa.. itu seharusnya"
        "{cps=25}namun.....{w}."
        jump MeiDie

label kumpul_PR:
show Pak Rudi Berbicara
pr "{cps=25}baiklah anak-anak"
pr "{cps=25}silahkan kumpul tugas yang minggu lalu saya berikan"
show Raven Sekolah Terkejut
rb "{cps=25}matilah aku..."
pr "{cps=25}Raven.."
show Raven Sekolah Berbicara Murung
rb "{cps=25}iya pak?"
show Pak Rudi Menatap with dissolve
pr "{cps=25}punyamu mana?, teman yang lain sudah kumpul"
show Raven Sekolah Murung

menu:
        rb "{cps=25}um........"
    
        "maaf Pak, saya lupa kerjakan":
            show Raven Sekolah Berbicara Murung
            rb "{cps=25}maaf Pak, saya lupa kerjakan"
            show Pak Rudi Menatap 
            pr "{cps=25}apa kamu bilang?!!"
            show Pak Rudi Marah with dissolve
            pr "{cps=25}berdiri diluar, SEKARANG!!"
            rb "{cps=25}baiklah Pak"
            jump dihukum

        "maaf Pak, buku saya ketinggalan":
            show Raven Sekolah Berbicara Murung
            rb "{cps=25}maaf Pak, buku saya ketinggalan"
            show Pak Rudi Menatap 
            pr "{cps=25}apa kamu bilang?!!"
            pr "{cps=25}kamu kira, saya percaya sama omonganmu?!"
            show Pak Rudi Marah with dissolve
            pr "{cps=25}berdiri diluar, SEKARANG!!"
            show Raven Sekolah Murung
            rb "{cps=25}..."
            "{cps=25}Raven segera beranjak dari bangkunya"
            jump dihukum
        
        "maaf Pak, saya belum selesaikan semua":
            show Raven Sekolah Berbicara Murung
            rb "{cps=25}maaf Pak, saya belum selesaikan semua"
            show Pak Rudi Menatap 
            pr "{cps=25}apa maksudmu?"
            rb "{cps=25}aku belum selesai, karena ada yang belum aku pahami pak"
            show Pak Rudi Berbicara with dissolve
            pr "{cps=25}hmm...{w}begitu ya"
            pr "{cps=25}bagian mana yang belum kamu pahami?"
            pr "{cps=25}coba kamu bawa pr kamu kesini"
            if kerja:
                "{cps=25}Raven membawa bukunya ke depan meja Pak Rudi"
                show Raven Sekolah Berbicara
                rb "{cps=25}bagian ini, Pak"
                show Pak Rudi Berbicara
                pr "{cps=25}yang mana?"
                rb "{cps=25}yang ini, Pak"
                hide Pak Rudi Berbicara
                "{cps=25}Raven menunjukkan pr-nya yang baru dia kerjakan"
                "{cps=25}dan Pak Rudi menjelaskan, bagian yang Raven belum selesaikan"
                show Raven Sekolah Tersenyum
                rb "{cps=25}terima kasih, Pak"
                show Pak Rudi Berbicara
                pr "{cps=25}kamu duduk dan selesaikan itu"
                show Raven Sekolah Berbicara
                rb "{cps=25}baiklah, Pak"
                jump lolos
            else:
                
                show Raven Sekolah Berbicara Datar
                rb "{cps=25}waduh.."
                rb "{cps=25}{i}'sial!!'{/i}"
                show Pak Rudi Berbicara
                pr "{cps=25}kenapa kamu?"
                show Pak Rudi Menatap with dissolve
                pr "{cps=25}jangan bilang, kamu berusaha membohongiku?"
                show Raven Sekolah Berbicara Murung
                rb "{cps=25}maaf Pak, sebenarnya aku belum kerja"
                pr "{cps=25}kamu ini, sudah malas kerja pr"
                pr "{cps=25}masih tidak jujur lagi!"
                show Pak Rudi Marah with dissolve
                pr "{cps=25}berdiri diluar, SEKARANG!!"
                show Raven Sekolah Murung
                rb "{cps=25}....."
                jump dihukum
            
            
label dihukum:
scene bg Lorong Kelas Raven
"{cps=25}Raven disetrap berdiri diluar kelas"
"{cps=25}kali ini, ia ditemani Asrid"
"{cps=25}Astrid adalah teman sekelasnya"
"{cps=25}mereka berdua sama-sama disetrap berdiri luar dikelas"
show Astrid Sekolah Berbicara
As "{cps=25}um.. Raven"
show Raven Sekolah Diam
rb "{cps=25}hm?"
As "{cps=25}ah.. tidak jadi.."
rb "{cps=25}...?"
show Raven Sekolah Berbicara Datar
rb "{cps=25}kalau ada sesuatu yang ingin kau katakan, katakan saja"
As "{cps=25}kenapa-.."
show Raven Sekolah Diam
rb "{cps=25}.......?"
show Astrid Sekolah Menatap
As "{cps=25}kenapa, kamu tidak kerja pr sejarah?"
show Raven Sekolah Terkejut
rb "{cps=25}heh?... hmm.."
menu :
    "menemanimu":
        show Raven Sekolah Berbicara
        rb "{cps=25}menemanimu, agar tidak sendiri"
        As "{cps=25}apa kau mengejekku?"
        show Raven Sekolah Berbicara Datar
        rb "{cps=25}aku tidak mengejekmu{p}aku memang mau menemanimu doang"
        show Astrid Sekolah Malu
        As "{cps=25}........"
        rb "{cps=25}{i}'kenapa wajahmu seperti itu'{/i}"
        jump lanjutkan1
    "saya tidak suka pelajaran sejarah":
        show Raven Sekolah Berbicara Datar
        rb "{cps=25}well.. sebenarnya aku tidak terlalu suka pelajaran sejarah"
        rb "{cps=25}dan juga, aku tidak suka masa lalu{p}masa lalu, hanya membuatmu terhambat untuk maju"
        show Astrid Sekolah Malu
        As "{cps=25}hmm begitu ya..{p}kebetulan ya, pemikiran kita sama"
        rb "{cps=25}{i}'kenapa wajahmu seperti itu'{/i}"
        jump lanjutkan1
label lanjutkan1:
show Astrid Sekolah Berbicara
As "{cps=25}eheem, kita ke kantin aja yuk"
show Raven Sekolah Berbicara Datar
rb "{cps=25}{i}'kelihatan sekali, bahwa dia berusaha mengalihkan pembicaraan'{/i}"
rb "{cps=25}untuk apa?"
As "{cps=25}ya, untuk makan lah{p}lagipula gak enak berdiri trus diluar kayak gini"
show Raven Sekolah Berpikir
rb "{cps=25}..........."
menu:
    "terima":
        show Raven Sekolah Berbicara
        rb "{cps=25}hmmm boleh juga"
        if sopan:
            show Raven Sekolah Berbicara Datar
            rb "{cps=25}tapi, gak apa-apa kan?"
            show Astrid Sekolah Berbicara
            As "{cps=25}gak apa-apa"
        else:
            show Raven Sekolah Berbicara
            rb "{cps=25}kebetulan aku belum sarapan tadi pagi"
            show Astrid Sekolah Berbicara
            As "{cps=25}tuh, kan"
        show Raven Sekolah Berbicara
        rb "{cps=25}kalau begitu, yuk!"
        scene bg blck
        "{cps=25}Raven dan Astrid pergi ke kantin"
        scene bg Kantin
        "{cps=25}sesampainya di kantin, mereka memesan makanan dan ngobrol dengan asiknya{p}sampai mereka lupa tentang masalah tadi"
        "{cps=25}tanpa sadar, waktu pelajaran pertama telah usai"
        rb "{cps=25}balik yuk"
        show Astrid Sekolah Tersenyum
        As "{cps=25}yuk!"
        hide Astrid Sekolah Tersenyum
        scene bg blck
        "{cps=25}mereka kembali kekelas.."
        scene bg Kelas Raven1 with fade
        "{cps=25}tapi, sesampainya disana kelas sudah bubar"
        "{cps=25}kelas dipulangkan, karena guru sedang rapat mendadak"
        show Raven Sekolah Terkejut
        rb "{cps=25}heh? bukannya ini terlalu mendadak?"
        show Astrid Sekolah Menatap
        As "{cps=25}iya ya.{p}ini terlalu mendadak"
        show Raven Sekolah Berbicara Datar
        rb "{cps=25}ah bodoh amat, sebaiknya aku mencari Mei, dulu"
        show Astrid Sekolah Terkejut
        As "{cps=25}heh? ada apa dengan Mei?"
        rb "{cps=25}bye..! aku pergi dulu"
        hide Astrid Sekolah Terkejut
        scene bg Kelas Mei
        "{cps=25}Raven mencari Mei di kelasnya"
        show Raven Sekolah Terkejut
        rb "{cps=25}apa kalian melihat Mei?"
        "{cps=25}Kelasnya sudah Kosong"
        scene bg Perpus01
        "{cps=25}Raven melanjukan mencari di perpus"
        "{cps=25}tapi, kemanapun Raven mencari"
        "{cps=25}ia tak menemukan Mei lagi"
        show Raven Sekolah Serius
        rb "{cps=25}aaaa... dimana Mei?"
        "{cps=25}Raven mengambil ponselnya"
        "{cps=25}dan berusaha menghubungi Mei"
        "{cps=25}.............{w}.........."
        "{cps=25}..............{w}.........."
        "{cps=25}tapi Mei tidak mengangkat telponnya"
        show Raven Sekolah Murung
        rb "{cps=25}............"
        show Raven Sekolah Berbicara Murung with dissolve
        rb "{cps=25}sebaiknya aku pulang saja"
        scene bg blck
        "{cps=25}Raven menyerah dan iapun memutuskan untuk pulang"
        jump lanjutkan2
        
    "tolak":
        show Raven Sekolah Berbicara Murung
        rb "{cps=25}lebih baik jangan deh...{p}nanti kita tambah dihukum"
        show Raven Sekolah Berbicara Datar with dissolve
        rb "{cps=25}kamu tau kan, Pak Rudi kayak gimana"
        show Astrid Sekolah Menatap
        As "{cps=25}baiklah...{p}kamu gak asik deh"
        show Astrid Sekolah Berbicara with dissolve
        As "{cps=25}tapi, kalau ke perpus bagaimana?"
        show Raven Sekolah Berbicara Datar
        rb "{cps=25}untuk apa lagi sih?"
        show Astrid Sekolah Berbicara
        As "{cps=25}ya, untuk kerja pr disana{p}aku tidak nyaman berdiri trus diluar kayak gini"
        scene bg blck
        show Raven Sekolah Diam
        rb "{cps=25}{i}'ah.. betul juga'{/i}"
        rb "{cps=25}{i}'mungkin, aku bisa meninggalkan pesan untuk Mei'{/i}"
        rb "{cps=25}{i}'semoga saja bisa'{/i}"
        scene bg Lorong Kelas Raven with fade
        show Raven Sekolah Berbicara
        rb "{cps=25}yuk ke perpus.."
        show Astrid Sekolah Berbicara
        As "Yuuk..!"
        scene bg blck
        "{cps=25}Raven dan Astrid menuju ke perpustakaan yang lumayan dekat dari kelasnya"
        scene bg Perpus01 with dissolve
        "{cps=25}sampailah mereka di perpustakaan"
        "{cps=25}Astrid mengabil tempat duduk dekat pintu{p}sedangkan Raven pergi ke lobby untuk mencari buku peminjam"
        "{cps=25}kemudian ia mencari nama Mei di buku tersebut{p}setelah mengetahuinya, ia berniat menulis tulisan kecil di belakang buku tersebut"
        show Raven Sekolah Berpikir
        rb "{cps=25}{i}'tapi, mencoret di buku perpus dihukum gak ya?'{/i}"
        show Raven Sekolah Diam
        rb "{cps=25}{i}'ah sudahlah, bodoh amat'{/i}"
        "{cps=25}Ravenpun menulis..."
        mem "{cps=25}kumohon mei{p=0.5}jangan datang ke acaraku{p=0.5}karena bahaya sedang mengintaimu{p=0.5}percaya atau tidak, aku datang dari masa depan untuk-{p=0.5}----------"
        "{cps=25}sementara Raven menulis"
        "{cps=25}tiba-tiba"
        play sound "Sound Effect/Heart_Beat01-3L.mp3"
        queue sound "Sound Effect/Heart_Beat01-3L.mp3"
        "{cps=25}jantungnya berdetak tak beraturan"
        "{cps=25}dan Raven hilang kesadaran, sehingga ia terjatuh"
        jump melanggar1

label lanjutkan2:
scene bg R_Home01
"{cps=25}Raven pulang ke rumahnya{p}dan ia memantu ibunya untuk persiapan perayaan ultahnya"
scene bg R_Home02 with dissolve
scene bg R_Home03 with dissolve
"{cps=25}malampun tiba"
"{cps=25}Sebelum memulai acaranya{p}Raven keluar dari rumah"
"{cps=25}dan hendak pergi ke rumah Mei{p}berniat untuk menjemputnya"
show Raven Rumahan Diam
rb "{cps=25}semoga Mei sedang menungguku"
show Raven Rumahan Terdiam
rb "{cps=25}...?"
"{cps=25}tiba-tiba di tengah perjalanan{p}Astrid memegang tangan Raven dari belakang"
show Astrid Rumahan Khawatir
As "{cps=25}Apakah semua baik-baik saja?"
show Raven Rumahan Penasaran1
rb "{cps=25}Ya.. baik-baik saja{p}aku hanya ingin menjemput Mei"
As "{cps=25}boleh aku ikut denganmu?{p}soalnya wajahmu  sedang ketakutan akan sesuatu"
show Raven Rumahan Berpikir
rb "{cps=25}{i}'apakah wajahku memang kelihatan begitu?'{/i}"
rb "{cps=25}{i}'tapi, dia kan cewek'{p}'ini sangat berbahaya kalau dia ikut'{/i}"
menu:
    rb "{cps=25}hmmm........"
    "aku bisa sendiri":
        show Raven Rumahan Tertawa
        rb "{cps=25}aku tidak apa-apa{p}aku bisa sendiri"
        show Astrid Rumahan Khawatir
        As "{cps=25}apa kau yakin?"
        rb "{cps=25}ya{p}kamu tunggu saja disitu"
        rb "{cps=25}aku pergi tidak lama kok"
        hide Astrid Rumahan Khawatir
        scene bg blck
        "{cps=25}Raven pura-pura tesenyum agar tidak membuat Atrid khawatir"
        "{cps=25}Raven memutuskan untuk pergi sendirian"
        scene bg Jalan Malam
        "{cps=25}sementara ditengah jalan"
        show Killer IV Diam with dissolve
        "{cps=25}Raven bertemu dengan si pembunuh berantai tersebut"
        show Raven Rumahan Terdiam
        rb "{cps=25}............."
        rb "{cps=25}{i}'aku harus melawannya'{/i}"
        show Raven Rumahan Berantem
        rb "{cps=25}maju sini!"
        hide Killer IV Diam with dissolve
        scene bg blck
        "{cps=25}Raven maju dan berusaha melawan pembunuh tersebut"
        "{cps=25}namun.."
        "{cps=25}Raven tidak punya kemampuan bela diri{p}sehingga Raven terbunuh malam itu"
        jump RavenDie
    "baiklah, ikut denganku":
        
        show Raven Rumahan Sedih
        rb "{cps=25}apa kau yakin ikut denganku?"
        show Astrid Rumahan Khawatir
        As "{cps=25}ya.. tentu saja"
        rb "{cps=25}tapi, perjalanan ini sangat berbahaya untukmu"
        show Astrid Rumahan Tersenyum
        As "{cps=25}apa maksudmu?{p}sudahlah, ayo.."
        show Raven Rumahan Penasaran1
        rb "{cps=25}{i}'apakah ini tidak apa-apa?'{/i}"
        show Raven Rumahan Diam
        rb "{cps=25}{i}'ya.. sudahlah'{/i}"
        scene bg blck
        "{cps=25}Raven dan Astrid pergi bersama untuk menjemput Mei"
        scene bg Jalan Malam
        rb "{cps=25}semoga Mei sedang menungguku.."
        "{cps=25}sementara mereka ditengah jalan"
        show Killer IV Diam with dissolve
        play music "BGM/008-Fight With Killer V-kurai tuuro.mp3" fadeout 1
        "{cps=25}mereka bertemu dengan si pembunuh berantai tersebut"
        show Raven Rumahan Terdiam
        rb "{cps=25}............."
        hide Killer IV Diam
        show Astrid Rumahan Serius
        As "{cps=25}........."
        As "{cps=25}apakah ini yang kau maksudkan, Raven?"
        "{cps=25}Raven Hanya Mengangguk, sementara berpikir untuk rute pelarian"
        show Astrid Rumahan Menantang
        As "{cps=25}aku tidak tau, kamu siapa{p}tapi, akan kupatahkan tanganmu"
        hide Astrid Rumahan Menantang
        show Killer IV Diam
        show Killer IV Menyerang with dissolve
        t "{cps=25}......"
        hide Killer IV Menyerang
        show Astrid Rumahan Berantem
        As "{cps=25}maju sini!"
        show Raven Rumahan Terkejut
        rb "{cps=25}Astrid!{p}apa yang kau pikirkan?!"
        As "{cps=25}hiiiaah!"
        hide Astrid Rumahan Berantem
        "{cps=25}Astrid langsung berlari menuju orang itu"
        "{cps=25}setelah menendang pisau yang dipegang orang itu hingga terlepas{p}Astrid langsung memegang tangan orang itu"
        play sound "Sound Effect/005-Astrid Mematahkan.mp3"
        "{cps=25}kemudian membantingnya dengan keras"
        "{cps=25}kejadian itu berlangsung sangat cepat{p}hingga Raven hanya terpukau melihat aksi Astrid"
        show Raven Rumahan Terdiam
        rb "{cps=25}{i}'aku baru ingat, bahwa yang pernah mematahkan tulang lenganku'{p}'adalah Astrid'{/i}"
        rb "{cps=25}{i}'Astrid, gadis yang menyeramkan'{p}'lebih baik aku tidak terlalu cari masalah dengannya'{/i}"
        "{cps=25}Astrid mengunci tangan orang itu yang sedang terbaring kesakitan"
        show Astrid Rumahan Menantang
        As "{cps=25}siapa kau?{p}apa maumu?!"
        t "*tertawa dalam*{cps=25}kuh..kuh.."
        t "{cps=25}KALIAN KETURUNAN BLANSOVIC HARUS MENDERITA!!!!!"
        show Raven Rumahan Berpikir
        rb "{cps=25}{i}'Blansovic?'{p}'entah kenapa, aku sangat familiar dengan nama itu'{/i}"
        stop music fadeout 1
        scene bg blck
        show image "images/Scene/Killer IV Terjatuh.png"
        t "*melotot kearah Raven dengan tajam*{p}{cps=25}dimulai dari kau!"
        hide image "images/Scene/Killer IV Terjatuh.png"
        
        scene bg Jalan Malam
        show Astrid Rumahan Awas
        As "{cps=25}Raven dibelakangmu!!!"
        show Raven Rumahan Terdiam
        rb "{cps=25}....?"
        show Raven Rumahan Terkejut
        play sound "Sound Effect/009-Raven Tertusuk.mp3"
        rb "{cps=25}....!!"
        "{cps=25}tiba-tiba Raven ditusuk dari belakang"
        play sound "Sound Effect/009-Raven Terjatuh.mp3"
        "{cps=25}Raven hilang keseimbangan{p}membuat Raven jatuh tersungkur"
        show Astrid Rumahan Terkejut        
        As "{cps=25}RAVEN!!!!!"
        hide Astrid Rumahan Terkejut        
        scene bg blck
        "{cps=25}darah yang begitu banyak keluar{p}membuat Raven tak sanggup lagi menjaga kesadarannya"
        jump RavenDie
        
        
label lolos:
scene bg Kelas Raven1
"{cps=25}Raven duduk kembali ke bangkunya{p}dan mulai mengerjakan prnya yang belum selesai"
"{cps=25}sambil ia mendengar pelajaran yang disampaikan Pak Rudi"
"{cps=25}jam pelajaran sejarah pun berakhir"
"{cps=25}Astrid masuk dalam kelas{p}dan duduk kembali di bangkunya"
scene bg Kelas Raven2 with dissolve
"{cps=25}Raven mengikuti semua mata pelajaran, hingga jam sekolah berakhir"
scene bg blck
"{cps=25}Raven ingin mencari Mei setelah pulang sekolah{p}tapi, sepertinya Mei sudah pulang dari tadi"
"{cps=25}sebab, dimanapun Raven mencari Mei{p}Mei tidak ada di lingkungan sekolah lagi"
show Raven Sekolah Berpikir
rb "{cps=25}hmmm..."
menu:
    "pulang saja":
        show Raven Sekolah Berbicara Murung
        rb "{cps=25}mungkin sebaiknya aku pulang saja"
        "{cps=25}Raven memtuskan untuk pulang kerumahnya"
        scene Raven House03
        "{cps=25}sesampainya dirumah"
        "{cps=25}Raven membantu ibunya untuk perayaan ultahnya{p}hingga malam"
        scene Raven House01 with dissolve
        "{cps=25}malam Perayaanpun tiba.."
        "{cps=25}Raven merayakan ultahnya dengan teman dan keluarganya"
        "{cps=25}perayaan berlangsung lancar hingga akhir{p}Mei tidak datang ke acaranya, karena ia belum mengundang Mei"
        "{cps=25}seharusnya itu yang dipikirkan Raven bahwa ia berhasil{p}yaa.. itu seharusnya"
        "{cps=25}namun.....{w}."
        jump MeiDie
        
    "singgah ke rumah Mei":
        show Raven Sekolah Berbicara
        rb "{cps=25}mungkin, sebaiknya aku ke rumah dia saja"
        scene bg blck
        "{cps=25}Raven memutuskan untuk pergi ke rumah Mei sebelum pulang ke rumahnya"
        scene bg Mei House
        play music "BGM/005-Mei House-himatubusi.mp3" fadeout 1
        "{cps=25}sampailah Raven di rumahnya Mei"
        show Raven Sekolah Diam
        rb "{cps=25}{i}'semoga aja, Mei ada..'{/i}"
        rb "{cps=25}*menekan bel rumah*{p}permisi.."
        "{cps=25}..."
        "{cps=25}pintu rumah terbuka"
        show Tante Rika Berbicara
        r "{cps=25}iya...?{p}eh.. rupanya Raven"
        "{cps=25}ia adalah Tante Rikka{p}ibunya Mei"
        show Raven Sekolah Berbicara
        rb "{cps=25}selamat siang...maaf menggangu, tante{p}Mei ada?"
        r "{cps=25}ah. ada{p}baru aja pulang"
        show Tante Rika Ramah with dissolve
        r "{cps=25}mari masuk"
        show Raven Sekolah Tersenyum
        rb "{cps=25}kalau begitu, permisi"
        hide Tante Rika Ramah
        scene bg In Mei Home
        "{cps=25}setelah diberi izin masuk{p}Raven masuk ke dalam rumahnya Mei"
        show Mei Sekolah Terkejut
        m "{cps=25}heh? Raven?{p}kenapa kamu disini?"
        hide Mei Rumahan Terkejut
        show Tante Rika Berbicara
        r "{cps=25}ibu yang izinini masuk"
        show Raven Sekolah Berbicara
        rb "{cps=25}maaf datang tiba-tiba"
        hide Tante Rika Berbicara
        show Mei Sekolah Berbicara
        m "{cps=25}ah.. sudahlah{p}tidak apa-apa kok"
        hide Mei Sekolah Berbicara
        scene bg Ruang Tamu Mei with fade
        show Tante Rika Ramah
        r "{cps=25}Raven duduk dulu{p}Mei buatkan minuman untuknya"
        show Raven Sekolah Berbicara
        rb "{cps=25}ah sudah gak perlu repot-repot{p}aku hanya perlu cepat dengan Mei"
        show Tante Rika Berbicara
        r "{cps=25}hmmm...begitu ya"
        hide Tante Rika Berbicara with moveoutleft
        "{cps=25}Tante Rikka pergi meninggalkan mereka{p}kini mereka hanya berduaan di ruang tamu"
        show Mei Sekolah Tersenyum
        m "{cps=25}oh iya, kamu ulang tahun ya{p}selamat ulang tahun, Raven"
        show Raven Sekolah Berbicara
        rb "{cps=25}terima kasih"
        show Mei Sekolah Berbicara
        m "{cps=25}jadi, kamu ada perlu apa denganku?{p}jangan bilang, kamu hanya ingin mendengar ucapan dariku?"
        show Raven Sekolah Berbicara Murung
        rb "{cps=25}hanya, katamu?{p}aku-"
        show Raven Sekolah Serius
        rb "{cps=25}ah sudahlah..{p}ada yang lebih penting dari itu"
        scene bg blck
        show Raven Sekolah Berpikir
        rb "{cps=25}{i}'salah satu cara ampuh, supaya Mei tetap hidup'{/i}"
        rb "{cps=25}{i}'semoga ini berhasil'{/i}"
        scene bg Ruang Tamu Mei with fade
        show Raven Sekolah Berbicara Datar
        rb "{cps=25}Mei ikut denganku, ke rumahku"
        show Mei Sekolah Terkejut
        m "{cps=25}heh? sekarang?{p}ada apa emangnya?"
        hide Mei Sekolah Terkejut
        scene bg blck
        show Raven Sekolah Berpikir
        rb "{cps=25}{i}'ah betul juga, agak aneh jika aku mengajaknya tiba-tiba'{/i}"
        rb "{cps=25}{i}'aku harus membuatnya agar tidak bisa menolak'{/i}"
        scene bg Ruang Tamu Mei with fade
        show Raven Sekolah Beralasan
        rb "{cps=25}um... {p}mamaku titip pesan untuk menjemputmu"
        show Raven Sekolah Berbicara
        rb "{cps=25}katanya, ingin kamu untuk membantunya dalam mempersiapkan acara ultah nanti"
        show Mei Sekolah Ramah
        m "{cps=25}oh gitu..{p}tunggu ya... aku bersiap dulu"
        hide Mei Sekolah Ramah with moveoutleft
        "{cps=25}Mei pergi ke kamarnya untuk bersiap"
        show Raven Sekolah Berbicara
        rb "{cps=25}apa kau tak perlu izin dari Tante Rikka dulu?"
        r "{cps=25}aku mengizinkan loh"
        "{cps=25}suara Tante Rikka yang samar-samar dari dapur, memberikan izin untuk Mei pergi bersama Raven"
        rb "{cps=25}terima kasih, Tante"
        r "{cps=25}iya.. {p}dan juga selamat ulang tahun ya, Raven"
        scene bg Dapur Mei with dissolve
        "{cps=25}Raven pergi ke dapur, untuk berbicara dengan Tante Rikka"
        show Raven Sekolah Tersenyum
        rb "{cps=25}terima kasih, Tante{p}atas ucapannya"
        show Tante Rika Ramah
        r "{cps=25}sama-sama.{p}eh...kamu sudah makan?"
        show Tante Rika Berbicara
        r "{cps=25}makan dulu, baru pergi"
        show Raven Sekolah Berbicara
        rb "{cps=25}ah sudah, gak apa-apa"
        hide Tante Rika Berbicara
        m "{cps=25}maaf menunggu.."
        "{cps=25}mei kembali dari kamarnya, setelah ia bersiap-siap"
        show Mei Rumahan Tersenyum
        m "{cps=25}yuk.."
        show Mei Rumahan Berbicara
        m "{cps=25}bu, aku pergi dulu"
        hide Mei Rumahan Berbicara
        show Tante Rika Berbicara
        r "{cps=25}iya..hati-hati, ya"
        show Raven Sekolah Berbicara
        rb "{cps=25}kalau begitu, aku pamit dulu Tante"
        r "{cps=25}iya... hati-hati{p}jaga baik-baik Mei, ya"
        rb "{cps=25}baik!"
        hide Tante Rika Berbicara
        stop music fadeout 1
        scene bg blck
        "{cps=25}Raven dan Mei langsung menuju rumah Raven menggunakan angkot"
        scene bg R_Home02 with fade
        "{cps=25}tak lama kemudian, sampailah mereka di depan rumahnya Raven"
        show Mama Berbicara
        m "{cps=25}sudah lama ya{p}aku tidak pernah main lagi kesini sejak 2 tahun lalu"
        hide Mama
        scene bg Raven House02 with dissolve
        "{cps=25}Raven dan Mei kini didalam rumah Raven"
        "{cps=25}keberadaan Mei disambut baik oleh ibunya Raven"
        scene bg Raven House03 with dissolve
        "{cps=25}mereka mengobrol santai bersama, makan siang bersama{p}hingga sorepun tiba"
        "{cps=25}mereka saling bekerja sama dalam mempersiapkan acara ultah{p}mulai dari makanan hingga dekorasi"
        scene bg Raven House01 with dissolve
        "{cps=25}malampun tiba"
        "{cps=25}pada saat malam perayaanpun tiba{p}acara perayaan berlangsung dengan lancar hingga berakhir dengan baik"
        
        if sopan:
            scene bg Raven House01
            "{cps=25}setelah mereka selesai beres-beres, Mei ingin pulang"
            show Mama Berbicara
            i "{cps=25}ah.. Mei jangan pulang{p}ini sudah malam"
            i "{cps=25}bahaya kalau gadis jalan malam-malam{p}bagaimana kamu nginap saja disini"
            i "{cps=25}benar kan, Raven?"
            hide Mama Berbicara
            show Raven Rumahan Senyum
            rb "{cps=25}{i}'nice idea, ma!'{/i}"
            rb "{cps=25}{i}'aku sudah kehabihan ide'{/i}"
            rb "{cps=25}{i}'bagaimana supaya Mei tidak kemana-mana'{/i}"
            show Mei Rumahan Terkejut
            m "{cps=25}eh? bentar aku minta izin ibuku dulu" 
            hide Mei Rumahan Terkejut
            "{cps=25}Mei Menelpon Ibunya untuk meminta izin"
            show Raven Rumahan Berbicara
            rb "{cps=25}bagaimana?"
            show Mei Rumahan Tersenyum
            m "{cps=25}aku diizinkan."
            show Raven Rumahan Tersenyum
            rb "{cps=25}{i}'nice assist, Tante!'{/i}"
            show Mei Rumahan Berbicara
            m "{cps=25}kenapa wajahmu kegirangan begitu?"
            show Raven Rumahan Bahagia
            rb "{cps=25}ah.. tidak{p}aku senang soal perayaan tadi"
            show Mei Rumahan Ramah
            m "{cps=25}hmm begitu ya"
            show Mei Rumahan Berbicara with dissolve
            m "{cps=25}maaf merepotkan bu, aku harus menginap disini"
            hide Mei Rumahan Berbicara
            show Mama Berbicara
            i "{cps=25}ah.. tidak merepotkan kok{p}lagipula kamu sudah lama sekali gak pernah main kesini lagi"
            i "{cps=25}anggap aja ini rumahmu{p}silahkan main-main seperti dulu"
            show Mei Rumahan Berbicara
            m "{cps=25}kalau begitu, baiklah bu"
            "{cps=25}mereka menghabiskan waktu bersama{p}bercerita, bermain bersama hingga hampir larut malam"
            show Mama Berbicara
            i "{cps=25}ibu tidur duluan ya{p}ibu sudah capek, besok juga harus kerja."
            i "{cps=25}kamu jangan macem-macem ya, Raven!"
            show Raven Rumahan Berbicara
            rb "{cps=25}gak akan..."
            "{cps=25}ibunya Raven masuk kekamarnya"
            rb "{cps=25}well.. kamu bisa gunakan kamarku{p}aku nanti tidur di ruang tamu saja"
            scene bg blck
            show Raven Rumahan Berpikir
            rb "{cps=25}{i}'ada satu hal lagi yang mengganjal dipikiranku'{/i}"
            rb "{cps=25}{i}'aku harus mengatakannya'{/i}"
            scene bg Raven House01
            show Raven Rumahan Sedih
            rb "{cps=25}um...., Mei{p}aku minta maaf soal itu, aku akan menggantinya"
            show Mei Rumahan Ramah
            m "{cps=25}ah.. soal itu?{p}sudahlah, tidak apa-apa"
            show Mei Rumahan Berbicara
            m "{cps=25}lagipula, kamu tidak sengaja kan?{p}aku tidak marah kok, jadi kau tak perlu khawatir"
            rb "{cps=25}sekali lagi, aku minta maaf{p}bagaimanapun juga itu benda berhargamu"
            show Mei Rumahan Tersenyum
            m "{cps=25}sudahlah."            
            show Mei Rumahan Berbicara
            m "{cps=25}sudah malam nih, aku tidur dulu ya{p}kamu jangan bergadang ya"
            show Raven Rumahan Diam
            rb "........."
            hide Mei Rumahan Berbicara
            jump ending2
        else:
            scene bg Raven House01
            "{cps=25}setelah mereka selesai beres-beres, Mei ingin pulang"
            show Raven Rumahan Berbicara
            rb "{cps=25}aku akan mengantarmu"
            "{cps=25}Raven ingin mengantar pulang ke Rumahnya"
            rb "{cps=25}semoga aja masih ada Taksi jam segini"
            scene bg Lorong Malam
            "{cps=25}sementara ditengah jalan"
            show Killer IV Diam
            "{cps=25}mereka bertemu dengan si pembunuh berantai tersebut"
            play music "BGM/002-Escape From Killer IV-Poisonous-David_Fesliyan.mp3" fadeout 1
            jump bahaya
            
label bahaya:
scene bg Lorong Malam
show Raven Rumahan Terdiam
rb "{cps=25}perasaanku tidak enak"
show Mei Rumahan Takut
"{cps=25}Mei Ketakutan, dan ia memegang tangan Raven dengan erat"
menu :
    "Lari!":
        scene bg Lorong Malam
        "{cps=25}Raven menarik tangan Mei{p}segera lari dari situ!"
        "{cps=25}Raven dan Mei berlari sekuat tenaga{p}berusaha menjauh dari pembunuh tersebut"
        scene bg blck
        "{cps=25}namun..."
        "{cps=25}pembunuh tersebut melempar sebilah pisau{p} hingga mengenai tepat di kepala Mei"
        show image "images/Scene/Mei_Rumahan_Scene 02.png"
        "{cps=25}Mei meninggal ditempat{p}dengan kepala yang bersibah darah"
        show Raven Rumahan Terkejut
        rb "{cps=25}......!!!"
        "{cps=25}Raven menjadi ketakutan, dan tak bisa bergerak lagi"
        "{cps=25}pembunuh tersebut mendekati Raven{p}lalu membunuhnya"
        "{cps=25}Raven dan Mei terbunuh malam itu"
        jump RavenDie
        
    "Lawan Pembunuh tersebut":
        scene bg Lorong Malam
        show Raven Rumahan Berantem
        rb "{cps=25}tetap dibelakangku Mei"
        "{cps=25}Raven maju dan berusaha melawan pembunuh tersebut"
        scene bg blck
        "{cps=25}namun.."
        "{cps=25}Raven tidak punya kemampuan bela diri{p}sehingga Raven terbunuh malam itu"
        jump RavenDie

return