from datetime import datetime
# Mengimpor class & struktur data asli dari project kamu
from structures import QueueLinear, StackLinear

# Class Model Data sesuai atribut di Lembar Aktivitas PDF
class Mahasiswa:
    def __init__(self, nim: str, nama: str, nomor_urut: str, waktu_datang: str):
        self.nim = nim
        self.nama = nama
        self.nomor_urut = nomor_urut
        self.waktu_datang = waktu_datang

    def __str__(self):
        return f"[{self.nomor_urut}] {self.nim} - {self.nama} (Datang: {self.waktu_datang})"

class Aktivitas:
    def __init__(self, id_aktivitas: str, deskripsi: str, waktu: str):
        self.id_aktivitas = id_aktivitas
        self.deskripsi = deskripsi
        self.waktu = waktu

    def __str__(self):
        return f"[{self.id_aktivitas}] {self.deskripsi} ({self.waktu})"


# Inisialisasi Struktur Data
antrean = QueueLinear()
history_undo = StackLinear()

counter_mhs = 1
counter_act = 1

print("="*60)
print("  SISTEM LAYANAN ADMINISTRASI MAHASISWA & UNDO HISTORY")
print("="*60)

while True:
    print("\n--- MENU UTAMA ---")
    print("1. Tambah Mahasiswa ke Antrean (Enqueue)")
    print("2. Layani Mahasiswa Terdepan (Dequeue + Otomatis Catat Undo)")
    print("3. Catat Aktivitas Lain Petugas (Push ke Undo)")
    print("4. Batalkan Aktivitas Terakhir (Pop / Undo)")
    print("5. Lihat Status Terdepan (Peek Antrean & Undo Stack)")
    print("6. Keluar")
    
    pilihan = input("Pilih Menu (1-6): ").strip()

    if pilihan == "1":
        print("\n--- INPUT DATA MAHASISWA (ANTREAN) ---")
        nim = input("Masukkan NIM          : ").strip()
        nama = input("Masukkan Nama         : ").strip()
        nomor_urut = f"A{counter_mhs:03d}"
        waktu_datang = datetime.now().strftime("%H:%M:%S")
        
        mhs = Mahasiswa(nim, nama, nomor_urut, waktu_datang)
        antrean.enqueue(mhs)
        counter_mhs += 1
        
        print(f"-> [SUCCESS ENQUEUE] Data Berhasil Masuk Antrean:")
        print(f"   {mhs}")

    elif pilihan == "2":
        print("\n--- PROSES PELAYANAN MAHASISWA ---")
        if not antrean.is_empty():
            mhs_dilayani = antrean.dequeue()
            waktu_act = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            id_act = f"ACT{counter_act:02d}"
            deskripsi = f"Melayani Antrean {mhs_dilayani.nomor_urut} ({mhs_dilayani.nama})"
            
            # Buat objek aktivitas dan Push ke Undo Stack
            act = Aktivitas(id_act, deskripsi, waktu_act)
            history_undo.push(act)
            counter_act += 1
            
            print(f"-> [SUCCESS DEQUEUE] Memproses Pelayanan:")
            print(f"   Mahasiswa: {mhs_dilayani}")
            print(f"-> [LOG UNDO] Aktivitas Otomatis Dicatat ke Stack Undo:")
            print(f"   {act}")
        else:
            print("-> [WARNING] Antrean Mahasiswa sedang kosong!")

    elif pilihan == "3":
        print("\n--- CATAT AKTIVITAS PETUGAS LAIN ---")
        deskripsi = input("Deskripsi Aktivitas (misal: Cetak KPU / Verifikasi Berkas): ").strip()
        id_act = f"ACT{counter_act:02d}"
        waktu_act = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        act = Aktivitas(id_act, deskripsi, waktu_act)
        history_undo.push(act)
        counter_act += 1
        
        print(f"-> [SUCCESS PUSH] Aktivitas Berhasil Dicatat ke Undo History:")
        print(f"   {act}")

    elif pilihan == "4":
        print("\n--- PROSES UNDO (BATALKAN AKTIVITAS TERAKHIR) ---")
        if not history_undo.is_empty():
            act_batal = history_undo.pop()
            print(f"-> [SUCCESS POP / UNDO] Aktivitas Berikut Berhasil Dibatalkan:")
            print(f"   {act_batal}")
        else:
            print("-> [WARNING] Riwayat Undo kosong! Tidak ada aktivitas yang bisa dibatalkan.")

    elif pilihan == "5":
        print("\n--- PEEK STATUS ANTREAN & UNDO ---")
        mhs_depan = antrean.peek()
        act_teratas = history_undo.peek()
        
        print(f"1. Mahasiswa Terdepan (Queue Peek) : {mhs_depan if mhs_depan else 'Kosong'}")
        print(f"2. Aktivitas Teratas   (Stack Peek) : {act_teratas if act_teratas else 'Kosong'}")

    elif pilihan == "6":
        print("\nTerima kasih! Program selesai.")
        break
    else:
        print("-> Pilihan tidak valid, silakan ketik angka 1 - 6.")