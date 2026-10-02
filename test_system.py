"""
Module Name: test_system.py
Description: Unit Testing komprehensif untuk pengujian Queue dan Stack.
"""

import unittest
from models import Mahasiswa, AktivitasLog
from structures import QueueLinear, StackLinear, StructureEmptyError

class TestQueueAntrean(unittest.TestCase):
    def setUp(self) -> None:
        self.queue: QueueLinear[Mahasiswa] = QueueLinear()
        self.m1 = Mahasiswa("12550110956", "Radish Al Sudais", "A001", "08:00:15")
        self.m2 = Mahasiswa("12550110957", "Budi Santoso", "A002", "08:05:00")

    def test_1_enqueue_and_is_empty(self) -> None:
        """Pengujian Penambahan Data & Memeriksa Kondisi Kosong"""
        self.assertTrue(self.queue.is_empty())
        self.queue.enqueue(self.m1)
        self.assertFalse(self.queue.is_empty())

    def test_2_dequeue_fifo_order(self) -> None:
        """Pengujian Penghapusan Data mengikuti prinsip FIFO"""
        self.queue.enqueue(self.m1)
        self.queue.enqueue(self.m2)
        dilayani = self.queue.dequeue()
        self.assertEqual(dilayani.nim, "12550110956")
        self.assertEqual(self.queue.peek().nim, "12550110957")

    def test_3_peek_data(self) -> None:
        """Pengujian Melihat Data Terdepan"""
        self.assertIsNone(self.queue.peek())
        self.queue.enqueue(self.m1)
        self.assertEqual(self.queue.peek().nama, "Radish Al Sudais")

    def test_4_dequeue_empty_exception(self) -> None:
        """Pengujian Exception Handling Dequeue Antrean Kosong"""
        with self.assertRaises(StructureEmptyError):
            self.queue.dequeue()


class TestStackUndo(unittest.TestCase):
    def setUp(self) -> None:
        self.stack: StackLinear[AktivitasLog] = StackLinear()
        self.act1 = AktivitasLog("ACT01", "Cetak KPU", "08:00:00")
        self.act2 = AktivitasLog("ACT02", "Update Profil", "08:10:00")

    def test_1_push_and_is_empty(self) -> None:
        """Pengujian Penambahan Aktivitas & Check Kosong"""
        self.assertTrue(self.stack.is_empty())
        self.stack.push(self.act1)
        self.assertFalse(self.stack.is_empty())

    def test_2_pop_lifo_order(self) -> None:
        """Pengujian Penghapusan Aktivitas (Undo) mengikuti LIFO"""
        self.stack.push(self.act1)
        self.stack.push(self.act2)
        undone = self.stack.pop()
        self.assertEqual(undone.id_aktivitas, "ACT02")
        self.assertEqual(self.stack.peek().id_aktivitas, "ACT01")

    def test_3_peek_data(self) -> None:
        """Pengujian Melihat Aktivitas Teratas"""
        self.assertIsNone(self.stack.peek())
        self.stack.push(self.act1)
        self.assertEqual(self.stack.peek().deskripsi, "Cetak KPU")

    def test_4_pop_empty_exception(self) -> None:
        """Pengujian Exception Handling Pop Stack Kosong"""
        with self.assertRaises(StructureEmptyError):
            self.stack.pop()

if __name__ == "__main__":
    unittest.main()