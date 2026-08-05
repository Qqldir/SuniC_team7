/* 트렌드룸 대시보드 데이터 (데모 시드).
 * 실제로는 백엔드에서 받아올 형태 — 추후 lib/api.js 의 fetchTrend() 로 교체.
 * OC 색상은 trendroom.html 의 사업부문별 램프(에너지=블루 / 배터리=틸 / LNG=퍼플). */

export const OC_COLOR = {
  SKE: "#0043ce", SKGC: "#0f62fe", SKEN: "#4589ff", SKIPC: "#78a9ff",
  SKTI: "#a6c8ff", SKEO: "#d0e2ff",
  SKO: "#007d79", SKIET: "#3ddbd9",
  SKES: "#8a3ffc",
};

export const OC_NAME = {
  SKE: "SK에너지", SKGC: "SK지오센트릭", SKEN: "SK엔무브", SKIPC: "SK인천석유화학",
  SKTI: "SK트레이딩인터내셔널", SKEO: "SK어스온",
  SKO: "SK온", SKIET: "SK아이이테크놀로지", SKES: "SK E&S",
};

/* 일별 과제 생성 건수 (최신순 아님 — 왼→오른쪽 시간순) */
export const DAILY = [
  { label: "2026.06.26", n: 3 },
  { label: "2026.07.01", n: 4 },
  { label: "2026.07.06", n: 2 },
  { label: "2026.07.09", n: 5 },
  { label: "2026.07.13", n: 3 },
  { label: "2026.07.15", n: 6 },
  { label: "2026.07.20", n: 2 },
  { label: "2026.07.22", n: 5 },
  { label: "2026.07.24", n: 8 },
  { label: "2026.07.29", n: 9 },
];

/* 월별 OC 구성 — { "2026-07": [{oc, c}, ...], ... } (건수 내림차순) */
export const OC_MONTHLY = {
  "2026-07": [
    { oc: "SKGC", c: 9 }, { oc: "SKE", c: 7 }, { oc: "SKEN", c: 5 },
    { oc: "SKO", c: 5 }, { oc: "SKIET", c: 4 }, { oc: "SKES", c: 3 },
    { oc: "SKIPC", c: 3 }, { oc: "SKTI", c: 2 }, { oc: "SKEO", c: 1 },
  ],
  "2026-06": [
    { oc: "SKE", c: 4 }, { oc: "SKGC", c: 3 }, { oc: "SKO", c: 2 },
    { oc: "SKEN", c: 2 }, { oc: "SKES", c: 1 },
  ],
};

/* 시황 티커 (SK 계열 + 동종사) */
export const QUOTES = [
  { n: "SK이노베이션", cd: "096770", p: "118,400", c: +2.07, sk: true },
  { n: "SK아이이테크놀로지", cd: "361610", p: "42,150", c: -1.28, sk: true },
  { n: "SK", cd: "034730", p: "156,900", c: +0.45, sk: true },
  { n: "SKC", cd: "011790", p: "134,700", c: +1.36, sk: true },
  { n: "롯데케미칼", cd: "011170", p: "71,300", c: -1.79 },
  { n: "에쓰오일", cd: "010950", p: "62,800", c: +1.45 },
  { n: "LG화학", cd: "051910", p: "298,500", c: -0.83 },
  { n: "금호석유화학", cd: "011780", p: "134,200", c: +0.60 },
  { n: "한화솔루션", cd: "009830", p: "24,750", c: -2.36 },
  { n: "대한유화", cd: "006650", p: "118,000", c: -0.42 },
  { n: "LG에너지솔루션", cd: "373220", p: "371,000", c: +1.92 },
  { n: "삼성SDI", cd: "006400", p: "329,500", c: -0.61 },
];

export const quoteUrl = (cd) => `https://finance.naver.com/item/main.naver?code=${cd}`;

/* 백분율 — 최대잉여법으로 합계 100% 보장 */
export function pctRound(vals, tot) {
  const raw = vals.map((v) => (v / tot) * 100);
  const fl = raw.map(Math.floor);
  const rem = 100 - fl.reduce((a, b) => a + b, 0);
  const ord = raw
    .map((r, i) => ({ i, f: r - Math.floor(r) }))
    .sort((a, b) => b.f - a.f);
  const out = fl.slice();
  for (let k = 0; k < rem && ord.length; k++) out[ord[k % ord.length].i]++;
  return out;
}
