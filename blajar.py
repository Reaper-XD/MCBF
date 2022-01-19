# module
import os,sys,time,random

def auto(z):
        for e in z + '\n':
                sys.stdout.write(e)
                sys.stdout.flush()
                time.sleep(0.05)

def titik():
        titik = ['\x1b[1;92m.   ', '\x1b[1;95m..  ', '\x1b[1;96m... ','\x1b[1;95m.   ', '\x1b[1;93m..  ', '\x1b[1;96m... ']
        for x in titik:
                print "\r\33[30;1m[\33[1;33m*\33[30;1m] \33[;0mMenunggulah tot %s"%(x),
                sys.stdout.flush()
                time.sleep(1)
def detik():
        detik = ["\33[30;1m[\x1b[1;96m01\33[30;1m]","\33[30;1m[\x1b[1;96m02\33[30;1m]","\33[30;1m[\x1b[1;96m03\33[30;1m]","\33[30;1m[\x1b[1;96m04\33[30;1m]","\33[30;1m[\x1b[1;96m05\33[30;1m]","\33[30;1m[\x1b[1;96m06\33[30;1m]","\33[30;1m[\x1b[1;96m07\33[30;1m]","\33[30;1m[\x1b[1;96m08\33[30;1m]","\33[30;1m[\x1b[1;96m09\33[30;1m]","\33[30;1m[\x1b[1;96m10\33[30;1m]","\33[30;1m[\x1b[1;96m11\33[30;1m]","\33[30;1m[\x1b[1;96m12\33[30;1m]","\33[30;1m[\x1b[1;96m13\33[30;1m]","\33[30;1m[\x1b[1;96m14\33[30;1m]","\33[30;1m[\x1b[1;96m15\33[30;1m]"]
        for x in detik:
                print "\r\33[1;33m[\33[30;1m+\33[1;33m] \33[;0mProses. Detik : %s"%(x),
                sys.stdout.flush()
                time.sleep(1)
def loding():
        wait = [".","..","...","....",".....","......","........","........",".........","...........","............"]
        for x in wait:
                print "\rLoading %s"%(x),
                sys.stdout.flush()
                time.sleep(1)
os.system("clear")
loding()
os.system("clear")
auto("\n---------------------")
auto("\n---------------------")
auto("\nMenunggu...")
titik()
detik()
print "\nMati Kw Besok:v"
time.sleep(3)
