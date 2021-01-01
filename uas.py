import mysql.connector

conn = mysql.connector.connect(host="localhost",port=3306,user="root",password="",database="pbo")
cursor=conn.cursor()

class Admin:
    def __init__(self):
        pass
    def tambahPaket(self):
        adminInput = int(input("\tambah paket game\n1. Mobile Legends\n2. Free Fire\n3. PUBG\n4. back\ninput angka pilihan diatas : "))
        if adminInput == 1:
            paket = str(input("input paket baru : "))
            harga = str(input("input harga baru : "))
            jumlahDiamond = str(input("input lokasi buku baru : "))
            query = "insert into mobileLegends values('','{}','{}','{}')".format(paket,harga,jumlahDiamond)
            cursor.execute(query)
            conn.commit()
            print("\nberhasil menambahkan paket dengan data:\nnama paket : {}\nharga : {}\njumlah diamond : {}\n".format(paket,harga,jumlahDiamond))
        elif adminInput == 2:
            paket = str(input("input paket baru : "))
            harga = str(input("input harga baru : "))
            jumlahDiamond = str(input("input lokasi buku baru : "))
            query = "insert into freeFire values('','{}','{}','{}')".format(paket,harga,jumlahDiamond)
            cursor.execute(query)
            conn.commit()
            print("\nberhasil menambahkan paket dengan data:\nnama paket : {}\nharga : {}\njumlah diamond : {}\n".format(paket,harga,jumlahDiamond))
        elif adminInput == 3:
            paket = str(input("input paket baru : "))
            harga = str(input("input harga baru : "))
            jumlahDiamond = str(input("input lokasi buku baru : "))
            query = "insert into pubg values('','{}','{}','{}')".format(paket,harga,jumlahDiamond)
            cursor.execute(query)
            conn.commit()
            print("\nberhasil menambahkan paket dengan data:\nnama paket : {}\nharga : {}\njumlah diamond : {}\n".format(paket,harga,jumlahDiamond))
        elif adminInput == 4:
            return True #iki opo cokkk!

    def ubahPaket(self):
        adminInput = int(input("\ubah harga paket\n1. Mobile Legends\n2. Free Fire\n3. PUBG\n4. back\ninput angka pilihan diatas : "))
        if adminInput == 1:
            paket = str(input("input paket yang ingin dirubah : "))
            cekPaket = "select paket from mobileLegends where paket = '{}'".format(paket)
            cursor.execute(cekPaket)
            cekPaket = cursor.fetchall()
            print("\npaket ditemukan dengan harga :",cekPaket[0][0])
            
            adminInput = int(input("\nubah paket mobile legend berdasarkan\n1. paket\n2. harga\n3. jumlahDiamond\n4. back\ninput angka pilihan diatas : "))
                if adminInput == 1:
                    try:
                        paketBaru = str(input("input paket baru : "))
                        query = "update mobileLegends set paket = '{}' where paket = '{}'".format(paketBaru,paket)
                        cursor.execute(query)
                        conn.commit()
                        print("\ndata buku berhasil dirubah :)\n")

                    except:
                        print("\npaket tersebut tidak ada!\n")
                elif adminInput == 2:
                    try:
                        hargaBaru = str(input("input harga paket baru : "))
                        query = "update mobileLegends set harga = '{}' where harga = '{}'".format(hargaBaru,harga)
                        cursor.execute(query)
                        conn.commit()
                        print("\ndata buku berhasil dirubah :)\n")

                    except:
                        print("\nharga tersebut tidak ada!\n")
                elif adminInput == 3:
                    try:
                        jumlahDiamondBaru = str(input("input jumlah diamond baru : "))
                        query = "update mobileLgends set jumlahDiamond = '{}' where jumlahDiamond = '{}'".format(jumlahDiamondBaru,jumlahDiamond)
                        cursor.execute(query)
                        conn.commit()
                        print("\njumlah diamond berhasil dirubah :)\n")

                    except:
                        print("\njumlah diamond tersebut tidak ada!\n")

        elif adminInput == 2:
            paket = str(input("input paket yang ingin dirubah : "))
            cekPaket = "select paket from mobileLegends where paket = '{}'".format(paket)
            cursor.execute(cekPaket)
            cekPaket = cursor.fetchall()
            print("\npaket ditemukan dengan harga :",cekPaket[0][0])
            
            adminInput = int(input("\nubah paket mobile legend berdasarkan\n1. paket\n2. harga\n3. jumlahDiamond\n4. back\ninput angka pilihan diatas : "))
                if adminInput == 1:
                    try:
                        paketBaru = str(input("input paket baru : "))
                        query = "update mobileLegends set paket = '{}' where paket = '{}'".format(paketBaru,paket)
                        cursor.execute(query)
                        conn.commit()
                        print("\ndata buku berhasil dirubah :)\n")

                    except:
                        print("\npaket tersebut tidak ada!\n")
                elif adminInput == 2:
                    try:
                        hargaBaru = str(input("input harga paket baru : "))
                        query = "update mobileLegends set harga = '{}' where harga = '{}'".format(hargaBaru,harga)
                        cursor.execute(query)
                        conn.commit()
                        print("\ndata buku berhasil dirubah :)\n")

                    except:
                        print("\nharga tersebut tidak ada!\n")
                elif adminInput == 3:
                    try:
                        jumlahDiamondBaru = str(input("input jumlah diamond baru : "))
                        query = "update mobileLgends set jumlahDiamond = '{}' where jumlahDiamond = '{}'".format(jumlahDiamondBaru,jumlahDiamond)
                        cursor.execute(query)
                        conn.commit()
                        print("\njumlah diamond berhasil dirubah :)\n")

                    except:
                        print("\njumlah diamond tersebut tidak ada!\n")
        elif adminInput == 4:
            return True
    def rekapPengunjung(self):
        query = "select idMahasiswa,namaLengkap,username,email,bukuPinjamJudul,bukuPinjamPenulis,bukuPinjamLokasi from dataMahasiswa"
        cursor.execute(query)
        dataMahasiswa = cursor.fetchall()
        for i in dataMahasiswa:
            print(i)


    def cariBuku(self):
        userInput = int(input("\n1. cari buku berdasarkan id\n2. cari buku berdasarkan judul\n3. cari buku berdasarkan lokasi\n4. back\ninput angka pilihan diatas : "))

        if userInput == 1:
            inputBuku = int(input("masukan id buku : "))
            query = "select * from buku where idBuku = {}".format(inputBuku)
            cursor.execute(query)
            try:
                dataBuku = cursor.fetchall()[0]
                print("\nid buku :",dataBuku[0])
                print("judul :",dataBuku[1])
                print("penulis buku :",dataBuku[2])
                print("lokasi buku :",dataBuku[3])
            except:
                print("\nid buku tidak ditemukan") 
        elif userInput == 2:
            inputBuku = str(input("masukan judul buku : "))
            query = "select * from buku where judul = '{}'".format(inputBuku)
            cursor.execute(query)
            try:
                dataBuku = cursor.fetchall()[0]
                print("\nid buku :",dataBuku[0])
                print("judul :",dataBuku[1])
                print("penulis buku :",dataBuku[2])
                print("lokasi buku :",dataBuku[3])
            except:
                print("\njudul buku tidak ditemukan") 
        elif userInput == 3:
            inputBuku = str(input("masukan lokasi buku : "))
            query = "select * from buku where lokasi = '{}'".format(inputBuku)
            cursor.execute(query)
            try:
                dataBuku = cursor.fetchall()[0]
                print("\nid buku :",dataBuku[0])
                print("judul :",dataBuku[1])
                print("penulis buku :",dataBuku[2])
                print("lokasi buku :",dataBuku[3])
            except:
                print("\nlokasi tidak ditemukan") 

        elif userInput == 4:
            return True

def login():
    for i in range(3):
        username = str(input("masukan username : "))
        if username == "admin": #sek bingung cokkkk
            return "admin"
        password = str(input("masukan password : "))
        query = "select pbo from login where username = '{}' and password = '{}'".format(username,password)
        cursor.execute(query)   
        data = cursor.fetchall()

        try:
            id = data[0][0]
            return id
        except:
            print("username atau password yang anda masukan salah")
    print("\nanda telah gagal login sebanyak 3 kali")

def programBerjalan():
    while True:
        main = int(input("\n1. admin\n2. pengunjung\n3. exit\npilih nomor, anda sebagai : "))
        if main == 1:
            id = login()
            if id == "admin":
                admin = Admin
                while True:
                    adminInput = int(input("\n1. tambah paket\n2. ubah paket\n3. cari game\n4. melihat rekap pembeli\n5. logout\ninput angka pilihan diatas : "))
                    if adminInput == 1:
                        admin.tambahPaket("tambah paket")
                    elif adminInput == 2:
                        admin.ubahPaket("ubah paket")
                    elif adminInput == 3:
                        admin.cariGame("cari game")
                    elif adminInput == 4:
                        admin.rekapPembeli("rekap pembeli")
                    elif adminInput == 5:
                        programBerjalan()
            else:
                print("Maaf, id password admin salah blok!!!!")
                    
        elif main == 2:
            userInput = int(input("\n1. beli paket\n2. exit\ninput angka pilihan diatas : "))
                    if userInput == 1:
                        pengunjung.beliPaket()
                    elif userInput == 2:
                        programBerjalan()
        elif main == 3:
            exit("selamat datang kembali :)")
        else:
            print("pilihan tidak tersedia")

programBerjalan()