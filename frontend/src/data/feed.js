/*
 * 외부 동향 피드 — 데모용 샘플.
 * 실서비스에서는 DART OpenAPI / SEC EDGAR / 뉴스 API 수집(지식 파밍 layer)으로 대체하며,
 * 백엔드가 뜬 경우 이 목록 대신 GET /api/feed 응답을 사용합니다. (lib/api.js 참고)
 */
export const FEED = [
  { id: "e01", d: "2026-07-21", kind: "adhoc",    src: "롯데케미칼",       title: "여수 NCC 일부 라인 가동 조정 결정", sum: "수요 부진에 따른 가동률 조정 공시. 고정비 흡수 구조 변화로 원가 경쟁 심화 예상.", tags: ["SKGC", "SKIPC"] },
  { id: "e02", d: "2026-07-20", kind: "news",     src: "에너지 정책",      title: "산업용 전기요금 추가 인상안 논의", sum: "요금 인상 시 전력 다소비 공정의 원단위 관리 중요성 확대.", tags: ["SKE", "SKGC", "SKIPC"] },
  { id: "e03", d: "2026-07-18", kind: "sec",      src: "Dow",              title: "10-Q — 연 10억 달러 비용절감 프로그램 진척 공시", sum: "물류·구매·정비 영역별 절감 실적과 잔여 목표 공개.", tags: ["SKGC"] },
  { id: "e04", d: "2026-07-17", kind: "news",     src: "미쓰이화학",       title: "정기보수(TA) 공정 개선으로 기간 단축 발표", sum: "결산설명회에서 TA 표준화·병렬화 사례와 기회손실 축소 효과 언급.", tags: ["SKGC", "SKE"] },
  { id: "e05", d: "2026-07-15", kind: "adhoc",    src: "LG에너지솔루션",   title: "신규 시설투자 집행 속도 조절 공시", sum: "수요 성장 둔화 구간의 CapEx 페이싱. 기존 라인 효율화로 무게중심 이동.", tags: ["SKO"] },
  { id: "e06", d: "2026-07-14", kind: "news",     src: "CATL",             title: "검사 자동화 확대로 셀 수율 개선 보도", sum: "머신비전 기반 전수검사 전환. 수율·검사 인건비 동시 개선 사례.", tags: ["SKO"] },
  { id: "e07", d: "2026-07-11", kind: "sec",      src: "LyondellBasell",   title: "유럽 자산 전략 검토 관련 공시", sum: "저수익 설비 매각·전환 검토. 다운사이클 포트폴리오 조정의 대표 사례.", tags: ["SKGC"] },
  { id: "e08", d: "2026-07-09", kind: "news",     src: "해운 시황",        title: "컨테이너 해상운임 지수 하락세 지속", sum: "장기 운송계약 재협상 여지. 물류비 원단위 절감 타이밍.", tags: ["SKTI", "SKE", "SKO"] },
  { id: "e09", d: "2026-07-08", kind: "periodic", src: "에쓰오일",         title: "반기보고서 — 정기보수 계획·원가 동향", sum: "하반기 TA 일정과 정비비 추이 공시. 동종사 대비 정비비율 비교 가능.", tags: ["SKE"] },
  { id: "e10", d: "2026-07-06", kind: "news",     src: "아사히카세이",     title: "분리막 라인 재편으로 수익성 개선 추진", sum: "저가동 라인 통합 운영. 가동률 방어형 원가 구조 전환 사례.", tags: ["SKIET"] },
  { id: "e11", d: "2026-07-03", kind: "adhoc",    src: "GS칼텍스",         title: "자가발전·유틸리티 설비 투자 결정 공시", sum: "전력비 부담 대응형 투자. 에너지 자립도와 원단위 개선 목적.", tags: ["SKE"] },
  { id: "e12", d: "2026-07-01", kind: "news",     src: "산업부",           title: "석화 콤비나트 경쟁력 방안 — 설비 공동활용 논의", sum: "단지 내 유틸리티·물류 공동화가 의제로. 인접사 협력형 과제 여지.", tags: ["SKGC", "SKIPC"] },
  { id: "e13", d: "2026-06-29", kind: "sec",      src: "Cheniere",         title: "운영비 가이던스 및 장기계약 업데이트", sum: "터미널 운영비 효율화 지표 공개. LNG 운영 벤치마크로 참고 가능.", tags: ["SKES"] },
  { id: "e14", d: "2026-06-27", kind: "news",     src: "Valero",           title: "정제마진 약세 구간 오펙스 절감 목표 제시", sum: "정기보수 최적화·에너지 효율 중심의 비용 대응 발표.", tags: ["SKE"] },
  { id: "e15", d: "2026-06-25", kind: "periodic", src: "삼성SDI",          title: "반기보고서 — 가동률 조정·재고 관리 동향", sum: "재고자산 회전과 가동 전략 공시. 운전자본 관리 비교 지표.", tags: ["SKO"] },
  { id: "e16", d: "2026-06-24", kind: "news",     src: "포스코인터내셔널", title: "E&P 운영 효율화·생산비 절감 계획 보도", sum: "해외 광구 운영비 구조 개선. 생산 단가 관리 사례.", tags: ["SKEO"] },
];

export const FEED_BY_ID = Object.fromEntries(FEED.map((f) => [f.id, f]));
