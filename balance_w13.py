# -*- coding: utf-8 -*-
import json,os
BASE="/sessions/modest-brave-pasteur/mnt/잇올 2028 입시 뉴스 & 대응 전략 데일리 업데이트/output/원장부원장_평가_12주_2026-06-29"
SPEC=[ # (q_sub, choice_idx, new_text)
 ("수능 모의 성적이 최상위인 N수생",0,"내신을 단기간에 끌어올려 학생부교과 전형에 집중해 지원하라고 안내한다"),
 ("세특·활동이 풍부하며 면접에",0,"수능 점수만으로 가는 정시 수능100% 전형"),
 ("논술 실력이 강하고 수능최저를 충족",0,"내신 정량 성적이 가장 중요한 학생부교과 전형에 집중"),
 ("지방에 거주하며 내신이 우수한 의대",0,"전국 단위로 선발하는 일반 학생부종합 전형에 집중"),
 ("지역 의무복무를",0,"전국 단위로 선발하는 일반 정시 전형에 단독 지원"),
 ("검정고시 출신이 메디컬을 목표",2,"내신 기록이 전혀 없어도 교과전형 위주로 최대한 폭넓게 지원한다"),
 ("학생부교과로 지원하려 할 때, 법정 고졸자",0,"가천대 교과전형"),
 ("9등급 학생부를 보유한 졸업생",0,"오직 정시 한 장만 믿고 끝까지 밀어붙여 지원한다"),
 ("영어가 1등급으로 강하고",2,"무조건 표준점수 총점이 가장 높은 대학만 골라서 본다"),
 ("수시에 적극 지원하고 싶지만 수능에 자신",0,"수능최저가 가장 높은 전형만 골라서 지원한다"),
 ("교과 변별이 약해진 상황에서 상위대 교과",0,"출결 기록과 봉사 시간의 단순 총합"),
 ("자연계열로 수학·과탐이 강하고",0,"국어 반영비율이 가장 높은 환산식의 대학"),
 ("연세대(신촌) 교과·학종 지원",0,"아무런 제한 조건 없이 누구나 자유롭게 지원할 수 있다고 안내한다"),
 ("내신·학생부가 모두 약하고 수능만 강한",0,"정시 학생부 반영 13개교 가운데 한 곳"),
 ("수도권에 거주하는 의대 지망 우수생이 지방대",0,"거주지나 출신 고교와는 전혀 무관하게 전국 누구나 자유롭게 지원 가능하다"),
 ("검정고시 출신 메디컬 지망생이 가천대",0,"교과·농어촌 등 검정고시가 배제되는 전형에 지원"),
 ("케이스 상담을 시작할 때 가장 먼저",2,"키·몸무게·혈액형·거주지·취미 다섯 가지"),
 ("구체 합격선·등급은 어디서 최종",0,"본 매핑표에 적힌 표 값을 그대로 최종 합격선으로 그냥 사용한다"),
]
p=os.path.join(BASE,"W13_주간평가_20문항.html");s=open(p,encoding="utf-8").read()
i=s.index("questions");j=s.index("[",i);d=0;k=j
while k<len(s):
    if s[k]=="[":d+=1
    elif s[k]=="]":
        d-=1
        if d==0:break
    k+=1
qs=json.loads(s[j:k+1])
for sub,ci,txt in SPEC:
    hits=[q for q in qs if sub in q['q']]
    assert len(hits)==1, f"'{sub}' {len(hits)}건"
    q=hits[0]
    assert ci!=q['answer'], f"'{sub}' 정답수정 시도"
    q['choices'][ci]=txt
    assert len(set(q['choices']))==4, f"'{sub}' 중복"
s2=s[:j]+json.dumps(qs,ensure_ascii=False)+s[k+1:]
open(p,"w",encoding="utf-8").write(s2)
# 검증
qs2=json.loads(s2[s2.index("[",s2.index("questions")):][:0]+s2[s2.index("[",s2.index("questions")):])  # placeholder
def gq(t):
    a=t.index("questions");b=t.index("[",a);dd=0;c=b
    while c<len(t):
        if t[c]=="[":dd+=1
        elif t[c]=="]":
            dd-=1
            if dd==0:break
        c+=1
    return json.loads(t[b:c+1])
qs2=gq(s2)
tell=sum(1 for it in qs2 if it['type']=='mc' and (lambda L,a:L[a]==max(L) and L.count(max(L))==1)([len(c) for c in it['choices']],it['answer']))
dupc=any(len(set(it['choices']))!=4 for it in qs2 if it['type']=='mc')
print("W13 적용완료 · 정답유일최장:",tell,"· 선지중복:",dupc,"· 문항:",len(qs2))
PYEOF=None
