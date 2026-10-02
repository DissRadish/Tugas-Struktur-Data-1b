"""
Module Name: models.py
Description: Mengodekan entity data untuk Mahasiswa dan Aktivitas Log Petugas.
"""

from dataclasses import dataclass
from datetime import datetime

@dataclass
class Mahasiswa:
    nim: str
    nama: str
    nomor_urut: str
    waktu_datang: str

    def __str__(self) -> str:
        return f"[{self.nomor_urut}] {self.nim} - {self.nama}"


@dataclass
class AktivitasLog:
    id_aktivitas: str
    deskripsi: str
    waktu_aktivitas: str

    def __str__(self) -> str:
        return f"[{self.id_aktivitas}] {self.deskripsi} ({self.waktu_aktivitas})"