from collections.abc import Sequence
from dataclasses import KW_ONLY, dataclass
from datetime import date, time


@dataclass(frozen=True)
class TalkSlot:
    day: date
    start_time: time
    _: KW_ONLY
    is_already_talked: bool = False


@dataclass(frozen=True)
class TalkSlots(Sequence):
    values: Sequence[TalkSlot]

    def __len__(self) -> int:
        raise NotImplementedError

    def __getitem__(self, key):
        raise NotImplementedError
