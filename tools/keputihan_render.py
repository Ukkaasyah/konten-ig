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
<div style='position:absolute;top:350px;left:110px;right:110px'>
  <div class='ar' style='text-align:left;font-size:62px;color:#D4A84B;line-height:1.25;margin-bottom:24px'>رُطُوبَةُ الْفَرْجِ</div>
  <div style="font-family:'Lora',serif;font-weight:700;font-size:90px;line-height:1.07;letter-spacing:-.01em">Keputihan:<br>Najis?<br>Batal Wudhu?</div>
  <div style='font-size:31px;line-height:1.45;color:rgba(243,235,221,.78);margin-top:34px;max-width:850px'>Para fuqaha membedakannya dari bagian mana cairan itu keluar. Di situ juga letak khilafnya.</div>
</div>
<div style='position:absolute;bottom:104px;left:110px;right:110px;display:flex;justify-content:space-between;align-items:flex-end'>
  <div><div style="font-family:'Lora',serif;font-weight:700;font-size:30px">Ukkaasyah Abdurrahman</div>
  <div style='font-size:22px;color:rgba(243,235,221,.65);margin-top:6px'>{HANDLE}</div></div>
  <div style='text-align:right'><div style='font-size:19px;color:rgba(243,235,221,.55);margin-bottom:8px'>Rujukan: Tuhfah · Nihayah · Mughni</div><div style='font-size:22px;font-weight:600;color:#D4A84B'>geser &rarr;</div></div>
</div>""", "cover")

# 2 PERTANYAAN
D.add(D.chrome(2) + """
<div class='wrap'>
  <h2>Pertanyaan yang hampir setiap muslimah pernah punya</h2>
  <div class='rule'></div>
  <ul class='dot'>
    <li>&ldquo;Celana dalam basah keputihan. Harus ganti dulu sebelum shalat?&rdquo;</li>
    <li>&ldquo;Baru selesai wudhu, terasa ada yang keluar. Wudhunya batal?&rdquo;</li>
    <li>&ldquo;Keputihannya keluar terus. Masa harus wudhu berkali-kali?&rdquo;</li>
    <li>&ldquo;Saya tidak tahu itu keluar dari luar atau dalam.&rdquo;</li>
  </ul>
  <div class='box' style='margin-top:auto'><div style='font-size:26px;line-height:1.5'>Jawabannya tidak satu untuk semua. Dalam madzhab Syafi'i, hukumnya <b class='g'>bergantung pada bagian mana cairan itu keluar</b>.</div></div>
</div>""")

# 9 PRAKTIS
D.add(D.chrome(3, "Jawaban singkat") + """
<div class='wrap'>
  <h2>Jawaban singkatnya</h2>
  <div class='rule'></div>
  <ol class='syarat'>
    <li><b class='g'>Basah di bagian luar saja?</b> Suci dan tidak membatalkan wudhu.</li>
    <li><b class='g'>Yakin keluar dari dalam?</b> Wudhu batal. Soal najisnya ada khilaf. Yang paling hati-hati, bersihkan dan ganti pantyliner sebelum shalat, sesuai pendapat Ar-Ramli dan Asy-Syirbini.</li>
    <li><b class='g'>Ragu dari luar atau dalam?</b> Wudhu tetap sah. Jangan dituruti rasa was-wasnya.</li>
    <li><b class='g'>Keluar terus tanpa jeda?</b> Bersihkan, pakai pembalut, wudhu setelah masuk waktu, lalu langsung shalat.</li>
    <li><b class='g'>Tidak mewajibkan mandi.</b> Keputihan bukan mani.</li>
  </ol>
  <div style='margin-top:auto;font-size:23px;font-weight:600;color:#9A7A33'>Dalil dan nukilan kitabnya di slide berikutnya &rarr;</div>
</div>""")

# 3 DALIL
D.add(D.chrome(4) + """
<div class='wrap'>
  <h2>Dasarnya</h2>
  <div class='rule'></div>
  <div class='box'>
    <div class='ar' style='font-size:36px;line-height:1.8;color:#1E3A2B'>﴿أَوْ جَاءَ أَحَدٌ مِنْكُمْ مِنَ الْغَائِطِ﴾</div>
    <p style='font-size:24px;line-height:1.5;margin-top:8px'>&ldquo;&hellip; atau salah seorang dari kalian datang dari tempat buang hajat &hellip;&rdquo;</p>
    <div class='src'>QS. Al-Ma'idah: 6</div>
  </div>
  <div class='box' style='margin-top:22px'>
    <div class='ar' style='font-size:34px;line-height:1.8;color:#1E3A2B'>لَا تُقْبَلُ صَلَاةُ مَنْ أَحْدَثَ حَتَّى يَتَوَضَّأَ</div>
    <p style='font-size:24px;line-height:1.5;margin-top:8px'>&ldquo;Tidak diterima shalat orang yang berhadats sampai ia berwudhu.&rdquo;</p>
    <div class='src'>Abu Hurairah &middot; HR. Al-Bukhari no. 135 (lafaz Al-Bukhari), Muslim no. 225</div>
  </div>
  <p class='body' style='margin-top:24px;font-size:26px'>Dalam madzhab Syafi'i, <b class='g'>apa pun yang keluar dari qubul atau dubur</b> membatalkan wudhu, kecuali mani. Dasarnya ayat dan hadits di atas, lalu diqiyaskan kepada keduanya setiap yang keluar dari jalan itu (Mughni Al-Muhtaj 1/140&ndash;141). Lalu bagaimana dengan keputihan, yang keluarnya dari tempat yang sama tapi sifatnya seperti keringat?</p>
</div>""")

# 4 TUHFAH 1/300-301: definisi dan hukum dasar
t_def = ("(وَلَيْسَتْ الْعَلَقَةُ) … (وَالْمُضْغَةُ) … ⟦(وَرُطُوبَةُ الْفَرْجِ) أَيْ الْقُبُلِ وَهُوَ مَاءٌ أَبْيَضُ مُتَرَدِّدٌ بَيْنَ الْمَذْيِ وَالْعَرَقِ⟧ "
         "يَخْرُجُ مِنْ بَاطِنِ الْفَرْجِ الَّذِي لَا يَجِبُ غَسْلُهُ ⟦بِخِلَافِ مَا يَخْرُجُ مِمَّا يَجِبُ غَسْلُهُ فَإِنَّهُ طَاهِرٌ قَطْعًا⟧ "
         "⟦وَمِنْ وَرَاءِ بَاطِنِ الْفَرْجِ فَإِنَّهُ نَجِسٌ قَطْعًا⟧ كَكُلِّ خَارِجٍ مِنْ الْبَاطِنِ كَالْمَاءِ الْخَارِجِ مَعَ الْوَلَدِ أَوْ قُبَيْلَهُ … "
         "⟦(بِنَجَسٍ)⟧ … ⟦(فِي الْأَصَحِّ)⟧ … وَأَمَّا الْأَخِيرَةُ … ⟦فَلِأَنَّهَا كَالْعَرَقِ⟧")
D.add(D.chrome(5, "Nukilan kitab · 1") + f"""
<div class='wrap' style='top:118px'>
  {K("تحفة المحتاج — ابن حجر الهيتمي", "ج ١ · ص ٣٠٠–٣٠١", t_def, "app.turath.io/book/9059?page=301")}
  <div class='tr'>
    <div class='lab'>Terjemah bagian yang ditandai</div>
    <p>&ldquo;<b class='g'>Cairan farji</b>, yaitu cairan putih yang sifatnya di antara madzi dan keringat, yang keluar dari bagian dalam farji yang tidak wajib dibasuh, <b class='g'>tidak najis menurut pendapat ashah</b>, karena ia seperti keringat.</p>
    <p style='margin-top:10px'>Yang keluar dari bagian yang wajib dibasuh <b class='g'>suci secara pasti</b>. Yang keluar dari balik bagian dalam farji <b class='g'>najis secara pasti</b>, seperti semua yang keluar dari rongga dalam tubuh.&rdquo;</p><p style='margin-top:10px;font-size:22px;color:#6B6257'>Catatan: Ibnu Hajar menyebut kata &ldquo;pasti&rdquo; ini berasal dari Imamul Haramain, dan ada yang menyanggah bahwa khilafnya berlaku di semua bagian.</p>
  </div>
</div>""")

# 5 SYARWANI: tiga bagian
t_tiga = ("(قَوْلُهُ بِخِلَافِ مَا يَخْرُجُ مِمَّا يَجِبُ غَسْلُهُ إلَخْ) ⟦وَالْحَاصِلُ أَنَّ رُطُوبَةَ الْفَرْجِ ثَلَاثُ أَقْسَامٍ⟧ "
          "⟦طَاهِرَةٌ قَطْعًا وَهِيَ مَا تَكُونُ فِي الْمَحَلِّ الَّذِي يَظْهَرُ عِنْدَ جُلُوسِهَا وَهُوَ الَّذِي يَجِبُ غَسْلُهُ فِي الْغُسْلِ وَالِاسْتِنْجَاءِ⟧، "
          "⟦وَنَجِسَةٌ قَطْعًا وَهِيَ مَا وَرَاءَ ذَكَرِ الْمُجَامِعِ⟧، ⟦وَطَاهِرَةٌ عَلَى الْأَصَحِّ وَهِيَ مَا يَصِلُهُ ذَكَرُ الْمُجَامِعِ⟧ شَيْخُنَا اهـ بُجَيْرِمِيٌّ")
tier = lambda c, n, t, d: (f"<div style='display:flex;gap:18px;align-items:flex-start;margin-bottom:14px'>"
                           f"<div style='min-width:46px;height:46px;border-radius:50%;background:{c};color:#F3EBDD;font-family:Lora,serif;font-weight:700;font-size:24px;display:flex;align-items:center;justify-content:center'>{n}</div>"
                           f"<div><div style=\"font-family:'Lora',serif;font-weight:700;font-size:26px;color:#1E3A2B\">{t}</div><div style='font-size:23px;line-height:1.4'>{d}</div></div></div>")
D.add(D.chrome(6, "Nukilan kitab · 2") + f"""
<div class='wrap' style='top:118px'>
  {K("حاشية الشرواني على التحفة", "ج ١ · ص ٣٠١", t_tiga, "app.turath.io/book/9059?page=302")}
  <div class='tr'>
    <div class='lab'>Ringkasnya, cairan farji ada tiga</div>
    {tier('#9A7A33','1','Bagian luar &rarr; suci, tanpa khilaf','Bagian yang tampak saat duduk berjongkok. Inilah yang wajib dibasuh ketika istinja dan mandi.')}
    {tier('#1E3A2B','2','Bagian tengah &rarr; suci menurut pendapat ashah','Bagian yang masih dicapai suami ketika berhubungan.')}
    {tier('#7A2E2E','3','Lebih dalam lagi &rarr; najis, tanpa khilaf','Bagian yang tidak lagi dicapai suami.')}
  </div>
</div>""")

# 6 KHILAF: Nihayah
t_nih = ("وَرُطُوبَةُ الْفَرْجِ وَهِيَ مَاءٌ أَبْيَضُ مُتَرَدِّدٌ بَيْنَ الْمَذْيِ وَالْعَرَقِ كَمَا فِي الْمَجْمُوعِ ⟦وَفِيهِ أَنَّ الْخَارِجَةَ مِنْ بَاطِنِ الْفَرْجِ نَجِسَةٌ⟧ "
         "⟦وَالْحَاصِلُ أَنَّهَا مَتَى خَرَجَتْ مِنْ مَحِلٍّ لَا يَجِبُ غَسْلُهُ فَهِيَ نَجِسَةٌ لِأَنَّهَا حِينَئِذٍ رُطُوبَةٌ جَوْفِيَّةٌ⟧، "
         "وَهِيَ إذَا خَرَجَتْ إلَى الظَّاهِرِ يُحْكَمُ بِنَجَاسَتِهَا فَلَا يَنْجَسُ ذَكَرُ الْمُجَامِعِ عِنْدَ الْحُكْمِ بِطَهَارَتِهَا، وَلَا يَجِبُ غَسْلُ الْوَلَدِ الْمُنْفَصِلِ فِي حَيَاةِ أُمِّهِ")
D.add(D.chrome(7, "Nukilan kitab · 3 · Khilaf") + f"""
<div class='wrap' style='top:118px'>
  {K("نهاية المحتاج — شمس الدين الرملي", "ج ١ · ص ٢٤٦–٢٤٧", t_nih, "app.turath.io/book/3565?page=244")}
  <div class='tr'>
    <div class='lab'>Di sinilah khilafnya</div>
    <p>&ldquo;&hellip; Dalam Al-Majmu&lsquo;: <b class='g'>yang keluar dari bagian dalam farji itu najis.</b> Kesimpulannya, <b class='g'>kapan saja ia keluar dari bagian yang tidak wajib dibasuh, ia najis</b>, karena ketika itu ia cairan dari rongga dalam.&rdquo;</p>
    <ul class='dot' style='margin-top:14px'>
      <li><b class='g'>Ibnu Hajar:</b> cairan dari bagian tengah (no. 2) tetap suci.</li>
      <li><b class='g'>Ar-Ramli dan Asy-Syirbini:</b> najis. Asy-Syirbini menambahkan, sedikit ataupun banyak sama saja (Mughni 1/236).</li>
      <li><b class='g'>Asy-Syabramalisi</b>, penulis hasyiyah atas Nihayah, menilai pendapat Ibnu Hajar <b class='g'>&ldquo;lebih dekat&rdquo;</b> (dinukil Asy-Syarwani 1/301).</li>
    </ul>
  </div>
</div>""")

# 7 BATAL WUDHU: Tuhfah 1/129-130
t_wudhu = ("(أَحَدُهَا خُرُوجُ شَيْءٍ) … (مِنْ قُبُلِهِ) أَيْ الْمُتَوَضِّئِ الْحَيِّ الْوَاضِحِ وَلَوْ رِيحًا مِنْ ذَكَرِهِ أَوْ قُبُلِهَا … "
           "⟦أَوْ خَرَجَتْ رُطُوبَةُ فَرْجِهَا إذَا كَانَتْ مِنْ وَرَاءِ مَا يَجِبُ غَسْلُهُ يَقِينًا وَإِلَّا فَلَا⟧ … "
           "— حاشية الشرواني — عِبَارَتُهُ فِي شَرْحِ الْإِرْشَادِ … ⟦كَمَا لَوْ خَرَجَتْ مِنْهَا رُطُوبَةٌ وَشَكَّ فِي أَنَّهَا مِنْ الظَّاهِرِ أَوْ الْبَاطِنِ⟧ … "
           "(قَوْلُهُ: وَإِلَّا فَلَا) ⟦يَدْخُلُ فِيهِ الشَّكُّ⟧ سم")
D.add(D.chrome(8, "Nukilan kitab · 4") + f"""
<div class='wrap' style='top:118px'>
  {K("تحفة المحتاج — ابن حجر الهيتمي", "ج ١ · ص ١٢٩–١٣٠", t_wudhu, "app.turath.io/book/9059?page=131")}
  <div class='tr'>
    <div class='lab'>Terjemah bagian yang ditandai</div>
    <p>&ldquo;(Yang membatalkan wudhu) &hellip; atau <b class='g'>keluarnya cairan farji wanita, jika dipastikan berasal dari balik bagian yang wajib dibasuh. Kalau tidak, maka tidak batal.</b>&rdquo;</p>
    <p style='margin-top:10px'>Asy-Syarwani menukil Ibnu Qasim: <b class='g'>keadaan ragu termasuk &ldquo;tidak batal&rdquo;</b>. Ibnu Hajar dalam Syarh Al-Irsyad juga mencontohkan wanita yang ragu cairannya dari luar atau dalam: wudhunya tetap.</p>
  </div>
</div>""")

# 8 TERUS-MENERUS: Mughni 1/281-282
t_daim = ("(وَالِاسْتِحَاضَةُ) … (حَدَثٌ دَائِمٌ) … ⟦(كَسَلَسٍ) بِفَتْحِ اللَّامِ أَيْ سَلَسِ الْبَوْلِ وَالْمَذْيِ وَالْغَائِطِ وَالرِّيحِ⟧ هُوَ لِلتَّشْبِيهِ لَا لِلتَّمْثِيلِ … "
          "⟦(فَتَغْسِلُ الْمُسْتَحَاضَةُ فَرْجَهَا)⟧ قَبْلَ الْوُضُوءِ أَوْ التَّيَمُّمِ … ⟦(وَ)⟧ بَعْدَ ذَلِكَ ⟦(تَعْصِبُهُ)⟧ … "
          "⟦(وَتَتَوَضَّأُ وَقْتَ الصَّلَاةِ وَتُبَادِرُ بِهَا)⟧")
D.add(D.chrome(9, "Nukilan kitab · 5") + f"""
<div class='wrap' style='top:118px'>
  {K("مغني المحتاج — الخطيب الشربيني", "ج ١ · ص ٢٨١–٢٨٢", t_daim, "app.turath.io/book/11444?page=197")}
  <div class='tr'>
    <div class='lab'>Kalau keputihannya keluar terus</div>
    <p>&ldquo;Istihadhah adalah <b class='g'>hadats yang terus-menerus, seperti beser</b>: beser kencing, madzi, buang air, atau angin &hellip; Maka ia <b class='g'>membasuh farjinya, lalu menyumbat atau membalutnya, berwudhu setelah masuk waktu, dan segera shalat.</b>&rdquo;</p>
    <p style='margin-top:10px'>Hukum ini berlaku bagi setiap orang yang hadatsnya terus-menerus (Mughni 1/169: &ldquo;وَمَنْ دَامَ حَدَثُهُ&rdquo;). Keputihan dari bagian dalam yang keluar tanpa jeda termasuk di sini, jadi caranya sama: <b class='g'>satu wudhu untuk satu shalat fardhu</b>.</p>
  </div>
</div>""")

# 10 PENUTUP
D.add(D.chrome(10, "Penutup", last=True) + f"""
<div class='wrap'>
  <h2>Yang menentukan adalah dari mana keluarnya, bukan banyak sedikitnya.</h2>
  <div class='rule'></div>
  <p class='body'>Luar: suci dan tidak membatalkan. Dalam: membatalkan wudhu, dan najisnya diperselisihkan. Ragu: kembali ke asal, wudhu tetap sah.</p>
  <p class='body'>Punya kasus lain? Tulis di kolom komentar, insya Allah dibahas di postingan berikutnya.</p>
  <div style='margin-top:auto;background:#1E3A2B;color:#F3EBDD;border-radius:22px;padding:30px 36px;display:flex;justify-content:space-between;align-items:center'>
    <div><div style="font-family:'Lora',serif;font-weight:700;font-size:30px">Simpan, lalu kirim ke saudarimu.</div>
    <div style='font-size:22px;color:rgba(243,235,221,.75);margin-top:6px'>Sering malu ditanyakan.</div></div>
    <div style='text-align:right;white-space:nowrap;margin-left:24px'><div style="font-family:'Lora',serif;font-weight:700;font-size:24px;color:#D4A84B">Ukkaasyah Abdurrahman</div>
    <div style='font-size:19px;color:rgba(243,235,221,.65);margin-top:4px'>{HANDLE}</div></div>
  </div>
</div>""")

if __name__ == "__main__":
    render(D, sys.argv[1] if len(sys.argv) > 1 else "out")
