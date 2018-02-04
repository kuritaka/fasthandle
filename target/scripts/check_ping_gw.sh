#!/bin/bash
#==============================================================================
# check_ping_gw.sh
#
# How to use
#     chek_ping_gw.sh
#==============================================================================

LANG=C

TMPFILE=/tmp/tmp.$$
ERROR=0

for i  in `route -n | awk {'print $2'} | grep -Evi "IP|Gateway|0.0.0.0"`
do
    ping -i 0.25 -c 3 -w 2 $i > ${TMPFILE}
    if [ $?  -ne 0 ] ; then
        ERROR=1
    fi
    tail -n 3 ${TMPFILE}
    rm ${TMPFILE}
done


if [ $ERROR -eq 1 ] ; then
   echo "ping NG"
   exit 1
fi

   echo "ping OK"
exit 0