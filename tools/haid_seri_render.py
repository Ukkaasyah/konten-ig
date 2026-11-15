import re, html, asyncio, sys
from pathlib import Path
from playwright.async_api import async_playwright

ROOT = Path(__file__).resolve().parent
BASE = (ROOT / "jamak_hujan_render.py").read_text()
CSS = re.search(r'CSS = """(.*?)"""', BASE, re.S).group(1)
CSS += """
.wrap > *{flex-shrink:0}
.cta{margin-top:auto;background:#1E3A2B;color:#F3EBDD;border-radius:22px;padding:34px 38px}
.cta .big{font-family:'Lora',serif;font-weight:700;font-size:40px;line-height:1.15}
.cta .kw{display:inline-block;background:#D4A84B;color:#1E3A2B;font-family:'Lora',serif;font-weight:700;padding:2px 16px;border-radius:10px}
.cta .sub{font-size:24px;line-height:1.45;color:rgba(243,235,221,.8);margin-top:14px}
.tl{display:flex;gap:6px;margin:6px 0 10px}
.tl div{flex:1;height:54px;border-radius:8px;display:flex;align-items:center;justify-content:center;font-size:19px;font-weight:700}
.tl .d{background:#8E2F2F;color:#fff}
.tl .n{background:#FFFDF8;border:1.5px dashed #C9B894;color:#8B7A5C}
.tl .lab{font-size:18px}
"""

OUT = Path(sys.argv[1] if len(sys.argv) > 1 else "/home/claude/build/haid")
HANDLE = "@ukkaasyah.abdurrahman"
TOTAL = 8


def page(inner, cls="cream"):
    return f"<!doctype html><html><head><meta charset='utf-8'><style>{CSS}</style></head><body><div class='slide {cls}'>{inner}</div></body></html>"


def chrome(n, label, last=False):
    sw = "" if last else "<span class='swipe'>geser &rarr;</span>"
    return (f"<div class='top'><span>{label}</span><span class='no'>{n:02d}/{TOTAL:02d}</span></div>"
            f"<div class='foot'><span>{HANDLE}</span>{sw}</div>")


def kitab_text(s):
    s = html.escape(s)
    s = re.sub(r"\(([^()]*)\)", r"<b>(\1)</b>", s)
    return s.replace("⟦", "<mark>").replace("⟧", "</mark>")


def kitab(title, pg, text, link):
    return (f"<div class='kitab'><div class='khead'><span class='p'>{pg}</span><span class='t'>{title}</span></div>"
            f"<div class='kbody'>{kitab_text(text)}</div>"
            f"<div class='kfoot'><span>{link}</span><span>teks dari Turath · bagian bertanda = nukilan</span></div></div>")


def cover(ar, title, sub, refs):
    return page(f"""
<div class='frame'></div>
<div style='position:absolute;top:120px;left:110px;right:110px'>
  <div style='font-size:22px;letter-spacing:.24em;font-weight:700;color:#D4A84B'>FIKIH MADZHAB SYAFI'I · SERI HAID</div>
  <div style='width:70px;height:3px;background:#D4A84B;margin:26px 0 0'></div>
</div>
<div style='position:absolute;top:330px;left:110px;right:110px'>
  <div class='ar' style='text-align:left;direction:rtl;unicode-bidi:plaintext;font-size:64px;color:#D4A84B;line-height:1.25;margin-bottom:26px'>{ar}</div>
  <div style="font-family:'Lora',serif;font-weight:700;font-size:92px;line-height:1.05;letter-spacing:-.015em">{title}</div>
  <div style='font-size:32px;line-height:1.45;color:rgba(243,235,221,.78);margin-top:38px;max-width:800px'>{sub}</div>
</div>
<div style='position:absolute;bottom:104px;left:110px;right:110px;display:flex;justify-content:space-between;align-items:flex-end'>
  <div><div style="font-family:'Lora',serif;font-weight:700;font-size:30px">Ukkaasyah Abdurrahman</div>
  <div style='font-size:22px;color:rgba(243,235,221,.65);margin-top:6px'>{HANDLE}</div></div>
  <div style='text-align:right'><div style='font-size:19px;color:rgba(243,235,221,.55);margin-bottom:8px'>Rujukan: {refs}</div>
  <div style='font-size:22px;font-weight:600;color:#D4A84B'>geser &rarr;</div></div>
</div>""", "cover")


def kitab_slide(n, label, title, pg, text, link, tr):
    return page(chrome(n, label) + f"""
<div class='wrap' style='top:118px'>
  {kitab(title, pg, text, link)}
  <div class='tr'><div class='lab'>Terjemah bagian yang ditandai</div><p>{tr}</p></div>
</div>""")


def closing(lead, items, note=""):
    lis = "".join(f"<li>{i}</li>" for i in items)
    return page(chrome(8, "Ringkasan", last=True) + f"""
<div class='wrap'>
  <h2>{lead}</h2>
  <div class='rule'></div>
  <ol class='syarat'>{lis}</ol>
  {note}
  <div class='cta' style='display:flex;justify-content:space-between;align-items:center'>
    <div><div class='big' style='font-size:34px'>Wallahu a'lam.</div>
    <div class='sub' style='margin-top:6px'>Simpan untuk dibaca lagi saat dibutuhkan.</div></div>
    <div style='text-align:right'><div style="font-family:'Lora',serif;font-weight:700;font-size:24px;color:#D4A84B">Ukkaasyah Abdurrahman</div>
    <div style='font-size:19px;color:rgba(243,235,221,.65);margin-top:4px'>{HANDLE}</div></div>
  </div>
</div>""")


AISYAH_QADHA = """
  <div class='box' style='margin-top:22px'>
    <div class='ar' style='font-size:34px;line-height:1.8;color:#1E3A2B'>كَانَ يُصِيبُنَا ذَلِكَ، فَنُؤْمَرُ بِقَضَاءِ الصَّوْمِ، وَلَا نُؤْمَرُ بِقَضَاءِ الصَّلَاةِ</div>
    <p style='font-size:25px;line-height:1.5;margin-top:12px'>&ldquo;Dahulu kami mengalami haid, lalu kami diperintahkan mengqadha puasa dan tidak diperintahkan mengqadha shalat.&rdquo;</p>
    <div class='src'>Perkataan Aisyah radhiyallahu 'anha &middot; HR. Muslim no. 335</div>
  </div>"""

# ============ CAROUSEL 1: NAQA' ============
c1 = []
L1 = "Fikih Haid · Darah terputus"
c1.append(cover("النَّقَاءُ بَيْنَ الدَّمَيْنِ",
                "Sudah Bersih,<br>Sudah Mandi,<br>Darahnya Keluar<br>Lagi.",
                "Tiga hari kemarin itu sebenarnya suci atau masih haid?",
                "Tuhfah · Nihayah · Mughni"))

c1.append(page(chrome(2, L1) + """
<div class='wrap'>
  <h2>Kasus yang sering ditanyakan</h2>
  <div class='rule'></div>
  <p class='body'>Seorang muslimah haid 5 hari. Hari ke-6 ia cek, kapasnya keluar putih bersih. Ia mandi, shalat, bahkan puasa qadha Ramadhan.</p>
  <p class='body'>Hari ke-9 darah keluar lagi selama 2 hari, lalu berhenti total.</p>
  <div class='tl' style='margin-top:30px'>
    <div class='d'>1</div><div class='d'>2</div><div class='d'>3</div><div class='d'>4</div><div class='d'>5</div>
    <div class='n'>6</div><div class='n'>7</div><div class='n'>8</div>
    <div class='d'>9</div><div class='d'>10</div>
  </div>
  <div style='display:flex;gap:28px;font-size:20px;color:#6B6257'><span>&#9632; <span style='color:#8E2F2F'>darah</span></span><span>&#9633; bersih</span></div>
  <div class='box' style='margin-top:auto'>
    <div style='font-size:27px;line-height:1.5'>Pertanyaannya: hari ke-6 sampai ke-8 itu <b class='g'>suci</b> atau <b class='g'>haid</b>? Puasa qadhanya sah atau tidak?</div>
  </div>
</div>"""))

c1.append(page(chrome(3, L1) + f"""
<div class='wrap'>
  <h2>Dalilnya</h2>
  <div class='rule'></div>
  <div class='box'>
    <div class='ar' style='font-size:36px;line-height:1.8;color:#1E3A2B'>وَيَسْأَلُونَكَ عَنِ الْمَحِيضِ قُلْ هُوَ أَذًى</div>
    <p style='font-size:25px;line-height:1.5;margin-top:10px'>&ldquo;Mereka bertanya kepadamu tentang haid. Katakanlah: itu adalah kotoran.&rdquo;</p>
    <div class='src'>QS. Al-Baqarah: 222</div>
  </div>
  <div class='box' style='margin-top:22px'>
    <div class='ar' style='font-size:34px;line-height:1.8;color:#1E3A2B'>لَا تَعْجَلْنَ حَتَّى تَرَيْنَ الْقَصَّةَ الْبَيْضَاءَ</div>
    <p style='font-size:25px;line-height:1.5;margin-top:10px'>Para wanita mengirim kapas berwarna kekuningan kepada Aisyah. Beliau berkata, &ldquo;Jangan terburu-buru sampai kalian melihat cairan putih.&rdquo;</p>
    <div class='src'>Diriwayatkan Al-Bukhari (mu'allaq) dan Malik dalam Al-Muwaththa'</div>
  </div>
  {AISYAH_QADHA}
</div>"""))

t1 = ("(وَ) الْأَظْهَرُ أَنَّ ⟦(النَّقَاءَ بَيْنَ الدَّمِ) الَّذِي يُمْكِنُ كَوْنُهُ حَيْضًا بِأَنْ لَمْ يَزِدْ النَّقَاءُ مَعَ الدَّمِ عَلَى خَمْسَةَ عَشَرَ وَاحْتَوَشَ بِدَمَيْنِ فِي الْخَمْسَةَ عَشَرَ وَلَمْ يَنْقُصْ مَجْمُوعُ الدَّمِ عَنْ أَقَلِّ الْحَيْضِ⟧ "
      "كَمَا تُفِيدُهُ \" أَلْ \" الْعَهْدِيَّةُ فِي الدَّمِ … ⟦(حَيْضٌ) سَحْبًا لِحُكْمِ الْحَيْضِ عَلَيْهِ؛ لِأَنَّهُ لَمَّا نَقَصَ عَنْ أَقَلِّ الطُّهْرِ أَشْبَهَ الْفَتْرَةَ بَيْنَ دَفَعَاتِ الدَّمِ⟧، "
      "وَالْفَرْقُ بَيْنَهُمَا أَنَّ ⟦النَّقَاءَ شَرْطُهُ أَنْ تَخْرُجَ الْقُطْنَةُ بَيْضَاءَ نَقِيَّةً⟧ وَالْفَتْرَةُ تَخْرُجُ مَعَهَا مُلَوَّثَةً، وَمِنْ ثَمَّ اتَّفَقُوا عَلَى أَنَّهَا حَيْضٌ "
      "⟦وَمَحَلُّ الْخِلَافِ فِي نَحْوِ الصَّلَاةِ وَالصَّوْمِ وَالْوَطْءِ⟧ دُونَ انْقِضَاءِ الْعِدَّةِ فَإِنَّهُ لَا يَحْصُلُ بِهِ إجْمَاعًا")
c1.append(kitab_slide(4, "Nukilan kitab · 1", "تحفة المحتاج — ابن حجر الهيتمي", "ج ١ · ص ٤١٢", t1, "app.turath.io/book/9059?page=413",
    "&ldquo;Menurut pendapat azhar, masa bersih di antara darah yang mungkin menjadi haid, yaitu bersih dan darahnya tidak melebihi <b class='g'>15 hari</b>, diapit dua darah di dalam 15 hari itu, dan jumlah darahnya tidak kurang dari minimal haid, <b class='g'>dihukumi haid</b>, menarik hukum haid kepadanya &hellip; Syarat disebut bersih: kapas keluar <b class='g'>putih bersih</b> &hellip; Khilaf ini berlaku pada urusan shalat, puasa, dan hubungan suami istri.&rdquo;"))

c1.append(page(chrome(5, L1) + """
<div class='wrap'>
  <h2>Jawabannya</h2>
  <div class='rule'></div>
  <p class='body'>Kesepuluh hari itu <b class='g'>haid semuanya</b>, termasuk tiga hari bersih di tengahnya. Syaratnya terpenuhi:</p>
  <ol class='syarat' style='margin-top:22px'>
    <li>Dari darah pertama sampai darah terakhir tidak lewat <b class='g'>15 hari</b>.</li>
    <li>Jumlah darahnya minimal <b class='g'>24 jam</b>.</li>
    <li>Masa bersihnya <b class='g'>diapit dua darah</b>.</li>
    <li>Sebelum haid ini ia sudah <b class='g'>suci minimal 15 hari</b>.</li>
  </ol>
  <div class='box' style='margin-top:auto'>
    <div style='font-size:21px;letter-spacing:.14em;font-weight:700;color:#9A7A33;margin-bottom:12px'>KONSEKUENSINYA</div>
    <ul class='dot'>
      <li>Puasa qadha di hari ke-6 sampai ke-8 <b class='g'>tidak sah, wajib diulang</b>.</li>
      <li>Shalat di hari-hari itu tidak perlu diqadha, karena shalat orang haid memang gugur.</li>
      <li>Ia tidak berdosa. Saat itu ia memang wajib bersikap sebagai orang suci.</li>
    </ul>
  </div>
</div>"""))

t2 = ("وَكَذَا فِي الِانْقِطَاعِ بِأَنْ كَانَتْ لَوْ أَدْخَلَتْ الْقُطْنَةَ خَرَجَتْ بَيْضَاءَ نَقِيَّةً ⟦فَيَلْزَمُهَا حِينَئِذٍ الْتِزَامُ أَحْكَامِ الطُّهْرِ، ثُمَّ إنْ عَادَ قَبْلَ خَمْسَةَ عَشَرَ كَفَّتْ وَإِنْ انْقَطَعَ فَعَلَتْ وَهَكَذَا حَتَّى تَمْضِيَ خَمْسَةَ عَشَرَ⟧ "
      "فَحِينَئِذٍ تُرَدُّ كُلٌّ إلَى مَرَدِّهَا الْآتِي ⟦فَإِنْ لَمْ تُجَاوِزْهَا بَانَ أَنَّ كُلًّا مِنْ الدَّمِ وَالنَّقَاءِ الْمُحْتَوَشِ حَيْضٌ⟧ "
      "وَفِي الشَّهْرِ الثَّانِي وَمَا بَعْدَهُ لَا تَفْعَلُ لِلِانْقِطَاعِ شَيْئًا مِمَّا مَرَّ لِأَنَّ الظَّاهِرَ أَنَّهَا فِيهِ كَالْأَوَّلِ هَذَا مَا صَحَّحَهُ الرَّافِعِيُّ، وَهُوَ وَجِيهٌ ⟦لَكِنَّ الَّذِي صَحَّحَهُ فِي التَّحْقِيقِ وَالرَّوْضَةِ وَهُوَ الْمَنْقُولُ كَمَا فِي الْمَجْمُوعِ أَنَّ الثَّانِيَ وَمَا بَعْدَهُ كَالْأَوَّلِ⟧")
c1.append(kitab_slide(6, "Nukilan kitab · 2", "تحفة المحتاج — ابن حجر الهيتمي", "ج ١ · ص ٤٠٠", t2, "app.turath.io/book/9059?page=401",
    "&ldquo;&hellip; maka saat itu ia <b class='g'>wajib menjalankan hukum orang suci</b>. Lalu jika darah kembali sebelum 15 hari, ia berhenti (shalat dan puasa); jika berhenti lagi, ia kerjakan lagi; begitu seterusnya sampai 15 hari berlalu &hellip; Jika tidak melewati 15 hari, <b class='g'>jelaslah bahwa darah dan masa bersih yang diapitnya semuanya haid</b> &hellip; Yang dishahihkan An-Nawawi dalam At-Tahqiq dan Ar-Raudhah: bulan kedua dan seterusnya sama seperti bulan pertama.&rdquo;"))

c1.append(page(chrome(7, "Khilaf dalam madzhab") + """
<div class='wrap'>
  <h2>Ada dua qaul tentang masa bersih ini</h2>
  <div class='rule'></div>
  <div class='kh'><div class='who'>Qaul as-Sahb (azhar, mu'tamad)</div><div class='what'>Masa bersih di tengah <b class='g'>ikut dihukumi haid</b>, seperti jeda antar semburan darah.</div>
    <div class='q'>سَحْبًا لِحُكْمِ الْحَيْضِ عَلَيْهِ</div><div class='ref'>Tuhfah 1/412 &middot; Nihayah 1/356 &middot; Mughni 1/293</div></div>
  <div class='kh'><div class='who'>Qaul al-Laqth / at-Talfiq</div><div class='what'>Masa bersih itu <b class='g'>suci</b>. Alasannya, kalau darah menunjukkan haid, bersih pun mestinya menunjukkan suci.</div>
    <div class='q'>لِأَنَّ الدَّمَ إذَا دَلَّ عَلَى الْحَيْضِ وَجَبَ أَنْ يَدُلَّ النَّقَاءُ عَلَى الطُّهْرِ</div><div class='ref'>Mughni Al-Muhtaj 1/294</div></div>
  <div class='kh'><div class='who'>Bulan berikutnya</div><div class='what'>Kalau pola terputus ini berulang di bulan kedua, Ar-Rafi'i menshahihkan: saat bersih ia tidak perlu berbuat apa-apa, karena kemungkinan besar sama seperti bulan pertama. An-Nawawi dalam At-Tahqiq dan Ar-Raudhah menshahihkan: tetap seperti bulan pertama. Ibnu Hajar menyebut pendapat pertama <b class='g'>wajih</b> dan pendapat kedua <b class='g'>manqul</b>.</div>
    <div class='ref'>Tuhfah 1/400</div></div>
</div>"""))

c1.append(closing("Ringkasnya",
    ["Masa bersih yang diapit dua darah, selama totalnya tidak lewat 15 hari dan darahnya minimal 24 jam, <b class='g'>dihukumi haid</b> (qaul as-sahb).",
     "Saat darah berhenti dan kapas putih bersih, ia <b class='g'>wajib mandi, shalat, dan puasa</b> seperti orang suci.",
     "Jika darah kembali dalam 15 hari, puasa wajib di masa bersih itu <b class='g'>diqadha</b>. Shalatnya tidak.",
     "Jika totalnya lewat 15 hari, hukumnya istihadhah dan dihitung dengan cara lain sesuai keadaannya."]))

# ============ CAROUSEL 2: < 24 JAM ============
c2 = []
L2 = "Fikih Haid · Kurang sehari"
c2.append(cover("دَمُ الْفَسَادِ",
                "Darah Keluar<br>Setengah Hari,<br>Shalatnya<br>Diqadha?",
                "Tidak semua darah yang keluar di waktu haid itu haid.",
                "Tuhfah · Mughni"))

c2.append(page(chrome(2, L2) + """
<div class='wrap'>
  <h2>Kasusnya</h2>
  <div class='rule'></div>
  <p class='body'>Selesai shalat Subuh, seorang muslimah mendapati darah. Ia mengira haid datang, jadi ia tidak shalat Zhuhur dan Ashar.</p>
  <p class='body'>Menjelang Maghrib darahnya berhenti. Ditunggu sampai lewat 15 hari, darah tidak keluar lagi.</p>
  <div class='box' style='margin-top:30px'>
    <div style='display:flex;justify-content:space-between;align-items:center;font-size:24px'>
      <span>Subuh</span><span style='flex:1;height:14px;margin:0 18px;border-radius:7px;background:linear-gradient(90deg,#8E2F2F,#B35050)'></span><span>Maghrib</span>
    </div>
    <div style='text-align:center;font-size:22px;color:#6B6257;margin-top:10px'>&plusmn; 11 jam, lalu bersih</div>
  </div>
  <div class='box' style='margin-top:auto'>
    <div style='font-size:27px;line-height:1.5'>Apakah itu haid? Zhuhur dan Ashar yang ditinggalkan, <b class='g'>wajib diqadha atau tidak</b>?</div>
  </div>
</div>"""))

c2.append(page(chrome(3, L2) + f"""
<div class='wrap'>
  <h2>Dalilnya</h2>
  <div class='rule'></div>
  <div class='box'>
    <div class='ar' style='font-size:34px;line-height:1.85;color:#1E3A2B'>فَإِذَا أَقْبَلَتِ الْحَيْضَةُ فَدَعِي الصَّلَاةَ، وَإِذَا أَدْبَرَتْ فَاغْسِلِي عَنْكِ الدَّمَ وَصَلِّي</div>
    <p style='font-size:25px;line-height:1.5;margin-top:10px'>&ldquo;Jika haid datang, tinggalkan shalat. Jika telah pergi, bersihkan darahnya lalu shalatlah.&rdquo;</p>
    <div class='src'>HR. Al-Bukhari no. 228 &middot; Muslim no. 333 (lafaz Muslim)</div>
  </div>
  {AISYAH_QADHA}
  <p class='small' style='margin-top:22px'>Batas minimal dan maksimal haid tidak disebut dalam nash. Ulama Syafi'iyyah menetapkannya dengan <b class='g'>istiqra'</b>, yaitu penelitian Imam Asy-Syafi'i terhadap kebiasaan haid para wanita. Riwayat &ldquo;minimal haid tiga hari, maksimal sepuluh&rdquo; dinilai lemah oleh An-Nawawi.</p>
</div>"""))

t3 = ("⟦(وَأَقَلُّهُ) زَمَنًا (يَوْمٌ وَلَيْلَةٌ) أَيْ مِقْدَارُ يَوْمٍ وَلَيْلَةٍ⟧. قَالَ الشَّارِحُ: مُتَّصِلًا … ⟦بَلْ الْمُرَادُ أَنَّهَا إذَا رَأَتْ دِمَاءً يَنْقُصُ كُلٌّ مِنْهَا عَنْ يَوْمٍ وَلَيْلَةٍ إلَّا أَنَّهَا إذَا اجْتَمَعَتْ كَانَتْ مِقْدَارَ يَوْمٍ وَلَيْلَةٍ عَلَى الِاتِّصَالِ كَفَى ذَلِكَ فِي حُصُولِ أَقَلِّ الْحَيْضِ⟧، "
      "وَالْمَسْأَلَةُ الْآتِيَةُ هِيَ قَوْلُهُ وَالنَّقَاءُ بَيْنَ أَقَلِّ الْحَيْضِ حَيْضٌ، ⟦وَهُمَا أَرْبَعَةٌ وَعِشْرُونَ سَاعَةً⟧، وَهَذَا مَا قَالَهُ الشَّافِعِيُّ فِي عَامَّةِ كُتُبِهِ وَنَصَّ فِي مَوْضِعٍ عَلَى أَنَّ أَقَلَّهُ قَدْرُ يَوْمٍ فَقَطْ وَقِيلَ دَفْعَةٌ كَالنِّفَاسِ، وَهُوَ غَرِيبٌ "
      "(وَأَكْثَرُهُ خَمْسَةَ عَشَرَ) يَوْمًا (بِلَيَالِيِهَا) … ⟦لِلِاسْتِقْرَاءِ⟧، وَأَمَّا خَبَرُ «أَقَلُّ الْحَيْضِ ثَلَاثَةُ أَيَّامٍ وَأَكْثَرُهُ عَشَرَةُ أَيَّامٍ» فَضَعِيفٌ كَمَا فِي الْمَجْمُوعِ")
c2.append(kitab_slide(4, "Nukilan kitab · 1", "مغني المحتاج — الخطيب الشربيني", "ج ١ · ص ٢٧٨", t3, "app.turath.io/book/11444?page=194",
    "&ldquo;Minimal haid dari sisi waktu adalah <b class='g'>sehari semalam</b> &hellip; Maksudnya, jika ia melihat beberapa darah yang masing-masing kurang dari sehari semalam, tetapi bila dijumlahkan mencapai sehari semalam, itu <b class='g'>sudah cukup</b> untuk minimal haid &hellip; Yaitu <b class='g'>24 jam</b> &hellip; Maksimalnya 15 hari 15 malam &hellip; berdasarkan <b class='g'>istiqra'</b>.&rdquo;"))

c2.append(page(chrome(5, L2) + """
<div class='wrap'>
  <h2>Jawabannya</h2>
  <div class='rule'></div>
  <p class='body'>Darah 11 jam itu <b class='g'>bukan haid</b>, karena tidak mencapai 24 jam dan tidak ada darah lain dalam 15 hari yang bisa melengkapinya. Ulama menyebutnya <b class='g'>dam fasad</b>, darah rusak.</p>
  <div class='box' style='margin-top:30px'>
    <ul class='dot'>
      <li>Zhuhur dan Ashar yang ditinggalkan <b class='g'>wajib diqadha</b>.</li>
      <li>Kalau saat itu ia sedang puasa wajib lalu membatalkannya, puasanya juga diqadha.</li>
      <li>Ia tidak berdosa meninggalkan shalat saat darah baru keluar. Begitu darah terlihat di masa yang mungkin haid, ia memang wajib bersikap sebagai orang haid.</li>
    </ul>
  </div>
  <div class='box' style='margin-top:auto;padding:24px 32px'><div style='font-size:24px;line-height:1.45'><b class='g'>Beda kasus:</b> kalau dalam 15 hari darah keluar lagi dan jumlah semuanya mencapai 24 jam, semuanya bisa menjadi haid. Lihat lagi bahasan &ldquo;masa bersih di antara dua darah&rdquo;.</div></div>
</div>"""))

t4 = ("فَلَوْ رَأَتْ خَمْسَةً أَسْوَدَ، ثُمَّ أَحْمَرَ حَكَمْنَا عَلَى الْأَحْمَرِ أَيْضًا أَنَّهُ حَيْضٌ ثُمَّ إنْ انْقَطَعَ قَبْلَ خَمْسَةَ عَشَرَ اسْتَمَرَّ الْحُكْمُ وَإِلَّا فَالْحَيْضُ الْأَسْوَدُ فَقَطْ، أَمَّا إذَا بَقِيَ عَلَيْهَا بَقِيَّةُ طُهْرٍ كَأَنْ رَأَتْ ثَلَاثَةً دَمًا، ثُمَّ اثْنَيْ عَشَرَ نَقَاءً، ثُمَّ ثَلَاثَةً دَمًا، ثُمَّ انْقَطَعَ فَالثَّلَاثَةُ الْأَخِيرَةُ دَمُ فَسَادٍ … "
      "⟦وَبِمُجَرَّدِ رُؤْيَةِ الدَّمِ لِزَمَنِ إمْكَانِ الْحَيْضِ يَجِبُ الْتِزَامُ أَحْكَامِهِ، ثُمَّ إنْ انْقَطَعَ قَبْلَ يَوْمٍ وَلَيْلَةٍ بَانَ أَنْ لَا شَيْءَ فَتَقْضِي صَلَاةَ ذَلِكَ الزَّمَنِ⟧ "
      "ــ [حاشية الشرواني] (قَوْلُهُ وَبِمُجَرَّدِ رُؤْيَةِ الدَّمِ) أَيْ مُبْتَدَأَةً كَانَتْ أَوْ مُعْتَادَةً … ⟦(قَوْلُهُ فَتَقْضِي صَلَاةَ ذَلِكَ الزَّمَنِ) وَكَذَا الصَّوْمُ⟧")
c2.append(kitab_slide(6, "Nukilan kitab · 2", "تحفة المحتاج — ابن حجر الهيتمي", "ج ١ · ص ٣٩٩", t4, "app.turath.io/book/9059?page=400",
    "&ldquo;Begitu melihat darah di masa yang mungkin haid, <b class='g'>wajib menjalankan hukum-hukum haid</b>. Kemudian jika darah berhenti sebelum sehari semalam, jelaslah bahwa itu bukan apa-apa, sehingga ia <b class='g'>mengqadha shalat</b> di masa itu.&rdquo; Asy-Syarwani menambahkan: <b class='g'>&ldquo;Demikian pula puasanya.&rdquo;</b>"))

c2.append(page(chrome(7, "Khilaf dalam madzhab") + """
<div class='wrap'>
  <h2>Bagaimana kalau kebiasaannya memang kurang sehari?</h2>
  <div class='rule'></div>
  <div class='kh'><div class='who'>Nash Asy-Syafi'i</div><div class='what'>Di sebagian besar kitabnya: minimal haid <b class='g'>sehari semalam</b>. Di satu tempat beliau menyebut <b class='g'>sehari saja</b>. Ada juga pendapat &ldquo;sekali semburan&rdquo; seperti nifas, tetapi pendapat ini dinilai gharib.</div>
    <div class='q'>وَهَذَا مَا قَالَهُ الشَّافِعِيُّ فِي عَامَّةِ كُتُبِهِ</div><div class='ref'>Mughni Al-Muhtaj 1/278</div></div>
  <div class='kh'><div class='who'>Kalau kebiasaan seorang wanita selalu kurang dari 24 jam?</div><div class='what'>Menurut pendapat <b class='g'>ashah</b>, kebiasaannya tidak diikuti. Alasannya, penelitian ulama terdahulu lebih lengkap, dan kemungkinan ia terkena darah rusak lebih besar daripada kemungkinan menyelisihi kebiasaan umum wanita.</div>
    <div class='q'>لَمْ يُتْبَعْ ذَلِكَ عَلَى الْأَصَحِّ لِأَنَّ بَحْثَ الْأَوَّلِينَ أَتَمُّ</div><div class='ref'>Mughni Al-Muhtaj 1/279</div></div>
</div>"""))

c2.append(closing("Ringkasnya",
    ["Minimal haid <b class='g'>24 jam</b>, boleh terputus-putus asalkan jumlahnya tercapai dalam 15 hari.",
     "Begitu darah keluar di masa yang mungkin haid, ia <b class='g'>langsung bersikap sebagai orang haid</b>.",
     "Jika ternyata kurang dari 24 jam dan tidak ada darah lain dalam 15 hari, itu <b class='g'>dam fasad</b>. Shalat yang ditinggalkan <b class='g'>diqadha</b>, begitu pula puasa wajib yang dibatalkan."]))

# ============ CAROUSEL 3: ISTIHADHAH MUBTADA'AH ============
c3 = []
L3 = "Fikih Haid · Istihadhah"
c3.append(cover("الْمُبْتَدَأَةُ الْمُسْتَحَاضَةُ",
                "Haid Pertama,<br>Darahnya Tidak<br>Berhenti 20 Hari.",
                "Berapa hari haidnya? Di madzhab Syafi'i jawabannya bisa mengejutkan.",
                "Nihayah · Tuhfah · Mughni"))

c3.append(page(chrome(2, L3) + """
<div class='wrap'>
  <h2>Kasusnya</h2>
  <div class='rule'></div>
  <p class='body'>Seorang remaja putri baru pertama kali haid. Darahnya keluar terus sampai 20 hari, warnanya sama dari awal sampai akhir.</p>
  <p class='body'>Ia bingung. Ibunya bilang, &ldquo;Haid itu paling lama 15 hari, sisanya penyakit.&rdquo; Temannya bilang, &ldquo;Ambil saja 7 hari seperti umumnya.&rdquo;</p>
  <div class='box' style='margin-top:auto'>
    <div style='font-size:27px;line-height:1.5'>Jadi, dari 20 hari itu, <b class='g'>berapa hari yang haid?</b> Shalat dan puasa yang ditinggalkan bagaimana?</div>
  </div>
</div>"""))

c3.append(page(chrome(3, L3) + """
<div class='wrap'>
  <h2>Dalilnya</h2>
  <div class='rule'></div>
  <div class='box'>
    <p style='font-size:25px;line-height:1.5;margin-bottom:12px'>Fathimah binti Abi Hubaisy berkata, &ldquo;Wahai Rasulullah, aku wanita yang terus keluar darah dan tidak suci. Apakah aku tinggalkan shalat?&rdquo; Beliau menjawab:</p>
    <div class='ar' style='font-size:34px;line-height:1.85;color:#1E3A2B'>لَا، إِنَّمَا ذَلِكِ عِرْقٌ، وَلَيْسَ بِالْحَيْضَةِ، فَإِذَا أَقْبَلَتِ الْحَيْضَةُ فَدَعِي الصَّلَاةَ، وَإِذَا أَدْبَرَتْ فَاغْسِلِي عَنْكِ الدَّمَ وَصَلِّي</div>
    <p style='font-size:25px;line-height:1.5;margin-top:12px'>&ldquo;Tidak. Itu hanyalah darah dari urat, bukan haid. Jika haid datang, tinggalkan shalat. Jika telah pergi, bersihkan darahnya lalu shalatlah.&rdquo;</p>
    <div class='src'>HR. Al-Bukhari no. 228 &middot; Muslim no. 333 (lafaz Muslim)</div>
  </div>
  <p class='body' style='margin-top:26px;font-size:28px'>Hadits ini menunjukkan: darah yang terus keluar itu <b class='g'>bercampur</b>, sebagian haid dan sebagian istihadhah. Pertanyaannya, bagaimana memisahkannya.</p>
</div>"""))

t5 = ("⟦وَلَهَا سَبْعَةُ أَحْوَالٍ لِأَنَّهَا إمَّا مُمَيِّزَةٌ أَوْ لَا، وَكُلٌّ مِنْهُمَا إمَّا مُبْتَدَأَةٌ أَوْ مُعْتَادَةٌ⟧، وَغَيْرُ الْمُمَيِّزَةِ النَّاسِيَةُ لِعَادَتِهَا وَهِيَ الْمُتَحَيِّرَةُ إمَّا نَاسِيَةٌ لِلْقَدْرِ وَالْوَقْتِ أَوْ لِلْأَوَّلِ دُونَ الثَّانِي أَوْ لِلثَّانِي دُونَ الْأَوَّلِ … "
      "(فَإِنْ) (كَانَتْ) أَيْ مَنْ جَاوَزَ دَمُهَا أَكْثَرَ الْحَيْضِ (مُبْتَدَأَةً) أَيْ أَوَّلَ مَا ابْتَدَأَهَا الدَّمُ (مُمَيِّزَةً) (بِأَنْ تَرَى) فِي بَعْضِ الْأَيَّامِ دَمًا (قَوِيًّا وَ) فِي بَعْضِهَا (ضَعِيفًا) كَالْأَسْوَدِ وَالْأَحْمَرِ … ⟦(فَالضَّعِيفُ) مِنْ ذَلِكَ (اسْتِحَاضَةٌ) وَإِنْ امْتَدَّ زَمَنُهُ. (وَالْقَوِيُّ) مِنْهُ (حَيْضٌ)⟧ بِثَلَاثَةِ شُرُوطٍ: "
      "(إنْ لَمْ يَنْقُصْ) الْقَوِيُّ (عَنْ أَقَلِّهِ) … (وَلَا عَبَرَ) أَيْ جَاوَزَ (أَكْثَرَهُ) … (وَلَا نَقَصَ الضَّعِيفُ عَنْ أَقَلِّ الطُّهْرِ)")
c3.append(kitab_slide(4, "Nukilan kitab · 1", "نهاية المحتاج — شمس الدين الرملي", "ج ١ · ص ٣٤١", t5, "app.turath.io/book/3565?page=339",
    "&ldquo;Wanita mustahadhah punya <b class='g'>tujuh keadaan</b>, karena ia bisa mumayyizah atau tidak, dan masing-masing bisa mubtada'ah (baru pertama haid) atau mu'tadah (sudah punya kebiasaan) &hellip; Jika ia mubtada'ah mumayyizah, yaitu melihat darah kuat dan lemah seperti hitam dan merah, maka <b class='g'>yang lemah istihadhah dan yang kuat haid</b>, dengan tiga syarat &hellip;&rdquo;"))

c3.append(page(chrome(5, L3) + """
<div class='wrap'>
  <h2>Jawabannya</h2>
  <div class='rule'></div>
  <p class='body'>Karena warnanya sama dan ini haid pertamanya, ia termasuk <b class='g'>mubtada'ah ghairu mumayyizah</b>. Menurut pendapat azhar:</p>
  <div class='box' style='margin-top:24px;text-align:center;padding:30px'>
    <div style="font-family:'Lora',serif;font-weight:700;font-size:46px;color:#1E3A2B">Haid 1 hari 1 malam</div>
    <div style='font-size:26px;color:#6B6257;margin-top:6px'>sisanya istihadhah, suci 29 hari</div>
  </div>
  <ul class='dot' style='margin-top:28px'>
    <li>Bulan pertama ia menunggu sampai darah lewat 15 hari. Setelah itu ia mandi, lalu <b class='g'>mengqadha shalat</b> hari ke-2 sampai ke-15. Puasa wajib yang ditinggalkan selama itu diqadha semuanya.</li>
    <li>Kalau darahnya ada yang kuat dan lemah, misalnya 5 hari hitam lalu merah, maka <b class='g'>yang hitam itulah haidnya</b> selama syaratnya terpenuhi.</li>
  </ul>
</div>"""))

t6 = ("⟦(فَالْأَظْهَرُ أَنَّ حَيْضَهَا يَوْمٌ وَلَيْلَةٌ) لِأَنَّ سُقُوطَ الصَّلَاةِ عَنْهَا فِي هَذَا الْقَدْرِ مُتَيَقَّنٌ وَفِيمَا سِوَاهُ مَشْكُوكٌ فِيهِ⟧، فَلَا يُتْرَكُ الْيَقِينُ إلَّا بِمِثْلِهِ أَوْ أَمَارَةٍ ظَاهِرَةٍ مِنْ تَمْيِيزٍ أَوْ عَادَةٍ، "
      "⟦لَكِنَّهَا فِي الدَّوْرِ الْأَوَّلِ تُمْهِلُ حَتَّى يَعْبُرَ الدَّمُ أَكْثَرَهُ فَتَغْتَسِلَ وَتَقْضِيَ عِبَادَةَ مَا زَادَ عَلَى الْيَوْمِ وَاللَّيْلَةِ⟧، وَفِي الدَّوْرِ الثَّانِي تَغْتَسِلُ بِمُجَرَّدِ مُضِيِّ يَوْمٍ وَلَيْلَةٍ عَلَى الْأَظْهَرِ إنْ اسْتَمَرَّ فَقْدُ التَّمْيِيزِ (وَطُهْرَهَا تِسْعٌ وَعِشْرُونَ) لِأَنَّهَا تَتِمَّةُ الدَّوْرِ. "
      "⟦وَالْقَوْلُ الثَّانِي أَنَّهَا تَرُدُّ إلَى غَالِبِ عَادَةِ النِّسَاءِ وَهُوَ سِتٌّ أَوْ سَبْعٌ⟧")
c3.append(kitab_slide(6, "Nukilan kitab · 2", "نهاية المحتاج — شمس الدين الرملي", "ج ١ · ص ٣٤٣", t6, "app.turath.io/book/3565?page=341",
    "&ldquo;Menurut pendapat azhar, <b class='g'>haidnya sehari semalam</b>, karena gugurnya shalat pada kadar itu yakin, sedangkan selebihnya diragukan &hellip; Hanya saja pada putaran pertama ia menunggu sampai darah melewati batas maksimal, lalu <b class='g'>mandi dan mengqadha ibadah</b> yang lebih dari sehari semalam &hellip; Qaul kedua: ia dikembalikan ke kebiasaan umum wanita, yaitu <b class='g'>enam atau tujuh hari</b>.&rdquo;"))

c3.append(page(chrome(7, "Khilaf dalam madzhab") + """
<div class='wrap'>
  <h2>Sehari semalam, atau enam-tujuh hari?</h2>
  <div class='rule'></div>
  <div class='kh'><div class='who'>Qaul azhar</div><div class='what'><b class='g'>Sehari semalam.</b> Yang yakin hanya kadar minimal, selebihnya ragu. Kewajiban shalat tidak gugur karena ragu.</div>
    <div class='q'>فَلَا يُتْرَكُ الْيَقِينُ إلَّا بِمِثْلِهِ</div><div class='ref'>Nihayatul Muhtaj 1/343</div></div>
  <div class='kh'><div class='who'>Qaul kedua</div><div class='what'><b class='g'>Enam atau tujuh hari</b>, mengikuti kebiasaan umum wanita. Dalilnya hadits Hamnah binti Jahsy:</div>
    <div class='q'>تَحَيَّضِي فِي عِلْمِ اللَّهِ سِتَّةَ أَيَّامٍ أَوْ سَبْعَةً</div><div class='ref'>HR. Abu Dawud no. 287 &middot; At-Tirmidzi no. 128, ia berkata: hasan shahih. Sebagian ahli hadits melemahkannya.</div></div>
  <div class='box' style='margin-top:auto;padding:24px 32px'><div style='font-size:24px;line-height:1.45'>Menurut Ar-Rafi'i, sumber khilafnya adalah keraguan Imam Asy-Syafi'i: apakah Hamnah saat itu baru pertama haid atau sudah punya kebiasaan. Qaul azhar memahami Hamnah <b class='g'>sudah punya kebiasaan</b>.<div class='src'>Nihayatul Muhtaj 1/343 &middot; Asy-Syarh Al-Kabir 1/311</div></div></div>
</div>"""))

c3.append(closing("Ringkasnya",
    ["Darah yang lewat <b class='g'>15 hari</b> berarti bercampur haid dan istihadhah.",
     "Jika warnanya berbeda, <b class='g'>yang kuat itulah haid</b> selama memenuhi tiga syaratnya.",
     "Jika ini haid pertama dan warnanya sama, haidnya <b class='g'>sehari semalam</b> menurut qaul azhar, dan suci 29 hari.",
     "Selama istihadhah ia tetap shalat dan puasa. Masih ada enam keadaan lain dengan cara hitung masing-masing."]))

SETS = {"2026-11-haid-1-naqa": c1, "2026-11-haid-2-kurang-sehari": c2, "2026-11-haid-3-istihadhah": c3}

FIT_JS = """() => {
  const w=document.querySelector('.wrap'); if(!w) return 1;
  const els=[...w.querySelectorAll('*')].filter(e=>!e.closest('.khead,.kfoot,.top,.foot'));
  const base=els.map(e=>parseFloat(getComputedStyle(e).fontSize));
  const apply=f=>els.forEach((e,k)=>{ if(e.tagName!=='H2') e.style.fontSize=(base[k]*f)+'px'; });
  const fits=()=>w.scrollHeight<=w.clientHeight+1;
  let lo,hi; if(fits()){lo=1;hi=1.45;} else {lo=0.55;hi=1;}
  for(let t=0;t<16;t++){const m=(lo+hi)/2; apply(m); if(fits()) lo=m; else hi=m;}
  apply(lo); return lo; }"""


async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page(viewport={"width": 1080, "height": 1350}, device_scale_factor=1)
        for name, slides in SETS.items():
            d = OUT / name
            d.mkdir(parents=True, exist_ok=True)
            for i, h in enumerate(slides, 1):
                await pg.set_content(h, wait_until="load")
                await pg.evaluate("document.fonts.ready")
                await pg.wait_for_timeout(150)
                f = 1
                if i > 1:
                    f = await pg.evaluate(FIT_JS)
                    await pg.wait_for_timeout(80)
                await pg.screenshot(path=str(d / f"{i:02d}.jpg"), type="jpeg", quality=93,
                                    clip={"x": 0, "y": 0, "width": 1080, "height": 1350})
                print(name, i, round(f, 3))
        await b.close()

asyncio.run(main())
