import asyncio, sys
from pathlib import Path
from playwright.async_api import async_playwright
exec(open('tools/base_css_navy.py').read())  # defines CSS (navy, no green)

OUT = Path(sys.argv[1] if len(sys.argv) > 1 else "/home/claude/build/out_riya")
OUT.mkdir(parents=True, exist_ok=True)
TOTAL = 10
HANDLE = "@ukkaasyah.abdurrahman"
NAVY = "#1B2340"
CSS += """
.cover{background:#1B2340}
.hd{font-family:'Amiri',serif;direction:rtl;text-align:right;color:#1B2340;line-height:1.8}
.arti{font-size:25px;line-height:1.5;margin-top:12px}
"""

def page(inner, cls="cream"):
    return f"<!doctype html><html><head><meta charset='utf-8'><style>{CSS}</style></head><body><div class='slide {cls}'>{inner}</div></body></html>"

def chrome(n, label="Tazkiyatun Nufus · Cinta pujian", last=False):
    sw = "" if last else "<span class='swipe'>geser &rarr;</span>"
    return (f"<div class='top'><span>{label}</span><span class='no'>{n:02d}/{TOTAL:02d}</span></div>"
            f"<div class='foot'><span>{HANDLE}</span>{sw}</div>")

S = []

# 1 COVER
dots = "".join(f"<circle cx='{x}' cy='{y}' r='{r}' fill='none' stroke='#D4A84B' stroke-width='2.5'/>"
               for x, y, r in [(470,150,90),(470,150,140),(470,150,190),(470,150,240)])
S.append(page(f"""
<div class='frame'></div>
<svg style='position:absolute;top:0;right:0;width:620px;height:620px;opacity:.16' viewBox='0 0 620 620'>{dots}<circle cx='470' cy='150' r='26' fill='#D4A84B'/></svg>
<div style='position:absolute;top:120px;left:110px;right:110px'>
  <div style='font-size:22px;letter-spacing:.24em;font-weight:700;color:#D4A84B'>TAZKIYATUN NUFUS</div>
  <div style='width:70px;height:3px;background:#D4A84B;margin:26px 0 0'></div>
</div>
<div style='position:absolute;top:380px;left:110px;right:110px'>
  <div class='ar' style='text-align:left;font-size:66px;color:#D4A84B;line-height:1.2;margin-bottom:26px'>حُبُّ الْمَدْحِ</div>
  <div style="font-family:'Young Serif',serif;font-size:104px;line-height:1.04;letter-spacing:-.015em">Diam-Diam<br>Menunggu<br>Dipuji</div>
  <div style='font-size:32px;line-height:1.45;color:rgba(243,235,221,.78);margin-top:38px;max-width:800px'>Penyakit hati yang paling betah tinggal di zaman media sosial.</div>
</div>
<div style='position:absolute;bottom:104px;left:110px;right:110px;display:flex;justify-content:space-between;align-items:flex-end'>
  <div><div style="font-family:'Young Serif',serif;font-size:30px">Ukkaasyah Abdurrahman</div>
  <div style='font-size:22px;color:rgba(243,235,221,.65);margin-top:6px'>{HANDLE}</div></div>
  <div style='font-size:22px;font-weight:600;color:#D4A84B'>geser &rarr;</div>
</div>
""", "cover"))

# 2 PEMBUKA
S.append(page(chrome(2) + """
<div class='wrap'>
  <h2>Habis posting, lalu&hellip;</h2>
  <div class='rule'></div>
  <p class='body'>Selesai upload potongan kajian, foto berbagi nasi, atau rekaman tilawah, jari kita sering refleks membuka aplikasinya lagi. Sudah berapa yang lihat? Ada yang komentar?</p>
  <p class='body'>Kalau sepi, ada kecewa yang susah dijelaskan. Kalau ramai, ada senang yang diam-diam membesar.</p>
  <p class='body'>Ulama menyebut akarnya <span class='ar' style='font-size:36px;color:#1B2340'>حُبُّ الْمَدْحِ وَالثَّنَاءِ</span>, cinta pada pujian. Dari sinilah riya' biasanya masuk.</p>
  <div class='box' style='margin-top:auto'><div style='font-size:25px;line-height:1.5'>Tulisan ini bukan untuk menunjuk orang lain. Ini cermin, dan yang pertama perlu bercermin adalah penulisnya sendiri.</div></div>
</div>"""))

# 3 QURAN + HADITS QUDSI
S.append(page(chrome(3) + """
<div class='wrap'>
  <h2>Allah tidak mau &ldquo;dibagi&rdquo;</h2>
  <div class='rule'></div>
  <div class='box'>
    <div class='hd' style='font-size:38px'>﴿فَمَن كَانَ يَرْجُو لِقَاءَ رَبِّهِ فَلْيَعْمَلْ عَمَلًا صَالِحًا وَلَا يُشْرِكْ بِعِبَادَةِ رَبِّهِ أَحَدًا﴾</div>
    <p class='arti'>&ldquo;Siapa yang berharap bertemu dengan Rabbnya, hendaklah ia beramal shalih dan tidak menyekutukan siapa pun dalam beribadah kepada Rabbnya.&rdquo;</p>
    <div class='src'>QS. Al-Kahfi: 110</div>
  </div>
  <div class='box' style='margin-top:24px'>
    <div class='hd' style='font-size:34px'>قَالَ اللَّهُ تَبَارَكَ وَتَعَالَى: أَنَا أَغْنَى الشُّرَكَاءِ عَنِ الشِّرْكِ، مَنْ عَمِلَ عَمَلًا أَشْرَكَ فِيهِ مَعِي غَيْرِي تَرَكْتُهُ وَشِرْكَهُ</div>
    <p class='arti'>Allah berfirman: &ldquo;Aku paling tidak butuh sekutu. Siapa yang beramal lalu menyertakan selain-Ku di dalamnya, Aku tinggalkan dia bersama sekutunya.&rdquo;</p>
    <div class='src'>HR. Muslim no. 2985</div>
  </div>
</div>"""))

# 4 SUM'AH
S.append(page(chrome(4) + """
<div class='wrap'>
  <h2>Ingin dilihat, ingin didengar</h2>
  <div class='rule'></div>
  <div class='box'>
    <div class='hd' style='font-size:42px;text-align:center'>مَنْ سَمَّعَ سَمَّعَ اللَّهُ بِهِ، وَمَنْ يُرَائِي يُرَائِي اللَّهُ بِهِ</div>
    <p class='arti' style='text-align:center'>&ldquo;Siapa yang memperdengarkan amalnya, Allah akan memperdengarkan (aibnya). Siapa yang memamerkan amalnya, Allah akan memamerkan (niat aslinya).&rdquo;</p>
    <div class='src' style='text-align:center'>HR. Al-Bukhari no. 6499 &middot; Muslim no. 2987</div>
  </div>
  <p class='body' style='margin-top:30px'><b class='g'>Riya'</b> itu beramal supaya dilihat. <b class='g'>Sum'ah</b> itu beramal supaya didengar dan dibicarakan.</p>
  <p class='body'>Dulu bentuknya bercerita di majelis. Sekarang bentuknya bisa sesederhana caption, story, atau &ldquo;tidak sengaja&rdquo; memperlihatkan sajadah dan mushaf di pojok foto.</p>
</div>"""))

# 5 PUJIAN TANPA DIMINTA
S.append(page(chrome(5) + """
<div class='wrap'>
  <h2>Kalau dipuji tanpa diminta?</h2>
  <div class='rule'></div>
  <div class='box'>
    <div class='hd' style='font-size:33px'>قِيلَ لِرَسُولِ اللَّهِ ﷺ: أَرَأَيْتَ الرَّجُلَ يَعْمَلُ الْعَمَلَ مِنَ الْخَيْرِ وَيَحْمَدُهُ النَّاسُ عَلَيْهِ؟ قَالَ: تِلْكَ عَاجِلُ بُشْرَى الْمُؤْمِنِ</div>
    <p class='arti'>Rasulullah &#xFDFA; ditanya tentang orang yang beramal baik lalu dipuji orang. Beliau menjawab: &ldquo;Itu kabar gembira yang disegerakan bagi seorang mukmin.&rdquo;</p>
    <div class='src'>HR. Muslim no. 2642, dari Abu Dzar</div>
  </div>
  <div class='box' style='margin-top:24px'>
    <div class='hd' style='font-size:31px'>هَذَا كُلُّهُ إِذَا حَمِدَهُ النَّاسُ مِنْ غَيْرِ تَعَرُّضٍ مِنْهُ لِحَمْدِهِمْ، وَإِلَّا فَالتَّعَرُّضُ مَذْمُومٌ</div>
    <p class='arti'>An-Nawawi: &ldquo;Semua ini berlaku jika orang memujinya <b class='g'>tanpa ia memancing pujian</b>. Kalau ia memancing, itu tercela.&rdquo;</p>
    <div class='src'>Syarh Shahih Muslim, An-Nawawi, 16/189</div>
  </div>
  <p class='body' style='margin-top:24px'>Bedanya tipis. Dipuji itu nikmat. <b class='g'>Memancing pujian</b> itu penyakit.</p>
</div>"""))

# 6 CERMIN
S.append(page(chrome(6) + """
<div class='wrap'>
  <h2>Cermin kecil di layar HP</h2>
  <div class='rule'></div>
  <p class='body' style='margin-bottom:22px'>Coba jujur pada diri sendiri. Pernahkah:</p>
  <ul class='dot'>
    <li>Amal yang tidak bisa difoto terasa kurang berarti?</li>
    <li>Ibadah lebih bersemangat saat ada yang melihat, lalu kendor saat sendirian?</li>
    <li>Menghapus postingan kebaikan karena responnya sepi?</li>
    <li>Memoles caption supaya terlihat lebih alim dari aslinya?</li>
    <li>Kesal karena bantuan kita tidak disebut-sebut?</li>
    <li>Merasa &ldquo;rugi&rdquo; bersedekah diam-diam karena tidak ada yang tahu?</li>
  </ul>
  <div class='box' style='margin-top:auto'><div style='font-size:25px;line-height:1.5'>Kalau ada yang terasa kena, jangan putus asa. Penyakit yang sudah dikenali itu lebih mudah diobati.</div></div>
</div>"""))

# 7 IBNUL QAYYIM
S.append(page(chrome(7) + """
<div class='wrap'>
  <h2>Air dan api tidak pernah akur</h2>
  <div class='rule'></div>
  <div class='box'>
    <div class='hd' style='font-size:37px'>لَا يَجْتَمِعُ الْإِخْلَاصُ فِي الْقَلْبِ وَمَحَبَّةُ الْمَدْحِ وَالثَّنَاءِ وَالطَّمَعُ فِيمَا عِنْدَ النَّاسِ، إِلَّا كَمَا يَجْتَمِعُ الْمَاءُ وَالنَّارُ، وَالضَّبُّ وَالْحُوتُ</div>
    <p class='arti'>&ldquo;Ikhlas tidak akan berkumpul dalam satu hati bersama cinta pujian dan berharap pada apa yang ada di tangan manusia, kecuali seperti berkumpulnya air dengan api, atau dhabb dengan ikan paus.&rdquo;</p>
    <div class='src'>Ibnul Qayyim, Al-Fawa'id, hlm. 149</div>
  </div>
  <p class='body' style='margin-top:30px'>Dhabb hidup di gurun pasir, paus hidup di laut. Keduanya tidak akan pernah bertemu.</p>
  <p class='body'>Begitu juga hati. Semakin ia haus pujian manusia, semakin sempit ruang untuk ikhlas.</p>
</div>"""))

# 8 OBAT
S.append(page(chrome(8) + """
<div class='wrap'>
  <h2>Obatnya, kata Ibnul Qayyim</h2>
  <div class='rule'></div>
  <div class='box'>
    <div class='hd' style='font-size:33px'>فَإِذَا حَدَّثَتْكَ نَفْسُكَ بِطَلَبِ الْإِخْلَاصِ فَأَقْبِلْ عَلَى الطَّمَعِ أَوَّلًا فَاذْبَحْهُ بِسِكِّينِ الْيَأْسِ، وَأَقْبِلْ عَلَى الْمَدْحِ وَالثَّنَاءِ فَازْهَدْ فِيهِمَا زُهْدَ عُشَّاقِ الدُّنْيَا فِي الْآخِرَةِ</div>
    <p class='arti'>&ldquo;Kalau jiwamu ingin ikhlas, datangi dulu rasa tamak, lalu sembelih dengan pisau putus harapan (dari manusia). Lalu datangi pujian dan sanjungan, dan zuhudlah terhadapnya, sebagaimana pecinta dunia zuhud terhadap akhirat.&rdquo;</p>
    <div class='src'>Al-Fawa'id, hlm. 149</div>
  </div>
  <p class='body' style='margin-top:26px'>Kuncinya, kata beliau, sadar bahwa <b class='g'>tidak ada yang pujiannya benar-benar mengangkat dan celaannya benar-benar menjatuhkan, selain Allah</b>.</p>
  <div class='box' style='margin-top:20px;padding:24px 32px'>
    <div class='hd' style='font-size:30px'>إِنَّ حَمْدِي زَيْنٌ وَإِنَّ ذَمِّي شَيْنٌ، فَقَالَ ﷺ: ذَاكَ اللَّهُ</div>
    <p class='arti' style='font-size:23px'>Seorang badui berkata, &ldquo;Pujianku mengangkat, celaanku menjatuhkan.&rdquo; Nabi &#xFDFA; menjawab, &ldquo;Itu hanya Allah.&rdquo;</p>
    <div class='src'>HR. At-Tirmidzi no. 3267, dishahihkan Al-Albani</div>
  </div>
</div>"""))

# 9 JANGAN BERHENTI
S.append(page(chrome(9) + """
<div class='wrap'>
  <h2>Tapi jangan berhenti beramal</h2>
  <div class='rule'></div>
  <div class='box'>
    <div class='hd' style='font-size:35px'>تَرْكُ الْعَمَلِ مِنْ أَجْلِ النَّاسِ رِيَاءٌ، وَالْعَمَلُ مِنْ أَجْلِ النَّاسِ شِرْكٌ، وَالْإِخْلَاصُ أَنْ يُعَافِيَكَ اللَّهُ مِنْهُمَا</div>
    <p class='arti'>Al-Fudhail bin 'Iyadh: &ldquo;Meninggalkan amal karena manusia itu riya'. Beramal karena manusia itu syirik. Ikhlas adalah ketika Allah menyelamatkanmu dari keduanya.&rdquo;</p>
    <div class='src'>Dinukil Ibnul Qayyim dalam Madarijus Salikin 2/92</div>
  </div>
  <p class='body' style='margin:26px 0 16px'><b class='g'>Yang bisa mulai dilatih:</b></p>
  <ul class='dot'>
    <li>Punya satu amalan rahasia yang tidak pernah diposting.</li>
    <li>Sebelum menekan &ldquo;bagikan&rdquo;, tanya diri: ini untuk siapa?</li>
    <li>Setelah posting, taruh HP. Tidak perlu memantau angka.</li>
    <li>Kalau dipuji, kembalikan kepada Allah dan doakan yang memuji.</li>
  </ul>
</div>"""))

# 10 PENUTUP
S.append(page(chrome(10, "Penutup", last=True) + f"""
<div class='wrap'>
  <h2>Doa yang diajarkan untuk syirik yang samar</h2>
  <div class='rule'></div>
  <div class='box'>
    <div class='hd' style='font-size:40px;text-align:center'>اللَّهُمَّ إِنِّي أَعُوذُ بِكَ أَنْ أُشْرِكَ بِكَ وَأَنَا أَعْلَمُ، وَأَسْتَغْفِرُكَ لِمَا لَا أَعْلَمُ</div>
    <p class='arti' style='text-align:center'>&ldquo;Ya Allah, aku berlindung kepada-Mu dari menyekutukan-Mu sedang aku mengetahuinya, dan aku memohon ampun kepada-Mu atas apa yang tidak aku ketahui.&rdquo;</p>
    <div class='src' style='text-align:center'>HR. Al-Bukhari dalam Al-Adab Al-Mufrad no. 716, dishahihkan Al-Albani</div>
  </div>
  <p class='body' style='margin-top:30px'>Semoga Allah menjaga hati kita dari ingin dilihat, dan dari berhenti beramal karena takut dilihat.</p>
  <div style='margin-top:auto;background:#1B2340;color:#F3EBDD;border-radius:22px;padding:30px 36px;display:flex;justify-content:space-between;align-items:center'>
    <div><div style="font-family:'Young Serif',serif;font-size:31px">Simpan, baca lagi sebelum posting.</div>
    <div style='font-size:22px;color:rgba(243,235,221,.75);margin-top:6px'>Bagikan ke yang sedang sama-sama belajar ikhlas.</div></div>
    <div style='text-align:right;min-width:240px'><div style="font-family:'Young Serif',serif;font-size:24px;color:#D4A84B">Ukkaasyah Abdurrahman</div>
    <div style='font-size:19px;color:rgba(243,235,221,.65);margin-top:4px'>{HANDLE}</div></div>
  </div>
</div>"""))

FIT = """() => {
  const w=document.querySelector('.wrap'); if(!w) return null;
  const els=[...w.querySelectorAll('*')];
  const base=els.map(e=>parseFloat(getComputedStyle(e).fontSize));
  const apply=f=>els.forEach((e,k)=>{ if(e.tagName!=='H2') e.style.fontSize=(base[k]*f)+'px'; });
  const autos=[...w.children].filter(c=>getComputedStyle(c).marginTop==='auto'||c.style.marginTop==='auto');
  autos.forEach(c=>c.style.marginTop='28px');
  const bottom=()=>Math.max(...[...w.children].map(c=>c.getBoundingClientRect().bottom));
  const lim=w.getBoundingClientRect().bottom-8; let lo=0.7,hi=1.4;
  for(let t=0;t<16;t++){const m=(lo+hi)/2; apply(m); if(bottom()<=lim) lo=m; else hi=m;}
  apply(lo); autos.forEach(c=>c.style.marginTop='auto'); return lo; }"""

async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page(viewport={"width": 1080, "height": 1350})
        for i, h in enumerate(S, 1):
            await pg.set_content(h, wait_until="load")
            await pg.evaluate("document.fonts.ready")
            await pg.wait_for_timeout(150)
            f = await pg.evaluate(FIT) if i > 1 else None
            await pg.wait_for_timeout(80)
            await pg.screenshot(path=str(OUT / f"{i:02d}.jpg"), type="jpeg", quality=93)
            print(i, f)
        await b.close()
asyncio.run(main())
