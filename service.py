"""
Module Name: service.py
Description: Pengelola sistem antrean dan fitur undo aktivitas petugas.
"""

from models import Mahasiswa, AktivitasLog
from structures import QueueLinear, StackLinear
from typing import Optional, List

class SystemLayananMahasiswa:
    def __init__(self) -> None:
        self.antrean: QueueLinear[Mahasiswa] = QueueLinear()
        self.history_undo: StackLinear[AktivitasLog] = StackLinear()

    def tambah_antrean(self, mhs: Mahasiswa) -> None:
        self.antrean.enqueue(mhs)

    def melayani_mahasiswa(self) -> Optional[Mahasiswa]:
        mhs = self.antrean.dequeue()
        return mhs

    def lihat_antrean_terdepan(self) -> Optional[Mahasiswa]:
        return self.antrean.peek()

    def catat_aktivitas(self, log: AktivitasLog) -> None:
        self.history_undo.push(log)

    def batalkan_aktivitas(self) -> AktivitasLog:
        return self.history_undo.pop()

    def lihat_aktivitas_terakhir(self) -> Optional[AktivitasLog]:
        return self.history_undo.peek()