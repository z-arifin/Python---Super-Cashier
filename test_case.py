from super_cashier import Transaction
import pandas as pd

order = Transaction()

print('=============== SUPER CASHIER ================')
print('==============================================')

while(True): # Pilihan untuk action users
    print('Silahkan pilih proses transaksi anda')
    print('1. ADD ORDER')
    print('2. UPDATE ORDER')
    print('3. DELETE/RESET ORDER')
    print('4. CHECK ORDER')
    print('5. TOTAL PAYMENT')

    process = input('Masukkan nomor proses yang ingin anda lakukan:')

    if process == '1':
        #proses add item
        while(True):
            item = input('Input Nama Item = ')
            if item.strip():
                break
            print('Pastikan item anda telah diinput dan tidak kosong')
        while(True):
            try:
                qty = int(input('Masukkan Jumlah Item dalam format number = '))
                break
            except ValueError:
                print('Pastikan Jumlah Item diinput menggunakan format Number')
        while(True):
            try:
                price = int(input('Masukkan Harga per Item dalam format number (ex: 5000) = '))
                break
            except ValueError:
                print('Pastikan Harga per Item diinput menggunakan format Number')
        order.add_item(item, qty, price)

    elif process == '2':
        #proses update item
        while(True):
            update = input('Input nomor sesuai dengan pilihan data yang ingin diupdate (1.Nama Item/2.Jumlah Item/3.Harga Item/4.Stop)')

            if update == '1':
                #update item name
                while(True):
                    try:
                        item = input('Masukkan nama item yang ingin diupdate:')
                        new_item = input('Masukkan nama item yang baru:')
                        if new_item.strip():
                            order.update_item_name(item, new_item)
                            break
                    except KeyError:
                        print('Pastikan item yang ingin anda update tersedia ditransaction dan inputan baru tidak boleh kosong') 
                    break

            elif update == '2':
                #update quantity
                while(True):
                    try:
                        item = input('Masukkan nama item yang ingin diupdate:')
                        while(True):
                            try:
                                new_qty = int(input('Masukkan jumlah item yang baru:'))
                                break
                            except ValueError:
                                print('Anda belum memasukkan jumlah item yang baru, pastikan item baru tidak kosong')
                        order.update_item_qty(item, new_qty)
                        break
                    except KeyError:
                        print('Nama item yang anda input salah, Pastikan format nama item sesuai atau tambahkan item anda terlebih dahulu')
                    break

            elif update == '3':
                #update harga item
                while(True):
                    try:
                        item = input('Masukkan nama item yang ingin diupdate harganya:')
                        while(True):
                            try:
                                new_price = int(input('Masukkan harga item yang baru:'))
                                break
                            except ValueError:
                                print('Anda belum memasukkan harga item yang baru, pastikan masukkan tidak kosong')
                        order.update_item_price(item, new_price)
                        break
                    except KeyError:
                        print('Nama item yang anda input salah, Pastikan format nama item sesuai atau tambahkan item anda terlebih dahulu')
                    break

            elif update == '4':
                # stop proses update
                jawab = input('Apakah anda yakin untuk menghentikan proses update? (Yes/No)') 
                if jawab == 'No':
                    print('Kembali ke proses update')
                elif jawab == 'Yes':
                    break
                else:
                    print('Input anda tidak sesuai!, Proses update berhenti secara paksa')
                    break
            else:
                #Stop apabila user masukkan value yang lain
                print('Input anda tidak sesuai!, pastikan memasukkan pilihan sesuai petunjuk jawaban')

    elif process == '3':
        #proses delete item
        while(True):
            delete = input('Input nomor sesuai dengan pilihan format untuk hapus data (1.Delete/2.Reset/3.Cancel)')
            if delete == '1':
                #delete per item
                try:
                    item = input('Masukkan item yang ingin anda delete: ') 
                    order.delete_item(item)
                    break
                except KeyError:
                    print('Item yang ingin anda delete tidak tersedia di transaction anda!')
                    break
            elif delete == '2':
                #reset semua item
                order.reset_transaction()
                break
            elif delete == '3':
                #User tidak jadi mengdelete
                print('Anda kembali ke menu utama')
                break
            else:
                #Ulangi jika user salah masukkan
                print('Masukan anda tidak sesuai!, pastikan memasukkan pilihan sesuai petunjuk jawaban ')

    elif process == '4':
        #proses check order
        order.check_order() 

    elif process == '5':
        #proses untuk liat total belanja dan total cost
        order.total_price()
        
        option = input('Apakah Anda masih ingin menambahkan Item? (Yes/No)')
        if option == 'Yes':
            print('Silahkan tambahkan item anda sesuai petunjuk')
        elif option == 'No':
            order.total_payment()
            print('Silahkan Lakukan Pembayaran')
            print('Terima Kasih!')
            break
        else:
            print('Masukan anda tidak sesuai!, Kembali ke menu awal')

    else:
        #Jika user salah masukkan kembali ke pilihan awal
        print('Permintaan anda tidak dapat diproses!, Silahkan masukkan nomor proses yang anda inginkan dengan benar')
        