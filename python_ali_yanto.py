"""
Pemrograman Berorientasi Objek - Kenalan Ali dan Yanto
"""


class Orang:
    def __init__(self, nama, umur, alamat, hobi):
        self.nama = nama
        self.umur = umur
        self.alamat = alamat
        self.hobi = hobi

    def sapa(self, orang_lain):
        print(f"{self.nama}: Halo {orang_lain.nama}, salam kenal ya!")

    def perkenalan(self):
        print(f"{self.nama}: Nama saya {self.nama}, umur saya {self.umur} tahun.")
        print(f"{self.nama}: Saya tinggal di {self.alamat}.")
        print(f"{self.nama}: Hobi saya {self.hobi}.")

    def tanya_hobi(self, orang_lain):
        print(f"{self.nama}: Hobi kamu apa, {orang_lain.nama}?")

    def jawab_hobi(self):
        print(f"{self.nama}: Hobi saya {self.hobi}.")


class Siswa(Orang):
    def __init__(self, nama, umur, alamat, hobi, sekolah, kelas):
        super().__init__(nama, umur, alamat, hobi)
        self.sekolah = sekolah
        self.kelas = kelas

    def perkenalan(self):
        super().perkenalan()
        print(f"{self.nama}: Saya sekolah di {self.sekolah}, kelas {self.kelas}.")

    def tanya_sekolah(self, orang_lain):
        print(f"{self.nama}: Kamu sekolah di mana, {orang_lain.nama}?")

    def jawab_sekolah(self):
        print(f"{self.nama}: Saya sekolah di {self.sekolah}, kelas {self.kelas}.")

    def pamit(self, orang_lain):
        print(f"{self.nama}: Senang berkenalan denganmu, {orang_lain.nama}. Sampai jumpa!")


# Membuat objek
ali = Siswa("Ali", 17, "Jakarta", "bermain sepak bola", "SMA Negeri 1", "XII IPA")
yanto = Siswa("Yanto", 16, "Bandung", "membaca buku", "SMA Negeri 2", "XI IPS")

# Percakapan kenalan
print("=== PERKENALAN ALI DAN YANTO ===\n")

ali.sapa(yanto)
yanto.sapa(ali)
print()

print("--- Ali memperkenalkan diri ---")
ali.perkenalan()
print()

print("--- Yanto memperkenalkan diri ---")
yanto.perkenalan()
print()

print("--- Ngobrol ---")
ali.tanya_hobi(yanto)
yanto.jawab_hobi()
yanto.tanya_sekolah(ali)
ali.jawab_sekolah()
print()

ali.pamit(yanto)
yanto.pamit(ali)