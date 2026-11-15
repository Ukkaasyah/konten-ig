import re, html, asyncio, sys
from pathlib import Path
from playwright.async_api import async_playwright

OUT = Path(sys.argv[1] if len(sys.argv) > 1 else "/home/claude/build/out")
OUT.mkdir(parents=True, exist_ok=True)
TOTAL = 10
HANDLE = "@ukkaasyah.abdurrahman"

CSS = """
*{box-sizing:border-box;margin:0;padding:0}
body{width:1080px;height:1350px;font-family:'Inter',sans-serif;-webkit-font-smoothing:antialiased}
.slide{width:1080px;height:1350px;position:relative;overflow:hidden}
.cream{background:#F3EBDD;color:#2A2723}
.cream::before{content:"";position:absolute;inset:0;background:radial-gradient(circle at 20% 10%,rgba(255,255,255,.55),transparent 55%),radial-gradient(circle at 90% 95%,rgba(212,168,75,.10),transparent 50%);pointer-events:none}
.top{position:absolute;top:58px;left:80px;right:80px;display:flex;justify-content:space-between;align-items:center;font-size:20px;letter-spacing:.18em;font-weight:600;color:#9A7A33;text-transform:uppercase}
.top .no{letter-spacing:.08em;color:#1E3A2B;opacity:.55}
.foot{position:absolute;bottom:52px;left:80px;right:80px;display:flex;justify-content:space-between;align-items:center;font-size:21px;color:#1E3A2B;opacity:.75;font-weight:500}
.foot .swipe{font-weight:600;color:#9A7A33;opacity:1}
.wrap{position:absolute;top:130px;left:80px;right:80px;bottom:120px;display:flex;flex-direction:column}
h2{font-family:'Lora',serif;font-weight:700;color:#1E3A2B;font-size:56px;line-height:1.12;letter-spacing:-.01em}
.rule{width:84px;height:4px;background:#D4A84B;border-radius:2px;margin:26px 0 30px}
p.body{font-size:30px;line-height:1.55;color:#2A2723}
p.body + p.body{margin-top:22px}
.ar{font-family:'Amiri',serif;direction:rtl;text-align:right}
.box{background:#FFFDF8;border:1.5px solid #E4D7BE;border-radius:22px;padding:30px 36px}
.small{font-size:22px;color:#6B6257;line-height:1.45}
.src{font-size:21px;color:#8B7A5C;margin-top:12px;font-weight:500}
b.g{color:#1E3A2B}
/* kitab page */
.kitab{background:#FFFEFA;border:1.5px solid #E2D5BB;border-radius:14px;box-shadow:0 18px 40px -18px rgba(30,58,43,.35),0 2px 0 rgba(0,0,0,.03);overflow:hidden}
.khead{display:flex;justify-content:space-between;align-items:center;padding:16px 28px;border-bottom:1.5px solid #ECE3D1;background:#FBF7EE}
.khead .t{font-family:'Amiri',serif;font-weight:700;font-size:26px;color:#1E3A2B;direction:rtl}
.khead .p{font-family:'Amiri',serif;font-size:23px;color:#7C6E57;direction:rtl}
.kbody{font-family:'Amiri',serif;direction:rtl;text-align:justify;font-size:25px;line-height:1.95;color:#262420;padding:20px 30px 22px}
.kbody b{font-weight:700;color:#111}
.kbody mark{background:linear-gradient(180deg,transparent 12%,rgba(255,214,58,.78) 12%,rgba(255,214,58,.78) 90%,transparent 90%);color:inherit;padding:0 3px;border-radius:3px;-webkit-box-decoration-break:clone;box-decoration-break:clone}
.kfoot{display:flex;justify-content:space-between;padding:9px 28px 12px;font-size:17px;color:#A0937B;border-top:1px dashed #ECE3D1}
.tr{margin-top:26px}
.tr .lab{font-size:19px;letter-spacing:.16em;font-weight:700;color:#9A7A33;text-transform:uppercase;margin-bottom:10px}
.tr p{font-size:25px;line-height:1.5;color:#2A2723}
ol.syarat{list-style:none;counter-reset:s}
ol.syarat li{counter-increment:s;position:relative;padding-left:66px;font-size:27px;line-height:1.45;margin-bottom:20px}
ol.syarat li::before{content:counter(s);position:absolute;left:0;top:0;width:44px;height:44px;border-radius:50%;background:#1E3A2B;color:#F3EBDD;font-family:'Lora',serif;font-weight:700;font-size:24px;display:flex;align-items:center;justify-content:center}
ul.dot{list-style:none}
ul.dot li{position:relative;padding-left:34px;font-size:26px;line-height:1.45;margin-bottom:18px}
ul.dot li::before{content:"";position:absolute;left:4px;top:15px;width:12px;height:12px;border-radius:50%;background:#D4A84B}
ul.dot li .ref{display:block;font-size:19px;color:#8B7A5C;margin-top:3px}
.pill{display:inline-block;background:#1E3A2B;color:#F3EBDD;font-size:19px;font-weight:600;letter-spacing:.06em;padding:6px 14px;border-radius:999px;margin-bottom:10px}
.kh{border-left:5px solid #D4A84B;padding:6px 0 6px 24px;margin-bottom:22px}
.kh .who{font-family:'Lora',serif;font-weight:700;font-size:29px;color:#1E3A2B}
.kh .what{font-size:24px;line-height:1.42;margin-top:4px}
.kh .q{font-family:'Amiri',serif;direction:rtl;text-align:right;font-size:27px;color:#1E3A2B;margin-top:6px}
.kh .ref{font-size:18px;color:#8B7A5C;margin-top:2px}
/* cover */
.cover{background:#1E3A2B;color:#F3EBDD}
.cover .frame{position:absolute;inset:44px;border:1.5px solid rgba(212,168,75,.55);border-radius:6px}
.cover .rain{position:absolute;top:0;right:0;width:620px;height:620px;opacity:.22}
"""

def page(inner, cls="cream"):
    return f"<!doctype html><html><head><meta charset='utf-8'><style>{CSS}</style></head><body><div class='slide {cls}'>{inner}</div></body></html>"

def chrome(n, label="Fikih Syafi'i · Jamak karena hujan", last=False):
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

slides = []

# 1 COVER
rain = "".join(f"<line x1='{x}' y1='{y}' x2='{x-26}' y2='{y+70}' stroke='#D4A84B' stroke-width='3' stroke-linecap='round'/>"
               for x, y in [(560,40),(480,120),(600,180),(400,60),(520,260),(330,170),(450,330),(590,380),(250,40),(380,300),(560,520),(470,460),(300,420),(200,250),(150,90),(600,40)])
slides.append(page(f"""
<div class='frame'></div>
<svg class='rain' viewBox='0 0 620 620'>{rain}</svg>
<div style='position:absolute;top:120px;left:110px;right:110px'>
  <div style='font-size:22px;letter-spacing:.24em;font-weight:700;color:#D4A84B'>FIKIH MADZHAB SYAFI'I</div>
  <div style='width:70px;height:3px;background:#D4A84B;margin:26px 0 0'></div>
</div>
<div style='position:absolute;top:360px;left:110px;right:110px'>
  <div class='ar' style='text-align:left;direction:rtl;unicode-bidi:plaintext;font-size:64px;color:#D4A84B;line-height:1.2;margin-bottom:26px'>الْجَمْعُ بِالْمَطَرِ</div>
  <div style="font-family:'Lora',serif;font-weight:700;font-size:100px;line-height:1.04;letter-spacing:-.015em">Hujan Deras,<br>Boleh Langsung<br>Jamak?</div>
  <div style='font-size:32px;line-height:1.45;color:rgba(243,235,221,.78);margin-top:38px;max-width:780px'>Rukhshahnya ada. Tapi syaratnya tidak sesederhana &ldquo;yang penting hujan&rdquo;.</div>
</div>
<div style='position:absolute;bottom:104px;left:110px;right:110px;display:flex;justify-content:space-between;align-items:flex-end'>
  <div><div style="font-family:'Lora',serif;font-weight:700;font-size:30px">Ukkaasyah Abdurrahman</div>
  <div style='font-size:22px;color:rgba(243,235,221,.65);margin-top:6px'>{HANDLE}</div></div>
  <div style='font-size:22px;font-weight:600;color:#D4A84B'>geser &rarr;</div>
</div>
<div style='position:absolute;top:120px;right:110px;font-size:20px;color:rgba(243,235,221,.55);letter-spacing:.08em'>Rujukan: Tuhfah · Nihayah · Mughni</div>
""", "cover"))

# 2 KASUS
slides.append(page(chrome(2) + """
<div class='wrap'>
  <h2>Kejadian yang hampir pasti pernah Antum lihat</h2>
  <div class='rule'></div>
  <p class='body'>Maghrib, hujan deras. Imam salam, lalu langsung iqamah lagi untuk Isya. Sebagian jamaah ikut, sebagian ragu, ada juga yang memilih pulang lalu &ldquo;menjamak&rdquo; di rumah.</p>
  <p class='body'>Di madzhab Syafi'i, jamak karena hujan itu memang ada dan dalilnya shahih. Masalahnya, banyak yang tahu <b class='g'>bolehnya</b>, tapi tidak tahu <b class='g'>batas-batasnya</b>.</p>
  <div class='box' style='margin-top:auto'>
    <div style='font-size:21px;letter-spacing:.14em;font-weight:700;color:#9A7A33;margin-bottom:10px'>DI SLIDE BERIKUTNYA</div>
    <div style='font-size:26px;line-height:1.5'>Dalilnya &middot; nukilan Tuhfah, Mughni &amp; Nihayah &middot; syarat-syaratnya &middot; siapa yang tidak boleh &middot; khilaf Ar-Ramli, Ibnu Hajar &amp; ashhabul hawasyi</div>
  </div>
</div>"""))

# 3 DALIL
slides.append(page(chrome(3) + """
<div class='wrap'>
  <h2>Dalilnya</h2>
  <div class='rule'></div>
  <div class='box'>
    <div class='ar' style='font-size:36px;line-height:1.85;color:#1E3A2B'>عَنِ ابْنِ عَبَّاسٍ رَضِيَ اللَّهُ عَنْهُمَا: أَنَّ النَّبِيَّ ﷺ صَلَّى بِالْمَدِينَةِ سَبْعًا وَثَمَانِيًا: الظُّهْرَ وَالْعَصْرَ، وَالْمَغْرِبَ وَالْعِشَاءَ. فَقَالَ أَيُّوبُ: لَعَلَّهُ فِي لَيْلَةٍ مَطِيرَةٍ؟ قَالَ: عَسَى.</div>
    <p style='font-size:25px;line-height:1.5;margin-top:16px'>Dari Ibnu Abbas, bahwa Nabi &#xFDFA; shalat di Madinah tujuh rakaat dan delapan rakaat secara jamak: Zhuhur dengan Ashar, Maghrib dengan Isya. Ayyub bertanya, &ldquo;Mungkin itu malam yang hujan?&rdquo; Jabir bin Zaid menjawab, &ldquo;Mungkin.&rdquo;</p>
    <div class='src'>HR. Al-Bukhari no. 543 &middot; Muslim no. 705</div>
  </div>
  <div class='box' style='margin-top:24px'>
    <div class='ar' style='font-size:34px;line-height:1.7;color:#1E3A2B'>قَالَ الشَّافِعِيُّ كَمَالِكٍ: أَرَى ذَلِكَ لِعُذْرِ الْمَطَرِ</div>
    <p style='font-size:25px;line-height:1.5;margin-top:10px'>Imam Asy-Syafi'i, sama seperti Imam Malik, berkata: &ldquo;Menurutku, itu karena uzur hujan.&rdquo;</p>
    <div class='src'>Tuhfatul Muhtaj 2/402</div>
  </div>
  <p class='small' style='margin-top:22px'>Ibnu Abbas dan Ibnu Umar juga diriwayatkan pernah menjamak karena hujan (disebut dalam Mughni Al-Muhtaj).</p>
</div>"""))

# 4 TUHFAH PAGE
tuhfah = ("⟦وَلَوْ لِلْمُقِيمِ (الْجَمْعُ) بَيْنَ مَا مَرَّ وَمِنْهُ الْجُمُعَةُ بَدَلُ الظُّهْرِ (بِالْمَطَرِ)، وَإِنْ ضَعُفَ بِشَرْطِ أَنْ يَبُلَّ الثَّوْبَ⟧ "
          "وَمِنْهُ شَفَّانِ وَهُوَ رِيحٌ بَارِدَةٌ فِيهَا مَطَرٌ خَفِيفٌ ⟦(تَقْدِيمًا) بِشُرُوطِهِ السَّابِقَةِ⟧ لِخَبَرِ الصَّحِيحَيْنِ «أَنَّهُ ﷺ صَلَّى بِالْمَدِينَةِ سَبْعًا جَمِيعًا وَثَمَانِيًا جَمِيعًا»، "
          "زَادَ مُسْلِمٌ مِنْ غَيْرِ خَوْفٍ وَلَا سَفَرٍ قَالَ الشَّافِعِيُّ كَمَالِكٍ ﵄ أَرَى ذَلِكَ لِعُذْرِ الْمَطَرِ وَاعْتُرِضَ بِرِوَايَتِهِ أَيْضًا مِنْ غَيْرِ خَوْفٍ وَلَا مَطَرٍ وَأُجِيبَ بِأَنَّهَا شَاذَّةٌ أَوْ وَلَا مَطَرَ كَثِيرٌ فَانْدَفَعَ أَخْذُ أَئِمَّةٍ بِظَاهِرِهَا "
          "⟦(وَالْجَدِيدُ مَنْعُهُ تَأْخِيرًا)⟧؛ لِأَنَّ الْمَطَرَ قَدْ يَنْقَطِعُ فَيُؤَدِّي إلَى إخْرَاجِ الْأُولَى عَنْ وَقْتِهَا بِغَيْرِ عُذْرٍ … "
          "⟦(وَشَرْطُ التَّقْدِيمِ وُجُودُهُ) أَيْ الْمَطَرِ (أَوَّلَهُمَا)⟧ أَيْ الصَّلَاتَيْنِ لِيَتَحَقَّقَ الْجَمْعُ مَعَ الْعُذْرِ ⟦(وَالْأَصَحُّ اشْتِرَاطُهُ عِنْدَ سَلَامِ الْأُولَى)⟧ لِيَتَحَقَّقَ اتِّصَالُ آخِرِ الْأُولَى بِأَوَّلِ الثَّانِيَةِ فِي حَالَةِ الْعُذْرِ")
slides.append(page(chrome(4, "Nukilan kitab · 1") + f"""
<div class='wrap' style='top:118px'>
  {kitab("تحفة المحتاج — ابن حجر الهيتمي", "ج ٢ · ص ٤٠٢", tuhfah, "app.turath.io/book/9059?page=907")}
  <div class='tr'>
    <div class='lab'>Terjemah bagian yang ditandai</div>
    <p>&ldquo;(Boleh) walaupun bagi orang mukim menjamak shalat-shalat tadi, termasuk Jumat sebagai ganti Zhuhur, karena hujan, meskipun ringan, dengan syarat membasahi pakaian &hellip; secara <b class='g'>taqdim</b> dengan syarat-syaratnya yang telah lalu &hellip; Menurut qaul jadid, <b class='g'>tidak boleh ta'khir</b> &hellip; Syarat taqdim: hujan ada di awal kedua shalat, dan menurut pendapat ashah, juga ada <b class='g'>saat salam shalat pertama</b>.&rdquo;</p>
  </div>
</div>"""))

# 5 SYARAT
slides.append(page(chrome(5) + """
<div class='wrap'>
  <h2>Syaratnya, diringkas</h2>
  <div class='rule'></div>
  <ol class='syarat'>
    <li><b class='g'>Hanya jamak taqdim.</b> Ashar ditarik ke waktu Zhuhur, Isya ke waktu Maghrib. Menunda ke waktu kedua (ta'khir) tidak boleh.</li>
    <li><b class='g'>Hujannya membasahi.</b> Cukup membasahi bagian atas pakaian atau bagian bawah sandal. Gerimis yang tidak membasahi tidak dihitung.</li>
    <li><b class='g'>Hujan ada di tiga titik:</b> saat takbiratul ihram shalat pertama, saat salamnya, dan saat masuk shalat kedua. Kalau sempat reda di tengah shalat, tidak masalah.</li>
    <li><b class='g'>Berjamaah</b> di masjid atau tempat jamaah lain yang <b class='g'>jauh</b> dari rumah menurut ukuran kebiasaan.</li>
    <li><b class='g'>Benar-benar terganggu</b> hujan di jalan menuju ke sana.</li>
  </ol>
  <p class='small' style='margin-top:6px'>Syarat jamak taqdim yang biasa tetap berlaku: mulai dari shalat pertama, niat jamak di dalam shalat pertama, dan tidak ada jeda lama di antara keduanya.</p>
  <div class='src'>Tuhfah 2/402&ndash;403 &middot; Mughni 1/534 &middot; Nihayah 2/281 &middot; Hasyiyah Asy-Syarwani</div>
</div>"""))

# 6 MUGHNI PAGE
mughni = ("(وَالْأَظْهَرُ) وَفِي الرَّوْضَةِ الْأَصَحُّ ⟦(تَخْصِيصُ الرُّخْصَةِ بِالْمُصَلِّي جَمَاعَةً) بِمُصَلًّى (بِمَسْجِدٍ) أَوْ غَيْرِهِ (بَعِيدٍ) عَنْ بَابِ دَارِهِ عُرْفًا بِحَيْثُ، (يَتَأَذَّى بِالْمَطَرِ فِي طَرِيقِهِ)⟧ إلَيْهِ نَظَرًا إلَى الْمَشَقَّةِ وَعَدَمِهَا، "
          "⟦بِخِلَافِ مَنْ يُصَلِّي بِبَيْتِهِ مُنْفَرِدًا أَوْ جَمَاعَةً⟧ أَوْ يَمْشِي إلَى الْمُصَلَّى فِي كِنٍّ أَوْ كَانَ الْمُصَلَّى قَرِيبًا فَلَا يَجْمَعُ لِانْتِفَاءِ التَّأَذِّي. "
          "وَأَمَّا جَمْعُهُ ﷺ بِالْمَطَرِ مَعَ أَنَّ بُيُوتَ أَزْوَاجِهِ كَانَتْ بِجَنْبِ الْمَسْجِدِ، فَأَجَابُوا عَنْهُ بِأَنَّ بُيُوتَهُنَّ كَانَتْ مُخْتَلِفَةً وَأَكْثَرُهَا كَانَ بَعِيدًا … "
          "⟦وَبِأَنَّ لِلْإِمَامِ أَنْ يَجْمَعَ بِالْمَأْمُومِينَ وَإِنْ لَمْ يَتَأَذَّ بِالْمَطَرِ⟧ كَمَا صَرَّحَ بِهِ ابْنُ أَبِي هُرَيْرَةَ وَغَيْرُهُ")
slides.append(page(chrome(6, "Nukilan kitab · 2") + f"""
<div class='wrap' style='top:118px'>
  {kitab("مغني المحتاج — الخطيب الشربيني", "ج ١ · ص ٥٣٤", mughni, "app.turath.io/book/11444?page=450")}
  <div class='tr'>
    <div class='lab'>Terjemah bagian yang ditandai</div>
    <p>&ldquo;Menurut pendapat azhar, rukhshah ini <b class='g'>khusus bagi yang shalat berjamaah</b> di masjid atau tempat lain yang <b class='g'>jauh</b> dari pintu rumahnya menurut ukuran kebiasaan, sehingga ia <b class='g'>terganggu hujan</b> di perjalanannya &hellip; Berbeda dengan orang yang shalat di rumahnya, sendirian maupun berjamaah &hellip; Dan imam boleh menjamak bersama makmum walaupun ia sendiri tidak terganggu hujan.&rdquo;</p>
  </div>
</div>"""))

# 7 FAQ
slides.append(page(chrome(7) + """
<div class='wrap'>
  <h2>Yang sering ditanyakan</h2>
  <div class='rule'></div>
  <ul class='dot'>
    <li><b class='g'>Shalat di rumah, mau dijamak?</b> Tidak boleh, baik sendirian maupun berjamaah dengan keluarga.<span class='ref'>Mughni 1/534 &middot; Tuhfah 2/403</span></li>
    <li><b class='g'>Rumah dekat masjid, atau jalannya beratap?</b> Tidak boleh, karena tidak ada gangguan hujan.<span class='ref'>Mughni 1/534</span></li>
    <li><b class='g'>Imam yang tinggal dekat masjid?</b> Tetap boleh memimpin jamak. Begitu juga orang yang kebetulan sudah di masjid saat hujan turun.<span class='ref'>Mughni 1/534 &middot; Tuhfah 2/404</span></li>
    <li><b class='g'>Jumat dijamak dengan Ashar?</b> Boleh, dengan syarat yang sama.<span class='ref'>Tuhfah 2/402</span></li>
    <li><b class='g'>Becek, angin kencang, gelap?</b> Bukan uzur jamak menurut pendapat masyhur.<span class='ref'>Mughni 1/534</span></li>
    <li><b class='g'>Karena sakit?</b> Masyhurnya tidak boleh. Tapi An-Nawawi menilai pendapat yang membolehkan &ldquo;kuat sekali&rdquo;, dan beliau memilihnya di Ar-Raudhah.<span class='ref'>Mughni 1/534 &middot; Tuhfah 2/404</span></li>
  </ul>
</div>"""))

# 8 NIHAYAH PAGE (khilaf)
nihayah = ("(وَشَرْطُ التَّقْدِيمِ) بَعْدَ مَا تَقَدَّمَ (وُجُودُهُ) أَيْ الْمَطَرِ (أَوَّلَهُمَا) أَيْ الصَّلَاتَيْنِ لِيَتَحَقَّقَ الْجَمْعُ مَعَ الْعُذْرِ (وَالْأَصَحُّ اشْتِرَاطُهُ عِنْدَ سَلَامِ الْأُولَى) لِيَتَحَقَّقَ اتِّصَالُ آخِرِ الْأُولَى بِأَوَّلِ الثَّانِيَةِ فِي حَالَةِ الْعُذْرِ. "
           "وَقَضِيَّتُهُ اشْتِرَاطُ امْتِدَادِهِ بَيْنَهُمَا، وَهُوَ كَذَلِكَ، وَلَا يَضُرُّ انْقِطَاعُهُ فِيمَا عَدَا ذَلِكَ … "
           "⟦وَهَلْ يُشْتَرَطُ تَيَقُّنُهُ لِذَلِكَ أَيْضًا حَتَّى لَا يَكْفِيَ الِاسْتِصْحَابُ⟧، صَرَّحَ الْقَاضِي بِالِاشْتِرَاطِ فَقَالَ: ⟦لَوْ قَالَ لِآخَرَ بَعْدَ سَلَامِهِ اُنْظُرْ هَلْ انْقَطَعَ الْمَطَرُ أَوْ لَا بَطَلَ جَمْعُهُ لِلشَّكِّ فِي سَبَبِهِ⟧ … "
           "وَمَالَ الْإِسْنَوِيُّ إلَى الِاكْتِفَاءِ بِالِاسْتِصْحَابِ، وَادَّعَى غَيْرُهُ أَنَّهُ الْقِيَاسُ، ⟦وَالْأَوْجَهُ الْأَوَّلُ، وَيُؤَيِّدُهُ أَنَّهُ رُخْصَةٌ فَلَا بُدَّ مِنْ تَحَقُّقِ سَبَبِهَا⟧")
slides.append(page(chrome(8, "Nukilan kitab · 3") + f"""
<div class='wrap' style='top:118px'>
  {kitab("نهاية المحتاج — شمس الدين الرملي", "ج ٢ · ص ٢٨١", nihayah, "app.turath.io/book/3565?page=831")}
  <div class='tr'>
    <div class='lab'>Terjemah bagian yang ditandai</div>
    <p>&ldquo;Apakah juga disyaratkan <b class='g'>yakin</b> hujan masih ada, sehingga tidak cukup istishab? &hellip; Jika setelah salam ia berkata kepada orang lain, &lsquo;Coba lihat, hujannya sudah berhenti belum?&rsquo;, <b class='g'>batal jamaknya</b> karena ragu pada sebabnya &hellip; Pendapat yang lebih kuat adalah yang pertama, dan dikuatkan bahwa ini rukhshah, sehingga sebabnya harus nyata.&rdquo;</p>
  </div>
</div>"""))

# 9 KHILAF
slides.append(page(chrome(9, "Khilaf mutaakhkhirin") + """
<div class='wrap'>
  <h2>Kalau ragu hujannya masih turun saat salam?</h2>
  <div class='rule'></div>
  <div class='kh'><div class='who'>Ar-Ramli</div><div class='what'>Harus <b class='g'>yakin</b>. Kalau ragu, jamaknya batal.</div>
    <div class='q'>وَالْأَوْجَهُ الْأَوَّلُ … فَلَا بُدَّ مِنْ تَحَقُّقِ سَبَبِهَا</div><div class='ref'>Nihayatul Muhtaj 2/281</div></div>
  <div class='kh'><div class='who'>Ibnu Hajar Al-Haitami</div><div class='what'>Menukil Al-Isnawi bahwa istishab cukup dan &ldquo;itulah qiyasnya&rdquo;, lalu memberi catatan: karena ini rukhshah, sebabnya mesti nyata. Beliau tidak memutus tegas.</div>
    <div class='q'>إلَّا أَنْ يُقَالَ: إنَّهُ رُخْصَةٌ فَلَا بُدَّ مِنْ تَحَقُّقِ سَبَبِهَا</div><div class='ref'>Tuhfatul Muhtaj 2/402&ndash;403</div></div>
  <div class='kh'><div class='who'>Ibnu Qasim Al-Abbadi &amp; Al-Bajuri</div><div class='what'><b class='g'>Dugaan kuat</b> hujan masih ada sudah cukup.</div>
    <div class='q'>وَلَا يَبْعُدُ الِاكْتِفَاءُ بِظَنِّ الْبَقَاءِ &nbsp;·&nbsp; يَقِينًا أَوْ ظَنًّا</div><div class='ref'>Hasyiyah Ibnu Qasim &amp; Hasyiyah Asy-Syarwani &lsquo;ala At-Tuhfah 2/402</div></div>
  <div class='box' style='margin-top:auto;padding:22px 30px'><div style='font-size:24px;line-height:1.45'><b class='g'>Praktisnya:</b> imam sebaiknya memastikan hujan masih jelas turun ketika salam shalat pertama, supaya keluar dari khilaf.</div></div>
</div>"""))

# 10 PENUTUP
slides.append(page(chrome(10, "Penutup", last=True) + f"""
<div class='wrap'>
  <h2>Rukhshah itu hadiah. Ambil sesuai aturannya.</h2>
  <div class='rule'></div>
  <p class='body'>Jangan diingkari kalau syaratnya terpenuhi. Jangan juga dijadikan alasan malas datang ke masjid, karena rukhshah ini justru untuk orang yang berjamaah.</p>
  <div class='box' style='margin-top:30px'>
    <div class='ar' style='font-size:38px;line-height:1.8;color:#1E3A2B'>إِنَّ اللَّهَ يُحِبُّ أَنْ تُؤْتَى رُخَصُهُ كَمَا يَكْرَهُ أَنْ تُؤْتَى مَعْصِيَتُهُ</div>
    <p style='font-size:25px;line-height:1.5;margin-top:12px'>&ldquo;Sesungguhnya Allah suka rukhshah-Nya diambil, sebagaimana Dia benci maksiat kepada-Nya dikerjakan.&rdquo;</p>
    <div class='src'>HR. Ahmad no. 5866, Ibnu Khuzaimah &amp; Ibnu Hibban. Dinilai hasan shahih oleh Al-Albani (Shahih At-Targhib no. 1059)</div>
  </div>
  <div style='margin-top:auto;background:#1E3A2B;color:#F3EBDD;border-radius:22px;padding:30px 36px;display:flex;justify-content:space-between;align-items:center'>
    <div><div style="font-family:'Lora',serif;font-weight:700;font-size:31px">Simpan untuk musim hujan.</div>
    <div style='font-size:22px;color:rgba(243,235,221,.75);margin-top:6px'>Kirim ke imam atau pengurus masjid di kampungmu.</div></div>
    <div style='text-align:right'><div style="font-family:'Lora',serif;font-weight:700;font-size:24px;color:#D4A84B">Ukkaasyah Abdurrahman</div>
    <div style='font-size:19px;color:rgba(243,235,221,.65);margin-top:4px'>{HANDLE}</div></div>
  </div>
</div>"""))

async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page(viewport={"width": 1080, "height": 1350}, device_scale_factor=1)
        for i, h in enumerate(slides, 1):
            await pg.set_content(h, wait_until="load")
            await pg.evaluate("document.fonts.ready")
            await pg.wait_for_timeout(150)
            if i in (4,5,6,7,8):
                await pg.evaluate("""() => {
                  const w=document.querySelector('.wrap'); const els=[...w.querySelectorAll('*')].filter(e=>!e.closest('.khead,.kfoot,.top,.foot'));
                  const base=els.map(e=>parseFloat(getComputedStyle(e).fontSize));
                  const apply=f=>els.forEach((e,k)=>{ if(e.tagName!=='H2') e.style.fontSize=(base[k]*f)+'px'; });
                  const bottom=()=>Math.max(...[...w.children].map(c=>c.getBoundingClientRect().bottom));
                  const lim=w.getBoundingClientRect().bottom-10; let lo=1,hi=1.5;
                  for(let t=0;t<14;t++){const m=(lo+hi)/2; apply(m); if(bottom()<=lim) lo=m; else hi=m;}
                  apply(lo); return lo; }""")
                await pg.wait_for_timeout(100)
            await pg.screenshot(path=str(OUT / f"{i:02d}.jpg"), type="jpeg", quality=93, clip={"x":0,"y":0,"width":1080,"height":1350})
            # overflow check
            ov = await pg.evaluate("""() => { const w=document.querySelector('.wrap'); if(!w) return null;
               const kids=[...w.children]; const r=w.getBoundingClientRect(); let m=0; for(const k of kids){m=Math.max(m,k.getBoundingClientRect().bottom)} return [Math.round(m), Math.round(r.bottom)] }""")
            print(i, ov)
        await b.close()

asyncio.run(main())
