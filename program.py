if __name__ =='__main__':

    baslik = 'Ogrenci Bilgi Sistemi (v1)'

    print(baslik)
    print(len(baslik))

    print('-' * 100)
    print(f'| {baslik:^94} |x|')
    print('-' * 100)
    

    ogrenci1_adi = input('1.ogrencinin adini giriniz:')
    ogrenci1_soyadi = input('1.ogrencinin soyadini giriniz:')
    ogrenci1_numarasi = input('1.ogrencinin numaranizi giriniz:')
    
    ogrenci2_adi = input('2.ogrencinin adini giriniz:')
    ogrenci2_soyadi = input('2.ogrencinin soyadini giriniz:')
    ogrenci2_numarasi = input('2.ogrencinin numaranizi giriniz:')

    ogrenci3_adi = input('3.ogrencinin adini giriniz:')
    ogrenci3_soyadi = input('3.ogrencinin soyadini giriniz:')
    ogrenci3_numarasi = input('3.ogrencinin numaranizi giriniz:')
    
    print('-' * 100)
    
    print(f'|{' '*9}| {"Isim":<35} | {"Soyisim":<25} | {"Numara":<20} |')
    print('-' * 100)
    print(f'| {1:>7d} | {ogrenci1_adi:<35} | {ogrenci1_soyadi:<25} | {ogrenci1_numarasi:<20} |')
    print(f'| {2:>7d} | {ogrenci2_adi:<35} | {ogrenci2_soyadi:<25} | {ogrenci2_numarasi:<20} |')
    print(f'| {3:>7d} | {ogrenci3_adi:<35} | {ogrenci3_soyadi:<25} | {ogrenci3_numarasi:<20} |')







# print('|' , ' ' * 96, '|')
# print('|' , ' ' * 96, '|')
# print('|' , ' ' * 96, '|')
# print('|' , ' ' * 96, '|')
# print('-' * 100)
