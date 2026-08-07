"""AI Reporting 설정 API — 발송 주기·시각·채널·수신자·제외 과제.

설정은 로그인 계정별로 저장됩니다. 실제 메일/Teams 발송 연동은
`send_report()` 자리에 붙이면 되고, 지금은 발송 시각만 기록합니다.
"""
from fastapi import APIRouter, Depends

from app import store
from app.api.deps import current_email
from app.models import ReportSettingIn

router = APIRouter(prefix="/api/report", tags=["report"])


# ★ 설정 조회 라우트는 따로 두지 않는다 — GET /api/bootstrap 의 state 가
#   send·channels·recipients·sendOff 를 이미 같은 모양으로 준다.
#   그 모양을 만드는 곳은 store._user_state 하나뿐이니(아래 PUT 도 같은 함수로 응답한다)
#   설정 키를 늘릴 때는 거기만 고치면 된다.


@router.put("/settings")
def put_settings(body: ReportSettingIn, email: str = Depends(current_email)):
    st = store.save_report(
        email, freq=body.freq, time=body.time, channels=body.channels,
        recipients=body.recipients, send_off=body.sendOff,
    )
    return {
        "ok": True, "send": st["send"], "channels": st["channels"],
        "recipients": st["recipients"], "sendOff": st["sendOff"],
    }


@router.post("/test")
def test_send(email: str = Depends(current_email)):
    """테스트 발송 — 발송 채널 연동 전까지는 발송 시각만 남긴다."""
    at = store.mark_report_sent(email)
    return {"ok": True, "sentAt": at}
