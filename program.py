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

    Ogrenci_sayisi = int(input('Ogrenci sayisini giriniz:'))

    for sira in range(Ogrenci_sayisi):
        ogrenci_adlari.append(input(f'{sira+1}.ogrencinin adini giriniz:'))      
        ogrenci_soyadlari.append(input(f'{sira+1}.ogrencinin soyadini giriniz:')) 
        ogrenci_nuamaralari.append(input(f'{sira+1}.ogrencinin numaranizi giriniz:')) 
    
    
    
    print('-' * 100)
    
    print(f'|{' '*9}| {"Isim":<35} | {"Soyisim":<25} | {"Numara":<20} |')
    print('-' * 100)
    for sira in range(Ogrenci_sayisi):
        print(f'| {(sira+1):>7d} | {ogrenci_adlari[sira]:<35} | {ogrenci_soyadlari[sira]:<25} | {ogrenci_nuamaralari[sira]:<20} |')
  






