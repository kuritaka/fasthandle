#!/bin/bash
#==============================================================================
# check_reboot.sh
#
# How to use
#     chek_reboot.sh  2>/dev/null
#==============================================================================

LANG=C

#==============================================================================
# Function
#==============================================================================
process_check(){
   COUNT=`ps aux | grep $1 |grep -v grep |wc -l`
   if [ "$COUNT" -ge 1 ] ; then
      echo "$1 Process Found"
   fi
}

#==============================================================================
# Main
#==============================================================================
cat << @
## hostname ####
`hostname`

## uptime |awk '{print $1, $2 ,$3}' ####
`uptime |awk '{print $1, $2 ,$3}'`


## which ntpq > /dev/null 2>&1 && ntpq -p ####
`which ntpq > /dev/null 2>&1 && ntpq -p`

## which chronyc > /dev/null 2>&1 && chronyc sources -v ####
`which chronyc > /dev/null 2>&1 && chronyc sources -v`


#----------------------------------------------------------
# Hardware
#----------------------------------------------------------
## The number of Processors like top command
## cat /proc/cpuinfo | grep processor |wc -l ####
`cat /proc/cpuinfo | grep processor |wc -l`

## The number of total core
## cat /proc/cpuinfo |grep "cpu cores" | perl -e 'while(<>){$n+=/(\d+)/?$1:0;}print"$n\n";' ####
`cat /proc/cpuinfo |grep "cpu cores" | perl -e 'while(<>){$n+=/(\d+)/?$1:0;}print"$n\n";'`


## cat /proc/meminfo  |egrep "MemTotal|SwapTotal" ####
`cat /proc/meminfo  |egrep "MemTotal|SwapTotal"`


## mount | egrep ^/dev ####
`mount | egrep "^/dev|nfs"`


#----------------------------------------------------------
# Networking
#----------------------------------------------------------
## ip a |egrep "mtu|inet" |grep -v inet6 ####
`ip a |egrep "mtu|inet" |grep -v inet6`

## ip r ####
`ip r`


#----------------------------------------------------------
# Process
#----------------------------------------------------------
# OS
`process_check snmp`

# middleware
`process_check httpd`
`process_check nginx`

@

