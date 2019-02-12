#!/bin/bash
#=====================================================================
# fhssh_menu.sh
# 
# How to use
#    fhssh_menu.sh  xx.xx.xx.xx
#=====================================================================

if [ -z $1 ]; then
    echo 'ERROR:  $1 argument is null'
    echo 'How to use:'
    echo 'fhssh_menu.sh 192.168.0.10'
    exit 1
fi

HOST=$1

# ------------------------------------------
SSH_PASS () {

expect -c "
set timeout 5
spawn ssh  ${USER}@${HOST}
expect \"assword:\"
send \"$PASSWD\r\"
interact
"
}

# ------------------------------------------
SSH_KEY_NOPASS () {

expect -c "
set timeout 5
spawn ssh -i ${KEY} ${USER}@${HOST}
expect \"$\"
interact
"
}

# ------------------------------------------
SSH_KEY_PASS () {

expect -c "
set timeout 5
spawn ssh -i ${KEY} ${USER}@${HOST}
expect \"assword:\"
send \"$PASSWD\r\"
expect \"$\"
interact
"
}

# ------------------------------------------
SRX () {

expect -c "
set timeout 5
spawn ssh  ${USER}@${HOST}
expect \"assword:\"
send \"$PASSWD\r\"
expect \"%\"
send \"cli\r\"
expect \">\"
send \"show configuration | display set | no-more\"
interact
"
}


cat <<MENU
=====================================================================
Select Number or character
---------------------------------------------------------------
   1) production  user01   password atuh
   2) stating  user01
   3) test  user01
   a) SRX  production
   b) SRX  staging
   c) SRX  qa
   q) quit
=====================================================================
MENU

echo -n -e "\t >"
read NUM
case ${NUM} in
  1) USER=user01
     PASSWD=testpass
     SSH_PASS
    ;;
  2) USER=user01
     PASSWD=testpass
     KEY=/home/xxx/.ssh/xxxx.pub
     SSH_KEY_NOPASS
    ;;
  3) USER=user01
     PASSWD=testpass
     SSH_KEY_PASS
    ;;
  a) USER=user01
     PASSWD=testpass
     SRX
    ;;
  b) USER=user01
     PASSWD=testpass
     SRX
    ;;
  c) USER=user01
     PASSWD=testpass
     SRX
    ;;
  q|Q) exit
     ;;
  *) echo "ERROR : selection is missed."
     exit
     ;;
esac

