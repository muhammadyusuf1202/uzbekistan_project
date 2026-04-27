"""
places_data.py - O'zbekiston joylari haqida barcha ma'lumotlar
Har bir joy uchun: nomi, tavsif, qiziqarli faktlar, rasm URL
"""

# Joylar lug'ati: kalit = joy ID, qiymat = ma'lumotlar
PLACES = {
    # =================== QORAQALPOG'ISTON ===================
    "orol_dengizi": {
        "id": "orol_dengizi",
        "viloyat": "Qoraqalpog'iston Respublikasi",
        "nomi": "Orol Dengizi",
        "emoji": "🌊",
        "tavsif": (
            "Orol dengizi — bir vaqtlar dunyodagi to'rtinchi eng katta ko'l bo'lgan. "
            "Lekin 1960-yillardan boshlab, Amudaryo va Sirdaryo suvlari paxta dalariga "
            "burilgani tufayli dengiz qurib ketdi. Bugun u ekologik falokatning ramziga aylangan. "
            "Qadimgi dengiz tubida eski kemalar zanglayapti — bu manzara olamda boshqa hech yerda ko'rinmaydi."
        ),
        "faktlar": [
            "1960-yilda maydoni 68,000 km² bo'lgan, bugun 10% dan kam qoldi",
            "Dengiz sathining tushishi 16 metrdan ortiq bo'ldi",
            "Eski port shahri Mo'ynoq dengizdan 150 km uzoqda qoldi",
            "Tuz va kimyoviy moddalar shamol orqali atrofga tarqalmoqda",
            "Bu ekologik falokat 20-asr eng katta ekologik ofati deb tan olingan",
        ],
        "rasm_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/96/AralSea1989_2008.jpg/640px-AralSea1989_2008.jpg",
        "qiziqarli": "Kemalar qabristoni — Orol dengizining qurib qolgan tubidagi zanglagan kemalar dunyodagi eng sirli manzaralardan biri hisoblanadi.",
    },
    "savitskiy_muzeyi": {
        "id": "savitskiy_muzeyi",
        "viloyat": "Qoraqalpog'iston Respublikasi",
        "nomi": "Savitskiy Muzeyi (Nukus Muzeyi)",
        "emoji": "🎨",
        "tavsif": (
            "Igor Savitskiy muzeyi Nukus shahrida joylashgan bo'lib, u 'cho'ldagi Louvr' deb ataladi. "
            "Muzey sovet davri taqiqlangan avangard san'ati, qoraqalpoq xalq san'ati va "
            "Markaziy Osiyo arxeologiyasining noyob kolleksiyasini o'z ichiga oladi. "
            "Savitskiy ko'plab san'at asarlarini maxfiy ravishda yig'ib, ularni sovet ta'qibidan saqlab qoldi."
        ),
        "faktlar": [
            "Kolleksiyada 90,000 dan ortiq eksponat mavjud",
            "Dunyoning 2-chi eng yirik rus avangard san'ati to'plami",
            "Ko'plab asarlar sovet davrida taqiqlangan edi",
            "Savitskiy ularni cho'l sharoitida yashirib saqladi",
            "2010-yilda 'Cho'ldagi San'atchi' hujjatli film suratga olingan",
        ],
        "rasm_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5d/Nukus_museum.jpg/640px-Nukus_museum.jpg",
        "qiziqarli": "Muzey Nukusda, Qoraqum cho'li yaqinida joylashgan — eng so'nggi joyda, lekin dunyodagi eng qimmatli san'at to'plamlaridan biri.",
    },

    # =================== ANDIJON ===================
    "bobur_bogi": {
        "id": "bobur_bogi",
        "viloyat": "Andijon viloyati",
        "nomi": "Bobur Bog'i",
        "emoji": "🌳",
        "tavsif": (
            "Zahiriddin Muhammad Bobur — Andijonning farzandi, buyuk shoir, jangchi va Boburiylar sulolasining asoschisi. "
            "Uning sharafiga qurilgan bog' Andijon shahrida joylashgan. "
            "Bobur 1483-yilda Andijonda tug'ilgan va keyinchalik Hindistonda Boburiylar imperiyasini barpo etgan. "
            "Uning 'Boburnoma' asari dunyo adabiyotining durdonalaridan sanaladi."
        ),
        "faktlar": [
            "Bobur 1483-1530 yillarda yashagan",
            "'Boburnoma' — o'z hayotini o'zi yozgan birinchi avtobiografiyalardan",
            "Hindistondagi Boburiylar imperiyasi Toj Mahalning qurilishiga sabab bo'ldi",
            "Bobur o'zbek va fors tillarida she'rlar yozgan",
            "Hindiston, Afg'oniston va O'zbekistonda unga nisbatan katta hurmat bor",
        ],
        "rasm_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f5/Babur_the_first_Mughal_Emperor.jpg/640px-Babur_the_first_Mughal_Emperor.jpg",
        "qiziqarli": "Bobur Andijonda tug'ilib, Samarqandni zabt etgan, lekin eng buyuk muvaffaqiyatiga Hindistonda erishgan.",
    },

    # =================== BUXORO ===================
    "ark_qalasi": {
        "id": "ark_qalasi",
        "viloyat": "Buxoro viloyati",
        "nomi": "Ark Qal'asi",
        "emoji": "🏰",
        "tavsif": (
            "Ark qal'asi Buxoroning qadimiy qal'asi bo'lib, u 5 asr davomida shahar hokimlari qarorgohi bo'lgan. "
            "Qalin devorlar ichida saroy, masjid, qozilik, zindon va ko'plab xonalar joylashgan. "
            "Bu yerda buyuk olim Ibn Sino (Avicenna) ham ta'lim olgan. "
            "1920-yilda Qizil Armiya hujumida bir qismi vayron qilingan."
        ),
        "faktlar": [
            "Qal'a taxminan 2500 yil avval qurilgan",
            "Qal'a devori 20 metr balandlikka yetadi",
            "Ibn Sino (980-1037) Buxoro amiri kutubxonasida ishlagan",
            "So'nggi Buxoro amiri 1920-yilda qal'ani tashlab qochgan",
            "Hozir muzey sifatida ishlaydi",
        ],
        "rasm_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0c/Ark_of_Bukhara.jpg/640px-Ark_of_Bukhara.jpg",
        "qiziqarli": "Ark qal'asi ichida bir butun shahar bo'lgan — bozor, masjid, zindon, saroy — hammasi bir devor ichida.",
    },
    "poi_kalon": {
        "id": "poi_kalon",
        "viloyat": "Buxoro viloyati",
        "nomi": "Po-i-Kalon Majmuasi",
        "emoji": "🕌",
        "tavsif": (
            "Po-i-Kalon ('Buyuk poydevor' ma'nosida) — Buxoroning eng ulug'vor me'moriy majmuasi. "
            "Majmua Kalon minorasi (1127), Kalon masjidi (16-asr) va Mir Arab madrasasini o'z ichiga oladi. "
            "Kalon minorasi o'rta asrlarda Markaziy Osiyodagi eng baland inshoot bo'lgan — 46 metr. "
            "Chingizxon Buxoroni bosib olganda, minoraning go'zalligiga hayratlanib, uni buzmaslikka buyurgan."
        ),
        "faktlar": [
            "Kalon minorasi 1127-yilda qurilgan — 900 yildan ortiq",
            "Minora balandligi 46 metr, poydevori 9 metr chuqurlikda",
            "Kalon masjidi 10,000 nafar namozxonni sig'dira oladi",
            "Mir Arab madrasasi bugungi kunda ham faoliyat ko'rsatmoqda",
            "Chingizxon bu minoraga ta'zim qilgan degan rivoyat bor",
        ],
        "rasm_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/26/Poi_Kalon_Bukhara_2007.jpg/640px-Poi_Kalon_Bukhara_2007.jpg",
        "qiziqarli": "Kalon minorasi 'O'lim minorasi' nomi bilan ham mashhur — qadimda jinoyatchilar shu yerdan pastga tashlanib jazolangan.",
    },
    "labi_hovuz": {
        "id": "labi_hovuz",
        "viloyat": "Buxoro viloyati",
        "nomi": "Labi Hovuz",
        "emoji": "🏛",
        "tavsif": (
            "Labi Hovuz — Buxoro markazidagi tarixiy hovuz atrofida joylashgan majmua. "
            "1620-yilda qurilgan ushbu hovuz atrofida Kukeldosh madrasasi (1568), "
            "Nodir Devonbegi xonaqosi va madrasasi joylashgan. "
            "Bu joy qadimdan shahar hayotining markaziga aylangan — savdogarlar, olimlar, "
            "oddiy xalq bu yerda to'planishgan."
        ),
        "faktlar": [
            "Labi Hovuz 1620-yilda qurilgan",
            "Hovuz atrofida 300 yillik chinor daraxtlari o'sadi",
            "Nodir Devonbegi madrasasi peshtoqidagi afsonaviy simurg' va bug'u tasviri mashhur",
            "Bu tarixiy joy UNESCO ro'yxatiga kirgan Buxoro shahri tarkibida",
            "Kechqurun bu yerda milliy qo'shiqlar va raqslar ijro etiladi",
        ],
        "rasm_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/70/Lyab-i_Hauz.jpg/640px-Lyab-i_Hauz.jpg",
        "qiziqarli": "Xo'ja Nasriddin (Afandi) haykalchasi Labi Hovuz yonida — u o'zbek xalq donishmandining timsoli.",
    },

    # =================== FARG'ONA ===================
    "rishton": {
        "id": "rishton",
        "viloyat": "Farg'ona viloyati",
        "nomi": "Rishton Kulolchilik Markazi",
        "emoji": "🏺",
        "tavsif": (
            "Rishton — O'zbekistondagi kulolchilik san'atining asosiy markazlaridan biri. "
            "Bu yerda ming yillik an'anaga ega ko'k-oq naqshli sopol idishlar tayyorlanadi. "
            "Rishton kulolchiligida ishlatiladigan loy va bo'yoqlar tabiiy manbalardan olinadi. "
            "Ustalar sirini avloddan-avlodga o'tkazib kelmoqda."
        ),
        "faktlar": [
            "Rishton kulolchiligi 2000 yildan ortiq tarixga ega",
            "Ko'k rang — kobalt oksididan, oq rang — qo'rg'oshin va qalay aralashmasidan",
            "UNESCO tomonidan nomoyimateriall meros sifatida tan olingan",
            "Har yili Rishton kulolchilik festivali o'tkaziladi",
            "Ustaxonalarda bolalar ham ishtirok etib, kasbni o'rganadi",
        ],
        "rasm_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5d/Rishtan_ceramics.jpg/640px-Rishtan_ceramics.jpg",
        "qiziqarli": "Rishton sopollari Buyuk Ipak yo'li orqali Xitoy, Hindiston va Yevropaga eksport qilingan.",
    },
    "marg_ilon": {
        "id": "marg_ilon",
        "viloyat": "Farg'ona viloyati",
        "nomi": "Marg'ilon Ipak Markazi",
        "emoji": "🦋",
        "tavsif": (
            "Marg'ilon — O'zbekistondagi ipakchilik va to'qimachilik san'atining poytaxti. "
            "Bu yerda 2000 yildan ortiq ipak ishlab chiqarilmoqda. "
            "Atlas, adras va shoyi matolar Marg'ilonning eng mashhur mahsulotlari. "
            "Yodgorlik Yodgorilik ipak zavodida hanuzgacha qo'lda ishlash usullari saqlanib qolmoqda."
        ),
        "faktlar": [
            "Marg'ilon Buyuk Ipak yo'lining muhim markazi bo'lgan",
            "Atlas matosining naqshi qo'lda bo'yalgan ipak iplardan to'qiladi",
            "Bir metr atlas matosi tayyorlash bir necha kun davom etadi",
            "Shahar aholisining katta qismi ipakchilik bilan shug'ullanadi",
            "Xomashyo: pilla (tut ipak qurti) Farg'ona vodiysida yetishtiriladi",
        ],
        "rasm_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1c/Margilan_silk.jpg/640px-Margilan_silk.jpg",
        "qiziqarli": "Marg'ilon atlasi UNESCO ro'yxatidagi nomoddiy madaniy meros hisoblanadi.",
    },

    # =================== JIZZAX ===================
    "zomin": {
        "id": "zomin",
        "viloyat": "Jizzax viloyati",
        "nomi": "Zomin Milliy Bog'i",
        "emoji": "🏔",
        "tavsif": (
            "Zomin milliy bog'i Turkiston tog' tizmasida joylashgan bo'lib, "
            "O'zbekistondagi eng go'zal tog' landshaftlaridan birini o'z ichiga oladi. "
            "Bu yerda qarag'ay va archa o'rmonlari, tog' daryolari, noyob hayvonlar va o'simliklar mavjud. "
            "Bog' 2500 metr balandlikkacha ko'tariladi."
        ),
        "faktlar": [
            "Bog' maydoni 25,600 gektardan ortiq",
            "250 dan ortiq qush turi bu yerda uchraydi",
            "Qoraquyruq (arxar) — tog' echkisi bu yerda saqlanib qolgan",
            "Yoz mavsumida harorat +25°C, qishda -20°C gacha tushadi",
            "Zomin kurort shahri dam olish maskani sifatida mashhur",
        ],
        "rasm_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f3/Zaamin_National_Park.jpg/640px-Zaamin_National_Park.jpg",
        "qiziqarli": "Zomin bog'ida 1000 yildan ortiq yashovchi qadimiy archa daraxtlari bor.",
    },

    # =================== NAMANGAN ===================
    "chortoq": {
        "id": "chortoq",
        "viloyat": "Namangan viloyati",
        "nomi": "Chortoq Kurorti",
        "emoji": "🌿",
        "tavsif": (
            "Chortoq — Namangan viloyatidagi tog' kurort shahri. "
            "Chatqol tog' tizmasining bag'rida joylashgan bu joy yoz va qish fasllarida "
            "turistlarga mashhur. Tog' havosi, mineral suvlar va go'zal manzara "
            "Chortoqni O'zbekistonning sevimli dam olish maskanlaridan biriga aylantirgan."
        ),
        "faktlar": [
            "Chatqol davlat qo'riqxonasi Chortoq yaqinida joylashgan",
            "Tog' cho'qqilari 2000-3000 metr balandlikda",
            "Qishda chang'i sport imkoniyatlari mavjud",
            "Mineral buloq suvlari dorivor xususiyatga ega",
            "Chortoqdan Farg'ona vodiysi ko'rinishi ajoyib",
        ],
        "rasm_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c4/Chortok_resort.jpg/640px-Chortok_resort.jpg",
        "qiziqarli": "Chortoq so'zi o'zbek tilida 'to'rt buloq' ma'nosini bildiradi.",
    },

    # =================== NAVOIY ===================
    "sarmishsoy": {
        "id": "sarmishsoy",
        "viloyat": "Navoiy viloyati",
        "nomi": "Sarmishsoy Darasi",
        "emoji": "🗿",
        "tavsif": (
            "Sarmishsoy — Navoiy viloyatidagi qoyatosh rasmlari (petroglif) bilan mashhur daryo darasi. "
            "Bu yerda 4000 yildan ortiq oldin insonlar tomonidan ishlangan 4000 ga yaqin tosh rasmlar mavjud. "
            "Ov manzaralari, hayvonlar, tantana sahnalari tasvirlangan bu rasmlar "
            "O'rta Osiyodagi tosh davri san'atining eng yirik yodgorligi hisoblanadi."
        ),
        "faktlar": [
            "Sarmishsoyda 4000 dan ortiq petroglif mavjud",
            "Rasmlar bronza va tosh davridan — 4000-6000 yil oldin",
            "Ko'pincha yovvoyi buqa (tur), arxar, ov sahnalari tasvirlangan",
            "Dara uzunligi 15 km dan ortiq",
            "Sarmishsoy UNESCO Jahon merosi ro'yxatiga kirishga tavsiya etilgan",
        ],
        "rasm_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a8/Sarmishsay_petroglyphs.jpg/640px-Sarmishsay_petroglyphs.jpg",
        "qiziqarli": "Sarmishsoy dunyodagi eng katta ochiq havo tosh-davri san'at galereyalaridan biri.",
    },

    # =================== QASHQADARYO ===================
    "shahrisabz": {
        "id": "shahrisabz",
        "viloyat": "Qashqadaryo viloyati",
        "nomi": "Shahrisabz — Amir Temur Vatani",
        "emoji": "👑",
        "tavsif": (
            "Shahrisabz — sohibqiron Amir Temurning tug'ilgan shahri. "
            "So'zma-so'z tarjimasi 'yashil shahar' demakdir. "
            "Bu yerda Temurning ulug'vor saroyi — Oqsaroy (1380) va "
            "Dor ut-Tilovot majmuasi joylashgan. "
            "Shahrisabz UNESCO Jahon merosi ro'yxatiga kiritilgan."
        ),
        "faktlar": [
            "Amir Temur 1336-yilda Shahrisabzda tug'ilgan",
            "Oqsaroy saroyining kirish darvozasi 40 metr baland bo'lgan",
            "Shahrisabz so'zma-so'z: 'yashil shahar' (fors tilida)",
            "Temur Samarqandni poytaxt qilgan, Shahrisabzni yozgi rezidensiya sifatida saqlagan",
            "2000-yilda UNESCO Jahon merosi ro'yxatiga kiritilgan",
        ],
        "rasm_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Shahrisabz_Ak_Saray.jpg/640px-Shahrisabz_Ak_Saray.jpg",
        "qiziqarli": "Temur o'zi uchun Shahrisabzda ulug'vor maqbara qurdirgan, lekin vafot etgach Samarqandga dafn etilgan.",
    },

    # =================== SAMARQAND ===================
    "registon": {
        "id": "registon",
        "viloyat": "Samarqand viloyati",
        "nomi": "Registon Maydoni",
        "emoji": "✨",
        "tavsif": (
            "Registon — Samarqandning qalbi, Markaziy Osiyodagi eng buyuk me'moriy ansambillardan biri. "
            "Maydon uchta muazzam madrasadan tashkil topgan: Ulug'bek (1417-1420), "
            "Sherdor (1619-1636) va Tillakori (1646-1660) madrasalari. "
            "So'g'dcha 'qumli joy' degan ma'noni anglatuvchi Registon Samarqand davlatchiligining "
            "ramzi bo'lib kelgan."
        ),
        "faktlar": [
            "Ulug'bek madrasasi O'rta Osiyoning birinchi oliy o'quv yurti",
            "Sherdor madrasasi peshtoqidagi sher-quyosh tasviri mashurdir",
            "Tillakori masjidining ichki qismi oltin suvi bilan bezatilgan",
            "Registon so'zi so'g'dchada 'qumli joy' demakdir",
            "Amir Temur bu maydondan turib xalqqa murojaat qilgan",
        ],
        "rasm_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/Samarkand_Registan_Tamerlane_Timurid.jpg/640px-Samarkand_Registan_Tamerlane_Timurid.jpg",
        "qiziqarli": "Sherdor madrasasidagi naqshda sher quyoshni yelkasida ko'tarib ketayotgandek ko'rinadi — bu tasvir falakatdan himoya belgisi.",
    },
    "shohi_zinda": {
        "id": "shohi_zinda",
        "viloyat": "Samarqand viloyati",
        "nomi": "Shohi Zinda Majmuasi",
        "emoji": "🕌",
        "tavsif": (
            "Shohi Zinda — 'Tirik shoh' degan ma'noni bildiruvchi qadimiy maqbaralar majmuasi. "
            "Bu yerda Hazrat Qusam ibn Abbos (payg'ambarimiz amakivachchasi) va "
            "Temuriylar sulolasining ko'plab vakillari dafn etilgan. "
            "Majmuadagi yupqa ko'k kashtali, naqshli plitkalar dunyodagi eng go'zal "
            "islomiy bezak san'atining namunalari sanaladi."
        ),
        "faktlar": [
            "Majmua 9-15 asrlar davomida qurilgan",
            "20 dan ortiq maqbara mavjud",
            "Ko'k rangdagi plitkalar lazurit va kobaltdan tayyorlangan",
            "Hazrat Qusam ibn Abbos 676-yilda bu yerda shahid bo'lgan deyiladi",
            "Har yili minglab ziyoratchilar keladi",
        ],
        "rasm_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/80/Shah-i-Zinda_Samarkand.jpg/640px-Shah-i-Zinda_Samarkand.jpg",
        "qiziqarli": "Rivoyatga ko'ra, Qusam ibn Abbos o'ldirilgandan so'ng boshini qo'liga olib quduqqa kirgan — shuning uchun 'tirik shoh' deyiladi.",
    },
    "gur_amir": {
        "id": "gur_amir",
        "viloyat": "Samarqand viloyati",
        "nomi": "Gur Amir Maqbarasi",
        "emoji": "🏛",
        "tavsif": (
            "Gur Amir — sohibqiron Amir Temurning maqbarasi. "
            "Fors tilida 'Amirning qabri' degan ma'noni anglatadi. "
            "Bu ulug'vor binoda Temur, uning o'g'illari va nabirasi — buyuk astronomn Ulug'bek dafn etilgan. "
            "Qovurg'ali ko'k gumbaz Movarounnahr me'morligining durdonasi sanaladi."
        ),
        "faktlar": [
            "Maqbara 1403-1404 yillarda qurilgan",
            "Gumbaz balandligi 34 metr, diametri 15 metr",
            "Temurning qabrtoshi qora nefritdan yasalgan",
            "1941-yilda sovet olimlari Temur suyaklarini tekshirgan",
            "Bu me'morlik usuli keyinchalik Hindistonda Toj Mahal qurilishiga ilhom bergan",
        ],
        "rasm_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4f/GourEmir.jpg/640px-GourEmir.jpg",
        "qiziqarli": "Temur qabri ustidagi tosh: 'Kim mening qabrimni bezovta qilsa, men undan kuchli dushman chiqaraman' deb yozilgan — 1941-yil 22-iyunda qabrni ochishdi va hujum boshlandi.",
    },

    # =================== SURXONDARYO ===================
    "boysun": {
        "id": "boysun",
        "viloyat": "Surxondaryo viloyati",
        "nomi": "Boysun",
        "emoji": "🎭",
        "tavsif": (
            "Boysun — O'zbekistonning eng janubidagi, Afg'oniston chegarasiga yaqin tog' tuman. "
            "Bu yer qadimiy madaniyati, an'anaviy liboslari va folklori bilan mashhur. "
            "Boysunliklar hali ham qadimgi urf-odatlarni, kiyim-kechak va musiqa an'analarini saqlab kelmoqda. "
            "UNESCO bu hududni nomoddiy madaniy meros sifatida tan olgan."
        ),
        "faktlar": [
            "2001-yilda UNESCO tomonidan 'Insoniyat og'zaki merosi' deb e'lon qilingan",
            "Boysun tog'lari 3000 metrdan oshadi",
            "Qadimiy qo'shiq va raqslar avloddan-avlodga o'tib kelmoqda",
            "Har yili 'Boysun bahori' bayrami o'tkaziladi",
            "Bu yerda arxaik til va dialektlar saqlanib qolgan",
        ],
        "rasm_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b6/Baysun_bazaar.jpg/640px-Baysun_bazaar.jpg",
        "qiziqarli": "Boysun qizlarining kiyimi bugun ham 2000 yil oldingi naqsh va tikuvlarni saqlab qolgan.",
    },

    # =================== TOSHKENT VILOYATI ===================
    "chorvoq": {
        "id": "chorvoq",
        "viloyat": "Toshkent viloyati",
        "nomi": "Chorvoq Suv Ombori",
        "emoji": "💧",
        "tavsif": (
            "Chorvoq suv ombori — Toshkentdan 80 km uzoqda, Chatqol va Pskom daryolari "
            "qo'shilgan joyda joylashgan sun'iy ko'l. "
            "1970-yilda qurilgan Chorvoq GES to'g'oni natijasida hosil bo'lgan bu ko'l "
            "O'zbekistondagi eng mashhur dam olish maskanlaridan biri. "
            "Moviy suv va atrofdagi tog'lar manzarasi hayratlanarli."
        ),
        "faktlar": [
            "Suv ombori 1970-yilda Chorvoq GES qurilishi bilan yaratilgan",
            "Ko'l uzunligi 40 km, kengligi 4 km gacha",
            "Suv harorati yozda +22°C gacha ko'tariladi",
            "Chorvoq GES Toshkent elektr ta'minotining muhim qismi",
            "Amirsoy yon bag'irlarida chang'i resort mavjud",
        ],
        "rasm_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5b/Charvak_Reservoir.jpg/640px-Charvak_Reservoir.jpg",
        "qiziqarli": "Chorvoq to'g'oni balandligi 168 metr — bu Eyffel minorasi balandligining yarmiga teng.",
    },

    # =================== XORAZM ===================
    "ichan_qala": {
        "id": "ichan_qala",
        "viloyat": "Xorazm viloyati",
        "nomi": "Ichan Qal'a (Xiva)",
        "emoji": "🏰",
        "tavsif": (
            "Ichan Qal'a — Xiva shahrining ichki qal'asi va O'rta Osiyodagi eng yaxshi saqlanib qolgan "
            "qadimiy shaharlardan biri. "
            "2700 yillik tarixga ega bu shahar qal'a devorlari ichida masjidlar, madrasalar, "
            "minoralar, saroylar va hammomlardan iborat. "
            "1990-yilda UNESCO Jahon merosi ro'yxatiga birinchi o'zbek yodgorligi sifatida kiritilgan."
        ),
        "faktlar": [
            "Ichan Qal'a 2700 yil oldin asos solingan",
            "Qal'a devori uzunligi 2.2 km, balandligi 8-10 metr",
            "Ichida 60 dan ortiq me'moriy yodgorlik mavjud",
            "Kalta Minor — tugallanmagan minora, faqat 29 metr",
            "1990-yilda birinchi o'zbek yodgorligi sifatida UNESCOga kiritilgan",
        ],
        "rasm_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Itchan_Kala.jpg/640px-Itchan_Kala.jpg",
        "qiziqarli": "Kalta Minor ('qisqa minora') — Xiva xoni uni eng baland minora qilmoqchi bo'lgan, lekin 29 metrdan keyin vafot etgani uchun qurilish to'xtatilgan.",
    },

    # =================== TOSHKENT SHAHRI ===================
    "hazrati_imom": {
        "id": "hazrati_imom",
        "viloyat": "Toshkent shahri",
        "nomi": "Hazrati Imom Majmuasi (Xast Imom)",
        "emoji": "📚",
        "tavsif": (
            "Hazrati Imom majmuasi — Toshkentning diniy va madaniy markazlaridan biri. "
            "Bu yerda O'zbekistonning bosh imomi Hazrat Imom Ismoil al-Buxoriy (Imom Buxoriy emas) "
            "sharafiga nomlangan masjid va madrasalar joylashgan. "
            "Majmuada dunyodagi eng qadimiy Qur'on nusxalaridan biri — Usmon mushafi saqlanadi."
        ),
        "faktlar": [
            "Usmon mushafi — Islom olamidagi eng qadimiy Qur'on, 7-asrga oid",
            "Mushaf halifasi Usmon ibn Affon (644-656) davrida yozilgan",
            "Mushaf Samarqanddan 1868-yilda Rossiyaga olib ketilgan, 1924-yilda qaytarilgan",
            "Majmua har yili o'nlab ming ziyoratchi qabul qiladi",
            "Bu yerda O'zbekiston muftiyati joylashgan",
        ],
        "rasm_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Khast_Imam_Tashkent.jpg/640px-Khast_Imam_Tashkent.jpg",
        "qiziqarli": "Usmon mushafi ko'k krashmal parchamen (terilik) sahifalariga qon bilan yozilgan — rivoyatga ko'ra Usmonning qonli izi mushafda qolgan.",
    },
    "mustaqillik_maydoni": {
        "id": "mustaqillik_maydoni",
        "viloyat": "Toshkent shahri",
        "nomi": "Mustaqillik Maydoni",
        "emoji": "🌟",
        "tavsif": (
            "Mustaqillik maydoni — O'zbekistonning 1991-yil mustaqilligini ulug'lash uchun barpo etilgan "
            "Toshkentning asosiy maydoni. "
            "Maydonda muazzam globus haykali, Ona-Vatan haykalti va ulug'vor fontan majmuasi joylashgan. "
            "9-may va 1-sentabr kabi milliy bayramlarda bu yerda katta tadbirlar o'tkaziladi."
        ),
        "faktlar": [
            "1991-yil 1-sentabrda O'zbekiston mustaqilligi e'lon qilingan",
            "Globus haykali O'zbekistonning joylashuvini ko'rsatadi",
            "Maydonda Baxtli ona va bolalar haykali bor",
            "Har yili Navro'z va mustaqillik bayramlari bu yerda nishonlanadi",
            "Maydoning umumiy maydoni 5 gektardan ortiq",
        ],
        "rasm_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/ea/Independence_Square_Tashkent.jpg/640px-Independence_Square_Tashkent.jpg",
        "qiziqarli": "Sovet davrida bu maydon Lenin maydoni deb atalgan va Lenin haykali turgan.",
    },
    "toshkent_metrosi": {
        "id": "toshkent_metrosi",
        "viloyat": "Toshkent shahri",
        "nomi": "Toshkent Metrosi",
        "emoji": "🚇",
        "tavsif": (
            "Toshkent metrosi — Markaziy Osiyodagi birinchi va yagona metro tizimi. "
            "1977-yilda ochilgan metro bugun 3 liniya va 29 stantsiyadan iborat. "
            "Har bir stantsiya o'ziga xos bezakli bo'lib, milliy naqshlar, marmar va mozaikalar bilan "
            "bezatilgan. Metro Toshkent quyi yer san'at galereyasi deb ham ataladi."
        ),
        "faktlar": [
            "1977-yil 6-noyabrda birinchi liniya ochildi",
            "Markaziy Osiyodagi birinchi metro",
            "3 liniya: Chilonzor, O'zbegiston, Yunusobod",
            "29 stantsiya, 36 km yo'l",
            "Kuniga o'rtacha 300,000 yo'lovchi tashiydi",
        ],
        "rasm_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Tashkent_metro.jpg/640px-Tashkent_metro.jpg",
        "qiziqarli": "Cosmonaut stantsiyasi kosmosga bag'ishlangan — devorlarida kosmik naqshlar va Toshkentlik kosmonavt Vladmir Janibekovga bag'ishlangan bezaklar bor.",
    },
}

# Viloyatlar ro'yxati
VILOYATLAR = {
    "Qoraqalpog'iston Respublikasi": ["orol_dengizi", "savitskiy_muzeyi"],
    "Andijon viloyati": ["bobur_bogi"],
    "Buxoro viloyati": ["ark_qalasi", "poi_kalon", "labi_hovuz"],
    "Farg'ona viloyati": ["rishton", "marg_ilon"],
    "Jizzax viloyati": ["zomin"],
    "Namangan viloyati": ["chortoq"],
    "Navoiy viloyati": ["sarmishsoy"],
    "Qashqadaryo viloyati": ["shahrisabz"],
    "Samarqand viloyati": ["registon", "shohi_zinda", "gur_amir"],
    "Surxondaryo viloyati": ["boysun"],
    "Toshkent viloyati": ["chorvoq"],
    "Xorazm viloyati": ["ichan_qala"],
    "Toshkent shahri": ["hazrati_imom", "mustaqillik_maydoni", "toshkent_metrosi"],
}

# Savollar bazasi — har bir joy uchun 10 ta savol
SAVOLLAR = {
    "orol_dengizi": [
        {"savol": "Orol dengizi qaysi asrda kichrayna boshladi?", "javoblar": ["A) 19-asr", "B) 1960-yillar", "C) 2000-yillar", "D) 1920-yillar"], "togri": "B"},
        {"savol": "Orol dengizining asl maydoni qancha edi?", "javoblar": ["A) 10,000 km²", "B) 35,000 km²", "C) 68,000 km²", "D) 100,000 km²"], "togri": "C"},
        {"savol": "Orol dengizi qaysi ro'yxatga kiradi?", "javoblar": ["A) Okeanglar", "B) To'rtinchi eng katta ko'l", "C) Birinchi eng chuqur ko'l", "D) Eng toza ko'l"], "togri": "B"},
        {"savol": "Dengiz qurishining asosiy sababi nima?", "javoblar": ["A) Global isish", "B) Zilzila", "C) Daryolar suvining paxta ekinlariga burilishi", "D) Sanoat ifloslanishi"], "togri": "C"},
        {"savol": "Qaysi daryolar Orol dengizini to'ldirgan?", "javoblar": ["A) Volga va Don", "B) Amudaryo va Sirdaryo", "C) Nil va Kongo", "D) Ob va Yenisey"], "togri": "B"},
        {"savol": "Mo'ynoq shahri hozir dengizdan qancha uzoqda?", "javoblar": ["A) 10 km", "B) 50 km", "C) 150 km", "D) 300 km"], "togri": "C"},
        {"savol": "Orol dengizi fojeasini qaysi tashkilot 20-asr eng katta ekologik ofati deb tan olgan?", "javoblar": ["A) NATO", "B) BMT (BM)", "C) Jahon banki", "D) FIFA"], "togri": "B"},
        {"savol": "Dengiz sathi qancha metrga pasayib ketdi?", "javoblar": ["A) 5 metr", "B) 10 metr", "C) 16 metr", "D) 30 metr"], "togri": "C"},
        {"savol": "Qaysi viloyatda Orol dengizi joylashgan?", "javoblar": ["A) Toshkent", "B) Samarqand", "C) Qoraqalpog'iston", "D) Buxoro"], "togri": "C"},
        {"savol": "Orol dengizining qurib qolgan tubida nima ko'rish mumkin?", "javoblar": ["A) Ko'hna shaharlar", "B) Zanglagan kemalar", "C) Oltin konlar", "D) Qadimiy haykallar"], "togri": "B"},
    ],
    "savitskiy_muzeyi": [
        {"savol": "Savitskiy muzeyi qaysi shaharda joylashgan?", "javoblar": ["A) Toshkent", "B) Samarqand", "C) Nukus", "D) Buxoro"], "togri": "C"},
        {"savol": "Muzey qanday nom bilan ham ataladi?", "javoblar": ["A) Cho'ldagi Louvr", "B) Sharqning Ermitaji", "C) Osiyo Prado", "D) Markaziy muzey"], "togri": "A"},
        {"savol": "Muzeyda necha eksponat mavjud?", "javoblar": ["A) 10,000", "B) 40,000", "C) 90,000", "D) 200,000"], "togri": "C"},
        {"savol": "Muzey qaysi san'at to'plamiga ko'ra 2-chi o'rinda turadi?", "javoblar": ["A) Fransuz impressionizmi", "B) Rus avangard san'ati", "C) Xitoy keramikasi", "D) Italiya rangtasviri"], "togri": "B"},
        {"savol": "Igor Savitskiy nima uchun bu asarlarni yig'ib saqladi?", "javoblar": ["A) Sotish uchun", "B) Sovet ta'qibidan himoyalash uchun", "C) Davlat buyurtmasi bilan", "D) Shaxsiy manfaat uchun"], "togri": "B"},
        {"savol": "Savitskiy muzeyi qaysi viloyatda?", "javoblar": ["A) Xorazm", "B) Navoiy", "C) Qoraqalpog'iston", "D) Farg'ona"], "togri": "C"},
        {"savol": "2010-yilda muzey haqida qanday film yaratildi?", "javoblar": ["A) 'Cho'l sirri'", "B) 'Cho'ldagi San'atchi'", "C) 'Nukus tarixchisi'", "D) 'Yashirin kolleksiya'"], "togri": "B"},
        {"savol": "Sovet davrida bu asarlarning ko'pi nima qilindi?", "javoblar": ["A) Eksport qilindi", "B) Taqiqlandi", "C) Yo'q qilindi", "D) Muzeylarga berildi"], "togri": "B"},
        {"savol": "Muzey qaysi cho'l yaqinida joylashgan?", "javoblar": ["A) Gobi cho'li", "B) Sahara cho'li", "C) Qoraqum cho'li", "D) Taklamakan cho'li"], "togri": "C"},
        {"savol": "Muzeyda asosan qaysi davr san'ati to'plangan?", "javoblar": ["A) Qadimiy yunon", "B) O'rta asr islom", "C) Sovet davri avangard va qoraqalpoq xalq san'ati", "D) Zamonaviy digital san'at"], "togri": "C"},
    ],
    "registon": [
        {"savol": "Registon maydonida nechta madrasa bor?", "javoblar": ["A) Bitta", "B) Ikkita", "C) Uchta", "D) To'rtta"], "togri": "C"},
        {"savol": "Ulug'bek madrasasi qachon qurilgan?", "javoblar": ["A) 1117-1120", "B) 1317-1320", "C) 1417-1420", "D) 1517-1520"], "togri": "C"},
        {"savol": "Registon so'zining ma'nosi nima?", "javoblar": ["A) Ko'k maydon", "B) Qumli joy", "C) Oltin darvoza", "D) Buyuk bozor"], "togri": "B"},
        {"savol": "Sherdor madrasasi peshtoqida nima tasviri bor?", "javoblar": ["A) Ot va qahramon", "B) Sher va quyosh", "C) Fil va tog'", "D) Burgut va ilon"], "togri": "B"},
        {"savol": "Tillakori masjidining ichki qismi nimadan bezatilgan?", "javoblar": ["A) Kumush suvi", "B) Oltin suvi", "C) Mis suvi", "D) Bronza"], "togri": "B"},
        {"savol": "Ulug'bek madrasasi tarixi jihatidan nima edi?", "javoblar": ["A) Harbiy maktab", "B) Tibbiyot maktabi", "C) O'rta Osiyoning birinchi oliy o'quv yurti", "D) Qo'mondonlik markazi"], "togri": "C"},
        {"savol": "Registon qaysi shahrda joylashgan?", "javoblar": ["A) Toshkent", "B) Buxoro", "C) Xiva", "D) Samarqand"], "togri": "D"},
        {"savol": "Amir Temur bu maydondan nima qilgan?", "javoblar": ["A) Jang o'tkazgan", "B) Xalqqa murojaat qilgan", "C) Bozor ochgan", "D) Ko'rgazma o'tkazgan"], "togri": "B"},
        {"savol": "Sherdor so'zma-so'z qanday ma'noni bildiradi?", "javoblar": ["A) Oltin bino", "B) Sherli", "C) Yulduzli", "D) Ko'k gumbaz"], "togri": "B"},
        {"savol": "Registon maydoni qaysi viloyatda?", "javoblar": ["A) Buxoro", "B) Navoiy", "C) Samarqand", "D) Qashqadaryo"], "togri": "C"},
    ],
    "ark_qalasi": [
        {"savol": "Ark qal'asi qaysi shaharda joylashgan?", "javoblar": ["A) Xiva", "B) Samarqand", "C) Buxoro", "D) Toshkent"], "togri": "C"},
        {"savol": "Qal'a devori qancha balandlikka yetadi?", "javoblar": ["A) 5 metr", "B) 10 metr", "C) 20 metr", "D) 35 metr"], "togri": "C"},
        {"savol": "Ark qal'asi taxminan qancha yil oldin qurilgan?", "javoblar": ["A) 500 yil", "B) 1000 yil", "C) 1500 yil", "D) 2500 yil"], "togri": "D"},
        {"savol": "Ark qal'asi ichida nima bo'lmagan?", "javoblar": ["A) Zindon", "B) Masjid", "C) Deniz porti", "D) Qozilik"], "togri": "C"},
        {"savol": "Ibn Sino (Avicenna) Buxoroda nima bilan shug'ullangan?", "javoblar": ["A) Savdo qilgan", "B) Amir kutubxonasida ishlagan", "C) Harbiy xizmat qilgan", "D) Dehqonchilik qilgan"], "togri": "B"},
        {"savol": "So'nggi Buxoro amiri qachon qal'ani tashlab qochgan?", "javoblar": ["A) 1905", "B) 1915", "C) 1920", "D) 1930"], "togri": "C"},
        {"savol": "Hozir Ark qal'asi nima sifatida ishlatiladi?", "javoblar": ["A) Mehmonxona", "B) Muzey", "C) Harbiy baza", "D) Madrasa"], "togri": "B"},
        {"savol": "Ark qal'asini 1920-yilda kim vayron qildi?", "javoblar": ["A) Britaniya armiyasi", "B) Qizil Armiya", "C) Mongol qo'shinlari", "D) Fors qo'shinlari"], "togri": "B"},
        {"savol": "Ibn Sinoning to'liq ismi nima?", "javoblar": ["A) Abu Ali ibn Sino", "B) Ulug'bek ibn Sino", "C) Muhammad ibn Sino", "D) Ahmad ibn Sino"], "togri": "A"},
        {"savol": "Ark qal'asi qaysi viloyatda?", "javoblar": ["A) Farg'ona", "B) Buxoro", "C) Xorazm", "D) Qashqadaryo"], "togri": "B"},
    ],
    "gur_amir": [
        {"savol": "Gur Amir maqbarasida kim dafn etilgan?", "javoblar": ["A) Ulug'bek", "B) Amir Temur va uning avlodlari", "C) Ibn Sino", "D) Navoiy"], "togri": "B"},
        {"savol": "Gur Amir so'zma-so'z nima ma'no bildiradi?", "javoblar": ["A) Temurning saroyai", "B) Amirning qabri", "C) Buyuk minora", "D) Yulduzli gumbaz"], "togri": "B"},
        {"savol": "Maqbara gumbazi qancha baland?", "javoblar": ["A) 20 metr", "B) 25 metr", "C) 34 metr", "D) 50 metr"], "togri": "C"},
        {"savol": "Gur Amir qachon qurilgan?", "javoblar": ["A) 1203-1204", "B) 1303-1304", "C) 1403-1404", "D) 1503-1504"], "togri": "C"},
        {"savol": "Temurning qabrtoshi qanday materialdan yasalgan?", "javoblar": ["A) Oltin", "B) Marmar", "C) Qora nefriy tosh", "D) Granit"], "togri": "C"},
        {"savol": "Gur Amir qaysi shaharda joylashgan?", "javoblar": ["A) Buxoro", "B) Toshkent", "C) Samarqand", "D) Xiva"], "togri": "C"},
        {"savol": "Sovet olimlari Temur suyaklarini qachon tekshirdi?", "javoblar": ["A) 1921", "B) 1931", "C) 1941", "D) 1951"], "togri": "C"},
        {"savol": "Gur Amirning me'morlik uslubi qaysi binoga ilhom berdi?", "javoblar": ["A) Parij Notr-Dam", "B) Hindistondagi Toj Mahal", "C) Moskva Qizil maydoni", "D) Qohira piramidalari"], "togri": "B"},
        {"savol": "Amir Temur qaysi yillarda yashagan?", "javoblar": ["A) 1136-1205", "B) 1236-1305", "C) 1336-1405", "D) 1436-1505"], "togri": "C"},
        {"savol": "Temur qabrining nisbatan mashxur yozuvi nimadan ogohlantiradi?", "javoblar": ["A) Yot odamdan", "B) Qabrni bezovta qiluvchidan", "C) Yolg'onchidan", "D) Xiyonatkordan"], "togri": "B"},
    ],
    "shohi_zinda": [
        {"savol": "Shohi Zinda so'zining ma'nosi nima?", "javoblar": ["A) Ko'k mozaika", "B) Qadimiy maqbara", "C) Tirik shoh", "D) Yashil bog'"], "togri": "C"},
        {"savol": "Bu majmuada asosan kim dafn etilgan?", "javoblar": ["A) Xonlar va vazirlar", "B) Qusam ibn Abbos va Temuriylar avlodlari", "C) Faqat harbiy qo'mondonlar", "D) Olimlar va shoirlar"], "togri": "B"},
        {"savol": "Majmua necha asrda qurilgan?", "javoblar": ["A) 5-7 asrlar", "B) 9-15 asrlar", "C) 15-18 asrlar", "D) 18-20 asrlar"], "togri": "B"},
        {"savol": "Ko'k rang plitkalar nimadan tayyorlangan?", "javoblar": ["A) Ko'k bo'yoq va loy", "B) Lazurit va kobalt", "C) Ko'k shisha", "D) Sintetik pigment"], "togri": "B"},
        {"savol": "Majmuada nechta maqbara mavjud?", "javoblar": ["A) 5 ta", "B) 10 ta", "C) 20 dan ortiq", "D) 50 ta"], "togri": "C"},
        {"savol": "Shohi Zinda qaysi shaharda joylashgan?", "javoblar": ["A) Buxoro", "B) Samarqand", "C) Toshkent", "D) Namangan"], "togri": "B"},
        {"savol": "Hazrat Qusam ibn Abbos kim bo'lgan?", "javoblar": ["A) Buyuk shoir", "B) Payg'ambarimizning amakivachchasi", "C) Mongol qo'mondoni", "D) Buxoro amiri"], "togri": "B"},
        {"savol": "Qachon Qusam ibn Abbos bu yerda shahid bo'lgan?", "javoblar": ["A) 476-yil", "B) 576-yil", "C) 676-yil", "D) 776-yil"], "togri": "C"},
        {"savol": "Shohi Zinda rivoyatida nima tasvirlanadi?", "javoblar": ["A) Shoh urushda g'olib bo'ldi", "B) Qusam boshini ko'tarib quduqqa kirdi", "C) Temur bu yerda dafn qilindi", "D) Masjid ko'kdan tushdi"], "togri": "B"},
        {"savol": "Bu yodgorlik qaysi davlat hisoblanadi?", "javoblar": ["A) Qashqadaryo", "B) Navoiy", "C) Buxoro", "D) Samarqand"], "togri": "D"},
    ],
    "poi_kalon": [
        {"savol": "Po-i-Kalon so'zining ma'nosi nima?", "javoblar": ["A) Katta masjid", "B) Buyuk poydevor", "C) Ko'k minora", "D) Qadimiy bozor"], "togri": "B"},
        {"savol": "Kalon minorasi qachon qurilgan?", "javoblar": ["A) 927", "B) 1027", "C) 1127", "D) 1227"], "togri": "C"},
        {"savol": "Kalon minorasi qancha metr baland?", "javoblar": ["A) 26 metr", "B) 36 metr", "C) 46 metr", "D) 56 metr"], "togri": "C"},
        {"savol": "Kim Buxoroni bosib olganda minoraga hayratlanib, uni buzmaslikka buyurgan?", "javoblar": ["A) Iskandar Zulqarnayn", "B) Chingizxon", "C) Timur", "D) Napolyon"], "togri": "B"},
        {"savol": "Kalon masjidi necha namozxon sig'dira oladi?", "javoblar": ["A) 1,000", "B) 5,000", "C) 10,000", "D) 20,000"], "togri": "C"},
        {"savol": "Mir Arab madrasasi hozir ham nima qilmoqda?", "javoblar": ["A) Muzey sifatida ishlaydi", "B) Mehmonxona", "C) Faoliyat ko'rsatmoqda (o'quvchilar o'qiydi)", "D) Turar joy"], "togri": "C"},
        {"savol": "Kalon minorasi poydevori qancha chuqurlikda?", "javoblar": ["A) 3 metr", "B) 6 metr", "C) 9 metr", "D) 12 metr"], "togri": "C"},
        {"savol": "Majmua qaysi shaharda joylashgan?", "javoblar": ["A) Samarqand", "B) Buxoro", "C) Xiva", "D) Toshkent"], "togri": "B"},
        {"savol": "Kalon minorasi qanday nom bilan ham ataladi?", "javoblar": ["A) Baxt minorasi", "B) O'lim minorasi", "C) Ko'k minora", "D) Yulduz minorasi"], "togri": "B"},
        {"savol": "Po-i-Kalon majmuasida nechta asosiy inshoot bor?", "javoblar": ["A) 2 ta", "B) 3 ta", "C) 5 ta", "D) 7 ta"], "togri": "B"},
    ],
    "labi_hovuz": [
        {"savol": "Labi Hovuz qachon qurilgan?", "javoblar": ["A) 1420", "B) 1520", "C) 1620", "D) 1720"], "togri": "C"},
        {"savol": "Hovuz atrofida qancha yoshlik chinorlar o'sadi?", "javoblar": ["A) 50 yillik", "B) 100 yillik", "C) 200 yillik", "D) 300 yillik"], "togri": "D"},
        {"savol": "Nodir Devonbegi madrasasi peshtoqida nima tasviri bor?", "javoblar": ["A) Sher va burgut", "B) Afsonaviy simurg' va bug'u", "C) Ot va qahramon", "D) Fil va fil"], "togri": "B"},
        {"savol": "Labi Hovuz qaysi shaharda?", "javoblar": ["A) Toshkent", "B) Samarqand", "C) Xiva", "D) Buxoro"], "togri": "D"},
        {"savol": "Bu majmua qaysi UNESCO ro'yxatiga kirgan?", "javoblar": ["A) Yolg'iz", "B) Buxoro tarixi shahri tarkibida", "C) Alohida yodgorlik", "D) Kiritilmagan"], "togri": "B"},
        {"savol": "Kechqurun Labi Hovuz atrofida nimalar bo'ladi?", "javoblar": ["A) Sport musobaqalari", "B) Milliy qo'shiq va raqslar", "C) Auksionlar", "D) Parlament yig'ilishlari"], "togri": "B"},
        {"savol": "Hovuz yonida qaysi mashhur haykal bor?", "javoblar": ["A) Amir Temur haykali", "B) Navoiy haykali", "C) Xo'ja Nasriddin (Afandi) haykalchasi", "D) Ibn Sino haykali"], "togri": "C"},
        {"savol": "Kukeldosh madrasasi qachon qurilgan?", "javoblar": ["A) 1268", "B) 1368", "C) 1468", "D) 1568"], "togri": "D"},
        {"savol": "Labi Hovuz atrofida yana qanday inshoot bor?", "javoblar": ["A) Ark qal'asi", "B) Nodir Devonbegi xonaqosi", "C) Kalon minorasi", "D) Ulug'bek observatoriyasi"], "togri": "B"},
        {"savol": "Labi so'zi nimani anglatadi?", "javoblar": ["A) Ko'l", "B) Lab (bo'g'iz)", "C) Hovuz", "D) Daryo"], "togri": "B"},
    ],
    "bobur_bogi": [
        {"savol": "Zahiriddin Muhammad Bobur qaysi yili tug'ilgan?", "javoblar": ["A) 1383", "B) 1433", "C) 1483", "D) 1533"], "togri": "C"},
        {"savol": "Bobur qayerda imperiya asos soldi?", "javoblar": ["A) Eron", "B) Hindiston", "C) Misr", "D) Xitoy"], "togri": "B"},
        {"savol": "Boburning mashhur asari nomi nima?", "javoblar": ["A) Layli va Majnun", "B) Boburnoma", "C) Shahid-ul-Iqbol", "D) Temurnoma"], "togri": "B"},
        {"savol": "Boburnoma qanday asar hisoblanadi?", "javoblar": ["A) She'riy to'plam", "B) Tarix kitobi", "C) O'z hayotini o'zi yozgan avtobiografiya", "D) Diniy kitob"], "togri": "C"},
        {"savol": "Bobur qaysi tillarda she'rlar yozgan?", "javoblar": ["A) Arab va turk", "B) O'zbek va fors", "C) Hind va fors", "D) Rus va turk"], "togri": "B"},
        {"savol": "Bobur qayerda tug'ilgan?", "javoblar": ["A) Samarqand", "B) Buxoro", "C) Toshkent", "D) Andijon"], "togri": "D"},
        {"savol": "Bobur qaysi yillarda yashagan?", "javoblar": ["A) 1383-1430", "B) 1433-1490", "C) 1483-1530", "D) 1533-1580"], "togri": "C"},
        {"savol": "Boburiylar imperiyasi Hindistonda qanday tarixiy yodgorlik qoldirgani mashhur?", "javoblar": ["A) Qutab Minar", "B) Toj Mahal", "C) Hindiston devori", "D) Ganga haykali"], "togri": "B"},
        {"savol": "Bobur Samarqandni qachon zabt etdi?", "javoblar": ["A) Yoshligida, 14-15 yoshida", "B) 30 yoshida", "C) 40 yoshida", "D) Hech qachon"], "togri": "A"},
        {"savol": "Bobur bog'i qaysi viloyatda joylashgan?", "javoblar": ["A) Samarqand", "B) Buxoro", "C) Farg'ona", "D) Andijon"], "togri": "D"},
    ],
    "rishton": [
        {"savol": "Rishton qaysi viloyatda joylashgan?", "javoblar": ["A) Namangan", "B) Andijon", "C) Farg'ona", "D) Jizzax"], "togri": "C"},
        {"savol": "Rishton kulolchiligi necha yil tarixga ega?", "javoblar": ["A) 500 yil", "B) 1000 yil", "C) 1500 yil", "D) 2000 yildan ortiq"], "togri": "D"},
        {"savol": "Rishton kulolchiligidagi ko'k rang nimadan olinadi?", "javoblar": ["A) Ko'k bo'yoq", "B) Kobalt oksidi", "C) Ko'k loy", "D) Lazurit"], "togri": "B"},
        {"savol": "Rishton kulolchiligi qaysi tashkilot tomonidan tan olingan?", "javoblar": ["A) FIFA", "B) NATO", "C) UNESCO", "D) BMT armiyasi"], "togri": "C"},
        {"savol": "Rishton sopollarini qachon qayerga eksport qilishgan?", "javoblar": ["A) Faqat qo'shni shaharlarga", "B) Buyuk Ipak yo'li orqali Xitoy va Evropaga", "C) Faqat Rossiyaga", "D) Hech qayerga emas"], "togri": "B"},
        {"savol": "Kulolchilikda ishlatiladigan oq rang nimadan tayyorlanadi?", "javoblar": ["A) Oq loy", "B) Ohak", "C) Qo'rg'oshin va qalay aralashmasi", "D) Kreda"], "togri": "C"},
        {"savol": "Rishton ustaxonalarida kimlar ham ishtirok etadi?", "javoblar": ["A) Faqat kattalar", "B) Faqat erkaklar", "C) Bolalar ham kasbni o'rganadi", "D) Faqat professional ustalar"], "togri": "C"},
        {"savol": "Rishton kulolchilik an'anasida yangi avlodlarga nima yetkaziladi?", "javoblar": ["A) Faqat buyumlar", "B) Ustalar siri avloddan-avlodga", "C) Pul va mol-mulk", "D) Faqat qo'l mehnati"], "togri": "B"},
        {"savol": "Har yili Rishtonda nima o'tkaziladi?", "javoblar": ["A) Palov festivali", "B) Kulolchilik festivali", "C) Ipakchilik bayrami", "D) Olma bayrami"], "togri": "B"},
        {"savol": "Rishton kulolchiligi qaysi yo'l bilan mashhur bo'lgan?", "javoblar": ["A) Dengiz yo'li", "B) Buyuk Ipak yo'li", "C) Temir yo'l", "D) Havo yo'li"], "togri": "B"},
    ],
    "marg_ilon": [
        {"savol": "Marg'ilon qaysi viloyatda joylashgan?", "javoblar": ["A) Namangan", "B) Andijon", "C) Farg'ona", "D) Toshkent"], "togri": "C"},
        {"savol": "Marg'ilon nima bilan mashhur?", "javoblar": ["A) Kulolchilik", "B) Ipakchilik va to'qimachilik", "C) Zargarlik", "D) Temirchilik"], "togri": "B"},
        {"savol": "Atlas matosi nimadan tayyorlanadi?", "javoblar": ["A) Paxta", "B) Jun", "C) Qo'lda bo'yalgan ipak iplar", "D) Sintetik tolalar"], "togri": "C"},
        {"savol": "Marg'ilon Ipak yo'lida qanday o'rin tutgan?", "javoblar": ["A) Muhim markaz bo'lgan", "B) Kichik bozor bo'lgan", "C) Yo'l bo'lmagan", "D) Harbiy punkt bo'lgan"], "togri": "A"},
        {"savol": "Bir metr atlas matosi tayyorlash qancha vaqt oladi?", "javoblar": ["A) Bir soat", "B) Bir kun", "C) Bir necha kun", "D) Bir oy"], "togri": "C"},
        {"savol": "Ipakchilikda xomashyo nima?", "javoblar": ["A) Paxtа", "B) Pilla (tut ipak qurti)", "C) Jun", "D) Zig'ir"], "togri": "B"},
        {"savol": "Marg'ilon atlasi qaysi tashkilot tomonidan tan olingan?", "javoblar": ["A) FIFA", "B) WHO", "C) UNESCO", "D) UNICEF"], "togri": "C"},
        {"savol": "Marg'ilonda ipak qancha yildan beri ishlab chiqariladi?", "javoblar": ["A) 500 yil", "B) 1000 yil", "C) 1500 yil", "D) 2000 yildan ortiq"], "togri": "D"},
        {"savol": "Yodgorlik Yodgorilik ipak zavodida qanday usullar saqlanib qolgan?", "javoblar": ["A) Zamonaviy mashina usullari", "B) Qo'lda ishlash usullari", "C) Elektron usullar", "D) Kimyoviy usullar"], "togri": "B"},
        {"savol": "Farg'ona vodiysi ipakchilik uchun nimasi bilan qimmatli?", "javoblar": ["A) Daryolari ko'p", "B) Tut daraxtlari ko'p, pilla yetishtirish qulay", "C) Havoiy iqlim", "D) Ko'mir konlari"], "togri": "B"},
    ],
    "zomin": [
        {"savol": "Zomin milliy bog'i qaysi tog' tizmasida?", "javoblar": ["A) Tyan-Shan", "B) Chatqol", "C) Turkiston", "D) Zarafshon"], "togri": "C"},
        {"savol": "Zomin bog'ining maydoni qancha?", "javoblar": ["A) 5,000 gektar", "B) 10,000 gektar", "C) 25,600 gektardan ortiq", "D) 50,000 gektar"], "togri": "C"},
        {"savol": "Bu yerda necha tur qush uchraydi?", "javoblar": ["A) 50 dan ortiq", "B) 150 dan ortiq", "C) 250 dan ortiq", "D) 500 dan ortiq"], "togri": "C"},
        {"savol": "Qaysi hayvon Zomin bog'ida saqlanib qolgan?", "javoblar": ["A) Yo'lbars", "B) Qoraquyruq (arxar)", "C) Fil", "D) Karkidon"], "togri": "B"},
        {"savol": "Yozda Zomin bog'ida harorat qancha?", "javoblar": ["A) +10°C", "B) +15°C", "C) +25°C", "D) +35°C"], "togri": "C"},
        {"savol": "Bog' qaysi viloyatda joylashgan?", "javoblar": ["A) Samarqand", "B) Navoiy", "C) Jizzax", "D) Qashqadaryo"], "togri": "C"},
        {"savol": "Zomin bog'idagi eng qadimiy daraxtlar necha yoshda?", "javoblar": ["A) 100 yil", "B) 500 yil", "C) 1000 yildan ortiq", "D) 2000 yil"], "togri": "C"},
        {"savol": "Qishda Zomin bog'ida harorat qancha bo'lishi mumkin?", "javoblar": ["A) 0°C", "B) -5°C", "C) -10°C", "D) -20°C gacha"], "togri": "D"},
        {"savol": "Zomin bog'ida qanday daraxtlar ko'p?", "javoblar": ["A) Palma va sarv", "B) Qarag'ay va archa", "C) Eman va zarang", "D) Tut va o'rik"], "togri": "B"},
        {"savol": "Zomin kurort shahri nima uchun mashhur?", "javoblar": ["A) Dengiz sohili uchun", "B) Dam olish maskani sifatida", "C) Sanoat shahri sifatida", "D) Harbiy baza sifatida"], "togri": "B"},
    ],
    "chortoq": [
        {"savol": "Chortoq qaysi viloyatda joylashgan?", "javoblar": ["A) Farg'ona", "B) Andijon", "C) Namangan", "D) Toshkent"], "togri": "C"},
        {"savol": "Chortoq so'zining ma'nosi nima?", "javoblar": ["A) To'rt tog'", "B) To'rt buloq", "C) To'rt daryo", "D) To'rt yo'l"], "togri": "B"},
        {"savol": "Chortoq yaqinida qaysi qo'riqxona joylashgan?", "javoblar": ["A) Zomin qo'riqxonasi", "B) Chatqol davlat qo'riqxonasi", "C) Boysun qo'riqxonasi", "D) Sarmishsoy qo'riqxonasi"], "togri": "B"},
        {"savol": "Chortoq tog' cho'qqilari qancha metr balandlikda?", "javoblar": ["A) 500-1000 metr", "B) 1000-1500 metr", "C) 2000-3000 metr", "D) 4000-5000 metr"], "togri": "C"},
        {"savol": "Qishda Chortoqda qanday sport bilan shug'ullanish mumkin?", "javoblar": ["A) Suzish", "B) Chang'i", "C) Yengilathletics", "D) Velosiped"], "togri": "B"},
        {"savol": "Chortoqdagi mineral buloq suvlari qanday xususiyatga ega?", "javoblar": ["A) Nordon ta'mli", "B) Dorivor", "C) Chuchuk ta'mli", "D) Sho'r"], "togri": "B"},
        {"savol": "Chortoq qaysi tog' tizmasida joylashgan?", "javoblar": ["A) Tyan-Shan", "B) Turkiston", "C) Chatqol", "D) Hisor"], "togri": "C"},
        {"savol": "Chortoqdan ko'rish mumkin bo'lgan manzara nima?", "javoblar": ["A) Orol dengizi", "B) Farg'ona vodiysi ko'rinishi", "C) Qizilqum cho'li", "D) Amudaryo"], "togri": "B"},
        {"savol": "Chortoq asosan qachon mashhur dam olish maskani?", "javoblar": ["A) Faqat kuzda", "B) Faqat bahorda", "C) Yoz va qishda", "D) Faqat yozda"], "togri": "C"},
        {"savol": "Namangan viloyatida qaysi kurorti mashhur?", "javoblar": ["A) Zomin", "B) Chortoq", "C) Chorvoq", "D) Amirsoy"], "togri": "B"},
    ],
    "sarmishsoy": [
        {"savol": "Sarmishsoyda necha petroglif mavjud?", "javoblar": ["A) 400 ta", "B) 1400 ta", "C) 4000 dan ortiq", "D) 40,000 ta"], "togri": "C"},
        {"savol": "Sarmishsoy petroliflari qachon ishlangan?", "javoblar": ["A) 1000 yil oldin", "B) 2000 yil oldin", "C) 4000-6000 yil oldin", "D) 10,000 yil oldin"], "togri": "C"},
        {"savol": "Sarmishsoy qaysi viloyatda joylashgan?", "javoblar": ["A) Buxoro", "B) Navoiy", "C) Jizzax", "D) Samarqand"], "togri": "B"},
        {"savol": "Petroliflarda ko'pincha nima tasvirlangan?", "javoblar": ["A) Dengiz va baliqlar", "B) Yovvoyi hayvon va ov sahnalari", "C) Shahar va binolar", "D) Yulduzlar va oy"], "togri": "B"},
        {"savol": "Sarmishsoy darasi uzunligi qancha?", "javoblar": ["A) 3 km", "B) 7 km", "C) 15 km dan ortiq", "D) 30 km"], "togri": "C"},
        {"savol": "Bu yodgorlik qaysi ro'yxatga kirishga tavsiya etilgan?", "javoblar": ["A) FIFA ro'yxati", "B) UNESCO Jahon merosi ro'yxati", "C) NATO muhofazasi", "D) G20 ro'yxati"], "togri": "B"},
        {"savol": "Petroglif nima demakdir?", "javoblar": ["A) Qadimiy kitob", "B) Tosh ustiga ishlangan rasm", "C) Ko'hna qurol", "D) Qadimiy kema"], "togri": "B"},
        {"savol": "Sarmishsoy dunyoda qaysi o'rinda turadi?", "javoblar": ["A) Birinchi eng chuqur darya", "B) Eng katta ochiq havo tosh-davri san'at galereyalaridan biri", "C) Eng baland tog' o'tishi", "D) Eng katta ko'l"], "togri": "B"},
        {"savol": "Bu joyda ko'proq qaysi davr tasvirlangan?", "javoblar": ["A) Temir davri", "B) Bronza va tosh davri", "C) O'rta asrlar", "D) Zamonaviy davr"], "togri": "B"},
        {"savol": "Sarmishsoy qaysi daryo nomi bilan mashhur?", "jawvar": "Sarmish daryosi darasi", "javoblar": ["A) Zarafshon", "B) Amudaryo", "C) Sarmish daryosi darasi", "D) Sirdaryo"], "togri": "C"},
    ],
    "shahrisabz": [
        {"savol": "Amir Temur qaysi yili Shahrisabzda tug'ilgan?", "javoblar": ["A) 1236", "B) 1286", "C) 1336", "D) 1386"], "togri": "C"},
        {"savol": "Shahrisabz so'zining ma'nosi nima?", "javoblar": ["A) Qadimiy shahar", "B) Yashil shahar", "C) Katta darvoza", "D) Ko'k baland"], "togri": "B"},
        {"savol": "Oqsaroy qurilishi qachon boshlangan?", "javoblar": ["A) 1280", "B) 1330", "C) 1380", "D) 1430"], "togri": "C"},
        {"savol": "Shahrisabz Temur tomonidan nima sifatida ishlatilgan?", "javoblar": ["A) Poytaxt", "B) Harbiy baza", "C) Yozgi rezidensiya", "D) Savdo markazi"], "togri": "C"},
        {"savol": "Oqsaroy saroyining kirish darvozasi qancha baland bo'lgan?", "javoblar": ["A) 20 metr", "B) 30 metr", "C) 40 metr", "D) 60 metr"], "togri": "C"},
        {"savol": "Shahrisabz qachon UNESCO ro'yxatiga kiritilgan?", "javoblar": ["A) 1990", "B) 1995", "C) 2000", "D) 2005"], "togri": "C"},
        {"savol": "Amir Temur qayerda dafn etildi?", "javoblar": ["A) Shahrisabz", "B) Samarqand (Gur Amir)", "C) Buxoro", "D) Toshkent"], "togri": "B"},
        {"savol": "Temur poytaxtini qayerda qildi?", "javoblar": ["A) Shahrisabz", "B) Buxoro", "C) Samarqand", "D) Andijon"], "togri": "C"},
        {"savol": "Shahrisabz qaysi viloyatda?", "javoblar": ["A) Buxoro", "B) Samarqand", "C) Qashqadaryo", "D) Navoiy"], "togri": "C"},
        {"savol": "Temur o'zi uchun maqbara qayerda qurdirdi?", "javoblar": ["A) Faqat Samarqandda", "B) Faqat Shahrisabzda", "C) Ham Samarqand, ham Shahrisabzda", "D) Hech qayerda emas"], "togri": "C"},
    ],
    "boysun": [
        {"savol": "Boysun qaysi viloyatda joylashgan?", "javoblar": ["A) Qashqadaryo", "B) Surxondaryo", "C) Buxoro", "D) Navoiy"], "togri": "B"},
        {"savol": "UNESCO Boysunni qachon 'Insoniyat og'zaki merosi' deb e'lon qildi?", "javoblar": ["A) 1991", "B) 1996", "C) 2001", "D) 2006"], "togri": "C"},
        {"savol": "Boysun tog'lari qancha metrga yetadi?", "javoblar": ["A) 1000 metr", "B) 2000 metr", "C) 3000 metrdan oshadi", "D) 5000 metr"], "togri": "C"},
        {"savol": "Har yili Boysunda qanday bayram o'tkaziladi?", "javoblar": ["A) Navro'z", "B) Boysun bahori", "C) Ipakchilik bayrami", "D) Kulolchilik festivali"], "togri": "B"},
        {"savol": "Boysun qaysi chegaraga yaqin?", "jawvar": "Afg'oniston", "javoblar": ["A) Tojikiston", "B) Qirg'iziston", "C) Afg'oniston", "D) Eron"], "togri": "C"},
        {"savol": "Boysun qizlarining kiyimi qancha yillik naqshlarni saqlab qolgan?", "javoblar": ["A) 500 yil", "B) 1000 yil", "C) 2000 yil", "D) 5000 yil"], "togri": "C"},
        {"savol": "Bu yerda qaysi noyob narsa saqlanib qolgan?", "javoblar": ["A) Qadimiy hayvonlar", "B) Arxaik til va dialektlar", "C) Ko'hna kemalar", "D) Qadimiy bronza buyumlar"], "togri": "B"},
        {"savol": "Boysunda qanday an'analar avloddan-avlodga o'tib kelmoqda?", "javoblar": ["A) Faqat hunarmandchilik", "B) Qo'shiq, raqs, urf-odatlar", "C) Faqat ov qilish", "D) Faqat dehqonchilik"], "togri": "B"},
        {"savol": "O'zbekistonning janubiy chegarasida joylashgan viloyat qaysi?", "javoblar": ["A) Qashqadaryo", "B) Buxoro", "C) Surxondaryo", "D) Navoiy"], "togri": "C"},
        {"savol": "Boysunning asosiy xususiyati nima?", "jawvar": "Qadimiy madaniyat va an'analar", "javoblar": ["A) Sanoat shahri", "B) Qadimiy madaniyat va an'analarni saqlagan tog' tumani", "C) Port shahri", "D) Oliy ta'lim markazi"], "togri": "B"},
    ],
    "chorvoq": [
        {"savol": "Chorvoq suv ombori qachon yaratilgan?", "javoblar": ["A) 1950", "B) 1960", "C) 1970", "D) 1980"], "togri": "C"},
        {"savol": "Chorvoq Toshkentdan qancha uzoqda?", "javoblar": ["A) 20 km", "B) 50 km", "C) 80 km", "D) 120 km"], "togri": "C"},
        {"savol": "Ko'l yozda qanday haroratga yetadi?", "javoblar": ["A) +10°C", "B) +15°C", "C) +22°C", "D) +30°C"], "togri": "C"},
        {"savol": "Chorvoq to'g'oni qancha metr baland?", "jawvar": "168 metr", "javoblar": ["A) 68 metr", "B) 100 metr", "C) 168 metr", "D) 250 metr"], "togri": "C"},
        {"savol": "Chorvoq to'g'oni balandligi nimaga teng?", "javoblar": ["A) Eyffel minorasi", "B) Eyffel minorasi balandligining yarmiga", "C) Birlik maydoni", "D) O'zbekiston teledirni"], "togri": "B"},
        {"savol": "Ko'l qaysi daryolar qo'shilishida hosil bo'lgan?", "javoblar": ["A) Amudaryo va Sirdaryo", "B) Zarafshon va Qashqadaryo", "C) Chatqol va Pskom", "D) Chirchiq va Angren"], "togri": "C"},
        {"savol": "Chorvoq GES nima qiladi?", "javoblar": ["A) Suvni tozalaydi", "B) Toshkent elektr ta'minotida ishtirok etadi", "C) Suv etkazib beradi", "D) Baliqchilik bilan shug'ullanadi"], "togri": "B"},
        {"savol": "Ko'l uzunligi qancha?", "javoblar": ["A) 10 km", "B) 20 km", "C) 40 km", "D) 80 km"], "togri": "C"},
        {"savol": "Chorvoq yaqinida qaysi ski-resort joylashgan?", "javoblar": ["A) Zomin", "B) Amirsoy", "C) Chimyon", "D) Chortoq"], "togri": "B"},
        {"savol": "Chorvoq qaysi viloyatda joylashgan?", "javoblar": ["A) Namangan", "B) Andijon", "C) Toshkent viloyati", "D) Samarqand"], "togri": "C"},
    ],
    "ichan_qala": [
        {"savol": "Ichan Qal'a qaysi shaharda joylashgan?", "javoblar": ["A) Urgench", "B) Xiva", "C) Turtkul", "D) Nukus"], "togri": "B"},
        {"savol": "Ichan Qal'a qancha yil avval asos solingan?", "javoblar": ["A) 1000 yil", "B) 1500 yil", "C) 2000 yil", "D) 2700 yil"], "togri": "D"},
        {"savol": "Qal'a devori uzunligi qancha?", "javoblar": ["A) 1 km", "B) 2.2 km", "C) 5 km", "D) 10 km"], "togri": "B"},
        {"savol": "Qal'a ichida necha me'moriy yodgorlik bor?", "javoblar": ["A) 10 ta", "B) 30 ta", "C) 60 dan ortiq", "D) 100 ta"], "togri": "C"},
        {"savol": "Kalta Minor nima uchun tugallanmay qoldi?", "javoblar": ["A) Pul tugadi", "B) Zilzila bo'ldi", "C) Xiva xoni vafot etdi", "D) Urush boshlandi"], "togri": "C"},
        {"savol": "Kalta Minor qancha metr baland?", "javoblar": ["A) 15 metr", "B) 29 metr", "C) 46 metr", "D) 60 metr"], "togri": "B"},
        {"savol": "O'zbekistondagi birinchi UNESCO yodgorligi qaysi?", "javoblar": ["A) Registon", "B) Gur Amir", "C) Ichan Qal'a", "D) Ark qal'asi"], "togri": "C"},
        {"savol": "UNESCO Ichan Qal'ani qachon ro'yxatga oldi?", "javoblar": ["A) 1980", "B) 1990", "C) 2000", "D) 2010"], "togri": "B"},
        {"savol": "Ichan Qal'a qaysi viloyatda?", "javoblar": ["A) Buxoro", "B) Surxondaryo", "C) Xorazm", "D) Qashqadaryo"], "togri": "C"},
        {"savol": "Qal'a devori qancha metr baland?", "javoblar": ["A) 3-5 metr", "B) 8-10 metr", "C) 15-20 metr", "D) 25-30 metr"], "togri": "B"},
    ],
    "hazrati_imom": [
        {"savol": "Hazrati Imom majmuasida qaysi noyob asar saqlanadi?", "javoblar": ["A) Avesta", "B) Boburnoma", "C) Usmon mushafi", "D) Qutadg'u bilig"], "togri": "C"},
        {"savol": "Usmon mushafi taxminan qachon yozilgan?", "javoblar": ["A) 4-asr", "B) 7-asr (Usmon halifat davrida)", "C) 10-asr", "D) 14-asr"], "togri": "B"},
        {"savol": "Mushaf Toshkentga qaytarilgan yili?", "javoblar": ["A) 1900", "B) 1914", "C) 1924", "D) 1950"], "togri": "C"},
        {"savol": "Mushaf qaysi mamlakatda saqlangan edi?", "jawvar": "Rossiyada", "javoblar": ["A) Fransiyada", "B) Angliyada", "C) Rossiyada", "D) Germaniyada"], "togri": "C"},
        {"savol": "Bu majmuada qaysi tashkilot joylashgan?", "javoblar": ["A) O'zbekiston parlamenti", "B) O'zbekiston muftiyati", "C) Oliy Sud", "D) Davlat Arxivi"], "togri": "B"},
        {"savol": "Hazrati Imom majmuasi qaysi shaharda?", "javoblar": ["A) Buxoro", "B) Samarqand", "C) Toshkent", "D) Namangan"], "togri": "C"},
        {"savol": "Usmon ibn Affon kimning davrida xalifa bo'lgan?", "javoblar": ["A) 544-556", "B) 644-656", "C) 744-756", "D) 844-856"], "togri": "B"},
        {"savol": "Mushaf qanday material ustiga yozilgan?", "javoblar": ["A) Qog'oz", "B) Yog'och", "C) Parchamen (terlik)", "D) Sopol"], "togri": "C"},
        {"savol": "Mushafdagi rivoyatga ko'ra, unda nima qolgan?", "jawvar": "Usmonning qonli izi", "javoblar": ["A) Oltin iz", "B) Ko'k bo'yoq izi", "C) Usmonning qonli izi", "D) Zarrin naqsh"], "togri": "C"},
        {"savol": "Hazrati Imom majmuasi qaysi joy?", "javoblar": ["A) O'zbekistonning harbiy markazi", "B) Diniy va madaniy markazi", "C) Savdo markazi", "D) Ta'lim universiteti"], "togri": "B"},
    ],
    "mustaqillik_maydoni": [
        {"savol": "O'zbekiston mustaqilligi qachon e'lon qilindi?", "javoblar": ["A) 1990-yil 1-sentabr", "B) 1991-yil 1-sentabr", "C) 1992-yil 1-sentabr", "D) 1993-yil 1-sentabr"], "togri": "B"},
        {"savol": "Maydondagi globus haykali nimani ko'rsatadi?", "javoblar": ["A) Dunyo xaritasini", "B) O'zbekistonning joylashuvini", "C) Quyosh tizimini", "D) O'rta Osiyoni"], "togri": "B"},
        {"savol": "Sovet davrida bu maydon qanday atalgan?", "javoblar": ["A) Stalin maydoni", "B) Marks maydoni", "C) Lenin maydoni", "D) Kommunizm maydoni"], "togri": "C"},
        {"savol": "Maydonning umumiy maydoni qancha?", "javoblar": ["A) 1 gektar", "B) 3 gektar", "C) 5 gektardan ortiq", "D) 10 gektar"], "togri": "C"},
        {"savol": "Bu maydonda qanday bayramlar nishonlanadi?", "javoblar": ["A) Faqat sport bayramlari", "B) Navro'z va mustaqillik bayrami", "C) Faqat xalqaro bayramlar", "D) Hech qanday bayramlar"], "togri": "B"},
        {"savol": "Maydonda qaysi haykal ham bor?", "javoblar": ["A) Temur haykali", "B) Baxtli ona va bolalar haykali", "C) Navoiy haykali", "D) Bobur haykali"], "togri": "B"},
        {"savol": "Mustaqillik maydoni qaysi shaharda?", "javoblar": ["A) Samarqand", "B) Toshkent", "C) Buxoro", "D) Namangan"], "togri": "B"},
        {"savol": "O'zbekiston mustaqilligi nechinchi yilligi?", "javoblar": ["A) 2025-yilda 33-yillik", "B) 2025-yilda 34-yillik", "C) 2025-yilda 35-yillik", "D) 2025-yilda 36-yillik"], "togri": "B"},
        {"savol": "Sovet davrida maydonda nima turgan?", "javoblar": ["A) Stalif haykali", "B) Lenin haykali", "C) Marks haykali", "D) Engles haykali"], "togri": "B"},
        {"savol": "O'zbekiston mustaqilligi qaysi davlatdan?", "javoblar": ["A) Britaniyadan", "B) SSSR (Sovet Ittifoqi)dan", "C) Xitoydan", "D) AQShdan"], "togri": "B"},
    ],
    "toshkent_metrosi": [
        {"savol": "Toshkent metrosi qachon ochildi?", "javoblar": ["A) 1967-yil", "B) 1977-yil", "C) 1987-yil", "D) 1997-yil"], "togri": "B"},
        {"savol": "Toshkent metrosi qaysi miqyosda birinchi?", "javoblar": ["A) Osiyo bo'yicha", "B) Markaziy Osiyoda birinchi metro", "C) MDH bo'yicha", "D) Islom dunyosida"], "togri": "B"},
        {"savol": "Metroда nechta liniya bor?", "javoblar": ["A) 2 ta", "B) 3 ta", "C) 4 ta", "D) 5 ta"], "togri": "B"},
        {"savol": "Metroда nechta stantsiya bor?", "javoblar": ["A) 15 ta", "B) 20 ta", "C) 29 ta", "D) 40 ta"], "togri": "C"},
        {"savol": "Metro liniyalarining umumiy uzunligi qancha?", "javoblar": ["A) 20 km", "B) 36 km", "C) 50 km", "D) 70 km"], "togri": "B"},
        {"savol": "Kuniga necha yo'lovchi metro bilan sayohat qiladi?", "javoblar": ["A) 100,000", "B) 200,000", "C) 300,000", "D) 500,000"], "togri": "C"},
        {"savol": "Metro qanday nom bilan ham ataladi?", "javoblar": ["A) Yer osti expressasi", "B) Toshkent quyi yer san'at galereyasi", "C) Kichik temir yo'l", "D) Tunnel transport"], "togri": "B"},
        {"savol": "Metrodan qaysi liniyalar bor?", "javoblar": ["A) Registan, Navoiy, Bobur", "B) Chilonzor, O'zbegiston, Yunusobod", "C) Sharq, G'arb, Markaz", "D) A, B, C liniyalari"], "togri": "B"},
        {"savol": "Cosmonaut stantsiyasi kimga bag'ishlangan?", "javoblar": ["A) Yuri Gagarin", "B) Neil Armstrong", "C) Vladmir Janibekov", "D) Valentina Tereşkova"], "togri": "C"},
        {"savol": "Metro stantsiyalari nimalar bilan bezatilgan?", "javoblar": ["A) Plastik va shisha", "B) Milliy naqshlar, marmar va mozaikalar", "C) Oddiy bo'yoq", "D) Zamonaviy reklama"], "togri": "B"},
    ],
}
