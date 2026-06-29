# -*- coding: utf-8 -*-
"""원장·부원장 12주 평가 W5~W8 + M2 빌더. 잇올 다크테마(관리자 블루). 합격 70점."""
import json, os

OUT = "/sessions/modest-brave-pasteur/mnt/잇올 2028 입시 뉴스 & 대응 전략 데일리 업데이트/output/원장부원장_평가_12주_2026-06-29"

STYLE_SUM = """:root{--bg:#09090f;--surface:#15151d;--surface2:#1d1d27;--border:#2a2a3c;--text:#e8e8f0;--dim:#8a8aa2;--accent:#3b9eff;--green:#22d07a;--red:#f0414a;--yellow:#f5b731}
*{box-sizing:border-box}body{background:var(--bg);color:var(--text);font-family:'Noto Sans KR',sans-serif;font-weight:300;line-height:1.75;margin:0;padding:40px 6vw 90px}
.wrap{max-width:820px;margin:0 auto}
.kick{font-family:'DM Mono',monospace;color:var(--accent);letter-spacing:2px;font-size:12.5px}
h1{font-size:clamp(22px,3.4vw,32px);font-weight:900;letter-spacing:-.02em;line-height:1.25;border-bottom:3px solid var(--accent);padding-bottom:14px;margin:6px 0 4px}
.meta{color:var(--dim);font-family:'DM Mono',monospace;font-size:12.5px;margin-bottom:8px}
h2{font-size:19px;font-weight:800;margin:30px 0 8px;color:#fff}
h2:before{content:"";display:inline-block;width:9px;height:19px;background:var(--accent);border-radius:2px;margin-right:10px;vertical-align:-2px}
p,li{font-size:15px;color:#d8d8e6}
strong{color:#fff;font-weight:700}
em{color:var(--accent);font-style:normal;font-weight:500}
table{width:100%;border-collapse:collapse;margin:12px 0;font-size:13.8px;background:var(--surface);border-radius:10px;overflow:hidden}
th{background:var(--surface2);color:#fff;text-align:left;padding:9px 12px;border-bottom:2px solid var(--border)}
td{padding:8px 12px;border-bottom:1px solid var(--border);color:#d6d6e6}
.key{background:var(--surface);border-left:3px solid var(--green);border-radius:0 10px 10px 0;padding:14px 18px;margin:18px 0}
.key b{color:var(--green)}
.warn{background:var(--surface);border-left:3px solid var(--yellow);border-radius:0 10px 10px 0;padding:12px 16px;margin:14px 0;font-size:14px;color:#e7e1cf}
.foot{color:var(--dim);font-size:12px;margin-top:36px;border-top:1px solid var(--border);padding-top:12px}"""

FOOT = '<div class="foot">교과입시팀 · 원장·부원장 12주 입시상식 프로그램 · 본 자료는 내부 학습용. 대학별 세부 전형·수능최저·정시 환산·일정은 어디가(adiga.kr)·각 대학 모집요강 최종본으로 확인. 일부 비율(상위15개대·의대·검정고시 등)은 기관·시행계획 기반 분석으로 모집요강 최종본과 차이가 있을 수 있습니다.</div>'

def summary(fname, title, kick, h1, meta, body):
    html = f"""<!DOCTYPE html><html lang="ko"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1"><title>{title}</title>
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300;400;500;700;900&family=DM+Mono:wght@400;500&display=swap" rel="stylesheet">
<style>
{STYLE_SUM}
</style></head><body><div class="wrap">
<div class="kick">{kick}</div><h1>{h1}</h1><p class="meta">{meta}</p>
{body}
{FOOT}
</div></body></html>"""
    with open(os.path.join(OUT, fname), "w", encoding="utf-8") as f:
        f.write(html)
    print("written:", fname, len(html), "bytes")

STYLE_QUIZ = """:root{--bg:#09090f;--surface:#15151d;--surface2:#1d1d27;--border:#2a2a3c;--text:#e8e8f0;--dim:#7a7a96;--accent:#3b9eff;--green:#22d07a;--red:#f0414a;--yellow:#f5b731}
*{box-sizing:border-box}
body{background:var(--bg);color:var(--text);font-family:'Noto Sans KR',sans-serif;font-weight:300;line-height:1.6;margin:0;padding:40px 5vw 80px}
.wrap{max-width:800px;margin:0 auto}
h1{font-size:clamp(21px,3vw,30px);font-weight:900;letter-spacing:-.02em;border-bottom:3px solid var(--accent);padding-bottom:14px}
.meta{color:var(--dim);font-family:'DM Mono',monospace;font-size:13px;margin:8px 0 4px}
.name{margin:20px 0}
.name input{width:100%;max-width:340px;background:var(--surface);border:1px solid var(--border);border-radius:9px;color:#fff;padding:11px 14px;font-size:15px;font-family:inherit}
label.nm{display:block;font-size:14px;color:var(--dim);margin-bottom:6px}
.q{background:var(--surface);border:1px solid var(--border);border-radius:14px;padding:18px 20px;margin:16px 0}
.qh{font-weight:700;color:#fff;font-size:15.5px;margin-bottom:6px}
.qh .n{color:var(--accent);font-family:'DM Mono',monospace;margin-right:8px}
.badge{font-size:11.5px;font-family:'DM Mono',monospace;color:var(--dim);border:1px solid var(--border);border-radius:5px;padding:1px 7px;margin-left:8px}
.opt{display:block;background:var(--surface2);border:1px solid var(--border);border-radius:9px;padding:10px 14px;margin:8px 0;cursor:pointer;font-size:15px;transition:.12s}
.opt:hover{border-color:var(--accent)}
.opt input{margin-right:10px;accent-color:var(--accent)}
.short input{width:100%;background:var(--surface2);border:1px solid var(--border);border-radius:9px;color:#fff;padding:10px 14px;font-size:15px;font-family:inherit}
button{background:var(--accent);color:#06121f;border:none;border-radius:10px;padding:13px 26px;font-size:16px;font-weight:700;font-family:inherit;cursor:pointer;margin-top:10px}
button.ghost{background:transparent;color:var(--accent);border:1px solid var(--accent)}
.res{background:var(--surface);border:1px solid var(--border);border-radius:14px;padding:22px;margin:18px 0}
.score{font-size:46px;font-weight:900;letter-spacing:-.02em}
.ok{color:var(--green)}.no{color:var(--red)}
.rev{font-size:14px;margin:10px 0;padding:10px 14px;border-radius:9px;background:var(--surface2);border:1px solid var(--border)}
.rev .ex{color:var(--dim);font-size:13.5px;margin-top:4px}
.codebox{width:100%;background:#06070c;border:1px solid var(--accent);border-radius:9px;color:var(--green);padding:12px;font-family:'DM Mono',monospace;font-size:12.5px;margin-top:8px;word-break:break-all;min-height:64px}
.hint{color:var(--dim);font-size:13px;margin-top:6px}"""

QUIZ_JS = """const form=document.getElementById('quiz');
QUIZ.questions.forEach((it,i)=>{const d=document.createElement('div');d.className='q';
 const tag=it.type==='mc'?'객관식':'단답형';
 let h=`<div class="qh"><span class="n">Q${i+1}</span>${it.q}<span class="badge">${tag}</span></div>`;
 if(it.type==='mc'){it.choices.forEach((c,j)=>{h+=`<label class="opt"><input type="radio" name="q${i}" value="${j}">${c}</label>`;});}
 else{h+=`<div class="short"><input type="text" name="q${i}" placeholder="답을 입력하세요" autocomplete="off"></div>`;}
 d.innerHTML=h;form.appendChild(d);});
function norm(s){return (s||'').toString().trim().toLowerCase().replace(/\\s+/g,'').replace(/[.\\-\\/]/g,'');}
document.getElementById('submit').onclick=()=>{
 const name=document.getElementById('nm').value.trim()||'(이름미입력)';
 let score=0;const flags=[];const ans=[];
 let html=`<div class="res"><div>채점 결과 — <b>${name}</b></div>`;
 QUIZ.questions.forEach((it,i)=>{let correct=false,given='';
  if(it.type==='mc'){const sel=document.querySelector(`input[name="q${i}"]:checked`);given=sel?sel.value:'';correct=sel&&Number(sel.value)===it.answer;}
  else{const v=document.querySelector(`input[name="q${i}"]`).value;given=v;correct=it.accept.some(a=>norm(a)===norm(v));}
  if(correct)score++;flags.push(correct?1:0);ans.push(given);});
 const pct=Math.round(score/QUIZ.questions.length*100);
 html+=`<div class="score ${pct>=70?'ok':'no'}">${score} / ${QUIZ.questions.length} <span style="font-size:18px">(${pct}점)</span></div>`;
 html+=`<div class="hint">${pct>=70?'합격 기준(70점) 충족':'합격 기준(70점) 미달 — 자료 재학습 권장'}</div>`;
 QUIZ.questions.forEach((it,i)=>{const ok=flags[i]===1;
  let yourTxt=it.type==='mc'?(ans[i]!==''?it.choices[Number(ans[i])]:'(무응답)'):(ans[i]||'(무응답)');
  let corrTxt=it.type==='mc'?it.choices[it.answer]:it.accept[0];
  html+=`<div class="rev"><b class="${ok?'ok':'no'}">${ok?'○':'✕'} Q${i+1}</b> ${it.q}<br><span class="${ok?'ok':'no'}">내 답: ${yourTxt}</span>${ok?'':` · <span class="ok">정답: ${corrTxt}</span>`}<div class="ex">${it.ex}</div></div>`;});
 const payload={t:QUIZ.id,n:name,d:new Date().toISOString().slice(0,16).replace('T',' '),s:score,tot:QUIZ.questions.length,c:flags};
 const code='ITALL1|'+btoa(unescape(encodeURIComponent(JSON.stringify(payload))));
 html+=`<div style="margin-top:18px"><b>결과코드</b> (복사해서 관리자에게 제출):<textarea class="codebox" id="code" readonly>${code}</textarea><button class="ghost" id="copy">결과코드 복사</button></div></div>`;
 const out=document.getElementById('out');out.innerHTML=html;out.scrollIntoView({behavior:'smooth'});
 document.getElementById('copy').onclick=()=>{const t=document.getElementById('code');t.select();document.execCommand('copy');document.getElementById('copy').textContent='복사됨 ✓';};
};"""

def quiz(fname, title, h1, meta, qid, qtitle, questions):
    qjson = json.dumps({"id": qid, "title": qtitle, "questions": questions}, ensure_ascii=False)
    html = f"""<!DOCTYPE html><html lang="ko"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300;400;500;700;900&family=DM+Mono:wght@400;500&display=swap" rel="stylesheet">
<style>
{STYLE_QUIZ}
</style></head><body><div class="wrap">
<h1>{h1}</h1>
<p class="meta">{meta}</p>
<p class="hint">먼저 「해당 주차 요약자료」를 읽고 응시하세요. 제출하면 즉시 채점되고, 하단에 <b>결과코드</b>가 생성됩니다. 그 코드를 관리자에게 제출(복사→전달)하면 통계에 집계됩니다.</p>
<div class="name"><label class="nm" for="nm">이름 / 소속(센터)</label><input id="nm" placeholder="예: 홍길동 / 천안센터"></div>
<form id="quiz"></form>
<button id="submit">제출하고 채점하기</button>
<div id="out"></div>
<script>
const QUIZ = {qjson};
{QUIZ_JS}
</script></div></body></html>"""
    with open(os.path.join(OUT, fname), "w", encoding="utf-8") as f:
        f.write(html)
    # sanity check answers
    for n,it in enumerate(questions):
        if it["type"]=="mc":
            assert 0 <= it["answer"] < len(it["choices"]), f"{fname} Q{n+1} bad answer idx"
        else:
            assert it.get("accept"), f"{fname} Q{n+1} no accept"
    print("written:", fname, len(html), "bytes,", len(questions), "Q")

print("OK templates loaded")
