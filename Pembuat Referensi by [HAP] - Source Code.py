def blank():
    for i in range(100):
        print()

# Credit
print('''
Created by [HAP] 2022...
Reff akupintar.id/

=========================='''      )
input('PRESS ENTER')
blank()

filename = str(input('NEW FILE------\nBuat Nama File Baru!\nNama File: '))
filename = str(''.join([filename,'.txt']))
file = open(filename,'w')
input(f'Sukses membuat file {filename}!\nPRESS ENTER')

while True:
    # Menu
    print(f'''
Editing {filename}
Mau Buat Referensi Dari:
A. Buku
B. Makalah / Jurnal dsb.
C. Website / URL     
D. Keluar (Selesai dan Save)''' )
    
    pilihan = str.upper(input('Pilihanmu: '))
    blank()
    
    #Function dan hasilnya
    def title(title):
        title = title.split(' ')
        title = [str.capitalize(x) for x in title]
        title = ' '.join(title) 
        return title
    
    def nama(penulis):
        nfull = penulis.split(' ')
        num = 0
        for i in nfull:
            num += 1
        if num > 1:
            nawal = nfull[-1] ; nfull.remove(nfull[-1])
            nfull = ' '.join(nfull)
            penulis = str(f'{nawal}, {nfull}.')
            return penulis
        else:
            return str(f'{nfull[0]}.')
    
    def cetak(n,m):
        m = str.capitalize(m)
        print(f'{m}'.ljust(8,' '),':',n)
    
    def fbuku():
        print('''
REFERENSI DARI BUKU
===================='''          )
        judul = title(input('Judul: '))
        penulis1 = input('Penulis: '); penulis1 = ' '.join([str.capitalize(x) for x in penulis1.split(' ')])
        penulis = nama(penulis1)
        penerbit = title(input('Penerbit: '))
        kota = title(input('Kota Terbit: '))
        tahun = str(input('Tahun Terbit: '))
        print('\nDATA');cetak(judul,'judul');cetak(penulis1,'penulis');cetak(penerbit,'penerbit');cetak(kota,'kota');cetak(tahun,'tahun')
        hasil = str(f'{penulis} {tahun}. {judul}. {kota}: {penerbit}.')
        return hasil
    
    def fjurnal():
        print('''
REFERENSI DARI JURNAL
===================='''          )
        judul = title(input('Jurnal: '))
        artikel = title(input('Artikel: '))
        penulis1 = input('Penulis: '); penulis1 = ' '.join([str.capitalize(x) for x in penulis1.split(' ')])
        penulis = nama(penulis1)
        penerbit = title(input('Penerbit: '))
        kota = title(input('Kota Terbit: '))
        tahun = str(input('Tahun Terbit: '))
        print('\nDATA');cetak(judul,'jurnal');cetak(artikel,'artikel');cetak(penulis1,'penulis');cetak(penerbit,'penerbit');cetak(kota,'kota');cetak(tahun,'tahun')
        hasil = str(f'{penulis} {tahun}. "{artikel}" dalam {judul}. {kota}: {penerbit}')
        return hasil
        
    def furl():
        print('''
REFERENSI DARI WEBSITE
===================='''          )
        judul = title(input('Judul: '))
        penulis1 = input('Penulis: '); penulis1 = ' '.join([str.capitalize(x) for x in penulis1.split(' ')])
        penulis = nama(penulis1)
        tahun = str(input('Tahun Terbit: '))
        print('\n*URL di-copy dari browser anda!')
        url = str(input('URL: '))
        print('\n*Contoh mengisi Waktu Tayang:\n10 Februari 2016 pukul 10.27')
        tayang = str(input('Waktu Tayang: '))
        print('\nDATA');cetak(judul,'judul');cetak(penulis1,'penulis');cetak(tahun,'tahun');cetak(tayang,'diakses');cetak(url,'alamat')
        hasil = str(f'{penulis} {tahun}. "{judul}", {url}, diakses pada {tayang}.')
        return hasil
    
    if pilihan == 'A':
        hasil = fbuku()
        print(f'\nHASIL:\n{hasil}')
        
    elif pilihan == 'B':
        hasil = fjurnal()
        print(f'\nHASIL:\n{hasil}')
        
    elif pilihan == 'C':
        hasil = furl()
        print(f'\nHASIL:\n{hasil}')
        
    elif pilihan == 'D':
        hasil = ''
        break
        
    file.write(f'\n\n{hasil}')
    input(f'\nDisave di {filename}\nPRESS ENTER')
    blank()

file.close()
blank()
input('Terimakasih!\n\nEND OF CODE~\nPRESS ENTER!')


