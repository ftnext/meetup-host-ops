from collections.abc import Sequence
from datetime import date, time
from unittest import TestCase

from select_slot import TalkSlot, TalkSlots


class TalkSlotTestCase(TestCase):
    def test_can_create(self):
        day = date(2022, 10, 14)
        start_time = time(13, 0)

        actual = TalkSlot(day, start_time)

        self.assertEqual(actual.day, day)
        self.assertEqual(actual.start_time, start_time)
        self.assertFalse(actual.is_already_talked)

    def test_can_create_already_talked(self):
        day = date(2022, 10, 15)
        start_time = time(15, 10)

        actual = TalkSlot(day, start_time, is_already_talked=True)

        self.assertTrue(actual.is_already_talked)


class TalkSlotsTestCase(TestCase):
    def setUp(self):
        self.slots = [
            TalkSlot(date(2022, 10, 14), time(13, 50), is_already_talked=True),
            TalkSlot(date(2022, 10, 14), time(14, 40)),
            TalkSlot(date(2022, 10, 15), time(16, 0)),
        ]

    def test_can_create(self):
        actual = TalkSlots(self.slots)

        self.assertIsInstance(actual, Sequence)
        self.assertEqual(actual.values, self.slots)

    def test_length_3_when_has_3_slots(self):
        sut = TalkSlots(self.slots)

        self.assertEqual(len(sut), 3)
