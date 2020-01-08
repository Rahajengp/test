import random #ramdomangka#
print ("Selamat datang di aplikasi Jodoh Meter") loop = True while loop:
pria = input("Masukkan nama Pria : ")
wanita= input("Masukkan nama Wanita : ")

print ("==================================")
print ("Nama Pria : ", pria)
print ("Nama Wanita :", wanita )

confirm = input ("Apakah nama yang dimasukkan sudah benar? y/n : ")

if confirm == "y" :
  loop = False
match = random.randrange(0,100)
print("") print("MATCH METER", match,"%") print("")
if match == 100: print ("Sudah menikah") else : print ("pacaran")
loop = True while loop:
pria = input("Masukkan nama Pria : ")
wanita= input("Masukkan nama Wanita : ")

print ("==================================")
print ("Nama Pria : ", pria)
print ("Nama Wanita :", wanita )

confirm = input ("Apakah nama yang dimasukkan sudah benar? y/n : ")

if confirm == "y" :
  loop = False
match = random.randrange(0,100)
print("") print("MATCH METER", match,"%") print("")
if match > 80 : print ("Ndang Rabi") else : if match > 60 : print ("Pikir-Pikir") else : if match > 40 : print ("Yaaakinn...!") else : if match > 20 : print ("cari lagi") else : print ("putus aja")
loop = True while loop:
pria = input("Masukkan nama Pria : ")
wanita1= input("Masukkan nama Wanita pertama: ")
wanita2= input("Masukkan nama Wanita kedua: ")

print ("==================================")
print ("Nama Pria : ", pria)
print ("Nama Wanita :", wanita1 )
print ("Nama Wanita :", wanita2 )

confirm = input ("Apakah nama yang dimasukkan sudah benar? y/n : ")

if confirm == "y" :
  loop = False
match = random.randrange(0,100)
print("") print("MATCH METER", match,"%") print("")
if match <= 60: print ("Cocok dengan wanita pertama", wanita1) else : print ("Cocok dengan wanita kedua")
loop = True while loop:
pria = input("Masukkan nama Pria : ")
wanita= input("Masukkan nama Wanita : ")

print ("==================================")
print ("Nama Pria : ", pria)
print ("Nama Wanita :", wanita )

confirm = input ("Apakah nama yang dimasukkan sudah benar? y/n : ")

if confirm == "y" :
  loop = False
match = random.randrange(0,100) print("") print("MATCH METER", match,"%") print("")
a = (pria) b = (wanita) print (a.strip()) print (b.strip()) if (len(a) == len (b)) : print ("Sangat cocok") else : print ("tidak cocok")
