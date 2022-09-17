from datetime import date, time
from unittest import TestCase

from select_slot import TalkSlot


class TalkSlotTestCase(TestCase):
    def test_can_create(self):
        day = date(2022, 10, 14)
        start_time = time(13, 0)

        actual = TalkSlot(day, start_time)

        self.assertEqual(actual.day, day)
        self.assertEqual(actual.start_time, start_time)
