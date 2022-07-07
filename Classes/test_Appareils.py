from classes_Appareils import *
o = OrdinateurPortable("Dell", "XPS15", "DX44503",
                       "IntelCorei7", "500GB",
                       "15po", "16GB")
t = Telephone("Google", "Pixel 3a", "RP2002-45",
              "Kryu 2.3ghz", "64GB",
              "5.7 x 2.7 x0.3", "374854948575imei")
s = Serveur("HP", "Proliant ML30", "HP93039984885-45",
            "Intel Xeon e2234 3.6ghz", "10TB",
            "64GB")
print(o.afficher())
print(t.afficher())
print(s.afficher())
