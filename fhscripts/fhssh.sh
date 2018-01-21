#!/bin/bash
#=====================================================================
# fhssh.sh
#
# How to use
#    fhssh.sh  auth.pro xx.xx.xx.xx
#=====================================================================

HELP () {
    echo "How to use"
    cat $0 |grep auth |grep ")"|grep -v "fhssh.sh" |awk -F")" {'print "  fhssh.sh" $1 " x.x.x.x"'}
    exit 0
}

AUTH=$1
HOST=$2

case ${AUTH} in
  -h|-l) HELP
     ;;
esac


# ------------------------------------------
if [ -z ${HOST} ]; then
    echo ""
    echo 'ERROR: HOST is null'
    echo ""
    HELP
    exit 1
fi


#===================================================================
#
#===================================================================
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


case ${AUTH} in
  auth.pro) :
     USER=user01
     PASSWD=testpass
     SSH_PASS
    ;;
  auth.stg) :
     USER=user01
     PASSWD=testpass
     KEY=/home/xxx/.ssh/xxxx.pub
     SSH_KEY_NOPASS
    ;;
  auth.dev) :
     USER=user01
     PASSWD=testpass
     SSH_KEY_PASS
    ;;
  auth.srx_pro) :
     USER=user01
     PASSWD=testpass
     SRX
    ;;
  auth.srx_dev) :
     USER=user01
     PASSWD=testpass
     SRX
    ;;
  *) HELP
     exit
     ;;
esac


