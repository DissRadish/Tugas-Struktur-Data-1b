"""
Module Name: main.py
Description: Runner simulasi 5 langkah sesuai data pada Lembar Aktivitas.
"""

from models import Mahasiswa, AktivitasLog
from service import SystemLayananMahasiswa

def run_simulation():
    system = SystemLayananMahasiswa()
    
    print("=== SIMULASI ANTREAN LAYANAN MAHASISWA (QUEUE) ===")
    m1 = Mahasiswa("12550110956", "Radish Al Sudais", "A001", "08:00:15")
    m2 = Mahasiswa("12550110957", "Budi Santoso", "A002", "08:05:00")
    m3 = Mahasiswa("12550110958", "Siti Rahma", "A003", "08:10:30")
    m4 = Mahasiswa("12550110959", "Ahmad Fauzi", "A004", "08:15:20")
    m5 = Mahasiswa("12550110960", "Dewi Lestari", "A005", "08:20:00")

    # Simulasi 5 Langkah Queue
    system.tambah_antrean(m1)
    print(f"Langkah 1 (Enqueue M1): {[str(x) for x in system.antrean.get_all()]}")
    
    system.tambah_antrean(m2)
    system.tambah_antrean(m3)
    print(f"Langkah 2 (Enqueue M2, M3): {[str(x) for x in system.antrean.get_all()]}")
    
    served = system.melayani_mahasiswa()
    print(f"Langkah 3 (Dequeue - Melayani {served.nama}): {[str(x) for x in system.antrean.get_all()]}")
    
    system.tambah_antrean(m4)
    system.tambah_antrean(m5)
    print(f"Langkah 4 (Enqueue M4, M5): {[str(x) for x in system.antrean.get_all()]}")
    
    served2 = system.melayani_mahasiswa()
    print(f"Langkah 5 (Dequeue - Melayani {served2.nama}): {[str(x) for x in system.antrean.get_all()]}")

    print("\n=== SIMULASI FITUR UNDO (STACK) ===")
    a1 = AktivitasLog("ACT01", "Melayani Antrean A001", "08:00:15")
    a2 = AktivitasLog("ACT02", "Cetak Surat Aktif Kuliah", "08:10:00")
    a3 = AktivitasLog("ACT03", "Verifikasi Transkrip Nilai", "08:20:45")
    a4 = AktivitasLog("ACT04", "Update Profil Mahasiswa", "08:35:10")
    a5 = AktivitasLog("ACT05", "Melayani Antrean A002", "08:50:00")

    # Simulasi 5 Langkah Stack
    system.catat_aktivitas(a1)
    print(f"Langkah 1 (Push ACT01): {[str(x) for x in system.history_undo.get_all()]}")
    
    system.catat_aktivitas(a2)
    system.catat_aktivitas(a3)
    print(f"Langkah 2 (Push ACT02, ACT03): {[str(x) for x in system.history_undo.get_all()]}")
    
    undone = system.batalkan_aktivitas()
    print(f"Langkah 3 (Pop Undo - Membatalkan {undone.deskripsi}): {[str(x) for x in system.history_undo.get_all()]}")
    
    system.catat_aktivitas(a4)
    system.catat_aktivitas(a5)
    print(f"Langkah 4 (Push ACT04, ACT05): {[str(x) for x in system.history_undo.get_all()]}")
    
    undone2 = system.batalkan_aktivitas()
    print(f"Langkah 5 (Pop Undo - Membatalkan {undone2.deskripsi}): {[str(x) for x in system.history_undo.get_all()]}")

if __name__ == "__main__":
    run_simulation()