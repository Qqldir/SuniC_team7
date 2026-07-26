/* 계열사 · 사업부문 · 자료 유형 상수 (데모 기준값) */

export const TODAY = "2026-07-22";

export const BIZ = {
  energy:  { label: "에너지·화학", color: "#B0522C" },
  battery: { label: "배터리·소재", color: "#2E6B57" },
  lng:     { label: "LNG·전력",   color: "#3A5E8C" },
};

export const AFFILIATES = [
  { code: "SKE",   name: "SK에너지",             biz: "energy"  },
  { code: "SKGC",  name: "SK지오센트릭",         biz: "energy"  },
  { code: "SKEN",  name: "SK엔무브",             biz: "energy"  },
  { code: "SKIPC", name: "SK인천석유화학",       biz: "energy"  },
  { code: "SKTI",  name: "SK트레이딩인터내셔널", biz: "energy"  },
  { code: "SKEO",  name: "SK어스온",             biz: "energy"  },
  { code: "SKO",   name: "SK온",                 biz: "battery" },
  { code: "SKIET", name: "SK아이이테크놀로지",   biz: "battery" },
  { code: "SKES",  name: "SK E&S",               biz: "lng"     },
];

export const AFF = Object.fromEntries(AFFILIATES.map((a) => [a.code, a]));

export const KIND = {
  adhoc:    { label: "DART 수시", cls: "badge-adhoc" },
  periodic: { label: "DART 정기", cls: "badge-periodic" },
  sec:      { label: "SEC",      cls: "badge-sec" },
  news:     { label: "뉴스",     cls: "badge-news" },
};
