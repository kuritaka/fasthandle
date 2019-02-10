#!/bin/bash
#================================================
# fhping.sh
#
# How to use
#     fhghost  "*"  hosts/test | fhping.sh
#     fhping.sh hosts
#================================================

for i in `cat $1 |grep -Ev "^#|^$" |awk {'print $1'}`
do
    echo "---------- $i ping start ----------"
    ping -i 0.5 -c 2 $i
    if [ "$?" -ne 0 ] ; then
        echo "#### NG : ping $i ####"
    fi
done

exit
