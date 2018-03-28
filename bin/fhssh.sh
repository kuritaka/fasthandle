#!/bin/bash
#=====================================================================
# fhssh.sh
#
# How to use
#    fhssh.sh  -l   <- list command (help)
#    fhssh.sh  -h   <- list command (help)
#    fhssh.sh  -H xx.xx.xx.xx  auth.pro
#    fhssh.sh  -H xx.xx.xx.xx  auth.stg
#=====================================================================

HELP () {
    echo "How to use"
    cat $0 |grep auth |grep ")"|grep -v "fhssh.sh" |awk -F")" {'print "  fhssh.sh -H x.x.x.x"  $1'}
    exit 0
}

ERROR () {
    echo ""
    echo 'ERROR: Option is mistake'
    echo ""
}

case ${1} in
  -h|-l) HELP
     ;;
esac

if [ -z ${3} ]; then
    ERROR
    HELP
    exit 1
fi

case ${1} in
  -H) :
    HOST=$2
    AUTH=$3
     ;;
  *) :
    ERROR
    HELP
    exit 1
    ;;
esac

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
esac
