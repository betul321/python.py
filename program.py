

def print_intro(version):
    print(f'''
          -----------------------------------
          Ogrenci bilgi sistemi v.1{version}
          -----------------------------------
          | Komut Listesi                   |
          -----------------------------------
          | kapat   | Uygulamayi sonlandir  |
          | ekle    | Ogrenci ekle          |
          | sil     | Ogrenci siler         |
          | listele | Ogrencileri listeler  |
          | guncelle| Ogrenci gunceller     |
          -----------------------------------
          ''')


def ogrenci_ekle(odict):
    Ogrenci_sayisi = int(input('Ogrenci sayisini giriniz:'))

    for sira in range(Ogrenci_sayisi):
                key =input(f'{sira+1}. Ogrenci numarasini giriniz:')
              
    if key in odict:
                print(f'{key} numarali ogrenci zaten mevcut!')
    else:
                isim=input(f'{sira+1}. Ogrenci adini giriniz:')
                soyisim=input(f'{sira+1}. Ogrenci soyismini giriniz:')
                odict[key] = {'isim': isim,'soyisim':soyisim}

def ogrenci_sil(odict):
    Ogrenci_numarasi = (input('Ogrenci numarasini giriniz:'))
            
    try:
        del odict[Ogrenci_numarasi]
        print(f'{Ogrenci_numarasi} numarali ogrenci silindi!')


    except:
        print(F'{Ogrenci_numarasi} numarali bir ogrenci yok!')


def ogrenci_guncelle(odict):
    key = input(f'Ogrenci numarasini giriniz:')

    if key in odict:
        isim= input(f'Ogrenci adini giriniz:')
        soyisim=input(f'Ogrenci soyismini giriniz:')
        odict[key]={'isim':isim,'soyisim':soyisim}

        print(f'{key} numarali ogrenci guncellendi!')


def ogrenci_listele(odict):
    print('-' * 100)
    print(f'|{' '*2}| {"isim":<12} | {"soyisim":<8} | {"Numara":<6} |')
    print('-' * 100)
    for sira, key in enumerate(odict):
        print(f'| {(sira+1):>2} | {odict[key]["isim"]:<13} | {odict[key]["soyisim"]:<8} | {key:<5}|')

if __name__ =='__main__':
  

    print_intro(1)

    
    #dictionary = demet
    
    ogrenciler = {"1234":{"isim":'Betul',"soyisim":'Becerikli'},
                "1235":{"isim":'Turkan',"soyisim":'Topkara'},
                "1236":{"isism":'Simge',"soyisim":'Dogan'}}
    
    komut = input("Komut giriniz:").strip().lower()
    while komut != 'kapat':
        if komut == 'ekle':
            print('------------------------------------------------------')
            ogrenci_ekle(ogrenciler)
            ogrenci_listele(ogrenciler)
            print('------------------------------------------------------')
        elif komut == 'sil':
            print('------------------------------------------------------')
            ogrenci_sil(ogrenciler)
            print('------------------------------------------------------')
        elif komut == 'guncelle':
            print('------------------------------------------------------')
            ogrenci_guncelle(ogrenciler)
        elif komut == 'listele':
            print('------------------------------------------------------')
            ogrenci_listele(ogrenciler)
            print('------------------------------------------------------')
        else:
            print('------------------------------------------------------')
            print(f'"{komut} seklinde tanimli bir komut bulunmamaktadir.')
            print('------------------------------------------------------')
   
        komut = input('Komut giriniz:').strip().lower()
        
    print('------------------------------------------------------')
    print('Program sonlandirildi.')
   
   
   
    
    
   




