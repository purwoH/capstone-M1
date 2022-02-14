
# List data rental mobil

brandMob = ['Toyota', 'Honda', 'Daihatsu']
listMob = [['Avanza', 6, 200000], ['Rush', 2, 200000], ['Calya', 4, 200000], ['Fortuner', 2, 400000], ['Inova', 4, 400000], ['Alphard', 1, 800000], ['Xenia', 6, 200000], ['Terios', 4, 200000], ['Sigra', 2, 200000], ['Jazz', 4, 350000], ['Mobilio', 4, 350000], ['Brio', 6, 250000]]



# menambah pesanan dalam list keranjang belanja
cart = []

# memasukkan fungsi user input pada menu utama. Dan menggunakan while true 
while True : 
    
    # Menu Utama
    menuUtama = input('''
                      ***** SELAMAT DATANG DI RENTAL MOBIL ANUGERAH *****
                      
                 Kami menyediakan armada dengan kualitas terbaik dengan tahun muda
                 
                List menu : 
                
                1. Menampilkan daftar armada
                2. Menambahkan daftar armada
                3. Menghapus daftar armada
                4. Menyewa armada
                5. Exit
                
                # Masukkan pilihan menu yang ingin di jalankan :  ''')
    
    # # Looping untuk menjalankan menu 1
    if menuUtama == '1':
        
        # Menampilkan daftar armada
        print('\n\t\t\t\t *** Daftar Armada ***\n')

        for pul in range(len(listMob)):
            print(f"\t| Nama: {listMob[pul][0]} \t | Stok: {listMob[pul][1]} \t | Harga Rp {listMob[pul][2]}")    
         
    
    # Looping untuk menjalankan menu 2
    # Menambah item mobil ke dalam list
    elif menuUtama == '2' :
        while True:
            kataSandi = input('Masukkan kata sandi : ')
            if kataSandi != '4444':
                print('Kata Sandi yang anda masukkan salah')
                break
        # sandi = '4444'
        
            brand = input('Masukkan brand mobil tersebut. Toyota/Honda/Daihatsu : ')        
            mob = input('Masukkan nama mobil yang ingin anda tambahkan : ')
            stk = int(input('Masukkan jumlah stok mobil yang ingin anda tambahkan : '))
            price = int(input('Masukkan harga per hari mobil tersebut : '))
                
            listMob.append([mob, stk, price])
            break
    # # Looping untuk menjalankan menu 3    
    # # Menghapus item mobil di dalam list
    elif menuUtama == '3' :
        while True:
            kataSandi = input('Masukkan kata sandi : ')
            if kataSandi != '4444':
                print('Kata Sandi yang anda masukkan salah')
                break
            
            print('\n\t\t\t *** Daftar Armada ***\n')
            print('Index\t| Nama  \t| Stock\t| Harga')
        
            for pul in range(len(listMob)):
                print(f"{pul}\t| Nama: {listMob[pul][0]} \t | Stok: {listMob[pul][1]} \t | Harga Rp {listMob[pul][2]}")    
                
            hapusMob = int(input(f'Masukkan index yang ingin di hapus : '))
        
        # menghapus item mobil di dalam list
            del listMob[hapusMob]    
            break
            
    # menyewa brand armada yang diinginkan, jumlah armada dan berapa lama durasi penyewaan.
     
    if menuUtama == '4':        
        
        # Menampilkan daftar armada
        print('\n\t\t\t *** Daftar Armada ***\n')
        print(f'***** {brandMob} *****')
        print('Index\t| Nama  \t| Stock\t| Harga')
        
        for pul in range(len(listMob)):
            print(f"{pul} \t| Nama: {listMob[pul][0]} \t | Stok: {listMob[pul][1]} \t | Harga Rp {listMob[pul][2]}")    
        
        while True:
            sewaMob = int(input('Masukkan index armada yang ingin anda sewa : '))
            qtyMob = int(input('Masukkan jumlah armada yang ingin disewa : '))
            durSewa = int(input('Masukkan durasi hari penyewaan armada (hari): '))
            
            # jika qty sewa melebihi stok maka tidak masuk keranjang
            if qtyMob > listMob[sewaMob][1]:
                print(f'Stock tidak cukup, stock {listMob[sewaMob][0]} tinggal {listMob[sewaMob][1]}')
            
            # jika qty stok masih tersedia  
            else :
                cart.append([listMob[sewaMob][0], qtyMob, durSewa, listMob[sewaMob][2], sewaMob])

            # tampilan isi keranjang sewa armada
            print('Isi Cart :')
            print('Nama\t| Qty\t| Durasi\t | Harga')
            for pil in cart :
                print(f'{pil[0]}\t| {pil[1]}\t| {pil[2]}\t| {pil[3]}')
            
            # cek apakah mau tambah belanjaan
            tambahMob = input('Mau sewa yang lain? (Y/N) = ')
            
            # kalau 'ya' maka akan looping terus, kalau tidak ada lagi yang mau dibeli maka keluar dari sistem looping keanjang belanja
            if(tambahMob == 'N') :
                break
    
    
         # menampilkan daftar belanja
        print('Daftar Sewa :')
        print('Nama\t| Qty\t| Harga\t| Durasi\t | Total Harga')
        
        totalSewa = 0
        for item in cart :
            print(f'{item[0]}\t| {item[1]}\t| {item[2]}\t| {item[3]}\t | {item[1]* item[2] * item[3]} ')
            totalSewa += item[1] * item[2] * item[3] 
        
        # kalau uangnya kurang, maka
        while True :
            print(f'Total Yang Harus Dibayar = Rp {totalSewa}')
            byr = input('Bayar DP / FULL : ')
            if byr.lower() == 'dp':
                dp = int(input('Masukkan nominal uang muka anda Rp: '))
                print(dp)
            sistByr = int(input('Pilihlah metode pembayaran yang anda inginkan (Tunai (1) / Non Tunai (2)) : '))
            if (sistByr == 2):
                if byr.lower() == 'dp':
                    print(totalSewa)
                    sisaDp = totalSewa - dp
                    print(f'Sisa pembayaran anda sebesar Rp {sisaDp} dan waktu pelunasan sisa pembayaran ketika waktu pengembalian armada')
                    print('Terima kasih dan semoga selamat dalam perjalanan')
                    for item in cart :
                        listMob[item[4]][1] -= item[1]
                    cart.clear()
                    break
                elif byr.lower() == 'full':
                    print('Terima kasih dan semoga selamat dalam perjalanan')
                    for item in cart :
                        listMob[item[4]][1] -= item[1]
                    cart.clear()
                    break
                else:
                 print('Input yang anda masukkan salah')
            elif (sistByr == 1):
                if byr.lower() == 'dp':
                    print(totalSewa)
                    sisaDp = totalSewa - dp
                    print(f'Sisa pembayaran anda sebesar Rp {sisaDp} dan waktu pelunasan sisa pembayaran ketika waktu pengembalian armada')
                    print('Terima kasih dan semoga selamat dalam perjalanan')
                    for item in cart :
                        listMob[item[4]][1] -= item[1]
                    cart.clear()
                    break
                elif byr.lower() == 'full':
                    bayar = int(input('Masukkan jumlah uang Rp : '))

                    # uang yang dibayar lebih dari total harga
                    if(bayar > totalSewa) :
                        kembali = bayar - totalSewa
                        print(f'Terima kasih \n\nUang kembali anda Rp: {kembali}')
                        print('Hati-hati dijalan semoga selamat sampai tujuan')

                        for item in cart :
                         listMob[item[4]][1] -= item[1]
                        cart.clear()
                        break
        
                    # uang yang dibayar pas
                    elif (bayar == totalSewa) :
                        print('Terima kasih dan semoga selamat dalam perjalanan')
                        for item in cart :
                            listMob[item[4]][1] -= item[1]
                        cart.clear()
                        break

                    # uang kurang, maka nanti akan dilooping sampai bayar uangnya pas atau lebih
                    else :
                        kekurangan = totalSewa - bayar
                        print(f'Uang anda kurang sebesar Rp {kekurangan}')
                        print('Terima kasih dan semoga selamat dalam perjalanan')
                        for item in cart :
                            listMob[item[4]][1] -= item[1]
                        cart.clear()
                        break    
                else:
                 print('Input yang anda masukkan salah')    
            else:
                print('Input yang anda masukkan salah')     
        # # looping menu utama selesai, exit dari aplikasi
    elif menuUtama == '5':
        break 
            
        
            
            
                
            
        
        





