CSS = """
*{box-sizing:border-box;margin:0;padding:0}
body{width:1080px;height:1350px;font-family:'Inter',sans-serif;-webkit-font-smoothing:antialiased}
.slide{width:1080px;height:1350px;position:relative;overflow:hidden}
.cream{background:#F3EBDD;color:#2A2723}
.cream::before{content:"";position:absolute;inset:0;background:radial-gradient(circle at 20% 10%,rgba(255,255,255,.55),transparent 55%),radial-gradient(circle at 90% 95%,rgba(212,168,75,.10),transparent 50%);pointer-events:none}
.top{position:absolute;top:58px;left:80px;right:80px;display:flex;justify-content:space-between;align-items:center;font-size:20px;letter-spacing:.18em;font-weight:600;color:#9A7A33;text-transform:uppercase}
.top .no{letter-spacing:.08em;color:#1B2340;opacity:.55}
.foot{position:absolute;bottom:52px;left:80px;right:80px;display:flex;justify-content:space-between;align-items:center;font-size:21px;color:#1B2340;opacity:.75;font-weight:500}
.foot .swipe{font-weight:600;color:#9A7A33;opacity:1}
.wrap{position:absolute;top:130px;left:80px;right:80px;bottom:120px;display:flex;flex-direction:column}
h2{font-family:'Lora',serif;font-weight:700;color:#1B2340;font-size:56px;line-height:1.12;letter-spacing:-.01em}
.rule{width:84px;height:4px;background:#D4A84B;border-radius:2px;margin:26px 0 30px}
p.body{font-size:30px;line-height:1.55;color:#2A2723}
p.body + p.body{margin-top:22px}
.ar{font-family:'Amiri',serif;direction:rtl;text-align:right}
.box{background:#FFFDF8;border:1.5px solid #E4D7BE;border-radius:22px;padding:30px 36px}
.small{font-size:22px;color:#6B6257;line-height:1.45}
.src{font-size:21px;color:#8B7A5C;margin-top:12px;font-weight:500}
b.g{color:#1B2340}
/* kitab page */
.kitab{background:#FFFEFA;border:1.5px solid #E2D5BB;border-radius:14px;box-shadow:0 18px 40px -18px rgba(27,35,64,.35),0 2px 0 rgba(0,0,0,.03);overflow:hidden}
.khead{display:flex;justify-content:space-between;align-items:center;padding:16px 28px;border-bottom:1.5px solid #ECE3D1;background:#FBF7EE}
.khead .t{font-family:'Amiri',serif;font-weight:700;font-size:26px;color:#1B2340;direction:rtl}
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
ol.syarat li::before{content:counter(s);position:absolute;left:0;top:0;width:44px;height:44px;border-radius:50%;background:#1B2340;color:#F3EBDD;font-family:'Lora',serif;font-weight:700;font-size:24px;display:flex;align-items:center;justify-content:center}
ul.dot{list-style:none}
ul.dot li{position:relative;padding-left:34px;font-size:26px;line-height:1.45;margin-bottom:18px}
ul.dot li::before{content:"";position:absolute;left:4px;top:15px;width:12px;height:12px;border-radius:50%;background:#D4A84B}
ul.dot li .ref{display:block;font-size:19px;color:#8B7A5C;margin-top:3px}
.pill{display:inline-block;background:#1B2340;color:#F3EBDD;font-size:19px;font-weight:600;letter-spacing:.06em;padding:6px 14px;border-radius:999px;margin-bottom:10px}
.kh{border-left:5px solid #D4A84B;padding:6px 0 6px 24px;margin-bottom:22px}
.kh .who{font-family:'Lora',serif;font-weight:700;font-size:29px;color:#1B2340}
.kh .what{font-size:24px;line-height:1.42;margin-top:4px}
.kh .q{font-family:'Amiri',serif;direction:rtl;text-align:right;font-size:27px;color:#1B2340;margin-top:6px}
.kh .ref{font-size:18px;color:#8B7A5C;margin-top:2px}
/* cover */
.cover{background:#1B2340;color:#F3EBDD}
.cover .frame{position:absolute;inset:44px;border:1.5px solid rgba(212,168,75,.55);border-radius:6px}
.cover .rain{position:absolute;top:0;right:0;width:620px;height:620px;opacity:.22}
"""