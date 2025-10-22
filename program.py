if __name__ =='__main__':

    baslik = 'Ogrenci Bilgi Sistemi (v1)'

    print(baslik)
    print(len(baslik))

    print('-' * 100)
    print(f'| {baslik:^94} |x|')
    print('-' * 100)
     
    ogrenci_adlari = []
    ogrenci_soyadlari = []
    ogrenci_nuamaralari = []

    ogrenci_adlari.append(input('1.ogrencinin adini giriniz:'))       #0.indeks
    ogrenci_soyadlari.append(input('1.ogrencinin soyadini giriniz:')) #0.indeks
    ogrenci_nuamaralari.append(input('1.ogrencinin numaranizi giriniz:')) #0.indeks

    ogrenci_adlari.append(input('2.ogrencinin adini giriniz:'))      #1.indeks
    ogrenci_soyadlari.append(input('2.ogrencinin soyadini giriniz:')) #1.indeks
    ogrenci_nuamaralari.append(input('2.ogrencinin numaranizi giriniz:')) #1.indeks

    ogrenci_adlari.append(input('3.ogrencinin adini giriniz:'))      #2.indeks
    ogrenci_soyadlari.append(input('3.ogrencinin soyadini giriniz:')) #2.indeks
    ogrenci_nuamaralari.append(input('3.ogrencinin numaranizi giriniz:')) #2.indeks
    
    print('-' * 100)
    
    print(f'|{' '*9}| {"Isim":<35} | {"Soyisim":<25} | {"Numara":<20} |')
    print('-' * 100)
    print(f'| {1:>7d} | {ogrenci_adlari[0]:<35} | {ogrenci_soyadlari[0]:<25} | {ogrenci_nuamaralari[0]:<20} |')
    print(f'| {2:>7d} | {ogrenci_adlari[1]:<35} | {ogrenci_soyadlari[1]:<25} | {ogrenci_nuamaralari[1]:<20} |')
    print(f'| {3:>7d} | {ogrenci_adlari[2]:<35} | {ogrenci_soyadlari[2]:<25} | {ogrenci_nuamaralari[2]:<20} |')







