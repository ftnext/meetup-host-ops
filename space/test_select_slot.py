from collections.abc import Sequence
from datetime import date, time
from unittest import TestCase
from unittest.mock import patch

from select_slot import TalkSlot, TalkSlots, UnfeaturedTalkSlots, main


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

    def test_human_readable_str(self):
        day = date(2022, 10, 14)
        start_time = time(13, 50)

        actual = TalkSlot(day, start_time)

        self.assertEqual(str(actual), "10/14 13:50開始のトーク")


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

    def test_get_by_index(self):
        sut = TalkSlots(self.slots)

        expected = TalkSlot(date(2022, 10, 14), time(14, 40))
        self.assertEqual(sut[1], expected)

    def test_exclude_talked_slots(self):
        sut = TalkSlots(self.slots)

        actual = sut.exclude_talked_slots()

        expected = TalkSlots(
            [
                TalkSlot(date(2022, 10, 14), time(14, 40)),
                TalkSlot(date(2022, 10, 15), time(16, 0)),
            ]
        )
        self.assertEqual(actual, expected)

    @patch("select_slot.random.choice", return_value=2)
    def test_sample_one_slot_randomly(self, random_choice):
        sut = TalkSlots(self.slots)

        actual = sut.sample_one()

        expected = TalkSlot(date(2022, 10, 15), time(16, 0))
        self.assertEqual(actual, expected)
        random_choice.assert_called_once_with(range(3))


class UnfeaturedTalkSlotsTestCase(TestCase):
    def test_can_create(self):
        slots = [
            TalkSlot(date(2022, 10, 14), time(14, 40)),
            TalkSlot(date(2022, 10, 15), time(16, 0)),
        ]

        actual = UnfeaturedTalkSlots(slots)

        self.assertIsInstance(actual, TalkSlots)
        self.assertEqual(actual.values, slots)

    def test_raise_error_when_including_already_talked_slot(self):
        slots = [
            TalkSlot(date(2022, 10, 14), time(14, 40)),
            TalkSlot(date(2022, 10, 15), time(16, 0), is_already_talked=True),
        ]

        with self.assertRaises(ValueError) as ex:
            _ = UnfeaturedTalkSlots(slots)

        expected = (
            "UnfeaturedTalkSlots cannot include any already talked slot: "
            "TalkSlot(day=datetime.date(2022, 10, 15), "
            "start_time=datetime.time(16, 0), is_already_talked=True)"
        )
        self.assertEqual(str(ex.exception), expected)


class MainTestCase(TestCase):
    def test_select_slot_to_be_talked(self):
        slots = [
            TalkSlot(date(2022, 10, 14), time(14, 40)),
            TalkSlot(date(2022, 10, 15), time(16, 0), is_already_talked=True),
        ]

        actual = main(slots)

        expected = TalkSlot(date(2022, 10, 14), time(14, 40))
        self.assertEqual(actual, expected)
