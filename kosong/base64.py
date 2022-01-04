# module
import os
import base64
import sys
import random
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
os.system('clear')
print "________________________"
print "|| Coded By Reza Gans ||"
print "-------------------------"
print "--=Encode Base 64 File=--"
print "*************************"

file = raw_input('Filenya : ')

baca = open(file, 'r').read()

encrypt = base64.b64encode(baca)

baru = open('enc_'+str(file), 'w')

baru.write('import base64 \n')
baru.write('exec(base64.b64("'+str(encrypt)+'"))')

print('encrypt sukses file save as | enc_'+str(file))
