#!/bin/bash
#================================================
# fhfping.sh
#
# How to use
#     fhghost  "*"  hosts/test | fhfping.sh
#     echo 192.168.0.10 | fhfping.sh
#     fhfping.sh  test.list
#================================================

if [ -z "$1" ] ; then
    grep -Ev "^#|^$" |awk {'print $1'} |fping -t 250 2>/dev/null
else
    cat "$1" |grep -Ev "^#|^$" |awk {'print $1'} |fping -t 250 2>/dev/null
fi

