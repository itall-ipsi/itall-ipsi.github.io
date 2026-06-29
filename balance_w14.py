# -*- coding: utf-8 -*-
import json,os
BASE="/sessions/modest-brave-pasteur/mnt/잇올 2028 입시 뉴스 & 대응 전략 데일리 업데이트/output/원장부원장_평가_12주_2026-06-29"
SPEC=[
 ("학생부·면접 노출을 최소화",0,"정시에 교과역량 평가와 면접을 단계별로 반영하는 대학"),
 ("부산대 의예의 정시 방식",0,"오직 순수하게 수능100%만으로 최종 선발한다"),
 ("정시에 '학생부(정성)를 새로 도입'",0,"가천대 의예(정시 수능100 방식 그대로 유지)"),
 ("권역 의무복무를 수용",0,"전국 단위로 신입생을 선발하는 일반 정시 전형"),
 ("약대의 현재 선발 구조로 옳은",2,"다른 학과 2년 수료 후 편입으로만 가는 구조"),
 ("약대 정시에 '학생부(서류)를 반영'",0,"성균관대 약학(정시 수능100 유지)"),
 ("한의예 정시 성향",0,"전국의 모든 한의대가 정시에서 학생부를 크게 반영한다"),
 ("검정고시 출신 메디컬 지망생에게 가장 현실적",0,"처음부터 서울대 의예 학종으로 정면으로 승부한다"),
 ("2028 의대 전형 중 모집 비중이 가장 큰",2,"수능100% 정시 전형 단독 운영 방식"),
 ("지역의사 선발전형의 핵심 조건",0,"수도권 대형병원에서 의무 근무해야 한다"),
 ("면접(인적성 등)을 함께 반영",0,"가천대 의예(정시 수능100·백분위 활용)"),
 ("수도권에 거주하는 의대 지망 우수생",0,"거주지나 출신 고교와 무관하게 누구나 자유롭게 지원 가능하다고 안내"),
 ("내신과 세특이 모두 우수한 의대 지망 현역",0,"수능100% 정시 전형 단독 집중 지원"),
 ("메디컬 케이스 상담을 시작할 때",0,"응시생의 취미·특기와 동아리 활동 개수만 먼저 확인"),
 ("개별 대학의 수능최저·정시 방식은 어디서 확정",0,"본 요약표에 적힌 값을 그대로 최종 합격 기준으로 그냥 사용"),
]
p=os.path.join(BASE,"W14_주간평가_20문항.html");s=open(p,encoding="utf-8").read()
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
    q=hits[0]; assert ci!=q['answer'], f"'{sub}' 정답수정"
    q['choices'][ci]=txt
    assert len(set(q['choices']))==4, f"'{sub}' 중복"
s2=s[:j]+json.dumps(qs,ensure_ascii=False)+s[k+1:]
open(p,"w",encoding="utf-8").write(s2)
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
print("W14 적용 · 문항",len(qs2),"· 정답유일최장",tell,"· 선지중복",any(len(set(it['choices']))!=4 for it in qs2 if it['type']=='mc'))
