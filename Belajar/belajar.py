## module ##
import os,sys,random,time,mechanize
### WARNA RANDOM ###
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
G = '\x1b[1;90m' # HITAM
my_color = [
 P, M, H, K, B, U, O, N, G]
warna = random.choice(my_color)

# pertanyaan (y/t)
def ngentot():
        auto("\033[34;1mApakah \033[32;1m anda \033[35;1m ingin \033[36;1matack lagi? \033[36;1m[\033[32;1mY\033[34;1m/\033[35;1mT\033[33;1m] \033[35;1m~\033[33;1m=> ")
        nanya = raw_input("[+] Masukkan Pilihan [Y/t] : ")
        if nanya =="Y" or nanya =="y":
                main()
        elif nanya =="T" or nanya =="t":
                auto("\033[35;1mBye \033[32;1mBye \033[33;1m:)")
                time.sleep(1)
                os.system("exit")
        elif nanya =="" or nanya =='':
                auto("\033[32;1mJangan \033[35;1msampe \033[36;1mkosong \033[32;1mya")
                time.sleep(1)
                raw_input("[+] Tekan enter Untuk Kembali [ENTER]");ngentot()
        else:
                auto("\033[32;1mSalah, \033[35;1mMasukkan \033[36;1minput \033[32;1mpilihan \033[36;1mdengan \033[33;1mbenar!")
                time.sleep(1)
                raw_input("Tekan Enter Untuk Kembali > [ENTER]");ngentot()

def auto(z):
        for e in z + "\n":
                sys.stdout.write(e)
                sys.stdout.flush()
                time.sleep(0.05)

def main():
        os.system("clear")
        os.system("figlet Belajar")
        print "%s______________________________________"%(O)
        print "%s[%s+%s] %sAuthor : %sReaper Official       %s[%s+%s]"%(G,K,G,M,H,G,K,G)
        print "%s[%s+%s] %sYoutube: %sReaper Official       %s[%s+%s]"%(G,K,G,M,H,G,K,G)
        print "%s[%s+%s] %sBelajar Menggunakan %sPython     %s[%s+%s]"%(G,K,G,N,O,G,K,G)
        print "%s______________________________________"%(O)


        nomor = raw_input("\x1b[;0mMasukkan nomor target : \x1b[1;91m")
        jumlah = int(input("\x1b[;0mMasukkan Jumlahnya : \x1b[1;91m"))
        time.sleep(1)


        try:
                for i in range(jumlah):
                        print "%sBerhasil %sMengirim %sKe > %s"%(N,O,K,M),nomor
                        time.sleep(0.1)
        except KeyboardInterrupt:
                print "%s>v< %sSelesai %s^>v<"%(O,M,O)
                ngentot()
main()
