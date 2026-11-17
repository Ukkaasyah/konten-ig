"""Carousel Ma'had Aly: Fenomena Nabi Palsu di Indonesia (AQIDAH).
Pakai: python3 tools/mahad_nabi_palsu_render.py OUT_DIR LOGO_DARK.png LOGO_LIGHT.png
"""
import re, html, asyncio, sys, base64, shutil
from pathlib import Path
from playwright.async_api import async_playwright

ROOT = Path(__file__).resolve().parent.parent
OUT = Path(sys.argv[1]); OUT.mkdir(parents=True, exist_ok=True)
b64 = lambda p: "data:image/png;base64," + base64.b64encode(Path(p).read_bytes()).decode()
LOGO_D, LOGO_L = b64(sys.argv[2]), b64(sys.argv[3])
TOTAL = 11
LABEL = "Kajian Aqidah &middot; Nabi Palsu"

NAVY, GOLD, GOLD2, CREAM = "#2A4B5C", "#B08E4E", "#D4B06A", "#F3EBDD"

CSS = f"""
*{{box-sizing:border-box;margin:0;padding:0}}
body{{width:1080px;height:1350px;font-family:'Inter',sans-serif;-webkit-font-smoothing:antialiased}}
.slide{{width:1080px;height:1350px;position:relative;overflow:hidden}}
.cream{{background:{CREAM};color:#2B2925}}
.cream::before{{content:"";position:absolute;inset:0;background:radial-gradient(circle at 18% 8%,rgba(255,255,255,.6),transparent 55%),radial-gradient(circle at 92% 96%,rgba(176,142,78,.12),transparent 50%)}}
.f1{{position:absolute;inset:34px;border:1.5px solid rgba(176,142,78,.75)}}
.f2{{position:absolute;inset:44px;border:1px solid rgba(176,142,78,.45)}}
.top{{position:absolute;top:74px;left:88px;right:88px;display:flex;justify-content:space-between;align-items:center;font-size:19px;letter-spacing:.2em;font-weight:700;color:{GOLD};text-transform:uppercase}}
.top .no{{letter-spacing:.08em;color:{NAVY};opacity:.55}}
.foot{{position:absolute;bottom:62px;left:88px;right:88px;display:flex;justify-content:space-between;align-items:center}}
.foot img{{height:60px}}
.foot .swipe{{font-size:19px;letter-spacing:.18em;font-weight:700;color:{GOLD}}}
.wrap{{position:absolute;top:132px;left:88px;right:88px;bottom:136px;display:flex;flex-direction:column}}
.wrap > *{{flex-shrink:0}}
h2{{font-family:'Lora',serif;font-weight:700;color:{NAVY};font-size:54px;line-height:1.12;letter-spacing:-.01em}}
h2 i{{color:{GOLD};font-style:italic}}
.rule{{width:84px;height:4px;background:{GOLD};border-radius:2px;margin:24px 0 28px}}
p.body{{font-size:29px;line-height:1.55}}
p.body + p.body{{margin-top:20px}}
b.g{{color:{NAVY}}}
.box{{background:#FFFDF8;border:1.5px solid #E4D7BE;border-radius:20px;padding:28px 34px}}
.hd{{font-family:'Amiri',serif;direction:rtl;text-align:right;color:{NAVY};line-height:1.8}}
.arti{{font-size:24px;line-height:1.5;margin-top:10px}}
.src{{font-size:20px;color:#8B7A5C;margin-top:10px;font-weight:500}}
.note{{background:{NAVY};color:{CREAM};border-radius:20px;padding:26px 32px;font-size:24px;line-height:1.5}}
.note b{{color:{GOLD2}}}
/* kitab */
.kitab{{background:#FFFEFA;border:1.5px solid #E2D5BB;border-radius:14px;box-shadow:0 18px 40px -18px rgba(42,75,92,.4);overflow:hidden}}
.khead{{display:flex;justify-content:space-between;align-items:center;padding:14px 28px;border-bottom:1.5px solid #ECE3D1;background:#FBF7EE}}
.khead .t{{font-family:'Amiri',serif;font-weight:700;font-size:26px;color:{NAVY};direction:rtl}}
.khead .p{{font-family:'Amiri',serif;font-size:23px;color:#7C6E57;direction:rtl}}
.kbody{{font-family:'Amiri',serif;direction:rtl;text-align:justify;font-size:25px;line-height:1.9;color:#262420;padding:18px 30px 20px}}
.kbody b{{font-weight:700;color:#111}}
.kbody mark{{background:linear-gradient(180deg,transparent 12%,rgba(255,214,58,.8) 12%,rgba(255,214,58,.8) 90%,transparent 90%);color:inherit;padding:0 3px;border-radius:3px;-webkit-box-decoration-break:clone;box-decoration-break:clone}}
.kfoot{{display:flex;justify-content:space-between;padding:9px 28px 12px;font-size:16px;color:#A0937B;border-top:1px dashed #ECE3D1}}
.tr{{margin-top:22px}}
.tr .lab{{font-size:18px;letter-spacing:.16em;font-weight:700;color:{GOLD};text-transform:uppercase;margin-bottom:8px}}
.tr p{{font-size:24px;line-height:1.5}}
ol.pola{{list-style:none}}
ol.pola li{{position:relative;padding-left:70px;margin-bottom:24px}}
ol.pola li .n{{position:absolute;left:0;top:2px;width:48px;height:48px;border-radius:50%;background:{NAVY};color:{CREAM};font-family:'Lora',serif;font-weight:700;font-size:24px;display:flex;align-items:center;justify-content:center}}
ol.pola li .h{{font-family:'Lora',serif;font-weight:700;font-size:29px;color:{NAVY};line-height:1.25}}
ol.pola li .d{{font-size:23px;line-height:1.45;margin-top:4px}}
ul.dot{{list-style:none}}
ul.dot li{{position:relative;padding-left:34px;font-size:25px;line-height:1.45;margin-bottom:16px}}
ul.dot li::before{{content:"";position:absolute;left:4px;top:14px;width:12px;height:12px;border-radius:50%;background:{GOLD}}}
/* cover */
.cover{{background:{NAVY};color:{CREAM}}}
.cover .f1{{border-color:rgba(176,142,78,.8)}}
"""


def page(inner, cls="cream"):
    return f"<!doctype html><html><head><meta charset='utf-8'><style>{CSS}</style></head><body><div class='slide {cls}'><div class='f1'></div><div class='f2'></div>{inner}</div></body></html>"


def chrome(n, label=LABEL):
    return (f"<div class='top'><span>{label}</span><span class='no'>{n:02d}/{TOTAL:02d}</span></div>"
            f"<div class='foot'><img src='{LOGO_D}'><span class='swipe'>GESER &rarr;</span></div>")


def kitab_text(s):
    s = html.escape(s)
    s = re.sub(r"\(([^()]*)\)", r"<b>(\1)</b>", s)
    return s.replace("⟦", "<mark>").replace("⟧", "</mark>")


def kitab(title, pg, text, link):
    return (f"<div class='kitab'><div class='khead'><span class='p'>{pg}</span><span class='t'>{title}</span></div>"
            f"<div class='kbody'>{kitab_text(text)}</div>"
            f"<div class='kfoot'><span>{link}</span><span>teks dari Turath &middot; stabilo = bagian yang dinukil</span></div></div>")


def kitab_slide(n, label, title, pg, text, link, tr, note=""):
    nt = f"<div class='note' style='margin-top:auto'>{note}</div>" if note else ""
    return page(chrome(n, label) + f"""
<div class='wrap'>
  {kitab(title, pg, text, link)}
  <div class='tr'><div class='lab'>Terjemah bagian yang distabilo</div><p>{tr}</p></div>
  {nt}
</div>""")


S = []

# 01 SAMPUL
S.append(page(f"""
<div style='position:absolute;top:250px;left:112px;right:112px'>
  <div style='font-size:22px;letter-spacing:.3em;font-weight:700;color:{GOLD2}'>KAJIAN AQIDAH</div>
  <div style="font-family:'Lora',serif;font-weight:700;font-size:118px;line-height:1.02;letter-spacing:-.01em;margin-top:34px">NABI<br>PALSU</div>
  <div style="font-family:'Lora',serif;font-weight:700;font-style:italic;font-size:70px;line-height:1.12;color:{GOLD2};margin-top:14px">Nama Berganti,<br>Polanya Tetap</div>
  <div style='width:120px;height:4px;background:{GOLD};margin:46px 0 40px'></div>
  <div style='font-size:31px;line-height:1.5;color:rgba(243,235,221,.92);max-width:820px'>Pintu kenabian sudah dikunci empat belas abad lalu. Mengapa selalu ada yang mengaku memegang kuncinya?</div>
</div>
<div style='position:absolute;bottom:96px;left:112px;right:112px;display:flex;justify-content:space-between;align-items:flex-end'>
  <img src='{LOGO_L}' style='height:76px'>
  <div style='text-align:right'>
    <div class='hd' style='color:{GOLD2};font-size:50px;line-height:1.5'>وَكُلُّ دَعْوَى النُّبُوَّةِ بَعْدَهُ فَغَيٌّ وَهَوًى</div>
    <div style='font-size:19px;letter-spacing:.2em;font-weight:700;color:rgba(243,235,221,.7);margin-top:6px'>IMAM ATH-THAHAWI</div>
    <div style='font-size:20px;letter-spacing:.2em;font-weight:700;color:{GOLD2};margin-top:18px'>GESER &rarr;</div>
  </div>
</div>""", "cover"))

# 02 PEMBUKA
S.append(page(chrome(2) + """
<div class='wrap'>
  <h2>Ceritanya berulang, <i>hanya pemerannya yang ganti</i></h2>
  <div class='rule'></div>
  <p class='body'>Hampir setiap beberapa tahun ada saja berita serupa di negeri kita. Seseorang mengaku didatangi Jibril, mengaku menerima wahyu, mengaku Imam Mahdi, lalu naik lagi menjadi rasul.</p>
  <p class='body'>Tempatnya berpindah-pindah. Kadang di kampung, kadang di kota, sekarang bahkan lewat grup WhatsApp dan live streaming. Namanya pun berganti.</p>
  <p class='body'>Kita sengaja tidak menyebut nama siapa pun. Nama akan dilupakan orang, tapi <b class='g'>polanya</b> akan datang lagi dengan wajah baru. Pola itulah yang perlu kita kenali.</p>
  <div class='note' style='margin-top:auto'>Yang menarik, Nabi &#xFDFA; sudah mengabarkan fenomena ini empat belas abad sebelum terjadi.</div>
</div>"""))

# 03 DALIL NAQLI
S.append(page(chrome(3) + """
<div class='wrap'>
  <h2>Sudah dikunci, <i>sudah dikabarkan</i></h2>
  <div class='rule'></div>
  <div class='box'>
    <div class='hd' style='font-size:38px'>﴿مَا كَانَ مُحَمَّدٌ أَبَا أَحَدٍ مِنْ رِجَالِكُمْ وَلَٰكِنْ رَسُولَ اللَّهِ وَخَاتَمَ النَّبِيِّينَ﴾</div>
    <p class='arti'>&ldquo;Muhammad itu bukan bapak dari seorang laki-laki pun di antara kalian, tetapi ia adalah Rasulullah dan <b class='g'>penutup para nabi</b>.&rdquo;</p>
    <div class='src'>QS. Al-Ahzab: 40</div>
  </div>
  <div class='box' style='margin-top:22px'>
    <div class='hd' style='font-size:35px'>وَإِنَّهُ سَيَكُونُ فِي أُمَّتِي كَذَّابُونَ ثَلَاثُونَ، كُلُّهُمْ يَزْعُمُ أَنَّهُ نَبِيٌّ، وَأَنَا خَاتَمُ النَّبِيِّينَ، لَا نَبِيَّ بَعْدِي</div>
    <p class='arti'>&ldquo;Akan muncul di tengah umatku tiga puluh pendusta. Semuanya mengaku nabi. Padahal akulah penutup para nabi, <b class='g'>tidak ada nabi sesudahku</b>.&rdquo;</p>
    <div class='src'>HR. Abu Dawud no. 4252 dan At-Tirmidzi no. 2219, dari Tsauban. At-Tirmidzi: hasan shahih.</div>
  </div>
  <p class='body' style='margin-top:24px;font-size:26px'>Jadi setiap kali muncul pengaku nabi baru, sebenarnya ia sedang membuktikan kebenaran sabda Nabi &#xFDFA;, bukan membatalkannya.</p>
</div>"""))

# 04 NUKILAN SALAF: ATH-THAHAWI (via syarah Ibnu Abil 'Izz)
t1 = ("قوله: «⟦وكل دعوى النبوة بعده فغي وهوى⟧».\n"
      "ش: ⟦لما ثبت أنه خاتم النبيين، علم أن من ادعى بعده النبوة فهو كاذب⟧. ولا يقال: فلو جاء المدعي للنبوة بالمعجزات الخارقة والبراهين الصادقة كيف يقال بتكذيبه؟ "
      "لأنا نقول: هذا لا يتصور أن يوجد، وهو من باب فرض المحال؛ لأن الله تعالى لما أخبر أنه خاتم النبيين، ⟦فمن المحال أن يأتي مدع يدعي النبوة ولا يظهر أمارة كذبه في دعواه⟧. "
      "والغي: ضد الرشاد. والهوى: عبارة عن شهوة النفس. أي: ⟦أن تلك الدعوى بسبب هوى النفس، لا عن دليل، فتكون باطلة⟧.\n"
      "قوله: «وهو المبعوث إلى عامة الجن وكافة الورى، بالحق والهدى، وبالنور والضياء». ش: أما كونه مبعوثا إلى عامة الجن، فقال تعالى حكاية عن قول الجن: ﴿يَا قَوْمَنَا أَجِيبُوا دَاعِيَ اللَّهِ﴾ …")
S.append(kitab_slide(4, "Nukilan salaf &middot; Imam Ath-Thahawi", "شرح العقيدة الطحاوية — ابن أبي العز", "ج ١ · ص ١٦٦", t1.replace("\n", " "),
    "app.turath.io/book/10549?page=160",
    "Ath-Thahawi: &ldquo;<b class='g'>Setiap pengakuan kenabian sesudah beliau adalah kesesatan dan hawa nafsu.</b>&rdquo; Pensyarah menjelaskan: &ldquo;Karena sudah pasti beliau penutup para nabi, diketahuilah bahwa siapa pun yang mengaku nabi sesudahnya adalah pendusta &hellip; Mustahil datang seorang pengaku nabi tanpa tampak tanda kedustaannya &hellip; Pengakuan itu lahir dari hawa nafsu, bukan dari dalil, maka ia batil.&rdquo;",
    "Imam Ath-Thahawi (239&ndash;321 H) hidup di masa salaf. Matan akidahnya menjadi pegangan ahlus sunnah lintas madzhab sampai hari ini."))

# 05 NUKILAN SYAFI'IYAH: IBNU KATSIR
t2 = ("والأحاديث في هذا كثيرة، فمن رحمة الله تعالى بالعباد إرسال محمد ﷺ إليهم، ثم من تشرف له ختم الأنبياء والمرسلين به، وإكمال الدين الحنيف له. "
      "وقد أخبر تعالى في كتابه، ورسوله في السنة المتواترة عنه: ⟦أنه لا نبي بعده ليعلموا أن كل من ادعى هذا المقام بعده فهو كذاب أفاك، دجال ضال مضل، ولو تخرق وشعبذ، وأتي بأنواع السحر والطلاسم والنيرجيات⟧، "
      "فكلها محال وضلال عند أولي الألباب، كما أجرى الله ﷾ على يدي الأسود العنسي باليمن، ومسيلمة الكذاب باليمامة، من الأحوال الفاسدة والأقوال الباردة، ما علم كل ذي لب وفهم وحجي أنهما كاذبان ضالان … "
      "⟦وكذلك كل مدع لذلك إلى يوم القيامة⟧ … ⟦يخلق الله معه من الأمور ما يشهد العلماء والمؤمنون بكذب من جاء بها⟧. وهنا من تمام لطف الله تعالى بخلقه، "
      "فإنهم بضرورة الواقع ⟦لا يأمرون بمعروف ولا ينهون عن منكر إلا على سبيل الاتفاق، أو لما لهم فيه من المقاصد⟧ …")
S.append(kitab_slide(5, "Ulama Syafi'iyah &middot; Al-Hafizh Ibnu Katsir", "تفسير القرآن العظيم — ابن كثير", "ج ١١ · ص ١٧٩", t2,
    "app.turath.io/book/1509?page=5075",
    "&ldquo;&hellip; tidak ada nabi sesudah beliau, agar mereka tahu bahwa <b class='g'>siapa pun yang mengaku menempati kedudukan ini sesudah beliau adalah pendusta besar, dajjal, sesat lagi menyesatkan</b>, sekalipun ia mengarang keajaiban, bermain sulap, dan membawa aneka sihir dan jimat &hellip; Begitu pula <b class='g'>setiap pengaku sampai hari kiamat</b> &hellip; Allah tampakkan bersamanya hal-hal yang membuat para ulama dan orang beriman bersaksi atas kedustaannya &hellip; Mereka tidak menyuruh yang ma'ruf dan tidak melarang yang mungkar, kecuali kebetulan atau karena ada kepentingan.&rdquo;",
    "Ibnu Katsir (w. 774 H), ahli tafsir dan hadits madzhab Syafi'i. Kalimat terakhirnya penting: <b>lihat apa yang ia perintahkan dan untuk siapa keuntungannya.</b>"))

# 06 POLA PENGAKUAN
S.append(page(chrome(6) + """
<div class='wrap'>
  <h2>Pola pengakuan: <i>dari mimpi sampai &ldquo;wahyu&rdquo;</i></h2>
  <div class='rule'></div>
  <ol class='pola'>
    <li><span class='n'>1</span><div class='h'>Berawal dari &ldquo;pengalaman batin&rdquo;</div><div class='d'>Mimpi, wangsit, bisikan saat menyepi atau bertapa, merasa didatangi malaikat. Tidak ada saksi, tidak bisa diuji, tapi diceritakan dengan sangat meyakinkan.</div></li>
    <li><span class='n'>2</span><div class='h'>Gelarnya naik bertahap</div><div class='d'>Mula-mula guru spiritual, lalu wali, lalu Imam Mahdi atau Al-Masih, baru kemudian rasul. Gelar dinaikkan ketika pengikut sudah terlanjur terikat.</div></li>
    <li><span class='n'>3</span><div class='h'>Mengutak-atik makna &ldquo;khatam&rdquo;</div><div class='d'>Katanya khatam itu &ldquo;cincin perhiasan&rdquo;, bukan penutup. Atau &ldquo;yang ditutup hanya nabi pembawa syariat&rdquo;. Ayat yang terang dibuat kabur.</div></li>
    <li><span class='n'>4</span><div class='h'>Syariat ikut diubah</div><div class='d'>Syahadat diganti, shalat lima waktu dianggap &ldquo;belum wajib&rdquo; atau cukup shalat batin, ibadah dialihkan ke tempat dan tata cara baru.</div></li>
  </ol>
</div>"""))

# 07 POLA MENJARING PENGIKUT
S.append(page(chrome(7) + """
<div class='wrap'>
  <h2>Pola menjaring <i>dan mengikat pengikut</i></h2>
  <div class='rule'></div>
  <ol class='pola'>
    <li><span class='n'>5</span><div class='h'>Menyasar yang sedang rapuh</div><div class='d'>Orang yang belum belajar agama, sedang terlilit masalah ekonomi atau keluarga, atau sedang mencari ketenangan. Yang dijual: jalan pintas.</div></li>
    <li><span class='n'>6</span><div class='h'>Menjual rasa takut</div><div class='d'>Ramalan bencana dan kiamat di tanggal tertentu, dan hanya kelompoknya yang akan selamat. Ketika ramalan meleset, tanggalnya diundur.</div></li>
    <li><span class='n'>7</span><div class='h'>Tertutup dan eksklusif</div><div class='d'>Pengajian sembunyi-sembunyi, ada baiat, dilarang bertanya ke ustadz lain. Orang di luar kelompok dianggap kafir atau belum suci.</div></li>
    <li><span class='n'>8</span><div class='h'>Harta dan hidup pengikut dikuasai</div><div class='d'>Ada setoran &ldquo;penyucian&rdquo;, pernikahan diatur, ketaatan harus mutlak. Sang pemimpin boleh melanggar aturan yang ia buat sendiri.</div></li>
  </ol>
  <div class='note' style='margin-top:auto'>Ujungnya hampir selalu sama: <b>dunia untuk yang mengaku, ketergantungan untuk yang mengikuti.</b></div>
</div>"""))

# 08 NUKILAN IBNU TAIMIYAH
t3 = ("… إذ قد يظن الرجل في نفسه أو غيره أنه رسول الله غير متعمد للكذب بل خطأ وضلال ⟦مثل كثير ممن يتمثل له الشيطان ويقول: إني ربك ويخاطبه بأشياء وقد يقول له: أحللت لك ما حرمت على غيرك وأنت عبدي ورسولي وأنت أفضل أهل الأرض⟧، "
      "وأمثال هذه الأكاذيب، فإن مثل هذا قد وقع لكثير من الناس فإذا كان مدعي الرسالة لم يكن صادقا فلا بد أن يكون كاذبا عمدا أو ضلالا … "
      "ومعلوم أن مدعي الرسالة إما أن يكون من أفضل الخلق وأكملهم وإما أن يكون من أنقص الخلق وأرذلهم … "
      "⟦وما من أحد ادعى النبوة من الكذابين إلا وقد ظهر عليه من الجهل والكذب والفجور واستحواذ الشياطين عليه ما ظهر لمن له أدنى تمييز⟧.")
S.append(kitab_slide(8, "Nukilan &middot; Syaikhul Islam Ibnu Taimiyah", "شرح العقيدة الأصفهانية — ابن تيمية", "ص ١٣٨", t3,
    "app.turath.io/book/11248?page=134",
    "&ldquo;&hellip; seperti banyak orang yang <b class='g'>didatangi setan yang menjelma</b>, lalu berkata, &lsquo;Aku Rabbmu,&rsquo; dan mengajaknya bicara. Kadang ia berkata, &lsquo;<b class='g'>Aku halalkan untukmu apa yang Aku haramkan atas orang lain. Engkau hamba-Ku dan rasul-Ku. Engkau manusia paling utama di bumi</b>&rsquo; &hellip; Tidak ada satu pun pendusta yang mengaku nabi, kecuali tampak padanya kebodohan, dusta, kefajiran, dan dikuasainya ia oleh setan, yang terlihat oleh siapa saja yang punya sedikit daya pembeda.&rdquo;",
    "Inilah akar pola nomor 1, 4, dan 8. &ldquo;Wahyu&rdquo; itu bisa jadi memang terdengar, tapi sumbernya bukan langit. Isinya pun khas: <b>kamu istimewa, aturan tidak berlaku untukmu.</b>"))

# 09 DALIL AQLI + ANALOGI
S.append(page(chrome(9) + """
<div class='wrap'>
  <h2>Akal sehat pun <i>menolaknya</i></h2>
  <div class='rule'></div>
  <div class='box'>
    <div style='font-size:18px;letter-spacing:.16em;font-weight:700;color:#B08E4E;margin-bottom:6px'>ANALOGI DARI NABI &#xFDFA;</div>
    <div class='hd' style='font-size:31px'>مَثَلِي وَمَثَلُ الْأَنْبِيَاءِ مِنْ قَبْلِي كَمَثَلِ رَجُلٍ بَنَى بَيْتًا فَأَحْسَنَهُ وَأَجْمَلَهُ إِلَّا مَوْضِعَ لَبِنَةٍ مِنْ زَاوِيَةٍ &hellip; فَأَنَا اللَّبِنَةُ، وَأَنَا خَاتَمُ النَّبِيِّينَ</div>
    <p class='arti'>&ldquo;Perumpamaanku dan para nabi sebelumku seperti orang yang membangun rumah. Ia membuatnya bagus dan indah, kecuali satu tempat batu bata di salah satu sudutnya &hellip; <b class='g'>Akulah batu bata itu, dan akulah penutup para nabi.</b>&rdquo;</p>
    <div class='src'>HR. Al-Bukhari no. 3535 dan Muslim no. 2286</div>
  </div>
  <p class='body' style='margin:22px 0 16px;font-size:26px'>Bangunannya sudah utuh. Pengaku nabi baru sebenarnya sedang membongkar tembok yang sudah sempurna untuk menyelipkan dirinya.</p>
  <ul class='dot'>
    <li>Allah menyatakan agama ini sudah sempurna (QS. Al-Ma'idah: 3). Menambah nabi berarti menganggap masih ada yang kurang.</li>
    <li>Kalau pintu kenabian dibuka, siapa saja bisa mengaku. Agama lalu menjadi milik orang yang paling pandai bercerita.</li>
    <li>Nabi &#xFDFA; dikenal jujur 40 tahun sebelum diutus dan tidak meminta upah dakwah. Bandingkan dengan ramalan yang meleset dan setoran yang wajib.</li>
  </ul>
</div>"""))

# 10 BENTENG
S.append(page(chrome(10) + """
<div class='wrap'>
  <h2>Membentengi diri <i>dan keluarga</i></h2>
  <div class='rule'></div>
  <div class='box'>
    <div class='hd' style='font-size:32px'>يَكُونُ فِي آخِرِ الزَّمَانِ دَجَّالُونَ كَذَّابُونَ، يَأْتُونَكُمْ مِنَ الْأَحَادِيثِ بِمَا لَمْ تَسْمَعُوا أَنْتُمْ وَلَا آبَاؤُكُمْ، فَإِيَّاكُمْ وَإِيَّاهُمْ، لَا يُضِلُّونَكُمْ وَلَا يَفْتِنُونَكُمْ</div>
    <p class='arti'>&ldquo;Di akhir zaman akan ada para dajjal pendusta. Mereka membawa kepada kalian cerita yang belum pernah kalian dan bapak-bapak kalian dengar. <b class='g'>Jauhi mereka</b>, jangan sampai mereka menyesatkan dan memfitnah kalian.&rdquo;</p>
    <div class='src'>HR. Muslim dalam Muqaddimah Shahih-nya, dari Abu Hurairah</div>
  </div>
  <ul class='dot' style='margin-top:26px'>
    <li>Pelajari akidah dari dasarnya, terutama makna syahadat <b class='g'>Muhammad Rasulullah</b> dan bahwa beliau penutup para nabi.</li>
    <li>Klaim wahyu, mimpi, atau &ldquo;perintah langit&rdquo; yang baru: <b class='g'>tolak</b>, tidak perlu ditimbang dulu isinya.</li>
    <li>Waspadai kajian yang serba rahasia, melarang bertanya ke ulama lain, atau menarik setoran.</li>
    <li>Kalau ada kerabat yang terlanjur ikut, rangkul, jangan dimaki. Ajak duduk dengan ustadz yang lurus, dan doakan.</li>
  </ul>
  <div class='note' style='margin-top:auto'>Para sahabat di bawah Abu Bakr Ash-Shiddiq bersepakat memerangi para pengaku nabi. Sejak generasi pertama, umat ini <b>tidak pernah berkompromi</b> dalam urusan ini.</div>
</div>"""))

FIT = """() => {
  const w=document.querySelector('.wrap'); if(!w) return null;
  const els=[...w.querySelectorAll('*')];
  const base=els.map(e=>parseFloat(getComputedStyle(e).fontSize));
  const apply=f=>els.forEach((e,k)=>{ if(e.tagName!=='H2' && !e.closest('h2')) e.style.fontSize=(base[k]*f)+'px'; });
  const autos=[...w.children].filter(c=>c.style.marginTop==='auto');
  autos.forEach(c=>c.style.marginTop='24px');
  const bottom=()=>Math.max(...[...w.children].map(c=>c.getBoundingClientRect().bottom));
  const lim=w.getBoundingClientRect().bottom-4; let lo=0.6,hi=1.15;
  for(let t=0;t<16;t++){const m=(lo+hi)/2; apply(m); if(bottom()<=lim) lo=m; else hi=m;}
  apply(lo); autos.forEach(c=>c.style.marginTop='auto'); return lo; }"""


async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page(viewport={"width": 1080, "height": 1350})
        for i, h in enumerate(S, 1):
            await pg.set_content(h, wait_until="load")
            await pg.evaluate("document.fonts.ready")
            await pg.wait_for_timeout(200)
            f = await pg.evaluate(FIT) if i > 1 else None
            await pg.wait_for_timeout(80)
            await pg.screenshot(path=str(OUT / f"{i:02d}.jpg"), type="jpeg", quality=93)
            print(i, f)
        await b.close()
    shutil.copy(ROOT / "mahad/aset/qris-navy.jpg", OUT / f"{TOTAL:02d}.jpg")

asyncio.run(main())
