from dataclasses import KW_ONLY, dataclass
from datetime import date, time


@dataclass(frozen=True)
class TalkSlot:
    day: date
    start_time: time
    _: KW_ONLY
    is_already_talked: bool = False
