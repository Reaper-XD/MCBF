mport os,sys,time,requests,concurrent.futures,bs4,random

# MY COLOR
HJ = "\33[0;32m"
HT = "\33[30;1m"
K = "\33[33;1m"
KT = "\33[1;33m"
P = "\33[37;1m"
M = "\33[31;1m"
BM = "\33[36;1m"
B = "\33[0;36m"
HJT = "\33[32;1m"
U = "\33[35;1m"

my_color = [
HJ, HT, K, KT, B, BM, M, HJT, U, P ]
warna = random.choice(my_color)
def menu():
   print "%s__________________________________"%(KT)
   print "%s(%sI%s) %sWARNA-WARNA RANDOM         %s(%sI%s)"%(HJT,M,HJT,HT,HJT,M,HJT)
   print "%s__________________________________"%(KT)
   print "%s1.%s)%sWarna Warni"%(BM,HJ,KT)
   print "%s2.%s)%sKeluar"%(BM,HJ,KT)
   pilih = raw_input("Masukkan Pilihan : ")
   if pilih =="1":
      print " %sOutput %sWarna-%sWarni"%(HT,HJ,KT)
menu()
