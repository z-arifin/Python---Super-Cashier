import pandas as pd

#Objek class Transaksi
class Transaction:  
    def __init__(self):
        '''Fungsi inisialisasi awal untuk input attribusi dari class.
        
        Attribute/Parameters:
        transaction : item dan kuantitas yang diinput melalui fungsi
        payment : kalkulasi pembayaran berdasarkan harga item (total price dan total payment)
        '''
        self.transaction = {}
        self.payment = {}

    def add_item(self, item, qty, price):
        '''Fungsi untuk menambahkan item-item yang ingin dibeli.
        Attribute/Parameters:
        item : nama item yang ditambahkan ke daftar pesanan
        qty : jumlah/kuantitas item 
        price : harga per item
        total : perhitungan jumlah dan harga item
       
        Print:
        Tampilkan informasi data item, jumlah, dan harga telah berhasil diinput ke transaction
        '''
        self.total = qty*price
        self.transaction.update({item:[qty, price, self.total]})
        self.payment.update({item: qty*price})
        print(f'Pesanan {item} - {qty} x Rp. {price} = {self.total} telah dipesan')

    def update_item_name(self, item, new_item):
        '''Fungsi yang digunakan untuk memperbarui nama item.
        Attribute/Parameters:
        item (string): nama item yang telah diinput. 
        new_item (string): nama item baru yang akan menggantikan nama item sebelumnya
        
        Print:
        Tampilkan update informasi data nama item
        '''
        update_name = self.transaction[item]
        self.transaction.pop(item)
        self.transaction.update({new_item: update_name})
        self.payment.pop(item)
        self.payment.update({new_item:self.transaction[new_item][0]*self.transaction[new_item][1] })
        print(f'Pesanan {item} berhasil diupdate menjadi {new_item}')

    def update_item_qty(self, item, new_qty):
        '''Fungsi yang digunakan untuk memperbarui jumlah item.
        Attribute/Parameters:
        item (string): nama item yang telah diinput/diupdate
        new_qty (int): jumlah item baru yang akan menggantikan jumlah item sebelumnya
        Print:
        Tampilkan update informasi data jumlah item
        '''
        self.transaction[item][0] = new_qty
        self.transaction[item][2] = new_qty*self.transaction[item][1]
        self.payment[item] = self.transaction[item][0]*self.transaction[item][1]
        print(f'Jumlah pesanan {item} berhasil diupdate dari {self.transaction[item][0]} menjadi {new_qty}')

        
    def update_item_price(self, item, new_price):
        '''Fungsi yang digunakan untuk memperbarui harga item.
        Attribute/Parameters:
        item (string): nama item yang telah diinput/diupdate
        new_price (int): harga item yang akan menggantikan harga item sebelumnya
        Print:
        Tampilkan update informasi data harga item
        '''
        self.transaction[item][1] = new_price
        self.transaction[item][2] = self.transaction[item][0]*new_price
        self.payment[item] = self.transaction[item][0]*self.transaction[item][1]
        print(f'Harga pesanan {item} berhasil diupdate dari {self.transaction[item][1]} menjadi Rp. {new_price}')

    
    def delete_item(self, item):
        ''' Fungsi untuk mengeluarkan salah satu item dari dalam transaction.
        Attribute/Parameters:
        item (string): nama item yang akan didelete dari transaction
        Print:
        Tampilkan bahwa item telah berhasil dikeluarkan dari transaction
        '''
        self.transaction.pop(item)
        print(f'{item} telah didelete dari pesanan')

    def reset_transaction(self):
        ''' Fungsi untuk mengeluarkan/ mengdelete seluruh item di dalam transaction.
        Print:
        Tampilkan reset telah berhasil dilakukan
        '''
        self.transaction.clear()
        print(f'Data pesanan telah direset, semua data pesanan telah dihapus')

    def check_order(self):
        ''' Fungsi untuk memeriksa masing-masing item telah memiliki data yang benar.
        Print:
        1. Terdapat 3 kondisi:
            - Jika terdapat value yang masih bernilai nol, tampilkan informasi nama item tersebut
            - Jika value sudah benar, tampilkan informasi bahwa item sudah benar
            - Jika belum ada item, tampilkan informasi transaction masih kosong
        2. Tabel order dan beberapa keterangannya
        '''
        try:
            shopping_cart = pd.DataFrame(self.transaction).T # untuk create table order
            shopping_cart.columns = ['Jumlah Item','Harga per Item','Harga Pesanan']
            print('Pastikan seluruh item pesanan sudah benar sebelum melanjutkan transaksi!')
            print('=====DATA PESANAN=====') 
            for item, value in self.transaction.items():
                if value[0] == 0 or value[1] == 0:
                    print(f'Terdapat Kesalahan input pada data {item}!')
                    print('Note: Harga dan Jumlah Item tidak boleh = 0')
               
                else:
                    print(f'Data {item} Sudah Benar')
                
            print(shopping_cart.to_markdown())
            
        except ValueError:
            print('Pesanan Anda Masih Kosong')

    def total_price(self):
        ''' Fungsi untuk menghitung total price dari item yang telah ditambahkan di transaction
        Print:
        1. Ketika item belum ditambahkan, tampilkan informasi transaction masih kosong
        2. Ketika item telah ditambahkan, tampilkan informasi total price 
        '''
        self.total_order = sum(self.payment.values())
        if self.total_order == 0:
            print('Pesanan Anda Masih Kosong')
        else:
            print(f'Harga Seluruh Item Pesanan Adalah Rp {self.total_order}')

    def total_payment(self):
        ''' Fungsi untuk menghitung total bayar dari item yang telah ditambahkan di transaction dengan mengurangi total price dengan diskon.
        Diskon rules:
        5% jika total belanja lebih dari 20000
        8% jika total belanja lebih dari 30000
        10% jika total belanja lebih dari 50000
        Selain dari rules diatas tidak mendapatkan diskon
        Print:
        Tampilkan diskon yang diperoleh dan total bayar setelah diskon
        '''
        self.total_order = sum(self.payment.values())
        if self.total_order > 200000 and self.total_order <= 300000:
            discount = (5/100)
            print(f'Anda mendapatkan diskon sebesar 5%')
        elif self.total_order > 300000 and self.total_order <= 500000:
            discount = (8/100)
            print(f'Anda mendapatkan diskon sebesar 8%')
        elif self.total_order > 500000:
            discount = (10/100)
            print(f'Anda mendapatkan diskon sebesar 10%')
        else:
            discount = 0
            print(f'Anda belum mendapatkan diskon')

        bayar = self.total_order - (self.total_order*discount)
        print(f'Biaya Total Pesanan Seharga Rp. {bayar}')