"""Slide ajakan Haidku (penutup carousel), 1080x1350.
Pakai: python3 tools/haidku_cta.py OUT.jpg [nomor_slide] [total]
"""
import asyncio, sys
from playwright.async_api import async_playwright

OUT = sys.argv[1] if len(sys.argv) > 1 else "cta.jpg"
NO = int(sys.argv[2]) if len(sys.argv) > 2 else 10
TOT = int(sys.argv[3]) if len(sys.argv) > 3 else 10
HANDLE = "@ukkaasyah.abdurrahman"

check = "<svg viewBox='0 0 24 24' width='22' height='22'><path d='M5 12.5l4.2 4.2L19 7' fill='none' stroke='#5A1A40' stroke-width='3' stroke-linecap='round' stroke-linejoin='round'/></svg>"
feats = ["Kalender haid, hukumnya otomatis", "Pengingat qadha shalat", "11 bab materi &amp; 50 tanya jawab", "Waktu shalat, dzikir, doa harian", "Kirim pertanyaan, insya Allah dijawab"]
times = [("Imsak","04.42"),("Subuh","04.52"),("Terbit","06.09"),("Dhuha","06.35"),("Zhuhur","12.12"),("Ashar","15.34"),("Maghrib","18.10"),("Isya","19.23")]

HTML = f"""<!doctype html><html><head><meta charset='utf-8'><style>
*{{box-sizing:border-box;margin:0;padding:0}}
body{{width:1080px;height:1350px;-webkit-font-smoothing:antialiased}}
.s{{width:1080px;height:1350px;position:relative;overflow:hidden;font-family:'Lora',serif;color:#fff;
  background:radial-gradient(circle at 85% 8%,rgba(255,255,255,.10),transparent 30%),linear-gradient(165deg,#3A1230 0%,#5E1C47 45%,#8C2F60 80%,#A8447A 100%)}}
.moon{{position:absolute;top:-170px;right:-150px;width:620px;height:620px;border-radius:50%;background:rgba(255,255,255,.07)}}
.moon::after{{content:'';position:absolute;top:-60px;left:-120px;width:620px;height:620px;border-radius:50%;background:#4A1739;opacity:.0}}
.top{{position:absolute;top:58px;left:80px;right:80px;display:flex;justify-content:space-between;align-items:center;font-family:'Inter';font-size:20px;letter-spacing:.18em;font-weight:600;color:#F0C46A;text-transform:uppercase}}
.top .no{{color:rgba(255,255,255,.55);letter-spacing:.08em}}
.brand{{position:absolute;top:122px;left:80px;display:flex;align-items:center;gap:20px}}
.logo{{width:78px;height:78px;border-radius:20px;background:linear-gradient(145deg,#D16A93,#9B3466);display:flex;align-items:center;justify-content:center;box-shadow:0 10px 24px -10px rgba(0,0,0,.5)}}
.brand .nm{{font-weight:700;font-size:44px}}
.pill{{position:absolute;top:230px;left:80px;border:2px solid #F0C46A;color:#F0C46A;border-radius:999px;padding:9px 26px;font-size:26px;font-weight:600}}
h1{{position:absolute;top:300px;left:80px;right:80px;font-size:86px;line-height:1.04;font-weight:700;letter-spacing:-.01em}}
h1 i{{color:#F0C46A}}
.sub{{position:absolute;top:592px;left:80px;width:920px;font-size:29px;line-height:1.45;color:rgba(255,255,255,.88)}}
.feats{{position:absolute;top:722px;left:80px;width:600px;list-style:none}}
.feats li{{display:flex;align-items:center;gap:16px;font-size:27px;margin-bottom:18px}}
.feats .c{{width:40px;height:40px;border-radius:50%;background:#F0C46A;display:flex;align-items:center;justify-content:center;flex:none}}
.ask{{position:absolute;top:930px;left:80px;width:510px;border:1.5px solid rgba(240,196,106,.6);border-radius:22px;padding:22px 26px;background:rgba(255,255,255,.06)}}
.ask b{{display:block;color:#F0C46A;font-size:29px;margin-bottom:6px}}
.ask span{{font-size:24px;line-height:1.4;color:rgba(255,255,255,.88)}}
.phone{{position:absolute;top:700px;left:660px;width:380px;height:640px;border-radius:52px;background:#141014;padding:12px;transform:rotate(6deg);box-shadow:0 30px 60px -20px rgba(0,0,0,.6)}}
.scr{{width:100%;height:100%;border-radius:42px;overflow:hidden;background:#FBF3F5;font-family:'Inter';color:#3B1630}}
.hd{{background:linear-gradient(160deg,#B24C7B,#8A2D5C);color:#fff;padding:30px 22px 46px}}
.hd .a{{font-size:13px;opacity:.85}} .hd .n{{font-family:'Lora';font-weight:700;font-size:24px;margin:2px 0 8px}} .hd .d{{font-size:12px;opacity:.85;line-height:1.4}}
.card{{margin:-30px 12px 0;background:#fff;border-radius:18px;padding:14px 14px 12px;box-shadow:0 6px 18px -8px rgba(90,26,64,.35)}}
.card .l{{font-size:12px;color:#7A5A6C}} .card .p{{font-family:'Lora';font-weight:700;font-size:27px;color:#8A2D5C;line-height:1.1}} .card .q{{font-size:12px;color:#7A5A6C;margin-bottom:10px}}
.g{{display:grid;grid-template-columns:repeat(4,1fr);gap:7px}}
.g div{{background:#F8E6EC;border-radius:11px;text-align:center;padding:8px 2px}}
.g div span{{display:block;font-size:10px;color:#8B6B7C}} .g div b{{font-size:15px}}
.g div.on{{background:#9B3466;color:#fff}} .g div.on span{{color:#F6D7E3}}
.mut{{margin:12px 12px 0;background:#fff;border-radius:18px;padding:12px 14px}}
.mut .t{{font-size:12px;font-weight:700;color:#9B3466;margin-bottom:6px}}
.mut .ar{{font-family:'Amiri';direction:rtl;font-size:19px;line-height:1.7;color:#3B1630}}
.cta{{position:absolute;left:80px;right:80px;bottom:76px;background:#fff;border-radius:28px;padding:26px 30px;display:flex;align-items:center;gap:24px;box-shadow:0 24px 50px -20px rgba(0,0,0,.55);color:#5A1A40}}
.cta .ic{{width:76px;height:76px;border-radius:50%;background:linear-gradient(145deg,#D16A93,#9B3466);display:flex;align-items:center;justify-content:center;flex:none}}
.cta .t1{{font-weight:700;font-size:40px;line-height:1.1}}
.cta .t2{{font-family:'Inter';font-size:22px;color:#7A5A6C;margin-top:6px}}
</style></head><body><div class='s'>
<div class='moon'></div>
<div class='top'><span>Bawa ilmunya ke HP</span><span class='no'>{NO:02d}/{TOT:02d}</span></div>
<div class='brand'><div class='logo'><svg viewBox='0 0 40 40' width='44' height='44'><path d='M24 6a14 14 0 1 0 10 23.5A12 12 0 1 1 24 6z' fill='#fff'/><path d='M22 15c0 0-4 4.6-4 7.2a4 4 0 0 0 8 0C26 19.6 22 15 22 15z' fill='#fff' opacity='.85'/></svg></div><div class='nm'>Haidku</div></div>
<div class='pill'>Aplikasi untuk muslimah</div>
<h1>Catat haidmu,<br><i>langsung tahu<br>hukumnya.</i></h1>
<div class='sub'>Haid, istihadhah, atau nifas? Shalat mana yang wajib diqadha? <b>Haidku menghitungnya untukmu.</b></div>
<ul class='feats'>{''.join(f"<li><span class='c'>{check}</span>{f}</li>" for f in feats)}</ul>
<div class='phone'><div class='scr'>
  <div class='hd'><div class='a'>Assalamu'alaikum,</div><div class='n'>Fulanah</div><div class='d'>Ahad, 15 November 2026<br>5 Jumadal Akhirah 1448 H</div></div>
  <div class='card'><div class='l'>Shalat berikutnya</div><div class='p'>Subuh</div><div class='q'>pukul 04.52</div>
   <div class='g'>{''.join(f"<div class='{'on' if n=='Isya' else ''}'><span>{n}</span><b>{t}</b></div>" for n,t in times)}</div></div>
  <div class='mut'><div class='t'>Mutiara salaf hari ini</div><div class='ar'>لَوْ نَفَعَ الْعِلْمُ بِلَا عَمَلٍ لَمَا ذَمَّ اللَّهُ سُبْحَانَهُ أَحْبَارَ أَهْلِ الْكِتَابِ</div></div>
</div></div>
<div class='cta'><div class='ic'><svg viewBox='0 0 24 24' width='38' height='38'><path d='M12 19V5M5.5 11.5L12 5l6.5 6.5' fill='none' stroke='#fff' stroke-width='2.8' stroke-linecap='round' stroke-linejoin='round'/></svg></div>
 <div><div class='t1'>Link-nya ada di bio</div><div class='t2'>Buka profil {HANDLE}, ketuk link, lalu tambahkan ke layar utama HP.</div></div></div>
</div></body></html>"""

async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(); pg = await b.new_page(viewport={"width": 1080, "height": 1350})
        await pg.set_content(HTML); await pg.evaluate("document.fonts.ready"); await pg.wait_for_timeout(200)
        await pg.screenshot(path=OUT, type="jpeg", quality=93); await b.close()
asyncio.run(main())
