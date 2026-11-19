import sys
sys.path.insert(0, __import__("os").path.dirname(__file__))
from carousel_lib import Deck, render, HANDLE

D = Deck("Fikih Syafi'i · Seri haid", 10)
K = D.kitab

# 1 COVER
D.add(f"""
<div class='frame'></div>
<div style='position:absolute;top:120px;left:110px;right:110px'>
  <div style='font-size:22px;letter-spacing:.24em;font-weight:700;color:#D4A84B'>FIKIH MADZHAB SYAFI'I · SERI HAID</div>
  <div style='width:70px;height:3px;background:#D4A84B;margin:26px 0 0'></div>
</div>
<div style='position:absolute;top:350px;left:110px;right:110px'>
  <div class='ar' style='text-align:left;font-size:58px;color:#D4A84B;line-height:1.25;margin-bottom:24px'>إِدْرَاكُ الْوَقْتِ بَعْدَ الطُّهْرِ</div>
  <div style="font-family:'Lora',serif;font-weight:700;font-size:88px;line-height:1.07;letter-spacing:-.01em">Suci 5 Menit<br>Sebelum Maghrib,<br>Zhuhur Ikut<br>Diqadha?</div>
  <div style='font-size:31px;line-height:1.45;color:rgba(243,235,221,.78);margin-top:34px;max-width:840px'>Juga kalau haid datang setelah azan, padahal belum sempat shalat.</div>
</div>
<div style='position:absolute;bottom:104px;left:110px;right:110px;display:flex;justify-content:space-between;align-items:flex-end'>
  <div><div style="font-family:'Lora',serif;font-weight:700;font-size:30px">Ukkaasyah Abdurrahman</div>
  <div style='font-size:22px;color:rgba(243,235,221,.65);margin-top:6px'>{HANDLE}</div></div>
  <div style='text-align:right'><div style='font-size:19px;color:rgba(243,235,221,.55);margin-bottom:8px'>Rujukan: Tuhfah · Nihayah · Mughni</div><div style='font-size:22px;font-weight:600;color:#D4A84B'>geser &rarr;</div></div>
</div>""", "cover")

# 2 KASUS
D.add(D.chrome(2) + """
<div class='wrap'>
  <h2>Tiga kejadian yang sering ditanyakan</h2>
  <div class='rule'></div>
  <div class='kh'><div class='who'>&ldquo;Darah berhenti jam 17.45&rdquo;</div><div class='what'>Maghrib jam 17.55. Selesai mandi sudah azan. Apakah Ashar masih wajib, atau cukup Maghrib saja?</div></div>
  <div class='kh'><div class='who'>&ldquo;Bersih jam 3 pagi&rdquo;</div><div class='what'>Langsung tidur, bangun pas Subuh. Maghrib dan Isya semalam bagaimana?</div></div>
  <div class='kh'><div class='who'>&ldquo;Haid datang jam 12.40&rdquo;</div><div class='what'>Azan Zhuhur jam 12.00 dan ia belum sempat shalat. Apakah Zhuhur hari itu harus diganti?</div></div>
  <div class='box' style='margin-top:auto'><div style='font-size:26px;line-height:1.5'>Banyak yang mengira cukup mengerjakan shalat yang waktunya sedang berjalan. Dalam madzhab Syafi'i, <b class='g'>jawabannya tidak sesederhana itu.</b></div></div>
</div>""")

# 3 DALIL
D.add(D.chrome(3) + """
<div class='wrap'>
  <h2>Dua pegangan dari hadits</h2>
  <div class='rule'></div>
  <div class='box'>
    <div class='ar' style='font-size:32px;line-height:1.8;color:#1E3A2B'>كَانَ يُصِيبُنَا ذَلِكَ، فَنُؤْمَرُ بِقَضَاءِ الصَّوْمِ، وَلَا نُؤْمَرُ بِقَضَاءِ الصَّلَاةِ</div>
    <p style='font-size:24px;line-height:1.5;margin-top:10px'>&ldquo;Dulu kami mengalami haid, lalu kami diperintah mengqadha puasa dan tidak diperintah mengqadha shalat.&rdquo;</p>
    <div class='src'>&lsquo;Aisyah radhiyallahu &lsquo;anha &middot; HR. Muslim no. 335</div>
  </div>
  <div class='box' style='margin-top:22px'>
    <div class='ar' style='font-size:32px;line-height:1.8;color:#1E3A2B'>مَنْ أَدْرَكَ مِنَ الصُّبْحِ رَكْعَةً قَبْلَ أَنْ تَطْلُعَ الشَّمْسُ فَقَدْ أَدْرَكَ الصُّبْحَ، وَمَنْ أَدْرَكَ رَكْعَةً مِنَ الْعَصْرِ قَبْلَ أَنْ تَغْرُبَ الشَّمْسُ فَقَدْ أَدْرَكَ الْعَصْرَ</div>
    <p style='font-size:24px;line-height:1.5;margin-top:10px'>&ldquo;Siapa yang mendapati satu rakaat Subuh sebelum matahari terbit, ia telah mendapati Subuh. Siapa yang mendapati satu rakaat Ashar sebelum matahari terbenam, ia telah mendapati Ashar.&rdquo;</p>
    <div class='src'>Abu Hurairah &middot; HR. Al-Bukhari no. 579 (lafaz Al-Bukhari), Muslim no. 608</div>
  </div>
  <p class='body' style='margin-top:24px;font-size:26px'>Jadi shalat <b class='g'>selama masa haid</b> tidak diganti. Yang dibahas di sini adalah shalat di <b class='g'>ujung-ujung waktu</b>: saat haid baru berhenti atau baru datang.</p>
</div>""")

# 4 TUHFAH 1/454: suci di akhir waktu, cukup seukuran takbir
t_takbir = ("(وَ) حُكْمُهُ أَنَّهُ (لَوْ زَالَتْ هَذِهِ الْأَسْبَابُ) الْكُفْرُ الْأَصْلِيُّ، وَالصِّبَا ⟦وَنَحْوُ الْحَيْضِ⟧، وَالْجُنُونِ "
            "⟦(وَ) قَدْ (بَقِيَ مِنْ) آخِرِ (الْوَقْتِ تَكْبِيرَةٌ) أَيْ قَدْرُهَا (وَجَبَتْ الصَّلَاةُ)⟧ أَيْ صَلَاةُ الْوَقْتِ "
            "⟦إنْ بَقِيَ سَلِيمًا زَمَنٌ يَسَعُ أَخَفَّ مُمْكِنٍ مِنْهَا⟧ كَرَكْعَتَيْنِ لِلْمُسَافِرِ الْقَاصِرِ ⟦وَمِنْ شُرُوطِهَا⟧ … "
            "— حاشية الشرواني — قَوْلُ الْمَتْنِ (وَقَدْ بَقِيَ مِنْ الْوَقْتِ تَكْبِيرَةٌ إلَخْ) "
            "⟦وَلَا يُشْتَرَطُ أَنْ يُدْرِكَ مَعَ التَّكْبِيرَةِ قَدْرَ الطَّهَارَةِ عَلَى الْأَظْهَرِ؛ لِأَنَّ الطَّهَارَةَ شَرْطٌ لِلصِّحَّةِ لَا اللُّزُومِ⟧ نِهَايَةٌ وَمُغْنِي")
D.add(D.chrome(4, "Nukilan kitab · 1") + f"""
<div class='wrap' style='top:118px'>
  {K("تحفة المحتاج — ابن حجر الهيتمي", "ج ١ · ص ٤٥٤", t_takbir, "app.turath.io/book/9059?page=455")}
  <div class='tr'>
    <div class='lab'>Terjemah bagian yang ditandai</div>
    <p>&ldquo;Jika penghalang seperti <b class='g'>haid</b> hilang, <b class='g'>sementara waktu yang tersisa seukuran takbir, maka shalat waktu itu wajib</b>, dengan syarat setelahnya ia tetap terbebas (dari penghalang) selama waktu yang cukup untuk shalat itu secara paling ringkas, <b class='g'>beserta syarat-syaratnya</b>.&rdquo;</p>
    <p style='margin-top:12px'>Hasyiyah Asy-Syarwani menukil Nihayah dan Mughni: <b class='g'>tidak disyaratkan sisa waktunya cukup untuk bersuci</b>, karena bersuci syarat sahnya shalat, bukan syarat wajibnya.</p>
  </div>
</div>""")

# 5 TUHFAH 1/455: shalat sebelumnya ikut wajib
t_jamak = ("وَالْأَظْهَرُ عَلَى الْأَوَّلِ ⟦وُجُوبُ الظُّهْرِ مَعَ الْعَصْرِ بِإِدْرَاكِ تَكْبِيرَةِ آخِرِ وَقْتِ الْعَصْرِ وَ وُجُوبُ الْمَغْرِبِ مَعَ الْعِشَاءِ "
           "بِإِدْرَاكِ تَكْبِيرَةِ آخِرِ وَقْتِ الْعِشَاءِ⟧ ⟦لِاتِّحَادِ الْوَقْتَيْنِ فِي الْعُذْرِ فَفِي الضَّرُورَةِ أَوْلَى⟧ "
           "وَيُشْتَرَطُ بَقَاءُ سَلَامَتِهِ هُنَا أَيْضًا بِقَدْرِ مَا مَرَّ وَمَا لَزِمَهُ فَلَوْ بَلَغَ ثُمَّ جُنَّ مَثَلًا قَبْلَ مَا يَسَعُ ذَلِكَ فَلَا لُزُومَ "
           "وَإِنْ زَالَ الْجُنُونُ فَوْرًا عَلَى مَا اقْتَضَاهُ إطْلَاقُهُمْ … وَخُصَّ مَا ذُكِرَ؛ ⟦لِأَنَّ الصُّبْحَ، وَالْعَصْرَ، وَالْعِشَاءَ لَا يُتَصَوَّرُ "
           "وُجُوبُ وَاحِدٍ مِنْهَا بِإِدْرَاكِ جُزْءٍ مِمَّا بَعْدَهَا إذْ لَا جَمْعَ⟧")
D.add(D.chrome(5, "Nukilan kitab · 2") + f"""
<div class='wrap' style='top:118px'>
  {K("تحفة المحتاج — ابن حجر الهيتمي", "ج ١ · ص ٤٥٥–٤٥٦", t_jamak, "app.turath.io/book/9059?page=456")}
  <div class='tr'>
    <div class='lab'>Terjemah bagian yang ditandai</div>
    <p>&ldquo;&hellip; <b class='g'>Zhuhur ikut wajib bersama Ashar</b> bila mendapati seukuran takbir di akhir waktu Ashar, dan <b class='g'>Maghrib ikut wajib bersama Isya</b> bila mendapatinya di akhir waktu Isya, <b class='g'>karena kedua waktu itu menyatu ketika ada uzur</b> (seperti jamak saat safar), maka dalam keadaan darurat lebih pantas lagi &hellip;</p>
    <p style='margin-top:10px'>Subuh, Ashar dan Isya tidak bisa menjadi wajib karena mendapati bagian waktu shalat sesudahnya, sebab tidak ada jamak (di antara keduanya).&rdquo;</p>
  </div>
</div>""")

# 6 TABEL
rows = [("di waktu Zhuhur", "Zhuhur"),
        ("di waktu Ashar,<br><span>walau sesaat sebelum Maghrib</span>", "Zhuhur + Ashar"),
        ("di waktu Maghrib", "Maghrib"),
        ("di waktu Isya,<br><span>walau sesaat sebelum Subuh</span>", "Maghrib + Isya"),
        ("di waktu Subuh,<br><span>sebelum matahari terbit</span>", "Subuh")]
trs = "".join(f"<tr><td>{a}</td><td class='w'>{b}</td></tr>" for a, b in rows)
D.add(D.chrome(6, "Ringkasan") + f"""
<style>
table.t{{width:100%;border-collapse:separate;border-spacing:0 12px;margin-top:-12px}}
table.t th{{text-align:left;font-size:19px;letter-spacing:.14em;text-transform:uppercase;color:#9A7A33;font-weight:700;padding:0 24px}}
table.t td{{background:#FFFDF8;border-top:1.5px solid #E4D7BE;border-bottom:1.5px solid #E4D7BE;padding:18px 24px;font-size:27px;line-height:1.3}}
table.t td:first-child{{border-left:1.5px solid #E4D7BE;border-radius:16px 0 0 16px}}
table.t td:last-child{{border-right:1.5px solid #E4D7BE;border-radius:0 16px 16px 0}}
table.t td span{{font-size:21px;color:#7C6E57}}
table.t td.w{{font-family:'Lora',serif;font-weight:700;color:#1E3A2B;white-space:nowrap}}
</style>
<div class='wrap'>
  <h2>Darah berhenti kapan, shalat apa yang wajib?</h2>
  <div class='rule'></div>
  <table class='t'><tr><th>Darah berhenti&hellip;</th><th>Wajib dikerjakan</th></tr>{trs}</table>
  <div class='box' style='margin-top:auto;padding:24px 30px'>
    <div style='font-size:23px;line-height:1.5'><b class='g'>&ldquo;Sesaat&rdquo;</b> = seukuran takbiratul ihram. Yang dihitung <b class='g'>saat darah benar-benar berhenti</b>, bukan saat selesai mandi. Syaratnya, setelah suci ia tidak kedatangan haid lagi selama waktu yang cukup untuk bersuci dan mengerjakan shalat-shalat itu.</div>
  </div>
</div>""")

# 7 TUHFAH 1/457-458: haid datang setelah masuk waktu
t_tara = ("(وَلَوْ) طَرَأَ مَانِعٌ كَأَنْ ⟦(حَاضَتْ)⟧ أَوْ نُفِسَتْ (أَوْ جُنَّ)، أَوْ أُغْمِيَ عَلَيْهِ (أَوَّلَ الْوَقْتِ) وَاسْتَغْرَقَهُ "
          "⟦(وَجَبَتْ تِلْكَ) الصَّلَاةُ (إنْ) كَانَ قَدْ (أَدْرَكَ) مِنْ الْوَقْتِ قَبْلَ طُرُوُّ مَانِعِهِ⟧ فَالْأَوَّلُ فِي كَلَامِهِ نِسْبِيٌّ … "
          "⟦(قَدْرَ الْفَرْضِ) الَّذِي يَلْزَمُهُ بِأَخَفِّ مُمْكِنٍ⟧ ⟦مَعَ إدْرَاكِ زَمَنِ طُهْرٍ يَمْتَنِعُ تَقْدِيمُهُ كَتَيَمُّمٍ وَطُهْرِ سَلَسٍ⟧ "
          "بِخِلَافِ غَيْرِهِ؛ لِأَنَّهُ كَانَ يُمْكِنُهُ تَقْدِيمُهُ … ⟦(وَإِلَّا) يُدْرِكْ ذَلِكَ (فَلَا) يَجِبْ لِانْتِفَاءِ التَّمَكُّنِ⟧ "
          "— حاشية الشرواني — (قَوْلُهُ: تِلْكَ الصَّلَاةُ) ⟦أَيْ: لَا الثَّانِيَةُ الَّتِي تُجْمَعُ مَعَهَا⟧ نِهَايَةٌ وَمُغْنِي")
D.add(D.chrome(7, "Nukilan kitab · 3") + f"""
<div class='wrap' style='top:118px'>
  {K("تحفة المحتاج — ابن حجر الهيتمي", "ج ١ · ص ٤٥٧–٤٥٨", t_tara, "app.turath.io/book/9059?page=458")}
  <div class='tr'>
    <div class='lab'>Terjemah bagian yang ditandai</div>
    <p>&ldquo;Kalau ia <b class='g'>haid</b> &hellip; setelah masuk waktu, <b class='g'>shalat itu tetap wajib</b> jika sebelum haid ia sempat mendapati waktu <b class='g'>seukuran shalat fardhu itu secara paling ringkas</b>, ditambah waktu bersuci yang tidak boleh didahulukan, seperti tayammum dan wudhunya orang beser &hellip; <b class='g'>Kalau tidak sempat, tidak wajib.</b>&rdquo;</p>
    <p style='margin-top:10px'>Syarwani menukil Nihayah dan Mughni: yang wajib <b class='g'>hanya shalat itu</b>, bukan shalat kedua yang biasa dijamak dengannya.</p>
  </div>
</div>""")

# 8 PENERAPAN HAID DATANG
D.add(D.chrome(8) + """
<div class='wrap'>
  <h2>Kalau haid datang setelah azan</h2>
  <div class='rule'></div>
  <div class='kh'><div class='who'>Azan 12.00, haid datang 12.40</div><div class='what'>Empat puluh menit sudah lebih dari cukup untuk empat rakaat. <b class='g'>Zhuhur wajib diqadha</b> setelah ia suci nanti.</div></div>
  <div class='kh'><div class='who'>Haid datang tak lama setelah azan</div><div class='what'>Belum cukup untuk shalat empat rakaat, walau dengan cara paling ringkas: <b class='g'>tidak wajib qadha</b>.</div></div>
  <div class='kh'><div class='who'>Ashar tidak ikut</div><div class='what'>Haid di waktu Zhuhur hanya mewajibkan Zhuhur. Begitu juga haid di waktu Maghrib hanya mewajibkan Maghrib, Isya tidak ikut.</div></div>
  <div class='kh'><div class='who'>Bagi yang beser atau istihadhah</div><div class='what'>Waktu wudhunya ikut dihitung, karena wudhu mereka baru boleh dilakukan setelah masuk waktu.</div></div>
  <div class='box' style='margin-top:auto;padding:24px 30px'><div style='font-size:24px;line-height:1.5'>Kalau jadwal haid sudah dekat, <b class='g'>jangan tunda shalat di awal waktu.</b> Itu cara paling sederhana supaya tidak punya utang shalat.</div></div>
</div>""")

# 9 KHILAF
t_khilaf = ("(قَوْلُهُ: وَمِنْ شُرُوطِهَا) ⟦اعْتَمَدَ النِّهَايَةُ، وَالْمُغْنِي وَالشِّهَابُ الرَّمْلِيُّ وَشَرْحُ الْمَنْهَجِ اعْتِبَارَ قَدْرِ الطَّهَارَةِ مِنْهَا فَقَطْ "
            "دُونَ قَدْرِ السِّتْرِ، وَالتَّحَرِّي فِي الْقِبْلَةِ⟧ وَزَادَ الْمُغْنِي ⟦وَيَدْخُلُ فِي الطَّهَارَةِ هُنَا وَفِيمَا يَأْتِي الْخُبْثُ، وَالْحَدَثُ أَصْغَرُ، أَوْ أَكْبَرُ⟧ اهـ")
D.add(D.chrome(9, "Nukilan kitab · 4 · Khilaf") + f"""
<div class='wrap' style='top:118px'>
  {K("حاشية الشرواني على التحفة", "ج ١ · ص ٤٥٤", t_khilaf, "app.turath.io/book/9059?page=455")}
  <div class='tr'>
    <div class='lab'>Beberapa khilaf yang perlu diketahui</div>
    <ul class='dot' style='margin-top:6px'>
      <li><b class='g'>Waktu bebas setelah suci.</b> Ibnu Hajar ikut memperhitungkan syarat-syarat shalat. Ar-Ramli, Asy-Syirbini, Asy-Syihab Ar-Ramli dan Syarh Al-Manhaj (Zakariya Al-Anshari) <b class='g'>hanya menghitung waktu bersuci</b>, tidak termasuk menutup aurat dan mencari kiblat. Asy-Syirbini menukil Al-Isnawi (Al-Muhimmat) dan menyetujuinya: bersuci di sini mencakup membersihkan najis dan mandi.</li>
      <li><b class='g'>Satu rakaat atau satu takbir?</b> Ada qaul dalam madzhab yang mensyaratkan satu rakaat, sesuai zahir hadits. Yang dipegang adalah cukup seukuran takbir (Nihayah 1/395).</li>
      <li><b class='g'>Di luar madzhab,</b> Abu Hanifah berpendapat hanya shalat yang waktunya didapati saja yang wajib. Jumhur (Malik, Asy-Syafi'i, Ahmad) mewajibkan juga shalat sebelumnya, dan ini diriwayatkan dari Abdurrahman bin &lsquo;Auf dan Ibnu &lsquo;Abbas.</li>
    </ul>
  </div>
</div>""")

# 10 PENUTUP
D.add(D.chrome(10, "Penutup", last=True) + f"""
<div class='wrap'>
  <h2>Yang dihitung saat darah berhenti, bukan saat selesai mandi.</h2>
  <div class='rule'></div>
  <ol class='syarat'>
    <li>Suci di waktu <b class='g'>Ashar</b> &rarr; Zhuhur dan Ashar. Suci di waktu <b class='g'>Isya</b> &rarr; Maghrib dan Isya.</li>
    <li>Haid datang setelah azan dan sudah lewat waktu yang cukup untuk shalat &rarr; <b class='g'>shalat itu diqadha</b>.</li>
    <li>Shalat selama masa haid <b class='g'>tidak diqadha</b> sama sekali.</li>
  </ol>
  <p class='body' style='font-size:27px'>Punya kasus lain? Tulis di kolom komentar, insya Allah dibahas di postingan berikutnya.</p>
  <div style='margin-top:auto;background:#1E3A2B;color:#F3EBDD;border-radius:22px;padding:30px 36px;display:flex;justify-content:space-between;align-items:center'>
    <div><div style="font-family:'Lora',serif;font-weight:700;font-size:30px">Simpan, lalu kirim ke saudarimu.</div>
    <div style='font-size:22px;color:rgba(243,235,221,.75);margin-top:6px'>Banyak yang belum tahu.</div></div>
    <div style='text-align:right;white-space:nowrap;margin-left:24px'><div style="font-family:'Lora',serif;font-weight:700;font-size:24px;color:#D4A84B">Ukkaasyah Abdurrahman</div>
    <div style='font-size:19px;color:rgba(243,235,221,.65);margin-top:4px'>{HANDLE}</div></div>
  </div>
</div>""")

if __name__ == "__main__":
    render(D, sys.argv[1] if len(sys.argv) > 1 else "out")
