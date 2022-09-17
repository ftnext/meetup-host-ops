from __future__ import annotations

import random
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
        return len(self.values)

    def __getitem__(self, key):
        if isinstance(key, slice):
            raise NotImplementedError
        return self.values[key]

    def exclude_talked_slots(self) -> TalkSlots:
        filtered = filter(lambda slot: not slot.is_already_talked, self.values)
        return self.__class__(list(filtered))

    def sample_one(self) -> TalkSlot:
        index = random.choice(range(len(self)))
        return self[index]
