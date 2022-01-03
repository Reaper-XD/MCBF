# module
import marshal, zlib, base64, os, sys, random
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
os.system("clear")
os.system("figlet CODE")
print "%s__________________________"%(K)
print "%s(%sI%s)%sWELCOME TO MY SCRIPT%s(%sI%s)" %(HT,M,HT,KT,HT,M,HT)
print "%s__________________________"%(K)
try:
    r = sys.argv[1]
except:
    exit("usage : python2 decode.py file.py")

if not os.path.isfile(r):
    exit("File Tidak Ditemukan!")

a = open(r).read()
b = marshal.dumps(a)
c = zlib.compress(b)
d = base64.b64encode(c)

sv = 'import marshal, zlib, base64\nexec(marshal.loads(zlib.decompress(base64.b64decode("{}"))))'

open("hasil.py", "w").write(sv.format(d))
exit("berhasil : save to as hasil.py")
