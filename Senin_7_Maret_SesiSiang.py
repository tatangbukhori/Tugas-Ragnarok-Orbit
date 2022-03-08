from abc import abstractmethod, ABC

# OOP1 (Class : Hewan)
# Abstraction
class abstract(ABC):
    def fact(ini):
        print("Ini adalah hewan")
        
    #AbstractMethod
    @abstractmethod
    def harga_hewan(ini, x):
        pass

#Encapsulation
class Hewan(object):
    def __init__(ini, nama, usia, jenis, mamalia):
        ini.nama = nama
        ini.usia = usia
        ini.jenis = jenis
        ini.mamalia = mamalia
    
    def tidur(ini, durasi):
        for x in range(durasi):
            print("ddrrr... ddrrr...")
        
    def info_hewan(ini):
        print(f"nama: {ini.nama}, usia: {ini.usia}, jenis: {ini.jenis}, mamalia: {ini.mamalia}")
        
#Inheritance
class Ayam(Hewan):
    def __init__(ini, nama, usia, jenis, mamalia, warna, jenis_ayam, jenis_hewan):
        super().__init__(nama, usia, jenis, mamalia)
        ini.warna = warna
        ini.jenis_ayam = jenis_ayam
        ini.jenis_hewan = jenis_hewan
    
    def suara(ini):
        super().tidur(2)
        print("kukuruyuk...")
        
    def harga_hewan(ini, x): # Abstract method
        print("Harga ayam ini adalah Rp", x)
    
    def info_ayam(ini):
        super().info_hewan()
        print(f"warna: {ini.warna}, jenis ayam: {ini.jenis_ayam}, jenis hewan: {ini.jenis_hewan}")

# Polymorphism
class Burung(Hewan):
    def __init__(ini, nama, usia, jenis, mamalia, warna):
        super().__init__(nama, usia, jenis, mamalia)
        ini.warna = warna
        
    def harga_hewan(ini, x): # abstract method
        print("Harga burung ini adalah Rp", x)
    
    def makan_jagung(ini, sendok_teh):
        if sendok_teh >=3 :
            print("Kenyang...")
        else:
            print("Lapar...")
            
    def info_burung(ini):
        super().info_hewan()
        print("warna: ", ini.warna)


# OOP2 (Class : Barang)
# Abstraction
class abstract2(ABC):
    def desc(self):
        print("Ini adalah barang")
        
    #AbstractMethod
    @abstractmethod
    def harga_barang(self, x):
        pass
    
class barang_random(abstract2):
    def __init__(self, nama, jenis):
        self.nama = nama
        self.jenis = jenis
    def harga_barang(self, x):
        print("Harga barang ini adalah Rp", x)
    def info_barang_rndm(self):
        print(f"nama barang: {self.nama}, jenis barang: {self.jenis}")

# Encapsulation
class Barang(object):
    def __init__(self, nama, warna, jenis):
        self.nama = nama
        self.warna = warna
        self.jenis = jenis
    def info_barang(self):
        print(f"nama barang: {self.nama}, warna: {self.warna}, jenis: {self.jenis}")

# Inheritance
class TV(Barang):
    def __init__(self, nama, warna, jenis, garansi, merk):
        super().__init__(nama, warna, jenis)
        self.garansi = garansi
        self.merk = merk
        
    def harga_barang(self, x): # Abstract method
        print("Harga TV ini adalah Rp", x)
        
    def ukuran_tv(self, inch):
        print("Ukuran TV:", inch, "Inch")
        
    def info_tv(self):
        super().info_barang()
        print(f"Mempunyai garansi: {self.garansi}, merk: {self.merk}")

# Polymorphism
class Lemari(Barang):
    def __init__(self, nama, warna, jenis, garansi, merk, bahan):
        super().__init__(nama, warna, jenis)
        self.garansi = garansi
        self.merk = merk
        self.bahan = bahan
        
    def harga_barang(self, x): # Abstract method
        print("Harga lemari ini adalah Rp", x)
        
    def info_lemari(self):
        super().info_barang()
        print(f"garansi: {self.garansi}, merk: {self.merk}, bahan: {self.bahan}")

# OOP3 (CLass : Kendaraan)
# Abstraction
class abstract3(ABC):
    def harga_kendaraan(self, x):
        print("Harga: Rp", x)
        
    #AbstractMethod
    @abstractmethod
    def bahan_bakar(self, x):
        pass
    
class kendaraan_random(abstract3):
    def __init__(self, nama, jenis):
        self.nama = nama
        self.jenis = jenis
    def bahan_bakar(self, x):
        print("Bahan bakar kendaraan ini adalah", x)
    def info_kendaraan_rndm(self):
        print(f"nama barang: {self.nama}, jenis barang: {self.jenis}")

# Encapsulation
class Kendaraan(object):
    def __init__(self, nama, warna, jenis):
        self.nama = nama
        self.warna = warna
        self.jenis = jenis
    def info_kendaraan(self):
        print(f"nama barang: {self.nama}, warna: {self.warna}, jenis: {self.jenis}")

# Inheritance
class Motor(Kendaraan):
    def __init__(self, nama, warna, jenis, roda, merk):
        super().__init__(nama, warna, jenis)
        self.roda = roda
        self.merk = merk
        
    def bahan_bakar(self, x):
        print("Bahan bakar kendaraan ini adalah", x)
        
    def cc_motor(self, cc):
        print("Motor ini", cc, "CC")
        
    def info_motor(self):
        super().info_kendaraan()
        print(f"mempunyai roda: {self.roda}, merk: {self.merk}")

# Polymorphism
class Truk(Kendaraan):
    def __init__(self, nama, warna, jenis, roda, merk, pajak):
        super().__init__(nama, warna, jenis)
        self.roda = roda
        self.merk = merk
        self.pajak = pajak
        
    def bahan_bakar(self, x): # Abstract method
        print("Bahan bakar kendaraan ini adalah", x)
    
    def muatan(self, x):
        print("Truk ini bermuatan:", x)
        
    def info_truk(self):
        super().info_kendaraan()
        print(f"mempunyai roda: {self.roda}, merk: {self.merk}, pajak aktif: {self.pajak}")