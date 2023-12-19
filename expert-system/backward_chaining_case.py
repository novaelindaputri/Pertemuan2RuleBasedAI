Model_Mobil = ('A-Class Saloon MAMG','C-Class Saloon MAMG','GLA MAMG','GLE Couple AMG','G-Class SUV','Mercedes-AMG SL Roadster','Mercedes-Maybach S-Class Saloon','Mercedes-Maybach GSL SUV')

def bool_converter(option):
    if option.lower() == 'y':
        return True
    elif option.lower() == 't':
        return False
    else:
        raise Exception('Error.. Tolong pilih YA atau TIDAK!')


Mercedes = str(input("Pilih Model Mobil Mercedes Berikut: ['A-Class Saloon MAMG','C-Class Saloon MAMG','GLA MAMG','GLE Couple AMG','G-Class SUV','Mercedes-AMG SL Roadster','Mercedes-Maybach S-Class Saloon','Mercedes-Maybach GSL SUV'] "))

if Mercedes in Model_Mobil:
    Type_Body_Saloons = bool_converter(input("Apakah Mobil Mercedes Yang Anda Cari Berbody Saloons [Y/T] "))
    Type_Body_SUVs = bool_converter(input("Apakah Mobil Mercedes Yang Anda Cari Berbody SUVs [Y/T] "))
    Type_Body_Cabriolet = bool_converter(input("Apakah Mobil Mercedes Yang Anda Cari Berbody Cabriolet [Y/T] "))
    Vleg_Jari_Bintang_5 = bool_converter(input("Apakah Mobil Mercedes Yang Anda Cari dengan Model Vleg Berjari Bintang 5 [Y/T] "))
    Vleg_Jari_Bintang_10 = bool_converter(input("Apakah Mobil Mercedes Yang Anda Cari dengan Model Vleg Berjari Bintang 10 [Y/T] "))
    Vleg_Polygon_Bintang_5 = bool_converter(input("Apakah Mobil Mercedes Yang Anda Cari dengan Model Vleg Berjari Polygon Bintang 5 [Y/T] "))
    Vleg_Jari_Bintang_8 = bool_converter(input("Apakah Mobil Mercedes Yang Anda Cari dengan Model Vleg Berjari Bintang 8 [Y/T] "))
    ground_clearance_Rendah = bool_converter(input("Apakah Mobil Mercedes Yang Anda Cari dengan Model Ground Clearance Yang Rendah [Y/T] "))
    ground_clearance_Tinggi = bool_converter(input("Apakah Mobil Mercedes Yang Anda Cari dengan Model Ground Clearance Yang Tinggi [Y/T] "))
    Bentuk_Roof_Oval_Tertutup = bool_converter(input("Apakah Mobil Mercedes Yang Anda Cari dengan Model Roof Berbentuk Oval Tertutup [Y/T] "))
    Bentuk_Roof_Kotak_Terutup =bool_converter(input("Apakah Mobil Mercedes Yang Anda Cari dengan Model Roof Berbentuk Kotak Tertutup [Y/T] "))
    Bentuk_Roof_Terbuka =bool_converter(input("Apakah Mobil Mercedes Yang Anda Cari dengan Model Roof Yang Terbua [Y/T] "))

else:
    raise Exception('Error.. Tolong pilih YA atau TIDAK!')

if Type_Body_Saloons and Vleg_Jari_Bintang_10 or Bentuk_Roof_Oval_Tertutup and ground_clearance_Rendah and Mercedes:
    print("Ciri Tersebut Adalah Model Mobil A-Class Saloon mercedes AMG ")
elif Type_Body_Saloons and Vleg_Jari_Bintang_10 and Mercedes:
    print("Ciri Tersebut Adalah Model Mobil A-Class Saloon mercedes AMG ")
elif Type_Body_Saloons and Vleg_Jari_Bintang_5 or Bentuk_Roof_Oval_Tertutup and ground_clearance_Rendah and Mercedes:
    print("Ciri Tersebut Adalah Model Mobil C-Class Saloon Mercedes AMG ")
elif Type_Body_Saloons  and Vleg_Jari_Bintang_5 and Mercedes:
    print("Ciri Tersebut Adalah Model Mobil C-Class Saloon Mercedes AMG ")
elif Type_Body_SUVs and Vleg_Jari_Bintang_5 or Bentuk_Roof_Oval_Tertutup and ground_clearance_Tinggi and Mercedes:
    print("Ciri Tersebut Adalah Model Mobil GLA Mercedes AMG ")
elif Type_Body_SUVs and Vleg_Jari_Bintang_5 or Bentuk_Roof_Oval_Tertutup and Mercedes:
    print("Ciri Tersebut Adalah Model Mobil GLA Mercedes AMG ")
elif Type_Body_SUVs and Vleg_Jari_Bintang_10 or Bentuk_Roof_Oval_Tertutup and ground_clearance_Tinggi and Mercedes:
    print("Ciri Tersebut Adalah Model Mobil GLE Coupe Mercedes AMG ")
elif Type_Body_SUVs and Vleg_Jari_Bintang_10 or Bentuk_Roof_Oval_Tertutup and Mercedes:
    print("Ciri Tersebut Adalah Model Mobil GLE Coupe Mercedes AMG ")
elif Type_Body_SUVs and Vleg_Jari_Bintang_10 or Bentuk_Roof_Kotak_Terutup and ground_clearance_Tinggi and Mercedes:
    print("Ciri Tersebut Adalah Model Mobil G-Class SUV Mercedes AMG ")
elif Type_Body_SUVs and Vleg_Jari_Bintang_10 or Bentuk_Roof_Kotak_Terutup and Mercedes:
    print("Ciri Tersebut Adalah Model Mobil G-Class SUV Mercedes AMG ")
elif Type_Body_Cabriolet and Vleg_Jari_Bintang_10 or Bentuk_Roof_Terbuka and ground_clearance_Rendah and Mercedes:
    print("Ciri Tersebut Adalah Model Mobil Mercedes-AMG SL Roadster ")
elif Type_Body_Cabriolet and Bentuk_Roof_Terbuka or ground_clearance_Rendah and Mercedes:
    print("Ciri Tersebut Adalah Model Mobil Mercedes-AMG SL Roadster ")
elif Type_Body_Cabriolet and Bentuk_Roof_Terbuka and Mercedes:
    print("Ciri Tersebut Adalah Model Mobil Mercedes-AMG SL Roadster ")
elif Type_Body_Saloons and Vleg_Polygon_Bintang_5 or Bentuk_Roof_Oval_Tertutup and ground_clearance_Rendah and Mercedes:
    print("Ciri Tersebut Adalah Model Mobil Mercedes-Maybach S-Class Saloon ")
elif Type_Body_Saloons and Vleg_Polygon_Bintang_5 and Mercedes:
    print("Ciri Tersebut Adalah Model Mobil Mercedes-Maybach S-Class Saloon ")
elif Type_Body_SUVs and Vleg_Jari_Bintang_8 or Bentuk_Roof_Kotak_Terutup and ground_clearance_Tinggi and Mercedes:
    print("Ciri Tersebut Adalah Model Mobil Mercedes-Maybach GSL SUV ")
elif Type_Body_SUVs and Vleg_Jari_Bintang_8 or Bentuk_Roof_Kotak_Terutup and Mercedes:
    print("Ciri Tersebut Adalah Model Mobil Adalah Mercedes-Maybach GSL SUV ")
else:
     print("Mohon Maaf Ciri-ciri yang anda Maksut Belum Tersedia di Produk Mercedes-Benz")
