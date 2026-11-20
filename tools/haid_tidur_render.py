import sys
sys.path.insert(0, __import__("os").path.dirname(__file__))
from carousel_lib import Deck, render, HANDLE

D = Deck("Fikih Syafi'i · Fikih wanita", 10)
K = D.kitab

# 1 COVER
D.add(f"""
<div class='frame'></div>
<div style='position:absolute;top:120px;left:110px;right:110px'>
  <div style='font-size:22px;letter-spacing:.24em;font-weight:700;color:#D4A84B'>FIKIH MADZHAB SYAFI'I · FIKIH WANITA</div>
  <div style='width:70px;height:3px;background:#D4A84B;margin:26px 0 0'></div>
</div>
<div style='position:absolute;top:330px;left:110px;right:110px'>
  <div class='ar' style='text-align:left;font-size:46px;color:#D4A84B;line-height:1.4;margin-bottom:26px'>الْأَصْلُ فِي كُلِّ حَادِثٍ تَقْدِيرُهُ بِأَقْرَبِ زَمَنٍ</div>
  <div style="font-family:'Lora',serif;font-weight:700;font-size:84px;line-height:1.08;letter-spacing:-.01em">Tidur Masih Haid,<br>Bangun Sudah Suci.<br>Dihitung Sejak Kapan?</div>
  <div style='font-size:31px;line-height:1.45;color:rgba(243,235,221,.78);margin-top:34px;max-width:860px'>Atau sebaliknya: tidur dalam keadaan suci, bangun sudah haid. Lalu bagaimana shalat yang waktunya lewat selama ia tidur?</div>
</div>
<div style='position:absolute;bottom:104px;left:110px;right:110px;display:flex;justify-content:space-between;align-items:flex-end'>
  <div><div style="font-family:'Lora',serif;font-weight:700;font-size:30px">Ukkaasyah Abdurrahman</div>
  <div style='font-size:22px;color:rgba(243,235,221,.65);margin-top:6px'>{HANDLE}</div></div>
  <div style='text-align:right'><div style='font-size:19px;color:rgba(243,235,221,.55);margin-bottom:8px'>Rujukan: Hasyiyah Al-Jamal · Nihayah · Fathul Mu'in</div><div style='font-size:22px;font-weight:600;color:#D4A84B'>geser &rarr;</div></div>
</div>""", "cover")

# 2 KASUS
D.add(D.chrome(2, "Kasusnya") + """
<div class='wrap'>
  <h2>Dua kejadian yang sering ditanyakan</h2>
  <div class='rule'></div>
  <div class='box'>
    <div class='pill'>KASUS 1</div>
    <div style='font-size:27px;line-height:1.5'>Seorang muslimah tidur siang setelah azan Zhuhur, belum sempat shalat. Ia bangun ketika waktu Ashar sudah masuk, dan <b class='g'>mendapati darah haid</b>.</div>
    <div style='font-size:25px;line-height:1.45;color:#6B6257;margin-top:10px'>Haidnya dihitung sejak ia tidur atau sejak bangun? Zhuhurnya bagaimana?</div>
  </div>
  <div class='box' style='margin-top:24px'>
    <div class='pill'>KASUS 2</div>
    <div style='font-size:27px;line-height:1.5'>Malamnya ia tidur dalam keadaan masih haid. Ia bangun setelah azan Subuh, dan ternyata <b class='g'>sudah bersih</b>. Ia tidak tahu bersihnya sejak jam berapa.</div>
    <div style='font-size:25px;line-height:1.45;color:#6B6257;margin-top:10px'>Wajibkah mengqadha Maghrib dan Isya? Kalau di bulan Ramadhan, sahkah puasanya hari itu?</div>
  </div>
</div>""")

# 3 KESIMPULAN
D.add(D.chrome(3, "Jawaban singkat") + """
<div class='wrap'>
  <h2>Jawaban singkatnya</h2>
  <div class='rule'></div>
  <p class='body' style='font-size:28px;margin-bottom:24px'>Patokannya adalah <b class='g'>saat ia mendapatinya, yaitu ketika bangun</b>. Bukan saat ia mulai tidur.</p>
  <ol class='syarat'>
    <li><b class='g'>Tidur suci, bangun haid.</b> Haidnya dihitung sejak bangun. Shalat yang waktunya sudah masuk sebelum ia bangun dan belum dikerjakan (Zhuhur pada kasus 1) wajib diqadha setelah ia suci nanti.</li>
    <li><b class='g'>Tidur haid, bangun suci.</b> Sucinya dihitung sejak bangun. Maghrib dan Isya semalam tidak wajib diqadha. Segera mandi, lalu shalat Subuh.</li>
    <li><b class='g'>Bulan Ramadhan.</b> Bangun sudah lewat Subuh dan tidak tahu kapan bersihnya: puasa hari itu tidak sah, wajib diganti.</li>
    <li><b class='g'>Kecuali ia tahu pasti waktunya</b>, misalnya sempat terbangun dan mengecek. Yang pasti itulah yang dipakai.</li>
  </ol>
  <div style='margin-top:auto;font-size:23px;font-weight:600;color:#9A7A33'>Dalil dan nukilan kitabnya di slide berikutnya &rarr;</div>
</div>""")

# 4 DALIL
D.add(D.chrome(4, "Dalil") + """
<div class='wrap'>
  <h2>Dasarnya dari hadits</h2>
  <div class='rule'></div>
  <div class='box'>
    <div class='ar' style='font-size:34px;line-height:1.8;color:#1E3A2B'>فَإِذَا أَقْبَلَتِ الْحَيْضَةُ فَدَعِي الصَّلَاةَ، وَإِذَا أَدْبَرَتْ فَاغْسِلِي عَنْكِ الدَّمَ وَصَلِّي</div>
    <p style='font-size:24px;line-height:1.5;margin-top:8px'>&ldquo;Jika haid datang, tinggalkan shalat. Jika ia sudah pergi, bersihkan darah darimu lalu shalatlah.&rdquo;</p>
    <div class='src'>Kisah Fathimah bintu Abi Hubaisy &middot; HR. Al-Bukhari no. 228, Muslim no. 333</div>
  </div>
  <div class='box' style='margin-top:22px'>
    <div class='ar' style='font-size:32px;line-height:1.8;color:#1E3A2B'>إِذَا وَجَدَ أَحَدُكُمْ فِي بَطْنِهِ شَيْئًا فَأَشْكَلَ عَلَيْهِ أَخَرَجَ مِنْهُ شَيْءٌ أَمْ لَا، فَلَا يَخْرُجَنَّ مِنَ الْمَسْجِدِ حَتَّى يَسْمَعَ صَوْتًا أَوْ يَجِدَ رِيحًا</div>
    <p style='font-size:24px;line-height:1.5;margin-top:8px'>&ldquo;Jika salah seorang dari kalian merasakan sesuatu di perutnya lalu ragu apakah ada yang keluar atau tidak, janganlah ia keluar dari masjid sampai mendengar suara atau mencium bau.&rdquo;</p>
    <div class='src'>Abu Hurairah &middot; HR. Muslim no. 362</div>
  </div>
  <p class='body' style='margin-top:24px;font-size:26px'>Hukum haid dikaitkan dengan <b class='g'>datang dan perginya darah</b>. Dan keadaan yang sudah pasti <b class='g'>tidak bergeser karena ragu</b>. Selama tidur, ia tidak tahu kapan darah itu datang atau berhenti. Yang ia ketahui pasti hanya saat ia melihatnya.</p>
</div>""")

# 5 KAIDAH
D.add(D.chrome(5, "Kaidah fikih") + """
<div class='wrap'>
  <h2>Kaidah yang dipakai</h2>
  <div class='rule'></div>
  <div class='box'>
    <div class='ar' style='font-size:40px;line-height:1.7;color:#1E3A2B'>الْأَصْلُ فِي كُلِّ حَادِثٍ تَقْدِيرُهُ بِأَقْرَبِ زَمَنٍ</div>
    <p style='font-size:25px;line-height:1.5;margin-top:8px'>&ldquo;Setiap kejadian yang tidak diketahui waktunya, dianggap terjadi pada waktu yang paling dekat.&rdquo;</p>
  </div>
  <div class='box' style='margin-top:20px'>
    <div class='ar' style='font-size:40px;line-height:1.7;color:#1E3A2B'>الْيَقِينُ لَا يُزَالُ بِالشَّكِّ</div>
    <p style='font-size:25px;line-height:1.5;margin-top:8px'>&ldquo;Sesuatu yang yakin tidak hilang karena keraguan.&rdquo;</p>
  </div>
  <ul class='dot' style='margin-top:26px'>
    <li>Darah yang didapati saat bangun <b class='g'>dianggap baru keluar menjelang ia bangun</b>. Sebelum itu ia tetap dihukumi suci, sesuai keadaan yakinnya.</li>
    <li>Bersih yang didapati saat bangun <b class='g'>dianggap baru terjadi menjelang ia bangun</b>. Sebelum itu ia tetap dihukumi haid.</li>
  </ul>
  <div style='margin-top:auto;font-size:21px;line-height:1.45;color:#6B6257;border-top:1px dashed #D9CBB0;padding-top:16px'>Catatan: dalam kitab Syafi'iyyah yang kami telusuri di Turath, belum kami temukan nash yang membahas persis kasus tidur ini. Jawabannya diambil dari kaidah di atas, yang dipakai para ulama madzhab pada kasus-kasus serupa.</div>
</div>""")

# 6 HASYIYAH AL-JAMAL 1/236 (menukil Ibnu Hajar, Syarh Al-'Ubab & Syarh Al-Irsyad)
t_jamal = ("وَعِبَارَةُ الْعُبَابِ وَشَرْحِهِ لِابْنِ حَجَرٍ: (فَرْعٌ) الْمُبْتَدَأَةُ وَالْمُعْتَادَةُ ⟦يَثْبُتُ لَهُمَا حُكْمُ الْحَائِضِ بِمُجَرَّدِ رُؤْيَةِ الدَّمِ⟧ فِي زَمَنِ الْإِمْكَانِ … "
           "وَعِبَارَةُ الْإِرْشَادِ وَشَرْحِهَا لِابْنِ حَجَرٍ: ⟦وَتَحِيضُ امْرَأَةٌ رَأَتْ الدَّمَ فِي سِنِّ الْحَيْضِ بِرُؤْيَتِهِ⟧ فَتُؤْمَرُ بِاجْتِنَابِ مَا تَجْتَنِبُهُ الْحَائِضُ مِنْ صَوْمٍ وَصَلَاةٍ وَوَطْءٍ "
           "وَلَا تَنْتَظِرُ بُلُوغَهُ يَوْمًا وَلَيْلَةً عَمَلًا بِالظَّاهِرِ … ⟦وَكَمَا أَنَّهَا تَحِيضُ بِرُؤْيَتِهِ تَطْهُرُ أَيْ يُحْكَمُ بِطُهْرِهَا بِانْقِطَاعِهِ⟧ بَعْدَ بُلُوغِ أَقَلِّهِ "
           "فَتُؤْمَرُ بِالْغُسْلِ وَالصَّلَاةِ وَالصَّوْمِ")
D.add(D.chrome(6, "Nukilan kitab · 1") + f"""
<div class='wrap' style='top:118px'>
  {K("حاشية الجمل على شرح المنهج", "ج ١ · ص ٢٣٦", t_jamal, "app.turath.io/book/21598?page=235")}
  <div class='tr'>
    <div class='lab'>Terjemah bagian yang ditandai</div>
    <p>Al-Jamal menukil dua kitab Ibnu Hajar: &ldquo;<b class='g'>Hukum haid berlaku baginya sejak ia melihat darah.</b>&rdquo; &ldquo;Wanita yang melihat darah pada usia haid <b class='g'>dihukumi haid dengan melihatnya</b> &hellip; Dan sebagaimana ia dihukumi haid dengan melihatnya, <b class='g'>ia dihukumi suci dengan berhentinya darah</b>.&rdquo;</p>
    <p style='margin-top:10px'>Jadi hukum haid dan suci terikat pada <b class='g'>apa yang ia lihat dan ketahui</b>, bukan perkiraan.</p>
  </div>
</div>""")

# 7 NIHAYATUL MUHTAJ 2/34: kaidah aqrab zaman pada najis
t_nih = ("(وَإِنْ عَلِمَ) بِالنَّجَسِ قَبْلَ الشُّرُوعِ فِيهَا (ثُمَّ نَسِيَ) فَصَلَّى ثُمَّ تَذَكَّرَ … (وَجَبَ الْقَضَاءُ عَلَى الْمَذْهَبِ) بِتَفْرِيطِهِ … "
         "وَحَيْثُ لَزِمَهُ الْإِعَادَةُ أَعَادَ حَتْمًا كُلَّ صَلَاةٍ تَيَقَّنَ فِعْلَهَا مَعَ النَّجَاسَةِ، "
         "⟦فَإِنْ احْتَمَلَ وُجُودَهَا بَعْدَ الصَّلَاةِ فَلَا إذْ الْأَصْلُ فِي كُلِّ حَادِثٍ تَقْدِيرُهُ بِأَقْرَبِ زَمَنٍ⟧")
D.add(D.chrome(7, "Nukilan kitab · 2") + f"""
<div class='wrap' style='top:118px'>
  {K("نهاية المحتاج — شمس الدين الرملي", "ج ٢ · ص ٣٤", t_nih, "app.turath.io/book/3565?page=584")}
  <div class='tr'>
    <div class='lab'>Terjemah bagian yang ditandai</div>
    <p>Tentang orang yang mendapati najis di pakaiannya setelah shalat: &ldquo;Ia wajib mengulang setiap shalat yang <b class='g'>pasti</b> dikerjakan bersama najis itu. <b class='g'>Adapun jika mungkin najis itu baru ada setelah shalat, maka tidak wajib diulang</b>, karena asal setiap kejadian dianggap terjadi pada waktu yang paling dekat.&rdquo;</p>
    <p style='margin-top:10px'>Kaidah yang sama dipakai untuk darah haid dan bersihnya: <b class='g'>dianggap terjadi paling akhir, yaitu menjelang ia mendapatinya.</b></p>
  </div>
</div>""")

# 8 MANHAJ ATH-THULLAB 1/13: kapan shalat menjadi wajib
t_man = ("فصل: إنما تجب على مسلم مكلف طاهر فلا قضاء على كافر أصلي ولا صبي … ولا حائض ونفساء "
         "⟦ولو زالت الموانع وبقي قدر تحرم وخلا منها قدر الطهر والصلاة لزمت⟧ مع فرض قبلها إن صلح لجمعه معها وخلا قدره … "
         "⟦ولو طرأ مانع في الوقت وأدرك قدر الصلاة وطهر لا يقدم لزمت⟧")
D.add(D.chrome(8, "Nukilan kitab · 3") + f"""
<div class='wrap' style='top:118px'>
  {K("منهج الطلاب — زكريا الأنصاري", "ج ١ · ص ١٣", t_man, "app.turath.io/book/12100?page=11")}
  <div class='tr'>
    <div class='lab'>Terjemah bagian yang ditandai</div>
    <p>&ldquo;<b class='g'>Jika penghalang (seperti haid) hilang</b> sementara waktu shalat masih tersisa seukuran takbiratul ihram &hellip; <b class='g'>maka shalat itu wajib</b> &hellip;</p>
    <p style='margin-top:10px'><b class='g'>Jika penghalang datang di tengah waktu</b>, padahal ia sempat mendapati waktu seukuran shalat dan bersuci yang tidak bisa didahulukan, <b class='g'>maka shalat itu wajib</b> (diqadha).&rdquo;</p>
    <p style='margin-top:10px;font-size:23px;color:#6B6257'>Kasus 1: Zhuhur sudah masuk saat ia masih dihukumi suci, maka wajib diqadha. Kasus 2: sucinya dihukumi terjadi di waktu Subuh, maka yang wajib Subuh saja.</p>
  </div>
</div>""")

# 9 FATHUL MU'IN 1/262: puasa
t_fm = ("قال شيخنا: ⟦ولو شك هل وقعت نيته قبل الفجر أو بعده؟ لم تصح لأن الأصل عدم وقوعها ليلا إذ الأصل في كل حادث تقديره بأقرب زمن⟧ "
        "بخلاف ما لو نوى ثم شك: هل طلع الفجر أو لا؟ لأن الأصل عدم طلوعه للأصل المذكور أيضا. انتهى. "
        "ولا يبطلها نحو أكل وجماع بعدها وقبل الفجر")
D.add(D.chrome(9, "Nukilan kitab · 4") + f"""
<div class='wrap' style='top:118px'>
  {K("فتح المعين — زين الدين المليباري", "ج ١ · ص ٢٦٢", t_fm, "app.turath.io/book/11327?page=238")}
  <div class='tr'>
    <div class='lab'>Terjemah bagian yang ditandai</div>
    <p>Zainuddin Al-Malibari menukil gurunya, Ibnu Hajar: &ldquo;<b class='g'>Jika ia ragu apakah niatnya terjadi sebelum fajar atau sesudahnya, puasanya tidak sah</b>, karena asalnya niat itu tidak terjadi di malam hari, sebab asal setiap kejadian dianggap terjadi pada waktu yang paling dekat.&rdquo;</p>
    <p style='margin-top:10px'>Begitu pula bersih dari haid yang baru diketahui setelah Subuh: <b class='g'>dianggap terjadi setelah fajar</b>. Maka ia tidak memenuhi syarat puasa sejak fajar, dan puasa hari itu wajib diganti.</p>
  </div>
</div>""")

# 10 KHILAF, CATATAN & PENUTUP
D.add(D.chrome(10, "Khilaf & catatan", last=True) + f"""
<div class='wrap'>
  <h2>Pendapat ulama dan catatan</h2>
  <div class='rule'></div>
  <div class='kh'><div class='who'>Syafi'iyyah</div><div class='what'>Ar-Ramli dan Ibnu Hajar sama-sama memakai kaidah &ldquo;waktu paling dekat&rdquo;. Dalam penelusuran kami, tidak ditemukan perbedaan di antara keduanya dalam soal ini.</div></div>
  <div class='kh'><div class='who'>Malikiyyah</div><div class='what'>Ibnu Rusyd: jika bangun setelah fajar dan sudah suci, ia dihukumi seperti keadaannya saat tidur, sehingga tidak wajib mengqadha shalat malam. Puasanya tetap diganti untuk berhati-hati.</div><div class='ref'>dinukil Mayyarah, Ad-Durr Ats-Tsamin 1/209</div></div>
  <div class='kh'><div class='who'>Ibnu Utsaimin</div><div class='what'>Tidak wajib mengqadha Isya. Tetapi ia wajib segera mandi dan shalat Subuh pada waktunya, jangan menunggu matahari terbit.</div><div class='ref'>Fatawa Nur 'ala Ad-Darb</div></div>
  <div style='margin-top:auto;background:#1E3A2B;color:#F3EBDD;border-radius:22px;padding:28px 36px;display:flex;justify-content:space-between;align-items:center'>
    <div><div style="font-family:'Lora',serif;font-weight:700;font-size:29px">Simpan, lalu kirim ke saudarimu.</div>
    <div style='font-size:21px;color:rgba(243,235,221,.75);margin-top:6px'>Wallahu a'lam.</div></div>
    <div style='text-align:right;white-space:nowrap;margin-left:24px'><div style="font-family:'Lora',serif;font-weight:700;font-size:24px;color:#D4A84B">Ukkaasyah Abdurrahman</div>
    <div style='font-size:19px;color:rgba(243,235,221,.65);margin-top:4px'>{HANDLE}</div></div>
  </div>
</div>""")

if __name__ == "__main__":
    render(D, sys.argv[1] if len(sys.argv) > 1 else "out")
