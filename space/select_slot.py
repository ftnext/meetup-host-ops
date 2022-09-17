from dataclasses import dataclass
from datetime import date, time


@dataclass(frozen=True)
class TalkSlot:
    day: date
    start_time: time
