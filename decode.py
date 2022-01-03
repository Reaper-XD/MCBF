# module
import marshal, zlib, base64, os, sys
os.system("clear")
os.system("figlet CODE")
print "\n\33[30;1m__________________________"
print "\n\33[1;33m(\33[31;1mI\33[1;33m)\33[32;1mWELCOME TO MY SCRIPT\33[1;33m(\33[31;1mI\33[1;33m)"
print "\n\33[30;1m__________________________"
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
