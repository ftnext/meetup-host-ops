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

    def __str__(self) -> str:
        return f"{self.day:%m/%d} {self.start_time:%H:%M}開始のトーク"


@dataclass(frozen=True)
class TalkSlots(Sequence):
    values: Sequence[TalkSlot]

    def __len__(self) -> int:
        return len(self.values)

    def __getitem__(self, key):
        if isinstance(key, slice):
            raise NotImplementedError
        return self.values[key]

    def exclude_talked_slots(self) -> UnfeaturedTalkSlots:
        filtered = filter(lambda slot: not slot.is_already_talked, self.values)
        return UnfeaturedTalkSlots(list(filtered))

    def sample_one(self) -> TalkSlot:
        index = random.choice(range(len(self)))
        return self[index]


@dataclass(frozen=True)
class UnfeaturedTalkSlots(TalkSlots):
    def __post_init__(self):
        for talk_slot in self.values:
            if talk_slot.is_already_talked:
                message = (
                    f"{self.__class__.__name__} cannot include any already "
                    f"talked slot: {talk_slot!r}"
                )
                raise ValueError(message)


def main(slots) -> TalkSlot:
    all_talk_slots = TalkSlots(slots)
    not_yet_talked_slots = all_talk_slots.exclude_talked_slots()
    return not_yet_talked_slots.sample_one()


if __name__ == "__main__":
    slots = [
        TalkSlot(date(2022, 10, 14), time(13, 0), is_already_talked=True),
        TalkSlot(date(2022, 10, 14), time(13, 50)),
        TalkSlot(date(2022, 10, 14), time(14, 40)),
        TalkSlot(date(2022, 10, 14), time(16, 20)),
        TalkSlot(date(2022, 10, 14), time(17, 10)),
        TalkSlot(date(2022, 10, 15), time(13, 0)),
        TalkSlot(date(2022, 10, 15), time(13, 50)),
        TalkSlot(date(2022, 10, 15), time(15, 10)),
        TalkSlot(date(2022, 10, 15), time(16, 0)),
    ]
    this_time_slot = main(slots)
    print(f"今回のスペースで話すのは、{this_time_slot}です")
