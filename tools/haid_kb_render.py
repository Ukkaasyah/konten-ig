import sys
sys.path.insert(0, __import__("os").path.dirname(__file__))
from carousel_lib import Deck, render, HANDLE

D = Deck("Fikih Syafi'i · Seri haid", 10)
K = D.kitab

# 1 COVER
D.add(f"""
<div class='frame'></div>
<div style='position:absolute;top:120px;left:110px;right:110px;display:flex;justify-content:space-between'>
  <div><div style='font-size:22px;letter-spacing:.24em;font-weight:700;color:#D4A84B'>FIKIH MADZHAB SYAFI'I · SERI HAID</div>
  <div style='width:70px;height:3px;background:#D4A84B;margin:26px 0 0'></div></div>
</div>
<div style='position:absolute;top:360px;left:110px;right:110px'>
  <div class='ar' style='text-align:left;font-size:60px;color:#D4A84B;line-height:1.25;margin-bottom:24px'>حَيْضٌ أَمْ دَمُ فَسَادٍ؟</div>
  <div style="font-family:'Lora',serif;font-weight:700;font-size:92px;line-height:1.06;letter-spacing:-.01em">Haid Kacau<br>Karena KB,<br>Shalat atau<br>Tidak?</div>
  <div style='font-size:31px;line-height:1.45;color:rgba(243,235,221,.78);margin-top:34px;max-width:820px'>Flek berhari-hari, datang dua kali sebulan, atau cuma sebentar. Begini cara menilainya.</div>
</div>
<div style='position:absolute;bottom:104px;left:110px;right:110px;display:flex;justify-content:space-between;align-items:flex-end'>
  <div><div style="font-family:'Lora',serif;font-weight:700;font-size:30px">Ukkaasyah Abdurrahman</div>
  <div style='font-size:22px;color:rgba(243,235,221,.65);margin-top:6px'>{HANDLE}</div></div>
  <div style='text-align:right'><div style='font-size:19px;color:rgba(243,235,221,.55);margin-bottom:8px'>Rujukan: Tuhfah · Mughni</div><div style='font-size:22px;font-weight:600;color:#D4A84B'>geser &rarr;</div></div>
</div>""", "cover")

# 2 KELUHAN
D.add(D.chrome(2) + """
<div class='wrap'>
  <h2>Keluhan yang paling sering ditanyakan</h2>
  <div class='rule'></div>
  <ul class='dot'>
    <li>&ldquo;Sejak KB suntik, flek keluar hampir tiap hari.&rdquo;</li>
    <li>&ldquo;Baru 10 hari selesai haid, sudah keluar darah lagi.&rdquo;</li>
    <li>&ldquo;Haidnya cuma setengah hari, terus hilang.&rdquo;</li>
    <li>&ldquo;Darahnya tidak berhenti-berhenti, sudah tiga minggu.&rdquo;</li>
  </ul>
  <p class='body' style='margin-top:14px'>Akhirnya ada yang meninggalkan shalat berminggu-minggu. Ada juga yang tetap shalat padahal sebenarnya sedang haid.</p>
  <div class='box' style='margin-top:auto'><div style='font-size:26px;line-height:1.5'>Dua-duanya keliru. Kabar baiknya, cara menilainya tidak serumit yang dibayangkan.</div></div>
</div>""")

# 3 PRINSIP + HADITS
D.add(D.chrome(3) + """
<div class='wrap'>
  <h2>Penyebabnya tidak mengubah cara menilainya</h2>
  <div class='rule'></div>
  <p class='body'>Darah karena KB, karena obat, atau datang sendiri, dinilai dengan cara yang sama. Yang dilihat <b class='g'>kapan keluarnya dan berapa lama</b>, bukan apa pemicunya.</p>
  <div class='box' style='margin-top:26px'>
    <div class='ar' style='font-size:34px;line-height:1.85;color:#1E3A2B'>إِنَّمَا ذَلِكِ عِرْقٌ وَلَيْسَ بِالْحَيْضَةِ، فَإِذَا أَقْبَلَتِ الْحَيْضَةُ فَدَعِي الصَّلَاةَ، وَإِذَا أَدْبَرَتْ فَاغْسِلِي عَنْكِ الدَّمَ وَصَلِّي</div>
    <p style='font-size:25px;line-height:1.5;margin-top:14px'>&ldquo;Itu hanyalah darah urat, bukan haid. Kalau haid datang, tinggalkan shalat. Kalau sudah berlalu, bersihkan darahnya lalu shalatlah.&rdquo;</p>
    <div class='src'>Sabda Nabi &#xFDFA; kepada Fathimah binti Abi Hubaisy &middot; HR. Al-Bukhari no. 228, Muslim no. 333</div>
  </div>
  <p class='body' style='margin-top:26px'>Jadi tidak semua darah itu haid. Ada darah yang tetap mewajibkan shalat.</p>
</div>""")

# 4 MUGHNI: haid karena obat tetap haid
mughni_obat = ("وَلَوْ ارْتَدَّتْ أَوْ سَكِرَتْ ثُمَّ حَاضَتْ أَوْ نَفِسَتْ، ⟦وَلَوْ اسْتَعْجَلَتْ الْحَيْضَ بِدَوَاءٍ أَوْ اسْتَخْرَجَتْ بِهِ جَنِينًا لَمْ تَقْضِ زَمَنَ الْحَيْضِ وَالنِّفَاسِ⟧ "
               "وَفَارَقَتْ الْمَجْنُونَ ⟦بِأَنَّ إسْقَاطَ الصَّلَاةِ عَنْهَا عَزِيمَةٌ؛ لِأَنَّهَا مُكَلَّفَةٌ بِالتَّرْكِ⟧، وَعَنْهُ رُخْصَةٌ، وَالْمُرْتَدُّ وَالسَّكْرَانُ لَيْسَا مِنْ أَهْلِهَا، "
               "وَمَا وَقَعَ فِي الْمَجْمُوعِ مِنْ قَضَاءِ الْحَائِضِ الْمُرْتَدَّةِ زَمَنَ الْجُنُونِ نُسِبَ فِيهِ إلَى السَّهْوِ.")
D.add(D.chrome(4, "Nukilan kitab · 1") + f"""
<div class='wrap' style='top:118px'>
  {K("مغني المحتاج — الخطيب الشربيني", "ج ١ · ص ٣١٣", mughni_obat, "app.turath.io/book/11444?page=229")}
  <div class='tr'>
    <div class='lab'>Terjemah bagian yang ditandai</div>
    <p>&ldquo;&hellip; Walaupun ia <b class='g'>mempercepat datangnya haid dengan obat</b>, atau mengeluarkan janin dengan obat, ia <b class='g'>tidak mengqadha</b> (shalat) di masa haid dan nifas itu &hellip; karena gugurnya shalat darinya adalah &lsquo;azimah, sebab ia memang diperintah untuk meninggalkannya.&rdquo;</p>
    <p style='margin-top:14px'>Artinya: <b class='g'>haid yang dipicu obat tetap dihukumi haid</b>, selama memenuhi syarat-syaratnya.</p>
  </div>
</div>""")

# 5 TUHFAH: tiga patokan
tuhfah_batas = ("⟦أَيْ قَدْرُهُمَا مُتَّصِلًا، وَهُوَ أَرْبَعٌ وَعِشْرُونَ سَاعَةً⟧، وَإِنْ لَمْ تَتَلَفَّقْ إلَّا مِنْ أَرْبَعَةَ عَشَرَ يَوْمًا مَثَلًا بِنَاءً عَلَى قَوْلِ السَّحْبِ الْآتِي آخَرَ الْبَابِ "
                "وَسَيَأْتِي ثَمَّ مَا يُعْلَمُ مِنْهُ أَنَّ الْمُرَادَ بِالِاتِّصَالِ أَنْ يَكُونَ نَحْوَ الْقُطْنَةِ بِحَيْثُ لَوْ أَدْخَلَ تَلَوَّثَ، وَإِنْ لَمْ يَخْرُجْ الدَّمُ إلَى مَا يَجِبُ غَسْلُهُ فِي الِاسْتِنْجَاءِ. "
                "⟦(وَأَكْثَرُهُ) زَمَنًا (خَمْسَةَ عَشَرَ) يَوْمًا (بِلَيَالِيِهَا)⟧، وَإِنْ لَمْ تَتَّصِلْ وَغَالِبُهُ سِتَّةٌ أَوْ سَبْعَةٌ كُلُّ ذَلِكَ بِاسْتِقْرَاءِ الشَّافِعِيِّ ﵁ بَلْ صَحَّ النَّصُّ بِالْأَخِيرِ. "
                "⟦(وَأَقَلُّ) زَمَنِ (طُهْرٍ بَيْنَ) زَمَنَيْ (الْحَيْضَتَيْنِ خَمْسَةَ عَشَرَ يَوْمًا)⟧ بِلَيَالِيِهَا لِأَنَّهُ أَقَلُّ مَا ثَبَتَ وُجُودُهُ")
D.add(D.chrome(5, "Nukilan kitab · 2") + f"""
<div class='wrap' style='top:118px'>
  {K("تحفة المحتاج — ابن حجر الهيتمي", "ج ١ · ص ٣٨٥", tuhfah_batas, "app.turath.io/book/9059?page=386")}
  <div class='tr'>
    <div class='lab'>Tiga patokan dari Tuhfah</div>
    <p>&ldquo;(Minimal haid sehari semalam) yaitu <b class='g'>kadar 24 jam</b> &hellip; <b class='g'>Maksimalnya 15 hari</b> beserta malamnya &hellip; <b class='g'>Minimal masa suci di antara dua haid 15 hari</b> beserta malamnya.&rdquo;</p>
    <p style='margin-top:12px'>Kalau darahnya putus-putus, cukup jumlah seluruh darahnya mencapai 24 jam dalam rentang 15 hari.</p>
  </div>
</div>""")

# 6 TUHFAH: kebiasaan yang menyalahi batas tidak diikuti
tuhfah_adat = ("فَإِنَّ الْمَرْأَةَ قَدْ لَا تَحِيضُ أَصْلًا وَغَالِبُهُ بَقِيَّةُ الشَّهْرِ بَعْدَ غَالِبِ الْحَيْضِ السَّابِقِ ⟦وَلَوْ اطَّرَدَتْ عَادَةُ امْرَأَةٍ أَوْ أَكْثَرُ بِمُخَالَفَةِ شَيْءٍ مِمَّا مَرَّ لَمْ تُتْبَعْ⟧ "
               "لِأَنَّ بَحْثَ الْأَوَّلَيْنِ أَتَمُّ ⟦وَحَمْلَ دَمِهَا عَلَى الْفَسَادِ أَوْلَى مِنْ خَرْقِ الْعَادَةِ الْمُسْتَمِرَّةِ⟧ وَقَدْ يُشْكِلُ عَلَيْهِ خَرْقُهُمْ لَهَا بِرُؤْيَةِ امْرَأَةٍ دَمًا بَعْدَ سِنِّ الْيَأْسِ "
               "حَيْثُ حَكَمُوا عَلَيْهِ بِأَنَّهُ حَيْضٌ وَأَبْطَلُوا بِهِ تَحْدِيدَهُمْ لَهُ بِمَا مَرَّ")
D.add(D.chrome(6, "Nukilan kitab · 3") + f"""
<div class='wrap' style='top:118px'>
  {K("تحفة المحتاج — ابن حجر الهيتمي", "ج ١ · ص ٣٨٦", tuhfah_adat, "app.turath.io/book/9059?page=387")}
  <div class='tr'>
    <div class='lab'>Terjemah bagian yang ditandai</div>
    <p>&ldquo;Kalau kebiasaan seorang wanita, atau lebih, <b class='g'>terus-menerus menyalahi batas-batas tadi, kebiasaan itu tidak diikuti</b> &hellip; Menghukumi darahnya sebagai <b class='g'>darah fasad</b> lebih tepat daripada menabrak kebiasaan umum yang terus berlaku.&rdquo;</p>
    <p style='margin-top:14px'>Jadi kalau &ldquo;haid&rdquo; selama pakai KB selalu cuma setengah hari, itu <b class='g'>bukan haid</b> walaupun terjadi tiap bulan.</p>
  </div>
</div>""")

# 7 KASUS
D.add(D.chrome(7) + """
<div class='wrap'>
  <h2>Coba terapkan ke kasusmu</h2>
  <div class='rule'></div>
  <div class='kh'><div class='who'>Flek setengah hari, lalu berhenti</div><div class='what'>Kalau dalam 15 hari tidak ada darah lain yang menggenapkannya jadi 24 jam: <b class='g'>bukan haid</b>. Shalat yang terlanjur ditinggalkan diqadha.</div></div>
  <div class='kh'><div class='who'>Darah 3 hari, bersih 4 hari, keluar lagi 2 hari</div><div class='what'><b class='g'>Semuanya haid</b>, termasuk 4 hari bersihnya, selama totalnya tidak lewat 15 hari dari awal.</div></div>
  <div class='kh'><div class='who'>Darah 3 hari, bersih 12 hari, keluar lagi 3 hari</div><div class='what'>3 hari terakhir itu <b class='g'>darah fasad</b>, karena masa sucinya belum genap 15 hari. Contoh ini disebut Asy-Syirbini dalam Mughni Al-Muhtaj 1/284.</div></div>
  <div class='kh'><div class='who'>Darah terus lebih dari 15 hari</div><div class='what'>Ini <b class='g'>istihadhah</b>. Hari haidnya ditentukan dari sifat darah atau kebiasaan sebelumnya. Rinciannya panjang, jadi tanyakan dengan catatan yang lengkap.</div></div>
</div>""")

# 8 FLEK (Mughni 1/284) + khilaf
mughni_flek = ("(فَصْلٌ) إذَا (رَأَتْ) الْمَرْأَةُ مِنْ الدِّمَاءِ (لِسِنِّ الْحَيْضِ أَقَلَّهُ) أَيْ الْحَيْضِ فَأَكْثَرَ (وَلَمْ يَعْبُرْ) أَيْ يُجَاوِزْ (أَكْثَرَهُ فَكُلُّهُ حَيْضٌ) سَوَاءٌ أَكَانَ أَسْوَدَ أَمْ لَا، "
               "⟦وَسَوَاءٌ أَكَانَتْ مُبْتَدَأَةً أَمْ مُعْتَادَةً، تَغَيَّرَتْ عَادَتُهَا أَمْ لَا⟧ … "
               "⟦(وَالصُّفْرَةُ وَالْكُدْرَةُ) كُلٌّ مِنْهُمَا (حَيْضٌ فِي الْأَصَحِّ)⟧ وَفِي الرَّوْضَةِ الصَّحِيحُ؛ لِأَنَّهُ الْأَصْلُ فِيمَا تَرَاهُ الْمَرْأَةُ فِي زَمَنِ الْإِمْكَانِ. "
               "⟦وَالثَّانِي: لَا لِأَنَّهُ لَيْسَ عَلَى لَوْنِ الدَّمِ⟧، لِقَوْلِ أُمِّ عَطِيَّةَ كُنَّا لَا نَعُدُّ الصُّفْرَةَ وَالْكُدْرَةَ شَيْئًا.")
D.add(D.chrome(8, "Nukilan kitab · 4 · Khilaf") + f"""
<div class='wrap' style='top:118px'>
  {K("مغني المحتاج — الخطيب الشربيني", "ج ١ · ص ٢٨٤", mughni_flek, "app.turath.io/book/11444?page=200")}
  <div class='tr'>
    <div class='lab'>Bagaimana dengan flek kuning atau coklat?</div>
    <p>&ldquo;&hellip; Semuanya haid, &hellip; <b class='g'>baik kebiasaannya berubah ataupun tidak</b> &hellip; Darah kuning dan keruh <b class='g'>termasuk haid menurut pendapat ashah</b>, karena itulah hukum asal darah yang keluar di masa yang memungkinkan haid. <b class='g'>Pendapat kedua: bukan haid</b>, karena warnanya bukan warna darah, berdasarkan perkataan Ummu &lsquo;Athiyyah.&rdquo;</p>
    <p style='margin-top:12px'>Yang dipegang dalam madzhab adalah pendapat pertama.</p>
  </div>
</div>""")

# 9 KALAU BUKAN HAID
D.add(D.chrome(9) + """
<div class='wrap'>
  <h2>Kalau ternyata bukan haid</h2>
  <div class='rule'></div>
  <ol class='syarat'>
    <li><b class='g'>Tetap shalat dan puasa.</b> Darah ini tidak menggugurkan kewajiban.</li>
    <li><b class='g'>Setiap mau shalat fardhu:</b> bersihkan, pakai pembalut, wudhu setelah masuk waktu, lalu segera shalat. Satu wudhu untuk satu shalat fardhu.</li>
    <li><b class='g'>Hubungan suami istri tetap boleh</b> di hari-hari yang dihukumi suci.</li>
    <li><b class='g'>Catat tanggal, jam mulai dan berhenti, juga warnanya.</b> Tanpa catatan, hukum hampir mustahil dihitung dengan tepat.</li>
  </ol>
  <div class='box' style='margin-top:auto'>
    <div class='ar' style='font-size:30px;line-height:1.7;color:#1E3A2B'>وَيَجُوزُ وَطْءُ الْمُسْتَحَاضَةِ فِي الزَّمَنِ الْمَحْكُومِ عَلَيْهِ بِأَنَّهُ طُهْرٌ، وَلَا كَرَاهَةَ فِي ذَلِكَ وَإِنْ كَانَ الدَّمُ جَارِيًا</div>
    <div class='src'>Mughni Al-Muhtaj 1/284</div>
  </div>
</div>""")

# 10 PENUTUP
D.add(D.chrome(10, "Penutup", last=True) + f"""
<div class='wrap'>
  <h2>Darahnya boleh tidak teratur. Shalatnya jangan.</h2>
  <div class='rule'></div>
  <p class='body'>Yang perlu diingat cukup tiga angka: <b class='g'>24 jam</b> minimal haid, <b class='g'>15 hari</b> maksimal haid, dan <b class='g'>15 hari</b> minimal suci. Selebihnya, catat dan hitung.</p>
  <p class='body'>Punya kasus yang belum terjawab di sini? Tulis di kolom komentar, insya Allah dibahas di postingan berikutnya.</p>
  <div style='margin-top:auto;background:#1E3A2B;color:#F3EBDD;border-radius:22px;padding:30px 36px;display:flex;justify-content:space-between;align-items:center'>
    <div><div style="font-family:'Lora',serif;font-weight:700;font-size:30px">Simpan, lalu kirim ke saudarimu.</div>
    <div style='font-size:22px;color:rgba(243,235,221,.75);margin-top:6px'>Terutama yang sedang memakai KB.</div></div>
    <div style='text-align:right;min-width:250px'><div style="font-family:'Lora',serif;font-weight:700;font-size:24px;color:#D4A84B">Ukkaasyah Abdurrahman</div>
    <div style='font-size:19px;color:rgba(243,235,221,.65);margin-top:4px'>{HANDLE}</div></div>
  </div>
</div>""")

if __name__ == "__main__":
    render(D, sys.argv[1] if len(sys.argv) > 1 else "out")
