# module
import os
import base64
import sys

os.system('clear')

file = raw_input('Filenya : ')

baca = open(file, 'r').read()

encrypt = base64.b32encode(baca)

baru = open('enc_'+str(file), 'w')

baru.write('import base64 \n')
baru.write('exec(base64.b32("'+str(encrypt)+'"))')

print('encrypt sukses file save as | enc_'+str(file))