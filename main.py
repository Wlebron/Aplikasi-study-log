# ================================
# APLIKASI STUDY LOG - Aplikasi Pencatat Kegiatan Belajar
# ================================

# List untuk menyimpan catatan belajar
catatan = []

# ================================
# FUNGSI UTAMA
# ================================

def tambah_catatan():
    """
    Fungsi untuk menambah catatan belajar baru.
    Meminta input: Mapel, Topik, dan Durasi (menit)
    """
    print("\n" + "="*50)
    print("📝 TAMBAH CATATAN BELAJAR")
    print("="*50)
    
    try:
        # Input dari pengguna
        mapel = input("Masukkan nama mapel: ").strip()
        if not mapel:
            print("❌ Mapel tidak boleh kosong!")
            return
        
        topik = input("Masukkan topik yang dipelajari: ").strip()
        if not topik:
            print("❌ Topik tidak boleh kosong!")
            return
        
        durasi_input = input("Masukkan durasi belajar (menit): ").strip()
        
        # Validasi durasi
        try:
            durasi = int(durasi_input)
            if durasi <= 0:
                print("❌ Durasi harus lebih dari 0 menit!")
                return
        except ValueError:
            print("❌ Durasi harus berupa angka!")
            return
        
        # Membuat struktur data catatan (dictionary)
        catatan_baru = {
            'mapel': mapel,
            'topik': topik,
            'durasi': durasi
        }
        
        # Menambah ke list catatan
        catatan.append(catatan_baru)
        print("\n✅ Catatan berhasil ditambahkan!")
        
    except KeyboardInterrupt:
        print("\n⚠️ Input dibatalkan!")


def lihat_catatan():
    """
    Fungsi untuk menampilkan semua catatan belajar.
    Jika belum ada data, tampilkan pesan yang sesuai.
    """
    print("\n" + "="*50)
    print("📋 DAFTAR CATATAN BELAJAR")
    print("="*50)
    
    # Cek apakah ada catatan
    if len(catatan) == 0:
        print("\n📭 Belum ada catatan belajar. Mulai tambahkan catatan Anda!")
        return
    
    # Tampilkan semua catatan dengan format yang rapi
    print(f"\n{'No':<4} {'Mapel':<15} {'Topik':<20} {'Durasi':<8}")
    print("-" * 50)
    
    for i, item in enumerate(catatan, start=1):
        print(f"{i:<4} {item['mapel']:<15} {item['topik']:<20} {item['durasi']:<8} menit")
    
    print("-" * 50)


def total_waktu():
    """
    Fungsi untuk menghitung total durasi belajar dari semua catatan.
    """
    print("\n" + "="*50)
    print("⏱️  TOTAL WAKTU BELAJAR")
    print("="*50)
    
    # Cek apakah ada catatan
    if len(catatan) == 0:
        print("\n📭 Belum ada catatan belajar!")
        return
    
    # Hitung total durasi
    total = sum(item['durasi'] for item in catatan)
    
    # Konversi ke jam dan menit
    jam = total // 60
    menit = total % 60
    
    print(f"\n📊 Total waktu belajar: {total} menit")
    print(f"   = {jam} jam {menit} menit")
    print(f"\n📈 Jumlah catatan: {len(catatan)}")


def filter_per_mapel():
    """
    FITUR PENGEMBANGAN: Filter catatan berdasarkan mapel tertentu.
    Menampilkan catatan hanya untuk mapel yang dipilih.
    """
    print("\n" + "="*50)
    print("🔍 FILTER CATATAN PER MAPEL")
    print("="*50)
    
    # Cek apakah ada catatan
    if len(catatan) == 0:
        print("\n📭 Belum ada catatan belajar!")
        return
    
    # Dapatkan daftar mapel yang unik
    mapel_list = list(set(item['mapel'] for item in catatan))
    mapel_list.sort()
    
    print("\n📚 Daftar Mapel:")
    for i, mapel in enumerate(mapel_list, start=1):
        print(f"   {i}. {mapel}")
    
    try:
        pilihan = int(input("\nPilih nomor mapel: "))
        
        if 1 <= pilihan <= len(mapel_list):
            mapel_terpilih = mapel_list[pilihan - 1]
            catatan_mapel = [item for item in catatan if item['mapel'] == mapel_terpilih]
            
            print(f"\n📋 CATATAN UNTUK MAPEL: {mapel_terpilih}")
            print("-" * 50)
            print(f"{'No':<4} {'Topik':<25} {'Durasi':<8}")
            print("-" * 50)
            
            for i, item in enumerate(catatan_mapel, start=1):
                print(f"{i:<4} {item['topik']:<25} {item['durasi']:<8} menit")
            
            # Hitung total durasi untuk mapel tersebut
            total_mapel = sum(item['durasi'] for item in catatan_mapel)
            print("-" * 50)
            print(f"💡 Total waktu untuk {mapel_terpilih}: {total_mapel} menit")
            
        else:
            print("❌ Pilihan tidak valid!")
            
    except ValueError:
        print("❌ Masukkan angka yang valid!")


def menu_utama():
    """
    Fungsi untuk menampilkan menu utama dan mengelola pilihan pengguna.
    """
    while True:
        print("\n" + "="*50)
        print("📚 APLIKASI STUDY LOG")
        print("="*50)
        print("\n1. ➕ Tambah Catatan Belajar")
        print("2. 📋 Lihat Semua Catatan")
        print("3. ⏱️  Total Waktu Belajar")
        print("4. 🔍 Filter per Mapel")
        print("5. ❌ Keluar")
        print("\n" + "="*50)
        
        pilihan = input("Pilih menu (1-5): ").strip()
        
        if pilihan == '1':
            tambah_catatan()
        elif pilihan == '2':
            lihat_catatan()
        elif pilihan == '3':
            total_waktu()
        elif pilihan == '4':
            filter_per_mapel()
        elif pilihan == '5':
            print("\n👋 Terima kasih telah menggunakan Study Log!")
            print("   Semoga belajar Anda produktif! 💪\n")
            break
        else:
            print("\n❌ Pilihan tidak valid! Silakan pilih 1-5.")
        
        input("\nTekan ENTER untuk lanjut...")


# ================================
# JALANKAN PROGRAM
# ================================

if __name__ == "__main__":
    print("\n🎓 Selamat datang di APLIKASI STUDY LOG!")
    print("   Aplikasi untuk mencatat kegiatan belajar Anda\n")
    menu_utama()
