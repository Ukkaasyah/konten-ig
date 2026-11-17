"""Pustaka render carousel fikih/tazkiyah (1080x1350). Dipakai skrip per-postingan."""
import re, html, asyncio
from pathlib import Path
from playwright.async_api import async_playwright
HERE = Path(__file__).parent
def load_css(theme="green"):
    ns = {}; exec(open(HERE / f"base_css_{'navy' if theme=='navy' else 'green'}.py").read(), ns); return ns["CSS"]
HANDLE = "@ukkaasyah.abdurrahman"

class Deck:
    def __init__(self, label, total, theme="green"):
        self.label, self.total, self.css, self.slides = label, total, load_css(theme), []
    def page(self, inner, cls="cream"):
        return f"<!doctype html><html><head><meta charset='utf-8'><style>{self.css}</style></head><body><div class='slide {cls}'>{inner}</div></body></html>"
    def chrome(self, n, label=None, last=False):
        sw = "" if last else "<span class='swipe'>geser &rarr;</span>"
        return (f"<div class='top'><span>{label or self.label}</span><span class='no'>{n:02d}/{self.total:02d}</span></div>"
                f"<div class='foot'><span>{HANDLE}</span>{sw}</div>")
    @staticmethod
    def kitab(title, pg, text, link):
        t = html.escape(text)
        t = re.sub(r"\(([^()]*)\)", r"<b>(\1)</b>", t).replace("⟦", "<mark>").replace("⟧", "</mark>")
        return (f"<div class='kitab'><div class='khead'><span class='p'>{pg}</span><span class='t'>{title}</span></div>"
                f"<div class='kbody'>{t}</div><div class='kfoot'><span>{link}</span><span>teks dari Turath · bagian bertanda = nukilan</span></div></div>")
    def add(self, inner, cls="cream"):
        self.slides.append(self.page(inner, cls))

FIT = """() => {
  const w=document.querySelector('.wrap'); if(!w) return null;
  const els=[...w.querySelectorAll('*')].filter(e=>!e.closest('.khead,.kfoot'));
  const base=els.map(e=>parseFloat(getComputedStyle(e).fontSize));
  const apply=f=>els.forEach((e,k)=>{ if(e.tagName!=='H2') e.style.fontSize=(base[k]*f)+'px'; });
  const autos=[...w.children].filter(c=>c.style.marginTop==='auto'); autos.forEach(c=>c.style.marginTop='28px');
  const bottom=()=>Math.max(...[...w.children].map(c=>c.getBoundingClientRect().bottom));
  const lim=w.getBoundingClientRect().bottom-8; let lo=0.7,hi=1.45;
  for(let t=0;t<16;t++){const m=(lo+hi)/2; apply(m); if(bottom()<=lim) lo=m; else hi=m;}
  apply(lo); autos.forEach(c=>c.style.marginTop='auto'); return lo; }"""

def render(deck, out):
    out = Path(out); out.mkdir(parents=True, exist_ok=True)
    async def main():
        async with async_playwright() as p:
            b = await p.chromium.launch(); pg = await b.new_page(viewport={"width": 1080, "height": 1350})
            for i, h in enumerate(deck.slides, 1):
                await pg.set_content(h, wait_until="load"); await pg.evaluate("document.fonts.ready"); await pg.wait_for_timeout(150)
                f = await pg.evaluate(FIT); await pg.wait_for_timeout(60)
                await pg.screenshot(path=str(out / f"{i:02d}.jpg"), type="jpeg", quality=93); print(i, f)
            await b.close()
    asyncio.run(main())
