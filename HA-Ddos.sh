#!/bin/bash

clear

# Variables
b='\033[1m'
u='\033[4m'
bl='\E[30m'
r='\E[31m'
g='\E[32m'
bu='\E[34m'
m='\E[35m'
c='\E[36m'
w='\E[37m'
endc='\E[0m'
enda='\033[0m'
blue='\e[1;34m'
cyan='\e[1;36m'
red='\e[1;31m'
errormsg () {
        printf "${red}[!] ${white}${1}\n${nc}"
}

check_internet () {
ping -c 1 google.com > /dev/null 2>&1
if [[ "$?" != 0 ]];then
   clear
   errormsg "PLEASE CHECK YOUR INTERNET CONNECTION"
    exit 0
fi
}

check_internet

fig="$PREFIX/bin/figlet"
lol="$PREFIX/bin/lolcat"
lolc="$usr/bin/lolcat"
fige="usr/bin/figlet"
if [ -e "$fig" ]; then
printf $blue"[✓] Packages Already Installed."
sleep 2
clear
elif [ -e "$fige" ]; then
printf $blue"[✓] Packages Already Installed..."
sleep 2
clear
else
echo "[!] Packages Installing..."
pkg install python python2 vim curl > /dev/null 2>&1
pkg install figlet > /dev/null 2>&1
pkg install php > /dev/null 2>&1
fi

if [ -e "$lol" ]; then
echo "[✓] Packages Already Installed"
sleep 2
clear
elif [ -e "$lolc"]; then
echo "[✓] Packages Already Installed."
sleep 2
clear
fi

figlet HA-Ddos | lolcat
echo "Author   : H@cker Alex" | lolcat
echo ""
echo "Github   : github.com/techaleex" | lolcat
echo ""
echo "Telegram : t.me/Techalex3658" | lolcat
echo ""
printf $red"Note- This Tool An Illegal Tool & It's Only For Educational Purpose.. Use It At Your Own Risk,We'll Be Not Responsible For Kind Of Problems"
python2 HA-Ddos.py
