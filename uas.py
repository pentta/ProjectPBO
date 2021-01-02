import mysql.connector

conn = mysql.connector.connect(
  host="localhost",
  port="3306",
  user="root",
  password="",
  database="pbo"
)
cursor=conn.cursor()
if conn.is_connected():
  print("Berhasil terhubung ke database")

class Admin:
    def __init__(self):
        pass

    def tambahPaket(self):
        adminInput = int(input("\tambah paket game\n1. Mobile Legends\n2. Free Fire\n3. PUBG\n4. back\ninput angka pilihan diatas : "))
        if adminInput == 1:
            paket = str(input("input paket baru : "))
            harga = str(input("input harga baru : "))
            jumlahDiamond = str(input("input jumlah diamond baru : "))
            query = "insert into mobilelegend values('{}','{}','{}')".format(paket,harga,jumlahDiamond)
            cursor.execute(query)
            conn.commit()
            print("\nberhasil menambahkan paket dengan data:\nnama paket : {}\nharga : {}\njumlah diamond : {}\n".format(paket,harga,jumlahDiamond))
        
        elif adminInput == 2:
            paket = str(input("input paket baru : "))
            harga = str(input("input harga baru : "))
            jumlahDiamond = str(input("input jumlah diamond baru : "))
            query = "insert into freefire values('{}','{}','{}')".format(paket,harga,jumlahDiamond)
            cursor.execute(query)
            conn.commit()
            print("\nberhasil menambahkan paket dengan data:\nnama paket : {}\nharga : {}\njumlah diamond : {}\n".format(paket,harga,jumlahDiamond))
        
        elif adminInput == 3:
            paket = str(input("input paket baru : "))
            harga = str(input("input harga baru : "))
            jumlahDiamond = str(input("input jumlah diamond baru : "))
            query = "insert into pubg values('{}','{}','{}')".format(paket,harga,jumlahDiamond)
            cursor.execute(query)
            conn.commit()
            print("\nberhasil menambahkan paket dengan data:\nnama paket : {}\nharga : {}\njumlah diamond : {}\n".format(paket,harga,jumlahDiamond))
        
        elif adminInput == 4:
            return True

    def ubahPaket(self):
        adminInput = int(input("ubah harga paket\n1. Mobile Legends\n2. Free Fire\n3. PUBG\n4. back\ninput angka pilihan diatas : "))
        
        if adminInput == 1:
            paket = str(input("input paket yang ingin dirubah : "))
            cekPaket = "select paket from mobilelegend where paket = '{}'".format(paket)
            cursor.execute(cekPaket)
            cekPaket = cursor.fetchall()
            print("\npaket ditemukan dengan harga :",cekPaket[0][0])
            adminInput = int(input("\nubah paket mobile legend berdasarkan\n1. paket\n2. harga\n3. jumlahDiamond\n4. back\ninput angka pilihan diatas : "))                
                
            if adminInput == 1:
                try:
                    paketBaru = str(input("input paket baru : "))
                    query = "update mobilelegend set paket = '{}' where paket = '{}'".format(paketBaru,paket)
                    cursor.execute(query)
                    conn.commit()
                    print("\ndata paket berhasil dirubah :)\n")

                except:
                    print("\npaket tersebut tidak ada!\n")
                
            elif adminInput == 2:
                try:
                    hargaBaru = str(input("input harga paket baru : "))
                    query = "update mobilelegend set harga = '{}' where harga = '{}'".format(hargaBaru,harga)
                    cursor.execute(query)
                    conn.commit()
                    print("\ndata paket berhasil dirubah :)\n")

                except:
                    print("\nharga tersebut tidak ada!\n")
                
            elif adminInput == 3:
                try:
                    jumlahDiamondBaru = str(input("input jumlah diamond baru : "))
                    query = "update mobilelegend set jumlahDiamond = '{}' where jumlahDiamond = '{}'".format(jumlahDiamondBaru,jumlahDiamond)
                    cursor.execute(query)
                    conn.commit()
                    print("\njumlah diamond berhasil dirubah :)\n")

                except:
                    print("\njumlah diamond tersebut tidak ada!\n")

        elif adminInput == 2:
            paket = str(input("input paket yang ingin dirubah : "))
            cekPaket = "select paket from freefire where paket = '{}'".format(paket)
            cursor.execute(cekPaket)
            cekPaket = cursor.fetchall()
            
            print("\npaket ditemukan dengan harga :",cekPaket[0][0])
            
            adminInput = int(input("\nubah paket free fire berdasarkan\n1. paket\n2. harga\n3. jumlahDiamond\n4. back\ninput angka pilihan diatas : "))
                
            if adminInput == 1:
                try:
                    paketBaru = str(input("input paket baru : "))
                    query = "update freefire set paket = '{}' where paket = '{}'".format(paketBaru,paket)
                    cursor.execute(query)
                    conn.commit()
                    print("\ndata paket berhasil dirubah :)\n")

                except:
                    print("\npaket tersebut tidak ada!\n")
                
            elif adminInput == 2:
                try:
                    hargaBaru = str(input("input harga paket baru : "))
                    query = "update freefire set harga = '{}' where harga = '{}'".format(hargaBaru,harga)
                    cursor.execute(query)
                    conn.commit()
                    print("\ndata paket berhasil dirubah :)\n")

                except:
                    print("\nharga tersebut tidak ada!\n")
                
            elif adminInput == 3:
                try:
                    jumlahDiamondBaru = str(input("input jumlah diamond baru : "))
                    query = "update freefire set jumlahDiamond = '{}' where jumlahDiamond = '{}'".format(jumlahDiamondBaru,jumlahDiamond)
                    cursor.execute(query)
                    conn.commit()
                    print("\njumlah diamond berhasil dirubah :)\n")

                except:
                    print("\njumlah diamond tersebut tidak ada!\n")
        
        elif adminInput == 3:
            paket = str(input("input paket yang ingin dirubah : "))
            cekPaket = "select paket from pubg where paket = '{}'".format(paket)
            cursor.execute(cekPaket)
            cekPaket = cursor.fetchall()
            print("\npaket ditemukan dengan harga :",cekPaket[0][0])
            
            adminInput = int(input("\nubah paket pubg berdasarkan\n1. paket\n2. harga\n3. jumlahDiamond\n4. back\ninput angka pilihan diatas : "))
                
            if adminInput == 1:
                try:
                    paketBaru = str(input("input paket baru : "))
                    query = "update pubg set paket = '{}' where paket = '{}'".format(paketBaru,paket)
                    cursor.execute(query)
                    conn.commit()
                    print("\ndata paket berhasil dirubah :)\n")

                except:
                    print("\npaket tersebut tidak ada!\n")
                
            elif adminInput == 2:
                try:
                    hargaBaru = str(input("input harga paket baru : "))
                    query = "update pubg set harga = '{}' where harga = '{}'".format(hargaBaru,harga)
                    cursor.execute(query)
                    conn.commit()
                    print("\ndata paket berhasil dirubah :)\n")

                except:
                    print("\nharga tersebut tidak ada!\n")
            
            elif adminInput == 3:
                try:
                    jumlahDiamondBaru = str(input("input jumlah diamond baru : "))
                    query = "update pubg set jumlahDiamond = '{}' where jumlahDiamond = '{}'".format(jumlahDiamondBaru,jumlahDiamond)
                    cursor.execute(query)
                    conn.commit()
                    print("\njumlah diamond berhasil dirubah :)\n")

                except:
                    print("\njumlah diamond tersebut tidak ada!\n")
    
        elif adminInput == 4:
            return True

class pengunjung:
    def __init__(self):
        pass

    def beliPaket(self):
        userInput = int(input("1. mobile legend \n2. free fire \n3. pubg \npilih game"))
        if userInput == 1:
            query = "select * from mobilelegend"
            cursor.execute(query)
            dataGame = cursor.fetchall()
            nomorindex = 1
            for i in dataGame:
                print(nomorindex,i)
                nomorindex +=1
            pilihanUser = int(input("input pilihan paket diatas"))
            namaPembeli = str(input("masukan nama anda "))
            if pilihanUser == 1:
                print ("Transaksis berhasil \nnama pembeli = {}\ndata game = {}".format(namaPembeli,dataGame[0]))
                query="insert into struk values ('{}','{}','{}','{}')".format(namaPembeli,dataGame[0][0],dataGame[0][1],dataGame[0][2])
                cursor.execute(query)
                conn.commit
            if pilihanUser == 2:
                print ("Transaksis berhasil \nnama pembeli = {}\ndata game = {}".format(namaPembeli,dataGame[1]))
                query="insert into struk values ('{}','{}','{}','{}')".format(namaPembeli,dataGame[1][0],dataGame[1][1],dataGame[1][2])
                cursor.execute(query)
                conn.commit
            if pilihanUser == 3:
                print ("Transaksis berhasil \nnama pembeli = {}\ndata game = {}".format(namaPembeli,dataGame[2]))
                query="insert into struk values ('{}','{}','{}','{}')".format(namaPembeli,dataGame[2][0],dataGame[2][1],dataGame[2][2])
                cursor.execute(query)
                conn.commit

        if userInput == 2:
            query = "select * from freefire"
            cursor.execute(query)
            dataGame = cursor.fetchall()
            nomorindex = 1
            for i in dataGame:
                print(nomorindex,i)
                nomorindex +=1
            pilihanUser = int(input("input pilihan paket diatas"))
            namaPembeli = str(input("masukan nama anda "))
            if pilihanUser == 1:
                print ("Transaksis berhasil \nnama pembeli = {}\ndata game = {}".format(namaPembeli,dataGame[0]))
                query="insert into struk values ('{}','{}','{}','{}')".format(namaPembeli,dataGame[0][0],dataGame[0][1],dataGame[0][2])
                cursor.execute(query)
                conn.commit
            if pilihanUser == 2:
                print ("Transaksis berhasil \nnama pembeli = {}\ndata game = {}".format(namaPembeli,dataGame[1]))
                query="insert into struk values ('{}','{}','{}','{}')".format(namaPembeli,dataGame[1][0],dataGame[1][1],dataGame[1][2])
                cursor.execute(query)
                conn.commit
            if pilihanUser == 3:
                print ("Transaksis berhasil \nnama pembeli = {}\ndata game = {}".format(namaPembeli,dataGame[2]))
                query="insert into struk values ('{}','{}','{}','{}')".format(namaPembeli,dataGame[2][0],dataGame[2][1],dataGame[2][2])
                cursor.execute(query)
                conn.commit

        if userInput == 3:
            query = "select * from pubg"
            cursor.execute(query)
            dataGame = cursor.fetchall()
            nomorindex = 1
            for i in dataGame:
                print(nomorindex,i)
                nomorindex +=1
            pilihanUser = int(input("input pilihan paket diatas"))
            namaPembeli = str(input("masukan nama anda "))
            if pilihanUser == 1:
                print ("Transaksis berhasil \nnama pembeli = {}\ndata game = {}".format(namaPembeli,dataGame[0]))
                query="insert into struk values ('{}','{}','{}','{}')".format(namaPembeli,dataGame[0][0],dataGame[0][1],dataGame[0][2])
                cursor.execute(query)
                conn.commit
            if pilihanUser == 2:
                print ("Transaksis berhasil \nnama pembeli = {}\ndata game = {}".format(namaPembeli,dataGame[1]))
                query="insert into struk values ('{}','{}','{}','{}')".format(namaPembeli,dataGame[1][0],dataGame[1][1],dataGame[1][2])
                cursor.execute(query)
                conn.commit
            if pilihanUser == 3:
                print ("Transaksis berhasil \nnama pembeli = {}\ndata game = {}".format(namaPembeli,dataGame[2]))
                query="insert into struk values ('{}','{}','{}','{}')".format(namaPembeli,dataGame[2][0],dataGame[2][1],dataGame[2][2])
                cursor.execute(query)
                conn.commit

def login():
    for i in range(3):
        username = str(input("masukan username : "))
        password = str(input("masukan password : "))
        query = "select * from login where Username = '{}' and Password = '{}'".format(username,password)
        cursor.execute(query)   
        data = cursor.fetchall()
        try:
            id = data[0][0]
            return "admin"
        except:
            print("username atau password yang anda masukan salah")
    print("\nanda telah gagal login sebanyak 3 kali")

def programBerjalan():
    while True:
        main = int(input("\n1. admin\n2. pengunjung\n3. exit\npilih nomor, anda sebagai : "))
        if main == 1:
            id = login()
            print (id)
            if id == "admin":
                admin = Admin()
                while True:
                    adminInput = int(input("\n1. tambah paket\n2. ubah paket\n3. logout\ninput angka pilihan diatas : "))
                    if adminInput == 1:
                        admin.tambahPaket()
                    elif adminInput == 2:
                        admin.ubahPaket()
                    elif adminInput == 3:
                        programBerjalan()
            else:
                print("Maaf, id password admin salah!!!!")
                    
        elif main == 2:
            user=pengunjung()
            userInput = int(input("\n1. beli paket\n2. exit\ninput angka pilihan diatas : "))
            if userInput == 1:
                pengunjung.beliPaket("belipaket")
            elif userInput == 2:
                programBerjalan()
        elif main == 3:
            exit("selamat datang kembali :)")
        else:
            print("pilihan tidak tersedia")

programBerjalan()