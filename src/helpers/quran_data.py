# quran_data.py
#
# Copyright 2020 mBilG
#
# This is a python helper file containing Quran data file for testing with python apps
# A JSON file or SQL (for more complex data including ayah info) may be better?

# Surah Names in Arabic
surahName_ar = (
"ٱلْفَاتِحَة","ٱلْبَقَرَة","آلِ عِمْرَان","ٱلنِّسَاء","ٱلْمَائِدَة","ٱلْأَنْعَام","ٱلْأَعْرَاف","ٱلْأَنْفَال","ٱلتَّوْبَة","يُونُس","هُود","يُوسُف","ٱلرَّعْد","إِبْرَاهِيم",
"ٱلْحِجْر","ٱلنَّحْل","ٱلْإِسْرَاء","ٱلْكَهْف","مَرْيَم","طه","ٱلْأَنْبِيَاء","ٱلْحَجّ","ٱلْمُؤْمِنُون","ٱلنُّور","ٱلْفُرْقَان","ٱلشُّعَرَاء","ٱلنَّمْل","ٱلْقَصَص","ٱلْعَنْكَبُوت",
"ٱلرُّوم","لُقْمَان","ٱلسَّجْدَة","ٱلْأَحْزَاب","سَبَأ","فَاطِر","يس","ٱلصَّافَّات","ص","ٱلزُّمَر","غَافِر","فُصِّلَت","ٱلشُّورىٰ","ٱلْزُّخْرُف","ٱلدُّخَان","ٱلْجَاثِيَة",
"ٱلْأَحْقَاف","مُحَمَّد","ٱلْفَتْح","ٱلْحُجُرَات","ق","ٱلذَّارِيَات","ٱلطُّور","ٱلنَّجْم","ٱلْقَمَر","ٱلرَّحْمَٰن","ٱلْوَاقِعَة","ٱلْحَدِيد","ٱلْمُجَادِلَة","ٱلْحَشْر","ٱلْمُمْتَحَنَة",
"ٱلصَّفّ","ٱلْجُمُعَة","ٱلْمُنَافِقُون","ٱلتَّغَابُن","ٱلطَّلَاق","ٱلتَّحْرِيم","ٱلْمُلْك","ٱلْقَلَم","ٱلْحَاقَّة","ٱلْمَعَارِج","نُوح","ٱلْجِنّ","ٱلْمُزَّمِّل","ٱلْمُدَّثِّر","ٱلْقِيَامَة",
"ٱلْإِنْسَان","ٱلْمُرْسَلَات","ٱلنَّبَأ","ٱلنَّازِعَات","عَبَسَ","ٱلتَّكْوِير","ٱلْإِنْفِطَار","ٱلْمُطَفِّفِين","ٱلْإِنْشِقَاق","ٱلْبُرُوج","ٱلطَّارِق","ٱلْأَعْلَىٰ","ٱلْغَاشِيَة","ٱلْفَجْر",
"ٱلْبَلَد","ٱلشَّمْس","ٱللَّيْل","ٱلضُّحَىٰ","ٱلشَّرْح","ٱلتِّين","ٱلْعَلَق","ٱلْقَدْر","ٱلْبَيِّنَة","ٱلزَّلْزَلَة","ٱلْعَادِيَات","ٱلْقَارِعَة","ٱلتَّكَاثُر","ٱلْعَصْر","ٱلْهُمَزَة",
"ٱلْفِيل","قُرَيْش","ٱلْمَاعُون","ٱلْكَوْثَر","ٱلْكَافِرُون","ٱلنَّصْر","ٱلْمَسَد","ٱلْإِخْلَاص","ٱلْفَلَق","ٱلنَّاس"
    )


# Surah Names translated in English
surahName_en = (
    "The Opening","The Cow","The Family Of Imran","Women","The Food","The Cattle","The Elevated Places",
    "The Spoils Of War","Repentance","Jonah","Hud","Joseph","The Thunder","Abraham","The Rock","The Bee","The Night Journey",
    "The Cave","Mary","Ta Ha","The Prophets","The Pilgrimage","The Believers","The Light","The Criterion","The Poets","The Ant",
    "The Narrative","The Spider","The Romans","Lukman","The Adoration","The Allies","Sheba","The Creator","Ya Sin","The Rangers",
    "Sad","The Companies","The Forgiving One","Revelations Well Expounded","The Counsel","The Embellishment","The Evident Smoke",
    "The Kneeling","The Sandhills","Muhammad","The Victory","The Chambers","Qaf","The Scatterers","The Mountain","The Star",
    "The Moon","The Merciful","That Which is Coming","The Iron","She Who Pleaded","The Exile","She Who is Tested","The Ranks",
    "The Day of Congregation","The Hypocrites","The Cheating","The Divorce","The Prohibition","The Kingdom","The Pen",
    "The Inevitable","The Ladders","Noah","The Jinn","The Mantled One","The Clothed One","The Resurrection","The Man",
    "The Emissaries","The Tidings","Those Who Pull Out","He Frowned","The Cessation","The Cleaving Asunder","The Defrauders",
    "The Rending","the Constellations","The Night-Comer","The Most High","The Overwhelming Calamity","The Dawn","The City",
    "The Sun","The Night","The Early Hours","The Expansion","The Fig","The Clot","The Majesty","The Proof","The Shaking",
    "The Assaulters","The Terrible Calamity","Worldly Gain","Time","The Slanderer","The Elephant","The Quraish","The Daily Necessaries",
    "Abundance","The Unbelievers","The Help","The Palm Fibre","The Unity","The Daybreak","The Men"
    )

# Surah Names transliterated
surahName_tr = (
    "al-Fatihah","al-Baqarah","Al-Imran","an-Nisa'","al-Ma'idah","al-An`am","al-A`raf","al-Anfal","at-Taubah","Yunus",
    "Hud","Yusuf","ar-Ra`d","Ibrahim","al-Hijr","an-Nahl","Al-Isra","al-Kahf","Maryam","Ta Ha","al-Anbiya'","al-Hajj",
    "al-Mu'minun","an-Nur","al-Furqan","ash-Shu`ara'","an-Naml","al-Qasas","al-`Ankabut","ar-Rum","Luqman","as-Sajdah",
    "al-Ahzab","Saba'","Fatir","Ya Sin","as-Saffat","Sad","az-Zumar","Ghafir","Fussilat","ash-Shura","az-Zukhruf",
    "ad-Dukhan","al-Jathiyah","al-Ahqaf","Muhammad","al-Fath","al-Hujurat","Qaf","ad-Dhariyat","at-Tur","an-Najm",
    "al-Qamar","ar-Rahman","al-Waqi`ah","al-Hadid","al-Mujadilah","al-Hashr","al-Mumtahanah","as-Saff","al-Jumu`ah",
    "al-Munafiqun","at-Taghabun","at-Talaq,","at-Tahrim","al-Mulk","al-Qalam","al-Haqqah","al-Ma`arij","Nuh","al-Jinn",
    "al-Muzammil","al-Mudathir","al-Qiyamah","al-Insan","al-Mursalat","an-Naba'","an-Nazi`at","`Abasa","at-Takwir",
    "al-Infitar","Al-Mutaffifeen","al-Inshiqaq","al-Buruj","at-Tariq","al-A`la","al-Ghashiya","al-Fajr","al-Balad",
    "ash-Shams","al-Layl","ad-Duha","ash-Sharh","at-Tin","al-`Alaq","al-qadr","al-Bayyinah","Az-Zalzala","al-`Adiyat",
    "al-Qari`ah","at-Takathur","al-`Asr","al-Humazah","al-Fil","al-Quraish","al-Ma`un","al-Kauthar","al-Kafirun",
    "an-Nasr","Al-Masad","al-Ikhlas","al-Falaq","an-Nas"
    )


# Page number of start of surah
surahStartPage = (
    1,2,50,77,106,128,151,177,187,208,221,235,249,255,262,267,282,293,305,312,322,
    332,342,350,359,367,377,385,396,404,411,415,418,428,434,440,446,453,458,467,
    477,483,489,496,499,502,507,511,515,518,520,523,526,528,531,534,537,542,545,
    549,551,553,554,556,558,560,562,564,566,568,570,572,574,575,577,578,580,582,
    583,585,586,587,587,589,590,591,591,592,593,594,595,595,596,596,597,597,598,
    598,599,599,600,600,601,601,601,602,602,602,603,603,603,604,604,604
    )


# Page number of end of surah
surahEndPage = (
    1,49,76,106,127,150,176,186,207,221,235,248,255,261,267,281,293,304,312,321,331,
    341,349,359,366,376,385,396,404,410,414,417,427,434,440,445,452,458,467,476,482,
    489,495,498,502,506,510,515,517,520,523,525,528,531,534,537,541,545,548,551,552,
    554,555,557,559,561,564,566,568,570,571,573,575,577,578,580,581,583,584,586,586,
    587,589,590,590,591,592,593,594,595,595,596,596,597,597,598,598,599,599,600,600,
    600,601,601,601,602,602,602,603,603,603,604,604,604
    )


# Total verses in surah
verses = (
    7, 286, 200, 176, 120, 165, 206, 75, 129, 109, 123, 111, 43, 52, 99, 128, 111,
    110, 98, 135, 112, 78, 118, 64, 77, 227, 93, 88, 69, 60, 34, 30, 73, 54, 45, 83,
    182, 88, 75, 85, 54, 53, 89, 59, 37, 35, 38, 29, 18, 45, 60, 49, 62, 55, 78, 96,
    29, 22, 24, 13, 14, 11, 11, 18, 12, 12, 30, 52, 52, 44, 28, 28, 20, 56, 40, 31,
    50, 40, 46, 42, 29, 19, 36, 25, 22, 17, 19, 26, 30, 20, 15, 21, 11, 8, 8, 19, 5,
    8, 8, 11, 11, 8, 3, 9, 5, 4, 7, 3, 6, 3, 5, 4, 5, 6
    )


# Page number of Hizb start (for future)
hizbStartPage = (
    1, 11, 22, 32, 42, 51, 62, 72, 82, 92, 102, 112, 121, 132, 142, 151, 162, 173, 182, 192, 201,
    212, 222, 231, 242, 252, 262, 272, 282, 292, 302, 312, 322, 332, 342, 352, 362, 371, 382, 392,
    402, 413, 422, 431, 442, 451, 462, 472, 482, 491, 502, 513, 522, 531, 542, 553, 562, 572, 582, 591
        )


# Page number of Juz start (for future)
juzPage = (
    1, 11, 22, 32, 42, 51, 62, 72, 82, 92, 102, 112, 121, 132, 142, 151, 162, 173, 182, 192, 201,
    212, 222, 231, 242, 252, 262, 272, 282, 292, 302, 312, 322, 332, 342, 352, 362, 371, 382, 392,
    402, 413, 422, 431, 442, 451, 462, 472, 482, 491, 502, 513, 522, 531, 542, 553, 562, 572, 582, 591
    )

