import os
import requests
import socket
import random
os.system('clear')
print('\033[0;50m             THE TOOL BY KAR13MA09 √')
print("""\033[1;50m
        ___________________________________
        |Facebook:facebook.com/kar13ma09  |
        |Youtube:@Kar13ma09_vnpc-vn       |
        |Tele:@Kar13ma09_vnpc_bot         |
        |_________________________________|
""")
print('\033[0;35m   ________________________________________________')
print("""\033[1;31m \033[3m
  [1]  Metasploite         [9]  Osif
  [2]  Nmap                [10]  Admin Hack
  [3]  Sqlmap              [11]  Cam Hack
  [4]  PyPhisher           [12]  GhostTRACK
  [5]  Kali Nethunter      [13]  Git info Victam
  [6]  Yarb DDoS           [14]  Android App Virus
  [7]  Red Hawk            [15]  bo_hyd_cat
  [8]  Fsociety            [16]  Parrot Banner

         [99] Rest       [0]  About Tool
""")
print('\033[0;35m   ______________________________________________ ')
####metasplite install
oooo = input('\033[31m     Enter Number ==> √  :    ')
if oooo == '1' :
   os.system("cd $HOME")
   os.system("apt update")
   os.system("apt upgrade")
   os.system("apt install python python3")
   os.system("apt install ruby")
   os.system("pkg install wget")
   os.system("wget https://github.com/gushmazuko/metasploit_in_termux/raw/master/metasploit.sh")
   os.system("chmod +x metasploit.sh")
   os.system("./metasploit.sh")
   os.system("msfconsole")
   print("to start metasploite type msfconsole")
   print('the metasploite Installed KAR13MA09')
#nmap install
elif oooo =='2' :
     print('install Namp in termux KAR13MA09')
     os.system("cd $HOME")
     os.system('pkg install nmap')
     print('the Namp Installed KAR13MA09')
     os.system('nmap')

##Sqlmap install
elif oooo =='3' :
     print('install SQlmap in termux KAR13MA09')
     os.system("cd $HOME")
     os.system("pip3 install sqlmap")
     print("the sqlmap Installed KAR13MA09")
     os.sytem("sqlmap")
##PyPhisher install
elif oooo =='4' :
     print('install PyPhisher in termux KAR13MA09')
     os.system('cd $HOME')
     os.system('apt update')
     os.system('apt upgrade')
     os.system('git clone https://github.com/KasRoudra/PyPhisher')
     os.system('cd PyPhisher')
     os.system('pip3 install -r files/requirements.txt')
     os.system('mv PyPhisher $HOME')
##kali netunter
elif oooo =='5' :
     print("install Kali Netunter in termux KAR13MA09")
     os.system("cd $HOME")
     os.system("termux-setup-storage")
     os.system("pkg install wget")
     os.system("wget -O install-nethunter-termux https://offs.ec/2MceZWr")
     os.system("chmod +x install-nethunter-termux")
     os.system("./install-nethunter-termux")
##yarb ddos insall
elif oooo =='6' :
     print('Install Yrab DDoS in termux KAR13MA09')
     os.system("git clone https://github.com/bohaydar/yarb-ddos.git")
     os.system('mv yarb-ddos $HOME')
##install red hawk
elif oooo =='7' :
     print('install red hawk in termux KAR13MA09')
     os.system("apt install git")
     os.system("git clone https://github.com/Tuhinshubhra/RED_HAWK.git")
     os.system('mv RED_HAWK $HOME')

##install facsyte
elif oooo =='8' :
     print('install fsociety in termux H-TOOL')
     os.system('pkg install wget -y')
     os.system('git clone https://github.com/Manisso/fsociety.git')
     os.system('mv fsociety $HOME')
#install osif
elif oooo== '9' :
     print('install osif in termux KAR13MA09')
     os.system('git clone https://github.com/ciku370/OSIF')
     #os.system('cd osif')
    # os.system('pip2 install -r requirements.txt')
     os.system('mv osif $HOME')
####admin fund
elif oooo =='10' :
     print('install Admin Faund in termux KAR13MA09')
     os.system('git clone https://github.com/mishakorzik/AdminHack')
     os.system('mv AdminHack $HOME')
##cam hack
elif oooo == '11' :
     print('install Cam hack in termux KAR13MA09')
     os.system('git clone https://github.com/OnlineHacKing/CameraHack ')
     os.system('mv CameraHack $HOME')
##gohst track
elif oooo == '12' :
     print('install GhostTR in termux KAR13MA09')
     os.system('git clone https://github.com/HunxByts/GhostTrack.git')
     os.system('mv GhostTrack $HOME')
##App visrus
elif oooo =='14' :
     print('install app virus H-TOOL ')
    # os.system('cd $HOME')
     os.system('git clone https://github.com/GH05T-HUNTER5/selfkiller')
     os.system('mv selfkiller $HOME')
##git info
elif oooo =='13' :
     print('install gut info in termux KAR13MA09')
     #os.system('cd $HOME')
     os.system('git clone https://github.com/majidtdeni666/getinfo')
     os.system('mv getinfo $HOME')
##bo_hyd_cat install
elif oooo =='15' :
     print('install bo hyd cat in termux KAR13MA09')
     os.system('cd $HOME')
     os.system('git clone https://github.com/bohaydar/bo_hyd_cat.git')
     os.system('mv bo_hyd_cat $HOME')
#### parrot banner
elif oooo =='16' :
     print('install parrot banner in termux KAR13MA09')
     #os.system('cd $HOME')
     os.system('git clone https://github.com/termuxprofessor/parrotshell')
     os.system('mv parrotshell $HOME')
##information
elif oooo =='0' :
     print (''' [!] Thes Tool By Kar13ma09 All Rights Reserved Free Palestine [!] 

        _____________________________________________
        |Facebook:facebook.com/kar13ma09            |
        |Youtube:@Kar13ma09_vnpc-vn                 |
        |Tele:@Kar13ma09_vnpc_bot                   |
        |___________________________________________|
''')
#####
elif oooo =='99' :
     os.system('python main.py')
