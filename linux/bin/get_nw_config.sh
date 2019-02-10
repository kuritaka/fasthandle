#!/bin/bash
#===============================================
# get_nw_config.sh
#
# How to use
#     get_nw_config.sh  srx  x.x.x.x  test-fw-01  root  password
#===============================================
  
DEVICE=$1
NWIP=$2
NWHOST=$3
NWUSER=$4
NWPASS=$5
  
DATE=`date +%Y%m%d_%H%M`
TSERVER=192.168.0.5
TUSER=user01
TDIR=/home/fasthandle/fhhome/linux/tftp
 
CONF=${TDIR}/${NWHOST}/${NWHOST}_${DATE}.conf
 
# ------------------------------------------
[ ! -d "${TDIR}" ] && mkdir ${TDIR}
chmod 777 ${TDIR}
 
 
# ------------------------------------------
HELP () {
  
cat <<@
How to use
      get_nw_config.sh  srx  x.x.x.x  test-fw-01 root  password
@
  
}
 
 
#-------------------------------------------
GET_SRX () {
 
expect -c "
set timeout 5
spawn ssh  ${NWUSER}@${NWIP}
expect \"assword:\"
send \"$NWPASSWD\r\"
expect \"%\"
send \"cli\r\"
expect \">\"
send \"show configuration | display set | save ${TUSER}@${TSERVER}:${CONF}\r\"
expect \">\"
send \"exit\r\"
interact
"
}
  
#===========================================
case ${DEVICE} in
  -h) HELP
    ;;
  srx|SRX) GET_SRX
    ;;
  *) HELP
     ;;
esac
