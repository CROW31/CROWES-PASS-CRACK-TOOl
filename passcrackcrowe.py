import hashlib
import sys
import time
from time import sleep


flag = 0

title =  "WELCOME TO CROWES PASS CRACKER\n"
for char in title:
    sleep(0.05)
    sys.stdout.write(char)

print('''
        %bld%dyel                        .,-:;//;:=,
%bld%dyel                    . :H@@@MM@M#H/.,+%;,
%bld%dyel                 ,/X+ +M@@M@MM%=,-%HMMM@X/,
%bld%dyel               -+@MM; $M@@MH+-,;XMMMM@MMMM@+-
%bld%dyel              ;@M@@M- XM@X;. -+XXXXXHHH@M@M#@/.
%bld%dyel            ,%MM@@MH ,@%=             .---=-=:=,.
%bld%dyel            =@#@@@MX.,                -%HX$$%%%:;
%bld%dyel           =-./@M@M$                   .;@MMMM@MM:
%bld%dyel           X@/ -$MM/                    . +MM@@@M$
%bld%dyel          ,@M@H: :@:                    . =X#@@@@-
%bld%dyel          ,@@@MMX, .                    /H- ;@M@M=
%bld%dyel          .H@@@@M@+,                    %MM+..%#$.
%bld%dyel           /MMMM@MMH/.                  XM@MH; =;
%bld%dyel            /%+%$XHH@$=              , .H@@@@MX,
%bld%dyel             .=--------.           -%H.,@@@@@MX,
%bld%dyel             .%MM@@@HHHXX$$$%+- .:$MMX =M@@MM%.
%bld%dyel               =XMMM@MM@MM#H;,-+HMM@M+ /MMMX=
%bld%dyel                 =%@M@M#@$-.=$@MM@@@M; %M%=
%bld%dyel                   ,:+$+-,/H#MMMMMMM@= =,
%bld%dyel                         =++%%%%+/:-.%clr
''')


print ('''
#============================#
#   CROWE PASS CRACK TOOL    #
# ===========================#\n''')

data = ["l","o","a","d","i","n","g"," ","t","o","o","l"]
for x in range(len(data)):


    old = data[x]


    data[x] = old.upper()


    text = "".join(data)


    sys.stdout.write("\r")
    sys.stdout.write(text)
    sys.stdout.flush()


    data[x] = old

    time.sleep(0.1)



text = "".join(data)

sys.stdout.write("\r")
sys.stdout.write(text)
sys.stdout.flush()

for x in range(len(data)):


    old = data[x]


    data[x] = old.upper()


    text = "".join(data)


    sys.stdout.write("\r")
    sys.stdout.write(text)
    sys.stdout.flush()


    data[x] = old

    time.sleep(0.1)



text = "".join(data)

sys.stdout.write("\r")
sys.stdout.write(text)
sys.stdout.flush()

for x in range(len(data)):


    old = data[x]


    data[x] = old.upper()


    text = "".join(data)


    sys.stdout.write("\r")
    sys.stdout.write(text)
    sys.stdout.flush()


    data[x] = old

    time.sleep(0.1)



text = "".join(data)

sys.stdout.write("\r")
sys.stdout.write(text)
sys.stdout.flush()

pass_hash = input("\n\nEnter md5 hash: ")

wordlist = input("File name: ")

try:
    pass_file = open (wordlist, "r")
except:
    print("No file found")
    quit()

for word in pass_file:

    enc_wrd = word.encode('utf-8')
    digest = hashlib.md5(enc_wrd.strip()).hexdigest()

    if digest == pass_hash:
        print("Password found")
        print("password is " + word)
        flag = 1
        break

if flag == 0:
    print("password is not in the list try again :) //")

