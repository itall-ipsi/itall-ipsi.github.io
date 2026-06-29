# -*- coding: utf-8 -*-
"""세부안내(참고서) 빌더. 요약 1p를 깊이·범위 확장. 검증 사실만."""
import os
OUT="/sessions/modest-brave-pasteur/mnt/잇올 2028 입시 뉴스 & 대응 전략 데일리 업데이트/output/원장부원장_평가_12주_2026-06-29"
CSS=""":root{--bg:#09090f;--surface:#15151d;--surface2:#1d1d27;--border:#2a2a3c;--text:#e8e8f0;--dim:#8a8aa2;--accent:#3b9eff;--green:#22d07a;--red:#f0414a;--yellow:#f5b731;--purple:#b794f6}
*{box-sizing:border-box}body{background:var(--bg);color:var(--text);font-family:'Noto Sans KR',sans-serif;font-weight:300;line-height:1.8;margin:0;padding:40px 6vw 100px}
.wrap{max-width:860px;margin:0 auto}
.kick{font-family:'DM Mono',monospace;color:var(--accent);letter-spacing:2px;font-size:12.5px}
.badge{font-family:'DM Mono',monospace;font-size:11px;color:var(--purple);border:1px solid var(--purple);border-radius:5px;padding:1px 8px;margin-left:8px;vertical-align:3px}
h1{font-size:clamp(22px,3.4vw,32px);font-weight:900;letter-spacing:-.02em;line-height:1.25;border-bottom:3px solid var(--accent);padding-bottom:14px;margin:6px 0 4px}
.meta{color:var(--dim);font-family:'DM Mono',monospace;font-size:12.5px;margin-bottom:8px}
h2{font-size:20px;font-weight:800;margin:34px 0 10px;color:#fff}
h2:before{content:"";display:inline-block;width:9px;height:20px;background:var(--accent);border-radius:2px;margin-right:10px;vertical-align:-2px}
h3{font-size:16px;font-weight:700;color:#dfe6ff;margin:18px 0 6px}
p,li,td,th{font-size:15px;color:#d8d8e6}
strong{color:#fff;font-weight:700}em{color:var(--accent);font-style:normal;font-weight:500}
ul{padding-left:20px}li{margin:4px 0}
table{width:100%;border-collapse:collapse;margin:12px 0;font-size:13.8px;background:var(--surface);border-radius:10px;overflow:hidden}
th{background:var(--surface2);color:#fff;text-align:left;padding:9px 12px;border-bottom:2px solid var(--border)}
td{padding:8px 12px;border-bottom:1px solid var(--border);color:#d6d6e6;vertical-align:top}
.lead{background:var(--surface);border-left:3px solid var(--accent);border-radius:0 10px 10px 0;padding:14px 18px;margin:14px 0;font-size:15.5px}
.key{background:var(--surface);border-left:3px solid var(--green);border-radius:0 10px 10px 0;padding:14px 18px;margin:18px 0}
.key b{color:var(--green)}
.warn{background:var(--surface);border-left:3px solid var(--yellow);border-radius:0 10px 10px 0;padding:12px 16px;margin:14px 0;font-size:14px;color:#e7e1cf}
.faq{background:var(--surface2);border:1px solid var(--border);border-radius:12px;padding:14px 18px;margin:12px 0}
.faq .q{color:#fff;font-weight:700}.faq .a{color:#cfd6e6;margin-top:4px}
.xref{background:var(--surface);border-left:3px solid var(--purple);border-radius:0 10px 10px 0;padding:14px 18px;margin:18px 0}
.xref b{color:var(--purple)}
.foot{color:var(--dim);font-size:12px;margin-top:40px;border-top:1px solid var(--border);padding-top:12px}
code{font-family:'DM Mono',monospace;font-size:13px;color:#bcd}"""

def detail(fname,kick,h1,meta,body):
    html=f"""<!DOCTYPE html><html lang="ko"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1"><title>{h1}</title>
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300;400;500;700;900&family=DM+Mono:wght@400;500&display=swap" rel="stylesheet">
<style>
{CSS}
</style></head><body><div class="wrap">
<div class="kick">{kick}</div><h1>{h1}</h1><p class="meta">{meta}</p>
{body}
<div class="foot">교과입시팀 · 원장·부원장 입시상식 프로그램 · 세부안내(참고서) · 본 자료는 내부 학습용. 대학별 세부·수능최저·정시 환산·검정고시 자격·일정은 어디가(adiga.kr)·각 대학 2028 모집요강 최종본으로 확인. 일부 비율·분류는 기관·시행계획(2026-06-02 정리) 기반으로 최종본과 차이가 있을 수 있음.</div>
</div></body></html>"""
    with open(os.path.join(OUT,fname),"w",encoding="utf-8") as f: f.write(html)
    print("written:",fname,len(html),"bytes")
print("detail_builder loaded")
