/* 메신저 봇 데일리 발송분 — 데모 샘플 */
export const BOT_SEED = [
  {
    id: "b1", aff: "SKGC", title: "NCC 정기보수(TA) 기간 단축 벤치마킹", category: "정비/TA",
    risk: "공기 단축에 따른 안전·품질 검증 부담 증가",
    effect: "TA 1일 단축 시 기회손실·고정비 부담 축소",
    kpi: { name: "TA 기간 단축률", formula: "(기준 TA일수 − 실제 TA일수) ÷ 기준 TA일수" },
    evidence: ["e04", "e01"],
  },
  {
    id: "b2", aff: "SKE", title: "전력 다소비 공정 요금제·피크 관리 최적화", category: "에너지비",
    risk: "부하 이동 시 생산 계획과의 충돌 가능성",
    effect: "요금 인상분 흡수 및 전력비 원단위 개선",
    kpi: { name: "전력 원단위", formula: "전력사용량(kWh) ÷ 생산량(t)" },
    evidence: ["e02", "e11"],
  },
  {
    id: "b3", aff: "SKO", title: "검사 자동화 확대를 통한 셀 수율 개선", category: "수율",
    risk: "설비 투자 대비 효과 검증에 기간 소요",
    effect: "불량 유출 감소와 검사 인건비 절감 동시 달성",
    kpi: { name: "공정 수율", formula: "양품 수 ÷ 투입 수 × 100(%)" },
    evidence: ["e06", "e05"],
  },
];
