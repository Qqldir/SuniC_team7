/* 트렌드룸 데이터 (trendroom.html 이식).
 * EV: 수집 외부자료 문서. theme/new/refs/biz 는 원본 TASKS 인용관계에서 계산해 baked. */

/* 테마 축 = 과제 레버 체계 (고정) */
export const TH2 = {
  "정비·설비 신뢰성": { c: "#0043ce", bg: "#eaf0fd",
    head: '정비를 "줄이는" 게 아니라 "다시 배치"하는 흐름',
    body: "공기 단축·주기 재설계 모두 안전·품질 절차를 축소하지 않고 순서와 간격을 바꿔 고정비를 흡수하는 접근입니다. 주기를 연장한 구간에는 상태 감시 계측을 추가하는 전제가 반복해서 등장합니다." },
  "에너지·유틸리티": { c: "#0f62fe", bg: "#eaf1fe",
    head: "전력비를 단가가 아니라 구조로 대응",
    body: "요금제·피크 관리에서 자가발전, 단지 내 공동활용까지 대응 축이 사외로 확장되고 있습니다. 공통적으로 투자 회수 기간이 의사결정의 핵심 변수로 언급됩니다." },
  "구매·조달": { c: "#4589ff", bg: "#edf3ff",
    head: "지역 단위 조달을 글로벌 단위로 통합",
    body: "공통 소모품·MRO를 통합 입찰로 전환하고, 규격 표준화로 관리 품목 수 자체를 줄이는 2단 접근이 공통 패턴입니다." },
  "공정 수율·품질": { c: "#007d79", bg: "#e6f4f3",
    head: "검사 자동화가 품질과 인원을 동시에 건드림",
    body: "전수검사 전환은 불량 유형 상위 공정에 먼저 적용한 뒤 검출률을 기존 방식과 비교 검증하는 순서를 밟습니다. 설비 투자 회수는 재작업 공수 절감과 함께 계산됩니다." },
  "물류·계약": { c: "#8a3ffc", bg: "#f1eafe",
    head: "운임 하락 구간에 열린 재협상 창",
    body: "지수 하락세가 이어지며 만료 임박 계약의 협상력이 커지는 구간입니다. 다만 반등 가능성 때문에 계약 기간을 분산하라는 견해가 함께 제시됩니다." },
  "간접비·원가구조": { c: "#2f4a57", bg: "#e9eff2",
    head: "절감액보다 구조 단순화를 목표로 제시",
    body: "중복 지원 기능 통합, 통제 가능·불가 항목 분리 등 금액 목표보다 관리 체계 자체를 바꾸는 서술이 늘고 있습니다." },
  "가동률·운전자본": { c: "#a56a00", bg: "#faf3e4",
    head: "다운사이클 대응이 가동 조정과 재고로 이동",
    body: "가동 조정 구간에 정비 일정을 겹쳐 비가동 시간을 압축하거나, 안전재고를 차등 적용해 회전일수를 줄이는 사례가 동시에 나타납니다." },
};

export const BIZ_C = { "에너지·화학": "#0043ce", "배터리·소재": "#007d79", "LNG·전력": "#8a3ffc" };

/* 수집 외부자료 — theme/new/refs/biz baked */
export const EV = {
  e1: { src: "미쓰이화학", kind: "결산설명회", date: "2026.07.17", url: "https://jp.mitsuichemicals.com/en/ir/",
    title: "정기보수(TA) 공정 표준화·병렬화로 공기 단축",
    sum: "FY2025 결산설명회 질의응답에서 TA 공정을 표준 작업 단위로 분해하고 상호 독립적인 공정을 병렬 배치해 평균 공기를 기존 대비 단축했다고 설명. 단축분은 가동일 확보로 이어져 고정비 흡수에 기여했다고 밝힘. 안전·품질 검증 절차는 축소하지 않고 사전 준비 단계를 앞당기는 방식을 택했다고 언급.",
    theme: "정비·설비 신뢰성", new: true, refs: 2, biz: ["에너지·화학"] },
  e2: { src: "Valero", kind: "Earnings call", date: "2026.06.27", url: "https://www.investorvalero.com/",
    title: "정제마진 약세 구간 오펙스 절감 프로그램 진척",
    sum: "2분기 실적발표 콜에서 정기보수 최적화와 에너지 효율 개선을 축으로 한 오펙스 절감 프로그램의 진척을 공개. 애널리스트 질의에서 절감분 중 상당 부분이 유틸리티 원단위 개선에서 발생했다고 답변. 배럴당 운영비 목표를 제시하며 추가 여력이 남아 있다고 설명.",
    theme: "에너지·유틸리티", new: false, refs: 4, biz: ["에너지·화학", "배터리·소재"] },
  e3: { src: "Dow", kind: "10-Q 공시", date: "2026.07.18", url: "https://investors.dow.com/",
    title: "연 10억 달러 규모 비용절감 프로그램 영역별 진척",
    sum: "분기 공시에서 물류·구매·정비 영역별 절감 실적과 잔여 목표를 구분해 기재. 구매 부문은 공통 소모품·MRO 품목을 지역 단위에서 글로벌 단위로 통합 조달하는 방식으로 단가를 인하했다고 설명. 규격 표준화를 통해 관리 품목 수를 축소한 효과도 함께 언급.",
    theme: "구매·조달", new: true, refs: 9, biz: ["에너지·화학", "배터리·소재"] },
  e4: { src: "CATL", kind: "전문지 (SNE Research)", date: "2026.07.14", url: "https://www.sneresearch.com/",
    title: "머신비전 기반 전수검사 전환으로 셀 수율 개선",
    sum: "샘플링 검사에서 머신비전 전수검사로 전환해 불량 유출을 줄이면서 검사 인원을 동시에 축소한 사례. 초기에는 불량 유형 상위 공정에만 시범 적용한 뒤 검출률을 기존 방식과 비교 검증하는 단계를 거쳤다고 보도. 설비 투자 회수에는 시간이 소요됐으나 재작업 공수 절감 효과가 병행됐다고 분석.",
    theme: "공정 수율·품질", new: true, refs: 1, biz: ["배터리·소재"] },
  e5: { src: "ENEOS", kind: "중기경영계획", date: "2026.05.30", url: "https://www.hd.eneos.co.jp/english/ir/",
    title: "설비별 고장 이력 기반 정비 주기 재설계",
    sum: "중기경영계획 자료에서 설비별 고장 이력과 정비비를 매칭해 과잉 정비 구간과 과소 정비 구간을 구분하고 주기를 재설정한 내용을 공개. 과잉 구간의 주기를 연장하고 과소 구간을 보강해 전체 정비비를 줄이면서 비계획 정지도 함께 감소시켰다고 설명. 주기 연장 구간은 상태 감시 계측을 추가해 신뢰성을 확보.",
    theme: "정비·설비 신뢰성", new: false, refs: 5, biz: ["에너지·화학"] },
  e6: { src: "해운 시황 (Argus)", kind: "시황 리포트", date: "2026.07.09", url: "https://www.argusmedia.com/",
    title: "컨테이너 해상운임 지수 하락세 지속",
    sum: "주간 시황 리포트에서 주요 항로 운임 지수의 하락세가 이어지고 있다고 분석. 장기 운송계약 갱신 시점이 임박한 화주에게 재협상 여지가 확대되는 구간이라고 평가. 다만 하반기 반등 가능성을 배제할 수 없어 계약 기간 설정에 유의가 필요하다는 견해도 함께 제시.",
    theme: "물류·계약", new: false, refs: 6, biz: ["에너지·화학", "배터리·소재"] },
  e7: { src: "아사히카세이", kind: "IR 자료", date: "2026.07.06", url: "https://www.asahi-kasei.co.jp/asahi/en/ir/",
    title: "저가동 분리막 라인 통합 운영으로 수익성 개선",
    sum: "IR 자료에서 가동률이 낮은 분리막 생산 라인을 통합 운영해 단위 고정비를 낮춘 사례를 소개. 라인별 생산 품목을 재배치하고 전환 횟수를 줄여 가동률을 끌어올린 방식. 통합 과정에서 일부 품목의 납기 대응력이 저하되는 문제가 있어 안전재고 기준을 별도로 조정했다고 부연.",
    theme: "공정 수율·품질", new: false, refs: 3, biz: ["배터리·소재", "에너지·화학"] },
  e8: { src: "LyondellBasell", kind: "Earnings call", date: "2026.07.11", url: "https://investors.lyondellbasell.com/",
    title: "간접비 구조 점검 및 지원 기능 통합",
    sum: "실적발표 콜에서 다운사이클 대응으로 간접비 구조를 점검하고 중복된 지원 기능을 통합한 내용을 설명. 사무공간과 출력·통신 등 공통 서비스 계약을 재검토해 유휴 자산을 정리했다고 언급. 절감 규모보다 구조 자체를 단순화하는 데 초점을 뒀다고 밝힘.",
    theme: "간접비·원가구조", new: false, refs: 6, biz: ["에너지·화학", "LNG·전력", "배터리·소재"] },
  e9: { src: "대한석유협회", kind: "협회 자료", date: "2026.07.01", url: "https://www.petroleum.or.kr/",
    title: "석화 콤비나트 경쟁력 방안 — 단지 내 설비 공동활용 논의",
    sum: "업계 공동 검토 자료에서 콤비나트 단지 내 유틸리티와 물류 설비의 공동활용이 의제로 다뤄짐. 인접사 간 스팀·질소 등 유휴 용량을 상호 활용해 고정비를 분담하는 구조를 검토. 실행에는 계약·정산 구조 합의가 선행되어야 하며 상당한 기간이 소요된다는 점도 지적.",
    theme: "에너지·유틸리티", new: false, refs: 2, biz: ["에너지·화학"] },
  e10: { src: "Cheniere", kind: "IR 자료", date: "2026.06.29", url: "https://lngir.cheniere.com/",
    title: "LNG 터미널 운영비 효율화 지표 공개",
    sum: "IR 자료에서 터미널 단위 운영비 지표와 개선 추이를 공개. 정비 계획을 선적 스케줄과 연동해 비가동 시간을 줄인 방식이 주요 개선 요인으로 제시됨. 장기계약 구조상 물량 변동이 제한적인 조건에서 운영비 관리가 수익성의 핵심 변수라고 설명.",
    theme: "정비·설비 신뢰성", new: false, refs: 2, biz: ["LNG·전력"] },
  e11: { src: "롯데케미칼", kind: "수시공시", date: "2026.07.21", url: "https://dart.fss.or.kr/",
    title: "여수 NCC 일부 라인 가동 조정 결정",
    sum: "수요 부진에 따른 가동률 조정을 공시. 가동 조정 구간에서 고정비 흡수 구조가 변화하며 단위 원가 경쟁이 심화될 것으로 예상된다고 기재. 조정 기간 중 정기보수 일정을 앞당겨 비가동 시간을 겹치게 배치하는 방안을 병행한다고 설명.",
    theme: "가동률·운전자본", new: true, refs: 3, biz: ["에너지·화학"] },
  e12: { src: "BASF", kind: "Annual report", date: "2026.03.28", url: "https://www.basf.com/global/en/investors",
    title: "재고 회전 개선 중심의 운전자본 관리 강화",
    sum: "연차보고서에서 다운사이클 구간의 운전자본 관리를 별도 항목으로 기술. 제품별 수요 변동성에 따라 안전재고 기준을 차등 적용하고 장기체화 재고를 분리 관리해 회전일수를 단축했다고 설명. 금리 상승 구간에서 재고 감축의 재무 효과가 확대됐다는 분석을 함께 제시.",
    theme: "가동률·운전자본", new: false, refs: 5, biz: ["에너지·화학", "LNG·전력"] },
  e13: { src: "ExxonMobil", kind: "Earnings call", date: "2026.05.02", url: "https://investor.exxonmobil.com/",
    title: "E&P 생산 단가 관리 및 운영비 구조 개선",
    sum: "실적발표 콜에서 광구별 생산 단가를 분해해 관리하는 체계를 설명. 운영비 중 통제 가능 항목과 불가 항목을 구분하고 통제 가능 항목에 목표를 부여하는 방식. 유가 하락 구간에서도 단위 생산비를 방어할 수 있었던 요인으로 제시.",
    theme: "간접비·원가구조", new: false, refs: 3, biz: ["에너지·화학"] },
  e14: { src: "GS칼텍스", kind: "수시공시", date: "2026.07.03", url: "https://dart.fss.or.kr/",
    title: "자가발전·유틸리티 설비 투자 결정 공시",
    sum: "전력비 부담에 대응하기 위한 자가발전 및 유틸리티 설비 투자를 공시. 에너지 자립도를 높여 단위 원가를 개선하는 목적이라고 기재. 투자 회수 기간과 전력 요금 전망을 함께 검토했다고 설명.",
    theme: "에너지·유틸리티", new: false, refs: 2, biz: ["에너지·화학"] },
};

const KIND_MAP = {
  "결산설명회": "실적발표", "Earnings call": "실적발표",
  "10-Q 공시": "공시", "수시공시": "공시",
  "전문지 (SNE Research)": "시황·전문지", "시황 리포트": "시황·전문지",
  "중기경영계획": "IR·보고서", "IR 자료": "IR·보고서", "Annual report": "IR·보고서",
  "협회 자료": "협회 자료",
};
export const evKind = (k) => KIND_MAP[EV[k].kind] || "IR·보고서";

export const TR_KINDS = ["전체", "공시", "실적발표", "IR·보고서", "시황·전문지", "협회 자료"];
export const TR_BIZS = ["전체", "에너지·화학", "배터리·소재", "LNG·전력"];
export const TR_PERIODS = [
  { k: "7d", l: "최근 1주", d: 7 }, { k: "1m", l: "최근 1개월", d: 30 }, { k: "3m", l: "최근 3개월", d: 91 },
  { k: "6m", l: "최근 6개월", d: 182 }, { k: "all", l: "전체", d: 9999 }, { k: "custom", l: "직접 설정", d: 0 },
];
const TR_TODAY = new Date(2026, 6, 30);

/* 날짜 헬퍼 */
export const trPd = (s) => { const [y, m, d] = s.split(".").map(Number); return new Date(y, m - 1, d); };
export const trIso = (dt) => dt.getFullYear() + "-" + String(dt.getMonth() + 1).padStart(2, "0") + "-" + String(dt.getDate()).padStart(2, "0");
export const trDot = (dt) => dt.getFullYear() + "." + String(dt.getMonth() + 1).padStart(2, "0") + "." + String(dt.getDate()).padStart(2, "0");
export const trMD = (dt) => String(dt.getMonth() + 1).padStart(2, "0") + "." + String(dt.getDate()).padStart(2, "0");
export const trShift = (dt, n) => { const x = new Date(dt); x.setDate(x.getDate() - n); return x; };
export const trMon = (dt) => { const x = new Date(dt); x.setDate(x.getDate() - ((x.getDay() + 6) % 7)); x.setHours(0, 0, 0, 0); return x; };

/* 기간 범위 [from, to] */
export function trRange(S) {
  if (S.trPeriod === "custom")
    return [new Date(S.trFrom + "T00:00:00"), new Date(S.trTo + "T23:59:59")];
  const p = TR_PERIODS.find((x) => x.k === S.trPeriod) || TR_PERIODS[1];
  return [trShift(TR_TODAY, p.d), new Date(2026, 6, 30, 23, 59)];
}
/* 기간 + 분야까지 적용한 모집단 (AI 요약·상위 테마) */
export function trScope(S) {
  const [f, t] = trRange(S);
  return Object.keys(EV).filter((k) => {
    const d = trPd(EV[k].date);
    if (d < f || d > t) return false;
    if (S.trBiz !== "전체" && !EV[k].biz.includes(S.trBiz)) return false;
    return true;
  });
}
